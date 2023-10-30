"""Les timings des effets des items."""

from __future__ import annotations
from typing import TYPE_CHECKING

# Imports de la classe parente
from ..item import EffetItem

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ....entitee.item.cadavre import Cadavre

class OnFinTourCadavre(EffetItem): #Le sursis par exemple
    """La classe des effets appelés à la fin du tour."""
    def fin_tour(self,_item:Cadavre) -> None:
        """L'effet est appelé à la fin du tour de l'item."""
