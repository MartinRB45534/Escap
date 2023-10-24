from __future__ import annotations
from typing import TYPE_CHECKING, Set
import carte as crt

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ...labyrinthe.labyrinthe import Labyrinthe

# Imports des classes parentes
from .item import Item

class Cle(Item):
    """La classe des items qui ouvrent les portes (et les coffres ?)."""
    def __init__(self,labyrinthe:Labyrinthe,codes:Set[str],position:crt.Position=crt.POSITION_ABSENTE):
        Item.__init__(self,labyrinthe,position)
        self.codes = codes

    def get_codes(self):
        return self.codes

    @staticmethod
    def get_image():
        return SKIN_CLE

# Imports utilisés dans le code
from ...Affichage.skins import SKIN_CLE