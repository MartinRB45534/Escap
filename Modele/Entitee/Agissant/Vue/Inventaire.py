"""Vue d'un inventaire."""

from __future__ import annotations
from typing import TYPE_CHECKING, Set

from .item import voit_item

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ..inventaire import Inventaire
    from .item import ItemVu

class InventaireVu:
    def __init__(self, items:Set[ItemVu], equippement:Set[ItemVu]):
        self.items = items
        self.equippement = equippement

def voit_inventaire(inventaire:Inventaire) -> InventaireVu:
    """Transforme un inventaire en inventaire vu."""
    return InventaireVu(
        items={voit_item(item) for item in inventaire.equippements}, # On ne voit que l'équippement
        equippement={voit_item(item) for item in inventaire.equippements},
    )
