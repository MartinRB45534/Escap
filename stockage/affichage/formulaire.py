"""Contient la classe Formulaire."""

from __future__ import annotations
from typing import Type, Callable, TypeVar, Optional, Tuple, Set, List

import pygame

import affichage as af
from affichage.cliquable import Cliquable

from ..stockage import StockageUnique, StockageNivele, StockageCategorie

# Le stockage hérite de StockageUnique
StockageUn = TypeVar("StockageUn", bound=StockageUnique)

class FormulaireUnique(af.WrapperNoeud):
    """Un formulaire, avec des champs à remplir pour créer un objet."""
    def __init__(self, stockage: Type[StockageUn], acceptor: Callable[[str], bool],
                 avertissement:str, ajouter: Callable[[StockageUn], None]):
        af.WrapperNoeud.__init__(self)
        self.stockage = stockage

        self.textes:dict[str, af.Texte] = {
            "nom": af.Texte("Nom :"),
        }
        self.inputs:dict[str, af.TexteInput] = {
            "nom": af.TexteInput(acceptor=acceptor),
        }
        self.avertissements:dict[str, af.TexteCache] = {
            "nom": af.TexteCache(""),
        }
        self.textes_avertissements:dict[str, str] = {
            "nom": avertissement,
        }

        for key in stockage.champs:
            self.form(key, stockage.champs[key], stockage.acceptors[key],
                      stockage.avertissements[key])

        self.contenu = af.ListeMargeVerticale()
        self.contenu.set_contenu(
            sum([
                [texte, self.inputs[key], self.avertissements[key]]
                for key, texte in self.textes.items()
            ], []) # type: ignore # Pylance wants me to specify the type if that empty list smh
            + [af.BoutonFonction(af.SKIN_SHADE, "Ajouter", self.ajouter)]
        )

        self.super_ajouter = ajouter

    def form(self, nom:str, type_: Type[int|str|float],
             acceptor: Callable[[str], bool], avertissement:str):
        """Ajoute un champ."""
        self.textes[nom] = af.Texte(nom)
        if type_ is int:
            self.inputs[nom] = af.IntInput(acceptor=acceptor)
        elif type_ is str:
            self.inputs[nom] = af.TexteInput(acceptor=acceptor)
        elif type_ is float:
            self.inputs[nom] = af.NumberInput(acceptor=acceptor)
        else:
            raise TypeError(f"Le type {type_} n'est pas supporté.")
        self.avertissements[nom] = af.TexteCache("")
        self.textes_avertissements[nom] = avertissement

    def check(self):
        """Met à jour les avertissements"""
        for key, input_ in self.inputs.items():
            if input_.accepte:
                self.avertissements[key].set_texte("")
            else:
                self.avertissements[key].set_texte(self.textes_avertissements[key])

    def update(self):
        self.check()
        af.WrapperNoeud.update(self)

    def ajouter(self):
        """Ajoute l'objet."""
        self.check()
        if all([avertissement.get_texte() == "" for avertissement in self.avertissements.values()]):
            json = f"""{{
    {", ".join([f'"{key}": {input_.valeur}' for key, input_ in self.inputs.items()])}
}}"""
            self.super_ajouter(self.stockage.parse(json))

    def select(self, selection: af.Cliquable, droit:bool=False):
        """Sélectionne l'élément."""
        self.update()
        af.WrapperNoeud.select(self, selection, droit)

class FormulaireModificationUnique(FormulaireUnique):
    """Un formulaire, avec des champs à remplir pour modifier un objet."""
    def __init__(self, stockage: Type[StockageUn], acceptor: Callable[[str], bool],
                 avertissement:str, modifier: Callable[[StockageUn], None],
                 objet:StockageUn, supprimer: Callable[[StockageUn], None]):
        FormulaireUnique.__init__(self, stockage,
                                  lambda nom: acceptor(nom) or nom == objet.nom,
                                  avertissement, modifier)
        self.objet = objet
        self.inputs["nom"].valeur = objet.nom
        for key in stockage.champs:
            self.inputs[key].valeur = str(getattr(objet, key)) # Est-ce que c'est pire que d'utiliset la jsonification ?

        assert isinstance(self.contenu, af.ListeMargeVerticale)
        self.contenu.set_contenu(
            sum([
                [texte, self.inputs[key], self.avertissements[key]]
                for key, texte in self.textes.items()
            ], []) # type: ignore # Pylance wants me to specify the type if that empty list smh
            + [af.BoutonFonction(af.SKIN_SHADE, "Modifier", self.ajouter),
               af.BoutonFonction(af.SKIN_SHADE, "Supprimer", lambda: supprimer(objet))]
        )

StockageNi = TypeVar("StockageNi", bound=StockageNivele)

class FormulaireNivele(af.WrapperNoeud):
    """Un formulaire, avec des champs à remplir pour créer un objet."""
    def __init__(self, stockage: Type[StockageNi], acceptor: Callable[[str], bool],
                 avertissement:str, ajouter: Callable[[StockageNi], None]):
        af.WrapperNoeud.__init__(self)
        self.stockage = stockage

        self.textes:dict[str, af.Texte] = {
            "nom": af.Texte("Nom :"),
            "niveau": af.Texte("Niveau :"),
        }
        self.inputs:dict[str, af.TexteInput] = {
            "nom": af.TexteInput(acceptor=acceptor),
            "niveau": af.IntInput(texte="1",acceptor=lambda niveau: 1 <= int(niveau) <= 10),
        }
        self.avertissements:dict[str, af.TexteCache] = {
            "nom": af.TexteCache(""),
            "niveau": af.TexteCache(""),
        }
        self.textes_avertissements:dict[str, str] = {
            "nom": avertissement,
            "niveau": "Les niveaux vont de 1 à 10.",
        }

        self.niveau = 1
        self.valeurs:dict[str, List[str]] = {}

        for key in stockage.champs:
            self.form(key, stockage.champs[key], stockage.acceptors[key],
                      stockage.avertissements[key])

        self.contenu = af.ListeMargeVerticale()
        self.contenu.set_contenu(
            sum([
                [texte, self.inputs[key], self.avertissements[key]]
                for key, texte in self.textes.items()
            ], []) # type: ignore # Pylance wants me to specify the type if that empty list smh
            + [af.BoutonFonction(af.SKIN_SHADE, "Ajouter", self.ajouter)]
        )

        self.super_ajouter = ajouter

    def form(self, nom:str, type_: Type[int|str|float],
             acceptor: Callable[[str], bool], avertissement:str):
        """Ajoute un champ."""
        self.textes[nom] = af.Texte(nom)
        if type_ is int:
            self.inputs[nom] = af.IntInput(acceptor=acceptor)
        elif type_ is str:
            self.inputs[nom] = af.TexteInput(acceptor=acceptor)
        elif type_ is float:
            self.inputs[nom] = af.NumberInput(acceptor=acceptor)
        else:
            raise TypeError(f"Le type {type_} n'est pas supporté.")
        self.avertissements[nom] = af.TexteCache("")
        self.textes_avertissements[nom] = avertissement
        self.valeurs[nom] = [self.inputs[nom].valeur] * 10

    def check(self):
        """Met à jour les avertissements"""
        # On enregistre d'abord les dernières valeurs
        niveaux_problematiques: Set[int] = set()
        for key, valeurs in self.valeurs.items():
            valeurs[self.niveau-1] = self.inputs[key].valeur
            for niveau in range(10):
                if niveau == self.niveau-1:
                    if self.inputs[key].accepte:
                        self.avertissements[key].set_texte("")
                    else:
                        self.avertissements[key].set_texte(self.textes_avertissements[key])
                elif not self.inputs[key].acceptor(valeurs[niveau]):
                    niveaux_problematiques.add(niveau+1)
        # On met à jour les avertissements
        if niveaux_problematiques:
            self.avertissements["niveau"].set_texte(
                f"Les niveaux {', '.join([str(niveau) for niveau in niveaux_problematiques])} ne sont pas valides.")

    def update(self):
        self.check()
        if self.inputs["niveau"].accepte and self.niveau != int(self.inputs["niveau"].valeur):
            self.niveau = int(self.inputs["niveau"].valeur)
            for key, input_ in self.inputs.items():
                input_.valeur = self.valeurs[key][self.niveau-1]
        self.check()
        af.WrapperNoeud.update(self)

    def ajouter(self):
        """Ajoute l'objet."""
        self.check()
        if all([avertissement.get_texte() == "" for avertissement in self.avertissements.values()]):
            json = f"""{{
    "nom": "{self.inputs["nom"].valeur}",
    {", ".join([f'"{key}": [{", ".join([valeur for valeur in valeurs])}]' for key, valeurs in self.valeurs.items()])}
}}"""
            self.super_ajouter(self.stockage.parse(json))

    def select(self, selection: af.Cliquable, droit:bool=False):
        """Sélectionne l'élément."""
        self.update()
        af.WrapperNoeud.select(self, selection, droit)

class FormulaireModificationNivele(FormulaireNivele):
    """Un formulaire, avec des champs à remplir pour modifier un objet."""
    def __init__(self, stockage: Type[StockageNi], acceptor: Callable[[str], bool],
                 avertissement:str, modifier: Callable[[StockageNi], None],
                 objet:StockageNi, supprimer: Callable[[StockageNi], None]):
        FormulaireNivele.__init__(self, stockage,
                                  lambda nom: acceptor(nom) or nom == objet.nom,
                                  avertissement, modifier)
        self.objet = objet
        self.inputs["nom"].valeur = objet.nom
        for key in stockage.champs:
            self.inputs[key].valeur = str(getattr(objet, key)[0]) # Est-ce que c'est pire que d'utiliset la jsonification ?
            self.valeurs[key] = [str(attr) for attr in getattr(objet, key)]

        assert isinstance(self.contenu, af.ListeMargeVerticale)
        self.contenu.set_contenu(
            sum([
                [texte, self.inputs[key], self.avertissements[key]]
                for key, texte in self.textes.items()
            ], []) # type: ignore # Pylance wants me to specify the type if that empty list smh
            + [af.BoutonFonction(af.SKIN_SHADE, "Modifier", self.ajouter),
               af.BoutonFonction(af.SKIN_SHADE, "Supprimer", lambda: supprimer(objet))]
        )

StockageCat = TypeVar("StockageCat", bound=StockageCategorie)

class FormulaireCategorie(af.WrapperNoeud):
    """Un formulaire pour les catégories. Donne accès aux formulaires des éléments."""
    def __init__(self, stockage: StockageCategorie, description: str, acceptor: Callable[[str], bool], avertissement:str, ajouter: Callable[[StockageUnique|StockageNivele], None]):
        af.WrapperNoeud.__init__(self)
        self.stockage = stockage

        self.texte = af.Pave(description)

        self.element = af.MenuDeroulant()
        self.element.set_contenu_liste(
            [af.TexteMenuDeroulant(self.element,element) for element in stockage.elements]
        )
        self.element.set_contenu(af.Texte("Choisissez un type"))

        self.niveau = af.MenuDeroulant()
        self.niveau.set_contenu_liste(
            [
                af.TexteMenuDeroulant(self.niveau, "Unique"),
                af.TexteMenuDeroulant(self.niveau, "10 niveaux"),
            ]
        )
        self.niveau.set_contenu(af.Texte("Choisissez si l'élément est unique ou a 10 niveaux"))

        self.formulaire:Optional[FormulaireUnique|FormulaireNivele] = None

        self.formulaires:dict[str, FormulaireUnique|Tuple[FormulaireUnique, FormulaireNivele]] = {
            nom: (FormulaireUnique(stockage_[0], acceptor, avertissement, ajouter),
                  FormulaireNivele(stockage_[1], acceptor, avertissement, ajouter))
            if isinstance(stockage_, tuple)
            else FormulaireUnique(stockage_, acceptor, avertissement, ajouter)
            for nom, stockage_ in stockage.elements.items()
        }

        self.contenu = af.ListeMargeVerticale()
        self.contenu.set_contenu(
            [self.texte, self.element]
        )
        self.set_tailles(self.tailles)

    def set_courant(self, element: Cliquable | None):
        self.courant = element
        if element is None:
            self.set_actif()
        elif isinstance(element, af.Noeud):
            element.set_courant(element.courant)
            if element is self.element:
                self.change_element()
            elif element is self.niveau:
                self.change_niveau()
        else:
            element.set_actif()

    def change_element(self):
        """Change le formulaire."""
        assert isinstance(self.contenu, af.ListeMargeVerticale)
        if isinstance(self.element.courant, af.TexteMenuDeroulant):
            formulaire = self.formulaires[self.element.courant.get_texte()]
            if isinstance(formulaire, tuple):
                self.niveau.set_contenu(af.Texte("Choisissez si l'élément est unique ou a 10 niveaux"))
                self.contenu.set_contenu([self.texte, self.element, self.niveau])
            else:
                self.formulaire = formulaire
                self.contenu.set_contenu([self.texte, self.element, self.formulaire])
        else:
            self.contenu.set_contenu([self.texte, self.element])

    def change_niveau(self):
        """Change le formulaire."""
        assert isinstance(self.contenu, af.ListeMargeVerticale)
        assert isinstance(self.element.courant, af.TexteMenuDeroulant)
        formulaire = self.formulaires[self.element.courant.get_texte()]
        assert isinstance(formulaire, tuple)
        if isinstance(self.niveau.courant, af.TexteMenuDeroulant):
            if self.niveau.courant.get_texte() == "Unique":
                self.formulaire = formulaire[0]
                self.contenu.set_contenu([self.texte, self.element, self.niveau, self.formulaire])
            elif self.niveau.courant.get_texte() == "10 niveaux":
                self.formulaire = formulaire[1]
                self.contenu.set_contenu([self.texte, self.element, self.niveau, self.formulaire])
            else:
                raise ValueError(f"Le niveau {self.niveau.courant.get_texte()} n'existe pas.")
        else:
            self.contenu.set_contenu([self.texte, self.element, self.niveau])

    def affiche(self, screen: pygame.Surface, frame: int = 1, frame_par_tour: int = 1):
        af.WrapperNoeud.affiche(self, screen, frame, frame_par_tour)
        if self.element.est_courant:
            self.element.liste.affiche(screen, frame, frame_par_tour)
        if self.niveau.est_courant:
            self.niveau.liste.affiche(screen, frame, frame_par_tour)
