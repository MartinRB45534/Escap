"""Définitions des noeuds de l'arbre d'affichage."""

from __future__ import annotations
from typing import Literal, TYPE_CHECKING

from .affichable import Affichable
from .direction import Direction
from .noeud import Noeud

from .erreur import NavigationError

if TYPE_CHECKING:
    from .cliquable import Cliquable

class NoeudVertical(Noeud):
    """Un élément dont le contenu est disposé verticalement (donc next et previous correspondent à haut et bas)."""
    def through_previous(self):
        return self.in_up()

    def through_next(self):
        return self.in_down()

class NoeudVerticalProfondeurAgnostique(Noeud):
    """Un knot_vertical qui ne fait pas de différence entre in et through (pour haut et bas)."""
    def through_up(self):
        return self.in_up()

    def through_down(self):
        return self.in_down()

class NoeudHorizontal(Noeud):
    """Un élément dont le contenu est disposé horizontalement (donc next et previous correspondent à gauche et droite)."""
    def through_previous(self):
        return self.in_left()

    def through_next(self):
        return self.in_right()

class NoeudHorizontalProfondeurAgnostique(Noeud):
    """Un knot_horizontal qui ne fait pas de différence entre in et through (pour gauche et droite)."""
    def through_left(self):
        return self.in_left()

    def through_right(self):
        return self.in_right()

class NoeudHierarchiqueSinistre(Noeud):
    """Un élément dont le contenu est hiérarchique de gauche à droite (donc gauche et droite correspondent à out et in)."""
    def in_left(self):
        return self.in_out()

    def through_left(self):
        return self.through_out()

    def in_right(self):
        return self.in_in()

class NoeudHierarchiqueSinistreSommet(Noeud):
    """Au sommet de la hiérarchie (donc il n'y a rien à gauche)"""
    def through_left(self):
        return self.through_out()

    def in_right(self):
        return self.in_in()

class NoeudHierarchiqueSinistreBase(Noeud):
    """En bas de la hiérarchie (donc il n'y a rien à droite)"""
    def in_left(self):
        return self.in_out()

class NoeudHierarchiqueDextre(Noeud):
    """Un élément dont le contenu est hiérarchique de droite à gauche (donc gauche et droite correspondent à in et out)."""
    def in_left(self):
        return self.in_in()

    def through_right(self):
        return self.through_out()

    def in_right(self):
        return self.in_out()

class NoeudHierarchiqueDextreSommet(Noeud):
    """Au sommet de la hiérarchie (donc il n'y a rien à droite)"""
    def through_right(self):
        return self.through_out()

    def in_left(self):
        return self.in_in()

class NoeudHierarchiqueDextreBase(Noeud):
    """En bas de la hiérarchie (donc il n'y a rien à gauche)"""
    def in_right(self):
        return self.in_out()

class NoeudBloque(Noeud):
    """Un élément bloqué (pas de navigation, ni d'effets pour les clics)."""
    def navigue(self, direction: Direction) -> Cliquable|Literal[False]:
        if self.courant is None:
            raise NotImplementedError("Un Noeud_bloque doit avoir un élément courant.")
        res = self.courant.navigue(direction)
        if res is False:
            return False
        else:
            return self

    def select(self, selection: Affichable, droit: bool = False) -> None:
        raise NavigationError("Comment est-ce qu'on a pu sélectionner un noeud bloqué ?")

    def set_actif(self):
        if self.courant is None:
            raise NotImplementedError("Un Noeud_bloque doit avoir un élément courant.")
        self.actif = False
        self.courant.set_actif()
