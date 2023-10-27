from __future__ import annotations
from typing import TYPE_CHECKING
import carte as crt

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ....labyrinthe.labyrinthe import Labyrinthe
    from ....effet.effet import Effet

# Imports des classes parentes
from ..item import Consommable

class Potion(Consommable):
    """La classe des consommables qui peuvent se boire (ne requièrent pas de magie pour être activés)."""
    def __init__(self,labyrinthe:Labyrinthe,effet:Effet,duree:float=2,position:crt.Position=crt.POSITION_ABSENTE):
        Item.__init__(self,labyrinthe,position)
        self.duree = duree
        self.effet = effet

    @staticmethod
    def get_image():
        return SKIN_POTION

# Imports utilisés dans le code
from ....affichage.skins import SKIN_POTION
from ..item import Item