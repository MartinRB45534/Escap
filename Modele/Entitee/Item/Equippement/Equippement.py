from __future__ import annotations
from typing import TYPE_CHECKING, Dict
import Carte as crt

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ...Agissant.Agissant import Agissant
    from ....Labyrinthe.Labyrinthe import Labyrinthe

# Imports des classes parentes
from ..Item import Item

class Equippement(Item):
    """La classe des items qui peuvent être portés. Sont toujours actifs tant qu'ils sont portés."""
    def __init__(self,labyrinthe:Labyrinthe,position:crt.Position=crt.POSITION_ABSENTE):
        Item.__init__(self,labyrinthe,position)
        self.taux_stats:Dict[str,float] = {}

    def equippe(self,agissant:Agissant):
        pass

    def desequippe(self):
        for cause in self.taux_stats:
            if cause == "incompatibilité porteur":
                self.taux_stats.pop(cause)
