"""Contient la classe Potion."""

from __future__ import annotations
from typing import TYPE_CHECKING
import carte as crt

# Imports des classes parentes
from ..item import Consommable

# Imports utilisés dans le code
from ....affichage import SKIN_POTION

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ....labyrinthe.labyrinthe import Labyrinthe
    from ....effet.agissant.agissant import EffetAgissant

class Potion(Consommable):
    """La classe des consommables qui peuvent se boire (ne requièrent pas de magie pour être activés)."""
    def __init__(self,labyrinthe:Labyrinthe,effet:EffetAgissant,duree:float,position:crt.Position=crt.POSITION_ABSENTE):
        Consommable.__init__(self,labyrinthe,position)
        self.duree = duree
        self.effet = effet

    @staticmethod
    def get_image():
        return SKIN_POTION
