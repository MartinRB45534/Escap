"""Contient les classes Placeholder et Placeheldholder."""

from __future__ import annotations
from typing import Optional, Tuple

from .affichable import Affichable
from .direction import Direction
from .cliquable import Cliquable
from .wrapper import Wrapper
from .noeud import Noeud
from .wrapper_noeud import WrapperNoeud

class Placeheldholder(WrapperNoeud):
    """L'élément où le placeheld du placeholder est placé."""
    def clique(self,position:Tuple[int,int], droit:bool=False):
        clique = Wrapper.clique(self,position,droit)
        if clique is self:
            self.set_actif()
        elif isinstance(clique, Placeheldholder):
            res = self.clique_placeholder(clique, droit)
            if not res:
                self.unset_actif()
                return clique
        elif clique:
            self.select(clique, droit)
            self.unset_actif()
        # else:
        #     self.unset_actif()
        if clique:
            return self
        return False

    def set_actif(self):
        if isinstance(self.contenu,Cliquable):
            self.contenu.set_actif()

    def unset_actif(self):
        if isinstance(self.contenu,Cliquable):
            self.contenu.unset_actif()

    def trouve_actif(self):
        if isinstance(self.contenu,Cliquable):
            self.contenu.trouve_actif()

class Placeholder(Noeud):
    """Un élément qui lie à un autre, ailleurs."""
    def __init__(self, placeheldholder:Placeheldholder, placeheld:Optional[Cliquable], placeheldholder_ajuster:Optional[Affichable]=None):
        Noeud.__init__(self)
        self.placeheldholder = placeheldholder
        self.placeheldholder_ajuster = placeheldholder_ajuster if placeheldholder_ajuster else placeheldholder # L'élément le plus proche dans la parenté du placeheldholder dont la taille n'est pas affectée par la taille du placeheldholder (celui jusqu'auquel il faut remonter pour ajuster la taille du placeheldholder)
        self.set_courant(placeheld)

    def set_courant(self,element: Optional[Cliquable]):
        self.courant = element
        self.set_actif()

    def set_actif(self):
        assert self.courant is not None
        super().set_actif()
        self.placeheldholder.set_contenu(self.courant)
        if self.placeheldholder_ajuster.tailles != (0,0):
            self.placeheldholder_ajuster.set_tailles(self.placeheldholder_ajuster.tailles)
        self.courant.set_actif()

    def unset_actif(self):
        assert self.courant is not None
        super().unset_actif()
        self.courant.unset_actif()

    def trouve_actif(self):
        assert self.courant is not None
        self.marque_actif = True
        self.courant.trouve_actif()

    def clique(self, position: Tuple[int,int], droit:bool=False):
        return Cliquable.clique(self, position, droit) # On ne veut pas que le clique soit propagé

    def clique_placeholder(self,placeheldholder:Placeheldholder, _droit:bool=False):
        if placeheldholder is self.placeheldholder and self.courant is placeheldholder.contenu:
            return self
        return False

    def survol(self, position: Tuple[int,int]):
        return Cliquable.survol(self, position)
    
    def navigue(self, direction: Direction):
        assert self.courant is not None
        res = self.courant.navigue(direction)
        self.actif = self.courant.actif
        return res

    def update(self):
        assert self.courant is not None
        super().update()
        self.courant.update()
        if self.placeheldholder.courant is self.courant and self.placeheldholder_ajuster.tailles != (0,0):
            self.placeheldholder_ajuster.set_tailles(self.placeheldholder_ajuster.tailles)
