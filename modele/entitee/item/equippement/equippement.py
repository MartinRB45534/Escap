"""Contient la classe Equippement."""

from __future__ import annotations
from typing import TYPE_CHECKING
import carte as crt

# Imports des classes parentes
from ..item import Item

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ...agissant.agissant import Agissant

class Equippement(Item):
    """La classe des items qui peuvent être portés. Sont toujours actifs tant qu'ils sont portés."""
    def __init__(self,position:crt.Position=crt.POSITION_ABSENTE):
        Item.__init__(self,position)
        self.taux_stats:dict[str,float] = {}

    def equippe(self,agissant:Agissant):
        """Équipe l'item sur l'agissant."""
        # Peut avoir des effets sur les stats de l'item

    def desequippe(self):
        """Déséquipe l'item."""
        for cause in self.taux_stats:
            if cause == "incompatibilité porteur":
                self.taux_stats.pop(cause)
        # On retire les effets sur les stats de l'item
