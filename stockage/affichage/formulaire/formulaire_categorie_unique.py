"""Contient la classe FormulaireCategorieUnique."""

from __future__ import annotations
from typing import  Callable, Optional

import pygame

import affichage as af

from ...stockage import StockageUnique, StockageCategorieUnique

from .formulaire_unique import FormulaireUnique

class FormulaireCategorieUnique(af.WrapperNoeud,af.NoeudVertical):
    """Un formulaire pour une catégorie qui n'a qu'un seul type d'élément, non nivelé."""
    def __init__(self, stockage: StockageCategorieUnique,
                 ajouter: Callable[[StockageUnique], None]):
        af.WrapperNoeud.__init__(self)
        af.NoeudVertical.__init__(self)
        self.stockage = stockage

        self.texte = af.Pave(stockage.description)

        self.element = af.MenuDeroulant(af.Texte("Choisissez un type"))
        self.element.set_contenu_liste(
            [af.TexteMenuDeroulant(self.element,element) for element in stockage.elements]
        )

        self.formulaire:Optional[FormulaireUnique] = None

        self.formulaires:dict[str, FormulaireUnique] = {
            nom: FormulaireUnique(stockage_, ajouter)
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
        else:
            element.set_actif()

    def change_element(self):
        """Change le formulaire."""
        if self.element.courant.get_texte() in self.formulaires:
            formulaire = self.formulaires[self.element.courant.get_texte()]
            self.formulaire = formulaire
            self.liste.set_contenu([self.texte, self.element, self.formulaire])
        else: # On a sélectionné "Choisissez un type"
            self.liste.set_contenu([self.texte, self.element])

    def in_right(self):
        # On continue vers l'intérieur (pour coller avec le reste)
        return self.in_in()

    def in_up(self):
        match self.courant:
            case self.element:
                return self
            case self.formulaire:
                assert self.formulaire is not None
                if not self.formulaire.in_up():
                    self.formulaire.unset_actif()
                    self.set_courant(self.element)
                    self.element.set_actif()
                return self
            case _:
                raise ValueError(f"Qu'est-ce que {self.courant} fait là ?")

    def in_down(self):
        match self.courant:
            case self.element:
                if self.formulaire:
                    self.unset_actif()
                    self.set_courant(self.formulaire)
                    input_nom = self.formulaire.inputs["nom"]
                    assert isinstance(input_nom, af.TexteInput)
                    self.formulaire.set_courant(input_nom)
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
