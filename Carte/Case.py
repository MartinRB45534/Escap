"""Case"""

from __future__ import annotations
from typing import TYPE_CHECKING

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from .structure_spatiale.position import Position

# Pas de classe parente

class Case:
    """Classe représentant une case sur la carte."""
    def __init__(self,position:Position):
        # Par défaut, pas de murs.
        self.position = position
