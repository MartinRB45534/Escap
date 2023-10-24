from __future__ import annotations
from typing import TYPE_CHECKING
import carte as crt

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ....effet.effet import Effet
    from ....labyrinthe.labyrinthe import Labyrinthe

# Imports des classes parentes
from ..item import Consommable

class Parchemin(Consommable):
    """La classe des consommables qui s'activent avec du mana."""
    def __init__(self,labyrinthe:Labyrinthe,effet:Effet,cout:float,duree:float=2,position:crt.Position=crt.POSITION_ABSENTE):
        Item.__init__(self,labyrinthe,position)
        self.effet = effet
        self.duree = duree
        self.cout = cout

    def get_classe(self):
        return Parchemin

    @staticmethod
    def get_image():
        return SKIN_PARCHEMIN

# Imports utilisés dans le code
from ....Affichage.skins import SKIN_PARCHEMIN
from ..item import Item