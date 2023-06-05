from __future__ import annotations
from typing import TYPE_CHECKING

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from .Structure_spatiale.Position import Position

# Pas de classe parente

class Mur:
    def __init__(self,cible:Position, niveau:int):
        self.niveau = niveau
        self.ferme = False
        self.cible = cible