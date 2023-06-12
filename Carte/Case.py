from __future__ import annotations
from typing import TYPE_CHECKING

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from .Structure_spatiale.Position import Position

# Pas de classe parente

class Case:
    def __init__(self,position:Position):
        # Par défaut, pas de murs.
        self.position = position