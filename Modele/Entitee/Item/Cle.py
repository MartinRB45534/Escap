from __future__ import annotations
from typing import TYPE_CHECKING, Set
import Carte as crt

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ...Labyrinthe.Labyrinthe import Labyrinthe

# Imports des classes parentes
from .Item import Item

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
from ...Affichage.Skins import SKIN_CLE