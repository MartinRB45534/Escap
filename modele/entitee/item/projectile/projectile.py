"""Contient la classe Projectile."""

from __future__ import annotations
from typing import TYPE_CHECKING
import carte as crt

# Imports des classes parentes
from ..item import Item

# Imports utilisés dans le code
from ....affichage import SKIN_PROJECTILE

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ....effet.effet import Effet
    from ....labyrinthe.labyrinthe import Labyrinthe

class Projectile(Item):
    """La classe des items destinés à être lancés. Possèdent naturellement une vitesse non nulle."""
    def __init__(self,labyrinthe:Labyrinthe,vitesse:float,effets:list[Effet],position:crt.Position=crt.POSITION_ABSENTE):
        Item.__init__(self,labyrinthe,position)
        self.vitesse = vitesse
        self.effets = effets #Les effets déclenché lors du choc avec un agissant.

    @staticmethod
    def get_image():
        return SKIN_PROJECTILE
