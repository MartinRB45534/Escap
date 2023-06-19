from __future__ import annotations
from typing import TYPE_CHECKING
import Carte as crt

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ...Entitee.Agissant.Agissant import Agissant

# Imports des classes parentes
from .Item import Item

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
from ...Affichage.Skins import SKIN_OEUF