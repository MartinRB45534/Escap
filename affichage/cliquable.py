"""
Cliquable : un élément qui réagit aux clics
"""

from __future__ import annotations
from typing import Literal

from .survolable import Survolable
from .direction import Direction, DirectionAff
# from .erreur import NavigationError

class Cliquable(Survolable): #Il faut être survolable pour être cliquable
    """Un élément qui réagit aux clics"""
    def __init__(self):
        super().__init__()
        self.marque_actif = False #Est-ce que c'est l'élément actif  de la hiérarchie ?
        self.marque_courant = False #Est-ce que c'est l'élément courant de l'élément actif ?
        self.est_courant = False #Est-ce que c'est l'élément courant de son élément parent ?
        self.actif = False #Est-ce que l'élément est actif ?

    def trouve_actif(self):
        """Renvoie l'élément actif, ou False sinon (récursif pour d'autres éléments)."""
        if self.actif:
            self.marque_actif = True
        else:
            self.marque_actif = True # On ne serait pas là sinon
            # raise NavigationError(f"On a atteint {self} qui n'est pas actif, mais n'est qu'un pauvre cliquable !")

    def set_actif(self):
        """Rend l'élément actif."""
        self.actif = True

    def unset_actif(self):
        """Rend l'élément inactif."""
        self.actif = False

    def clique(self,position:tuple[int,int], _droit:bool=False) -> Cliquable|Literal[False]:
        """Renvoie l'élément cliqué, ou False sinon (récursif pour d'autres éléments)."""
        if self.touche(position):
            self.set_actif()
            return self
        self.unset_actif()
        return False

    def navigue(self,direction: Direction) -> Cliquable|Literal[False]:
        """Navigue dans la direction donnée, et renvoie l'élément navigué, ou False sinon
           (récursif pour d'autres éléments).
           """
        if self.actif: #On est à ce niveau
            if direction == DirectionAff.IN:
                return self
            return False
        else:
            raise ValueError(f"Erreur : on a atteint {self} qui n'est pas actif, mais ne navigue pas !")
