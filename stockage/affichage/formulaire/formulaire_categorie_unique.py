"""Contient la classe FormulaireCategorieUnique."""

from __future__ import annotations
from typing import  Callable

import pygame

import affichage as af

from ...stockage import StockageUnique, StockageCategorie

from .formulaire_unique import FormulaireUnique

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

        self.formulaire:FormulaireUnique = FormulaireUnique(element, ajouter)

        self.liste = af.ListeMargeVerticale(shrink=True)
        self.liste.set_contenu([self.texte, self.formulaire])

        self.contenu = af.WrapperMarge()
        self.contenu.set_contenu(self.liste)

        self.courant = self.formulaire

    def set_courant(self, element: af.Cliquable | None):
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
