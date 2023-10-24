from __future__ import annotations
from typing import TYPE_CHECKING
import carte as crt

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ...entitee.agissant.agissant import Agissant

# Imports des classes parentes
from .item import Item

class Oeuf(Item):
    def __init__(self,agissant:Agissant,position:crt.Position=crt.POSITION_ABSENTE):
        """Un item qui transporte un agissant. Va éclore avec le temps."""
        Item.__init__(self,agissant.labyrinthe,position)
        self.poids = 1
        self.agissant = agissant

    @staticmethod
    def get_image():
        return SKIN_OEUF
    
# Imports utilisés dans le code
from ...affichage.skins import SKIN_OEUF