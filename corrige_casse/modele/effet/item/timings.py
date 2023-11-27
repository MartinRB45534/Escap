"""Les timings des effets des items."""

from __future__ import annotations
from typing import TYPE_CHECKING

# Imports de la classe parente
from .item import EffetItem

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ...entitee.item.item import Item

class OnDebutTourItem(EffetItem):
    """La classe des effets appelés au début du tour d'un item."""
    def debut_tour(self,_item:Item) -> None:
        """L'effet est appelé au début du tour de l'item."""

class OnFinTourItem(EffetItem): #Le sursis par exemple
    """La classe des effets appelés à la fin du tour."""
    def fin_tour(self,_item:Item) -> None:
        """L'effet est appelé à la fin du tour de l'item."""
