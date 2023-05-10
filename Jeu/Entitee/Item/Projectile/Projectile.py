from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Jeu.Effet.Effet import Effet

from Jeu.Entitee.Item.Item import *

class Projectile(Item):
    """La classe des items destinés à être lancés. Possèdent naturellement une vitesse non nulle."""
    def __init__(self,position:Optional[Position]=None,vitesse:float=0,effets:List[Effet]=[]):
        Item.__init__(self,position)
        self.vitesse = vitesse
        self.effets = effets #Les effets déclenché lors du choc avec un agissant.

    def get_classe(self):
        return Projectile

    def get_titre(self,observation=0):
        return "Projectile"

    @staticmethod
    def get_image():
        return SKIN_PROJECTILE