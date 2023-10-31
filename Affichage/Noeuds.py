"""Définitions des noeuds de l'arbre d'affichage."""

from __future__ import annotations
from typing import Literal, Optional, TYPE_CHECKING

from .affichable import Affichable
from .direction import Direction, DirectionAff
from .noeud import Noeud

if TYPE_CHECKING:
    from .cliquable import Cliquable

class NoeudVertical(Noeud):
    """Un élément dont le contenu est disposé verticalement (donc next et previous correspondent à haut et bas)."""
    def through_previous(self):
        assert self.courant is not None
        self.courant.unset_actif() # Devrait être inutile
        res = self.in_up()
        self.courant.set_actif()
        return res
    
    def through_next(self):
        if self.courant is None:
            raise RuntimeError("Noeud.through_next : self.courant is None")
        self.courant.unset_actif() # Devrait être inutile
        res = self.in_down()
        self.courant.set_actif()
        return res

class NoeudVerticalProfondeurAgnostique(Noeud):
    """Un knot_vertical qui ne fait pas de différence entre in et through (pour haut et bas)."""
    def through_up(self):
        assert self.courant is not None
        self.courant.unset_actif() # Devrait être inutile
        res = self.in_up()
        self.courant.set_actif()
        return res
    
    def through_down(self):
        assert self.courant is not None
        self.courant.unset_actif()
        res = self.in_down()
        self.courant.set_actif()
        return res

class NoeudHorizontal(Noeud):
    """Un élément dont le contenu est disposé horizontalement (donc next et previous correspondent à gauche et droite)."""
    def through_previous(self):
        assert self.courant is not None
        self.courant.unset_actif() # Devrait être inutile
        res = self.in_left()
        self.courant.set_actif()
        return res
    
    def through_next(self):
        assert self.courant is not None
        self.courant.unset_actif() # Devrait être inutile
        res = self.in_right()
        self.courant.set_actif()
        return res

class NoeudHorizontalProfondeurAgnostique(Noeud):
    """Un knot_horizontal qui ne fait pas de différence entre in et through (pour gauche et droite)."""
    def through_left(self):
        assert self.courant is not None
        self.courant.unset_actif() # Devrait être inutile
        res = self.in_left()
        self.courant.set_actif()
        return res
    
    def through_right(self):
        assert self.courant is not None
        self.courant.unset_actif()
        res = self.in_right()
        self.courant.set_actif()
        return res

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
    def navigue(self, direction: Direction) -> Optional[Cliquable]|Literal[False]:
        if self.actif:
            if direction == DirectionAff.IN:
                if self.courant is None:
                    raise(NotImplementedError("Un Noeud_bloque doit avoir un élément courant."))
                self.unset_actif()
                self.courant.set_actif()
                return self
            if direction == DirectionAff.OUT:
                self.unset_actif()
                return False
            if direction == DirectionAff.PREVIOUS:
                self.unset_actif()
                return False
            if direction == DirectionAff.NEXT:
                self.unset_actif()
                return False
        elif self.courant is None:
            raise NotImplementedError("Un Wrapper_bloque doit avoir un élément courant.")
        else:
            nav = self.courant.navigue(direction)
            if nav:
                self.select(nav)
                return self
            else:
                if direction == DirectionAff.OUT:
                    self.set_actif()
                    return self
            return self

    def select(self, selection: Affichable, droit: bool = False):
        pass
