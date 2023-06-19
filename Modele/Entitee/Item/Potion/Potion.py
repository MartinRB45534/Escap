from __future__ import annotations
from typing import TYPE_CHECKING
import Carte as crt

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ....Labyrinthe.Labyrinthe import Labyrinthe
    from ....Effet.Effet import Effet

# Imports des classes parentes
from ..Item import Consommable

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
from ....Affichage.Skins import SKIN_POTION
from ..Item import Item