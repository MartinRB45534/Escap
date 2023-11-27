"""
Ce module contient la classe Survolable, qui est un élément qui réagit au survol.
"""

from __future__ import annotations
from typing import Tuple, Literal
from .affichable import Affichable

class Survolable(Affichable):
    """Un élément qui réagit au survol"""
    def __init__(self):
        super().__init__()
        self.marque_survol = False #Est-ce que la souris est dessus ?

    def survol(self,position:Tuple[int,int]) -> Survolable|Literal[False]:
        """Renvoie l'élément survolé, ou False sinon (récursif pour d'autres éléments)."""
        if self.touche(position):
            self.marque_survol = True
            return self
        self.marque_survol = False
        return False