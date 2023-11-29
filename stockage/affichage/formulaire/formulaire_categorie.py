"""Contient la classe FormulaireCategorie."""

from __future__ import annotations
from typing import  Callable, Optional

import pygame

import affichage as af

from ...stockage import StockageUnique, StockageNivele, StockageCategorie

from .formulaire_unique import FormulaireUnique
from .formulaire_nivele import FormulaireNivele

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
            nom: (FormulaireUnique(stockage_[0], ajouter),
                  FormulaireNivele(stockage_[1], ajouter))
            if isinstance(stockage_, tuple)
            else FormulaireUnique(stockage_, ajouter)
            for nom, stockage_ in stockage.elements.items()
        }

        self.liste = af.ListeMargeVerticale(shrink=True)
        self.liste.set_contenu(
            [self.texte, self.element]
        )

        self.contenu = af.WrapperMarge()
        self.contenu.set_contenu(self.liste)

        self.courant = self.element

    def set_courant(self, element: af.Cliquable | None):
        self.courant = element
        if element is None:
            self.set_actif()
        elif isinstance(element, af.Noeud):
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
