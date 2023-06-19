from __future__ import annotations
from typing import List
from warnings import warn

from .Affichable import Affichable
from .Survolable import Survolable
from .Direction import Direction, Direction_aff

class Cliquable(Survolable): #Il faut être survolable pour être cliquable
    """Un élément qui réagit aux clics"""
    def __init__(self):
        self.tailles = (0,0) #La largeur et la hauteur (ou l'inverse ?)
        self.position = (0,0)
        self.marque_survol = False #Est-ce que la souris est dessus ?
        self.marque_actif = False #Est-ce que c'est l'élément actif  de la hiérarchie ?
        self.marque_courant = False #Est-ce que c'est l'élément courant de l'élément actif ?
        self.est_courant = False #Est-ce que c'est l'élément courant de son élément parent ?
        self.actif = True #Est-ce que l'élément est actif ?

    def trouve_actif(self):
        if self.actif:
            self.marque_actif = True
        else:
            warn(f"Erreur : on a atteint {self} qui n'est pas actif, mais n'est qu'un pauvre cliquable !")

    def set_actif(self):
        self.actif = True

    def unset_actif(self):
        self.actif = False

    def clique(self,position:List[int], droit:bool=False):
        clique = Affichable.clique(self,position,droit)
        if clique is self:
            self.set_actif()
        else:
            self.unset_actif()
        if clique:
            return self
        return False

    def navigue(self,direction: Direction):
        if self.actif: #On est à ce niveau
            if direction == Direction_aff.IN:
                return self
            return False
        else:
            warn(f"Erreur : on a atteint {self} qui n'est pas actif, mais ne navigue pas !")
