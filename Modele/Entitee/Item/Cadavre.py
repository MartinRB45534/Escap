from __future__ import annotations
from typing import TYPE_CHECKING
import Carte as crt

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ..Agissant.Agissant import Agissant

# Imports des classes parentes
from .Item import Item

class Cadavre(Item):
    def __init__(self,agissant:Agissant,position:crt.Position=crt.POSITION_ABSENTE):
        """Les restes d'un agissant. Peut être ressuscité ou réanimé. Certains monstres se vendent aussi à bon prix."""
        Item.__init__(self,agissant.labyrinthe,position)
        self.poids = 1
        self.agissant = agissant

    @staticmethod
    def get_image():
        return SKIN_CADAVRE

# Imports utilisés dans le code
from Old_Affichage.Skins.Skins import SKIN_CADAVRE