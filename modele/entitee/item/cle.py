"""Contient la classe Cle."""

from __future__ import annotations
from typing import TYPE_CHECKING
import carte as crt

# Imports des classes parentes
from .item import Item

# Imports utilisés dans le code
from ...affichage import SKIN_CLE

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ...labyrinthe.labyrinthe import Labyrinthe

class Cle(Item):
    """La classe des items qui ouvrent les portes (et les coffres ?)."""
    def __init__(self,labyrinthe:Labyrinthe,codes:set[str],position:crt.Position=crt.POSITION_ABSENTE):
        Item.__init__(self,labyrinthe,position)
        self.codes = codes

    def get_codes(self):
        """Renvoie les codes de la clef."""
        return self.codes

    @staticmethod
    def get_image():
        return SKIN_CLE
