from __future__ import annotations
from typing import TYPE_CHECKING, List
import Carte as crt

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ....Effet.Effet import Effet
    from ....Labyrinthe.Labyrinthe import Labyrinthe

# Imports des classes parentes
from ..Item import Item

class Projectile(Item):
    """La classe des items destinés à être lancés. Possèdent naturellement une vitesse non nulle."""
    def __init__(self,labyrinthe:Labyrinthe,vitesse:float=0,effets:List[Effet]=[],position:crt.Position=crt.POSITION_ABSENTE):
        Item.__init__(self,labyrinthe,position)
        self.vitesse = vitesse
        self.effets = effets #Les effets déclenché lors du choc avec un agissant.

    @staticmethod
    def get_image():
        return SKIN_PROJECTILE

# Imports utilisés dans le code
from ....Affichage.Skins import SKIN_PROJECTILE