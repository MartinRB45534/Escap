"""Contient la classe Formulaire."""

from __future__ import annotations
from typing import  Callable, TypeVar, Optional

import pygame

import affichage as af
from affichage.cliquable import Cliquable

from ..stockage import StockageUnique, StockageNivele, StockageCategorie

# Le stockage hérite de StockageUnique
StockageUn = TypeVar("StockageUn", bound=StockageUnique)

class FormulaireUnique(af.WrapperNoeud):
    """Un formulaire, avec des champs à remplir pour créer un objet."""
    def __init__(self, stockage: type[StockageUn], acceptor: Callable[[str], bool],
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

        self.liste = af.ListeMargeVerticale(shrink=True)
        self.liste.set_contenu(
            sum([
                [texte, self.inputs[key], self.avertissements[key]]
                for key, texte in self.textes.items()
            ], []) # type: ignore # Pylance wants me to specify the type if that empty list smh
            + [af.BoutonFonction(af.SKIN_SHADE, "Ajouter", self.ajouter)]
        )

        self.contenu = af.WrapperMarge()
        self.contenu.set_contenu(self.liste)

        self.courant = self.inputs["nom"]

        self.super_ajouter = ajouter

    def form(self, nom:str, type_: type[int|str|float],
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
        self.set_tailles(self.tailles)

    def update(self):
        self.check()
        af.WrapperNoeud.update(self)

    def ajouter(self):
        """Ajoute l'objet."""
        self.check()
        if all([avertissement.get_texte() == "" for avertissement in self.avertissements.values()]):
            json = f"""{{{
", ".join([f'"{key}": "{input_.valeur}"' for key, input_ in self.inputs.items()])
}}}"""
            self.super_ajouter(self.stockage.parse(json))

    def select(self, selection: af.Cliquable, droit:bool=False):
        """Sélectionne l'élément."""
        self.update()
        af.WrapperNoeud.select(self, selection, droit)

    def set_actif(self):
        if self.courant:
            self.courant.set_actif()
        else:
            raise af.NavigationError("Les formulaires devraient toujours avoir un élément courant.")

    def unset_actif(self):
        if self.courant:
            self.courant.unset_actif()
        else:
            raise af.NavigationError("Les formulaires devraient toujours avoir un élément courant.")

    def in_up(self):
        if isinstance(self.courant, af.TexteInput):
            i = list(self.inputs.values()).index(self.courant)
            if i == 0:
                self.courant.unset_actif()
                return False
            self.courant.unset_actif()
            self.courant = list(self.inputs.values())[i-1]
            self.courant.set_actif()
            return self
        self.courant.unset_actif()
        self.courant = list(self.inputs.values())[-1]
        self.courant.set_actif()
        return self

    def in_down(self):
        if isinstance(self.courant, af.TexteInput):
            i = list(self.inputs.values()).index(self.courant)
            if i == len(self.inputs.values())-1:
                courant = self.liste.contenu[-1]
                if isinstance(courant, af.Bouton):
                    self.courant.unset_actif()
                    self.courant = courant
                    self.courant.set_actif()
                else:
                    raise ValueError(f"Que fait {self.courant} en dernier élément de la liste ?")
            else:
                self.courant.unset_actif()
                self.courant = list(self.inputs.values())[i+1]
                self.courant.set_actif()
            return self
        return False

    def through_out(self):
        self.courant.unset_actif()
        self.unset_actif() # Just to be really sure
        return False

class FormulaireModificationUnique(FormulaireUnique, af.NoeudVertical):
    """Un formulaire, avec des champs à remplir pour modifier un objet."""
    def __init__(self, stockage: type[StockageUn], acceptor: Callable[[str], bool],
                 avertissement:str, modifier: Callable[[StockageUn], None],
                 objet:StockageUn, supprimer: Callable[[StockageUn], None]):
        af.NoeudVertical.__init__(self)
        FormulaireUnique.__init__(self, stockage,
                                  lambda nom: acceptor(nom) or nom == objet.nom,
                                  avertissement, modifier)

        self.objet = objet
        self.inputs["nom"].valeur = objet.nom
        for key in stockage.champs:
            # Est-ce que c'est pire que d'utiliset la jsonification ?
            self.inputs[key].valeur = str(getattr(objet, key))

        self.bouton_modifier = af.BoutonFonction(af.SKIN_SHADE, "Modifier", self.ajouter)
        self.bouton_supprimer = af.BoutonFonction(af.SKIN_SHADE, "Supprimer", lambda: supprimer(objet))

        self.liste.set_contenu(
            sum([
                [texte, self.inputs[key], self.avertissements[key]]
                for key, texte in self.textes.items()
            ], []) # type: ignore # Pylance wants me to specify the type if that empty list smh
            + [self.bouton_modifier, self.bouton_supprimer]
        )

    def in_right(self):
        # On continue vers l'intérieur (pour coller avec le reste)
        return self.in_in()

    def in_up(self):
        if isinstance(self.courant, af.TexteInput):
            i = list(self.inputs.values()).index(self.courant)
            if i == 0:
                self.courant.unset_actif()
                return False
            self.courant.unset_actif()
            self.courant = list(self.inputs.values())[i-1]
            self.courant.set_actif()
            return self
        if self.courant is self.bouton_modifier:
            self.courant.unset_actif()
            self.courant = list(self.inputs.values())[-1]
            self.courant.set_actif()
            return self
        self.courant.unset_actif()
        self.courant = self.bouton_modifier
        self.courant.set_actif()
        return self

    def in_down(self):
        if isinstance(self.courant, af.TexteInput):
            i = list(self.inputs.values()).index(self.courant)
            if i == len(self.inputs.values())-1:
                courant = self.bouton_modifier
                self.courant.unset_actif()
                self.courant = courant
                self.courant.set_actif()
            else:
                self.courant.unset_actif()
                self.courant = list(self.inputs.values())[i+1]
                self.courant.set_actif()
            return self
        if self.courant is self.bouton_modifier:
            self.courant.unset_actif()
            self.courant = self.bouton_supprimer
            self.courant.set_actif()
            return self
        return False

    def through_up(self):
        return self.in_up()

    def through_down(self):
        return self.in_down()

StockageNi = TypeVar("StockageNi", bound=StockageNivele)

class FormulaireNivele(af.WrapperNoeud):
    """Un formulaire, avec des champs à remplir pour créer un objet."""
    def __init__(self, stockage: type[StockageNi], acceptor: Callable[[str], bool],
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
        self.valeurs:dict[str, list[str]] = {}

        for key in stockage.champs:
            self.form(key, stockage.champs[key], stockage.acceptors[key],
                      stockage.avertissements[key])

        self.liste = af.ListeMargeVerticale(shrink=True)
        self.liste.set_contenu(
            sum([
                [texte, self.inputs[key], self.avertissements[key]]
                for key, texte in self.textes.items()
            ], []) # type: ignore # Pylance wants me to specify the type if that empty list smh
            + [af.BoutonFonction(af.SKIN_SHADE, "Ajouter", self.ajouter)]
        )

        self.contenu = af.WrapperMarge()
        self.contenu.set_contenu(self.liste)

        self.courant = self.inputs["nom"]

        self.super_ajouter = ajouter

    def form(self, nom:str, type_: type[int|str|float],
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
        niveaux_problematiques: set[int] = set()
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
                f"""Les niveaux {', '.join([str(niveau) for niveau in niveaux_problematiques])}
ne sont pas valides.""")

    def update(self):
        self.check()
        if self.inputs["niveau"].accepte and self.niveau != int(self.inputs["niveau"].valeur):
            self.niveau = int(self.inputs["niveau"].valeur)
            for key, input_ in self.inputs.items():
                if key in ["nom", "niveau"]:
                    continue
                input_.valeur = self.valeurs[key][self.niveau-1]
        self.check()
        af.WrapperNoeud.update(self)

    def ajouter(self):
        """Ajoute l'objet."""
        self.check()
        if all([avertissement.get_texte() == "" for avertissement in self.avertissements.values()]):
            json = f"""{{"nom": "{self.inputs["nom"].valeur}", {
", ".join([f'"{key}": [{", ".join([valeur for valeur in valeurs])}]' for key, valeurs in self.valeurs.items()])
}}}"""
            self.super_ajouter(self.stockage.parse(json))

    def select(self, selection: af.Cliquable, droit:bool=False):
        """Sélectionne l'élément."""
        self.update()
        af.WrapperNoeud.select(self, selection, droit)

    def set_actif(self):
        if self.courant:
            self.courant.set_actif()
        else:
            raise af.NavigationError("Les formulaires devraient toujours avoir un élément courant.")

    def unset_actif(self):
        if self.courant:
            self.courant.unset_actif()
        else:
            raise af.NavigationError("Les formulaires devraient toujours avoir un élément courant.")

    def in_up(self):
        if isinstance(self.courant, af.TexteInput):
            i = list(self.inputs.values()).index(self.courant)
            if i == 0:
                self.courant.unset_actif()
                return False
            self.courant.unset_actif()
            self.courant = list(self.inputs.values())[i-1]
            self.courant.set_actif()
            return self
        self.courant.unset_actif()
        self.courant = list(self.inputs.values())[-1]
        self.courant.set_actif()
        return self

    def in_down(self):
        if isinstance(self.courant, af.TexteInput):
            i = list(self.inputs.values()).index(self.courant)
            if i == len(self.inputs.values())-1:
                courant = self.liste.contenu[-1]
                if isinstance(courant, af.Bouton):
                    self.courant.unset_actif()
                    self.courant = courant
                    self.courant.set_actif()
                else:
                    raise ValueError(f"Que fait {self.courant} en dernier élément de la liste ?")
            else:
                self.courant.unset_actif()
                self.courant = list(self.inputs.values())[i+1]
                self.courant.set_actif()
            return self
        return False

    def through_out(self):
        self.courant.unset_actif()
        self.unset_actif() # Just to be really sure
        return False

class FormulaireModificationNivele(FormulaireNivele, af.NoeudVertical):
    """Un formulaire, avec des champs à remplir pour modifier un objet."""
    def __init__(self, stockage: type[StockageNi], acceptor: Callable[[str], bool],
                 avertissement:str, modifier: Callable[[StockageNi], None],
                 objet:StockageNi, supprimer: Callable[[StockageNi], None]):
        af.NoeudVertical.__init__(self)
        FormulaireNivele.__init__(self, stockage,
                                  lambda nom: acceptor(nom) or nom == objet.nom,
                                  avertissement, modifier)

        self.objet = objet
        self.inputs["nom"].valeur = objet.nom
        for key in stockage.champs:
            # Est-ce que c'est pire que d'utiliset la jsonification ?
            self.inputs[key].valeur = str(getattr(objet, key)[0])
            self.valeurs[key] = [str(attr) for attr in getattr(objet, key)]

        self.bouton_modifier = af.BoutonFonction(af.SKIN_SHADE, "Modifier", self.ajouter)
        self.bouton_supprimer = af.BoutonFonction(af.SKIN_SHADE, "Supprimer", lambda: supprimer(objet))

        self.liste.set_contenu(
            sum([
                [texte, self.inputs[key], self.avertissements[key]]
                for key, texte in self.textes.items()
            ], []) # type: ignore # Pylance wants me to specify the type if that empty list smh
            + [self.bouton_modifier, self.bouton_supprimer]
        )

    def in_right(self):
        # On continue vers l'intérieur (pour coller avec le reste)
        return self.in_in()

    def in_up(self):
        if isinstance(self.courant, af.TexteInput):
            i = list(self.inputs.values()).index(self.courant)
            if i == 0:
                self.courant.unset_actif()
                return False
            self.courant.unset_actif()
            self.courant = list(self.inputs.values())[i-1]
            self.courant.set_actif()
            return self
        if self.courant is self.bouton_modifier:
            self.courant.unset_actif()
            self.courant = list(self.inputs.values())[-1]
            self.courant.set_actif()
            return self
        self.courant.unset_actif()
        self.courant = self.bouton_modifier
        self.courant.set_actif()
        return self

    def in_down(self):
        if isinstance(self.courant, af.TexteInput):
            i = list(self.inputs.values()).index(self.courant)
            if i == len(self.inputs.values())-1:
                courant = self.bouton_modifier
                self.courant.unset_actif()
                self.courant = courant
                self.courant.set_actif()
            else:
                self.courant.unset_actif()
                self.courant = list(self.inputs.values())[i+1]
                self.courant.set_actif()
            return self
        if self.courant is self.bouton_modifier:
            self.courant.unset_actif()
            self.courant = self.bouton_supprimer
            self.courant.set_actif()
            return self
        return False

    def through_up(self):
        return self.in_up()

    def through_down(self):
        return self.in_down()

StockageCat = TypeVar("StockageCat", bound=StockageCategorie)

class FormulaireCategorie(af.WrapperNoeud, af.NoeudVertical):
    """Un formulaire pour les catégories. Donne accès aux formulaires des éléments."""
    def __init__(self, stockage: StockageCategorie,
                 ajouter: Callable[[StockageUnique|StockageNivele], None]):
        af.WrapperNoeud.__init__(self)
        af.NoeudVertical.__init__(self)
        self.stockage = stockage

        self.texte = af.Pave(stockage.description)

        self.element = af.MenuDeroulant(af.Texte("Choisissez un type"))
        self.element.set_contenu_liste(
            [af.TexteMenuDeroulant(self.element,element) for element in stockage.elements]
        )

        self.menu_niveau = af.MenuDeroulant(
            af.Texte("Choisissez si l'élément est unique ou a 10 niveaux")
        )
        self.menu_niveau.set_contenu_liste(
            [
                af.TexteMenuDeroulant(self.menu_niveau, "Unique"),
                af.TexteMenuDeroulant(self.menu_niveau, "10 niveaux"),
            ]
        )

        self.niveau:Optional[af.MenuDeroulant] = None

        self.formulaire:Optional[FormulaireUnique|FormulaireNivele] = None

        self.formulaires:dict[str, FormulaireUnique|tuple[FormulaireUnique, FormulaireNivele]] = {
            nom: (FormulaireUnique(stockage_[0], stockage.acceptor, stockage.avertissement, ajouter),
                  FormulaireNivele(stockage_[1], stockage.acceptor, stockage.avertissement, ajouter))
            if isinstance(stockage_, tuple)
            else FormulaireUnique(stockage_, stockage.acceptor, stockage.avertissement, ajouter)
            for nom, stockage_ in stockage.elements.items()
        }

        self.liste = af.ListeMargeVerticale(shrink=True)
        self.liste.set_contenu(
            [self.texte, self.element]
        )

        self.contenu = af.WrapperMarge()
        self.contenu.set_contenu(self.liste)

        self.courant = self.element

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
        if self.element.courant.get_texte() in self.formulaires:
            formulaire = self.formulaires[self.element.courant.get_texte()]
            if isinstance(formulaire, tuple):
                self.niveau = self.menu_niveau
                self.niveau.set_contenu(
                    af.Texte("Choisissez si l'élément est unique ou a 10 niveaux"))
                self.liste.set_contenu([self.texte, self.element, self.niveau])
            else:
                self.niveau = None
                self.formulaire = formulaire
                self.liste.set_contenu([self.texte, self.element, self.formulaire])
        else: # On a sélectionné "Choisissez un type"
            self.liste.set_contenu([self.texte, self.element])

    def change_niveau(self):
        """Change le formulaire."""
        formulaire = self.formulaires[self.element.courant.get_texte()]
        if isinstance(formulaire, tuple) and self.niveau:
            match self.niveau.courant.get_texte():
                case "Unique":
                    self.formulaire = formulaire[0]
                    self.liste.set_contenu([self.texte, self.element, self.niveau, self.formulaire])
                case "10 niveaux":
                    self.formulaire = formulaire[1]
                    self.liste.set_contenu([self.texte, self.element, self.niveau, self.formulaire])
                case "Choisissez si l'élément est unique ou a 10 niveaux":
                    self.liste.set_contenu([self.texte, self.element, self.niveau])
                case _:
                    raise ValueError(f"Le niveau {self.niveau.courant.get_texte()} n'existe pas.")
        else:
            raise ValueError("On a accès à un choix de niveau pour un élément unique")

    def in_right(self):
        # On continue vers l'intérieur (pour coller avec le reste)
        return self.in_in()

    def in_up(self):
        match self.courant:
            case self.element:
                return self
            case self.niveau:
                self.set_courant(self.element)
                self.element.set_actif()
                return self
            case self.formulaire:
                assert self.formulaire is not None
                if not self.formulaire.in_up():
                    self.formulaire.unset_actif()
                    if self.niveau:
                        self.set_courant(self.niveau)
                        self.niveau.set_actif()
                    else:
                        self.set_courant(self.element)
                        self.element.set_actif()
                return self
            case _:
                raise ValueError(f"Qu'est-ce que {self.courant} fait là ?")

    def in_down(self):
        match self.courant:
            case self.element:
                if self.niveau:
                    self.set_courant(self.niveau)
                    self.niveau.set_actif()
                elif self.formulaire:
                    self.unset_actif()
                    self.set_courant(self.formulaire)
                    self.formulaire.set_courant(self.formulaire.inputs["nom"])
                    self.formulaire.set_actif()
                return self
            case self.niveau:
                if self.formulaire:
                    self.unset_actif()
                    self.set_courant(self.formulaire)
                    self.formulaire.set_courant(self.formulaire.inputs["nom"])
                    self.formulaire.set_actif()
                return self
            case self.formulaire:
                assert self.formulaire is not None
                self.formulaire.in_down()
                return self
            case _:
                raise ValueError(f"Qu'est-ce que {self.courant} fait là ?")

    def through_up(self):
        if self.courant is self.formulaire:
            return self.in_up()
        return self

    def through_down(self):
        if self.courant is self.formulaire:
            return self.in_down()
        return self

    def affiche(self, screen: pygame.Surface, frame: int = 1, frame_par_tour: int = 1):
        af.WrapperNoeud.affiche(self, screen, frame, frame_par_tour)
        if self.courant is self.element:
            self.element.affiche_liste(screen, (5, 5), frame, frame_par_tour)
        if self.niveau and self.courant is self.niveau:
            self.niveau.affiche_liste(screen, (5, 5), frame, frame_par_tour)

class FormulaireCategorieUnique(af.WrapperNoeud,af.NoeudVertical):
    """Un formulaire pour une catégorie qui n'a qu'un seul type d'élément, non nivelé."""
    def __init__(self, stockage: StockageCategorie,
                 ajouter: Callable[[StockageUnique], None]):
        af.WrapperNoeud.__init__(self)
        af.NoeudVertical.__init__(self)
        self.stockage = stockage
        element = list(stockage.elements.values())[0]
        if isinstance(element, tuple):
            raise ValueError("Une catégorie unique ne peut pas avoir un formulaire double.")

        self.texte = af.Pave(stockage.description)

        self.formulaire:FormulaireUnique = FormulaireUnique(element, stockage.acceptor, stockage.avertissement, ajouter)

        self.liste = af.ListeMargeVerticale(shrink=True)
        self.liste.set_contenu([self.texte, self.formulaire])

        self.contenu = af.WrapperMarge()
        self.contenu.set_contenu(self.liste)

        self.courant = self.formulaire

        self.set_tailles(self.tailles)

    def set_courant(self, element: Cliquable | None):
        self.courant = element
        if element is None:
            self.set_actif()
        elif isinstance(element, af.Noeud):
            element.set_courant(element.courant)
        else:
            element.set_actif()

    def in_right(self):
        # On continue vers l'intérieur (pour coller avec le reste)
        return self.in_in()

    def in_up(self):
        return self.formulaire.in_up()

    def in_down(self):
        return self.formulaire.in_down()

    def through_up(self):
        return self.in_up()

    def through_down(self):
        return self.in_down()

    def affiche(self, screen: pygame.Surface, frame: int = 1, frame_par_tour: int = 1):
        af.WrapperNoeud.affiche(self, screen, frame, frame_par_tour)

class FormulaireCategorieNivele(af.WrapperNoeud, af.NoeudVertical):
    """Un formulaire pour une catégorie qui n'a qu'un seul type d'élément, nivelé."""
    def __init__(self, stockage: StockageCategorie,
                 ajouter: Callable[[StockageUnique|StockageNivele], None]):
        af.WrapperNoeud.__init__(self)
        af.NoeudVertical.__init__(self)
        self.stockage = stockage
        element = list(stockage.elements.values())[0]
        if not isinstance(element, tuple):
            raise ValueError("Une catégorie nivelée doit avoir un formulaire double.")

        self.texte = af.Pave(stockage.description)

        self.niveau = af.MenuDeroulant(
            af.Texte("Choisissez si l'élément est unique ou a 10 niveaux")
        )
        self.niveau.set_contenu_liste(
            [
                af.TexteMenuDeroulant(self.niveau, "Unique"),
                af.TexteMenuDeroulant(self.niveau, "10 niveaux"),
            ]
        )

        self.formulaire:Optional[FormulaireUnique|FormulaireNivele] = None

        self.formulaires:tuple[FormulaireUnique, FormulaireNivele] = (
            FormulaireUnique(element[0], stockage.acceptor, stockage.avertissement, ajouter),
            FormulaireNivele(element[1], stockage.acceptor, stockage.avertissement, ajouter))

        self.liste = af.ListeMargeVerticale(shrink=True)
        self.liste.set_contenu(
            [self.texte, self.niveau]
        )

        self.contenu = af.WrapperMarge()
        self.contenu.set_contenu(self.liste)

        self.courant = self.niveau

        self.set_tailles(self.tailles)

    def set_courant(self, element: Cliquable | None):
        self.courant = element
        if element is None:
            self.set_actif()
        elif isinstance(element, af.Noeud):
            element.set_courant(element.courant)
            if element is self.niveau:
                self.change_niveau()
        else:
            element.set_actif()

    def change_niveau(self):
        """Change le formulaire."""
        match self.niveau.courant.get_texte():
            case "Unique":
                self.formulaire = self.formulaires[0]
                self.liste.set_contenu([self.texte, self.niveau, self.formulaire])
            case "10 niveaux":
                self.formulaire = self.formulaires[1]
                self.liste.set_contenu([self.texte, self.niveau, self.formulaire])
            case "Choisissez si l'élément est unique ou a 10 niveaux":
                self.liste.set_contenu([self.texte, self.niveau])
            case _:
                raise ValueError(f"Le niveau {self.niveau.courant.get_texte()} n'existe pas.")

    def in_right(self):
        # On continue vers l'intérieur (pour coller avec le reste)
        return self.in_in()

    def in_up(self):
        match self.courant:
            case self.niveau:
                return self
            case self.formulaire:
                assert self.formulaire is not None
                if not self.formulaire.in_up():
                    self.formulaire.unset_actif()
                    self.set_courant(self.niveau)
                    self.niveau.set_actif()
                return self
            case _:
                raise ValueError(f"Qu'est-ce que {self.courant} fait là ?")

    def in_down(self):
        match self.courant:
            case self.niveau:
                if self.formulaire:
                    self.unset_actif()
                    self.set_courant(self.formulaire)
                    self.formulaire.set_courant(self.formulaire.inputs["nom"])
                    self.formulaire.set_actif()
                return self
            case self.formulaire:
                assert self.formulaire is not None
                self.formulaire.in_down()
                return self
            case _:
                raise ValueError(f"Qu'est-ce que {self.courant} fait là ?")

    def through_up(self):
        if self.courant is self.formulaire:
            return self.in_up()
        return self

    def through_down(self):
        if self.courant is self.formulaire:
            return self.in_down()
        return self

    def affiche(self, screen: pygame.Surface, frame: int = 1, frame_par_tour: int = 1):
        af.WrapperNoeud.affiche(self, screen, frame, frame_par_tour)
        if self.niveau and self.courant is self.niveau:
            self.niveau.affiche_liste(screen, (5, 5), frame, frame_par_tour)
