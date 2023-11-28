"""Contient la classe FormulaireCategorieUnique."""

from __future__ import annotations
from typing import  Callable, Optional

import pygame

import affichage as af

from ...stockage import StockageUnique, StockageNivele, StockageCategorie

from .formulaire_unique import FormulaireUnique
from .formulaire_nivele import FormulaireNivele

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

    def set_courant(self, element: af.Cliquable | None):
        self.courant = element
        if element is None:
            self.set_actif()
        elif isinstance(element, af.Noeud):
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
