from __future__ import annotations
from typing import TYPE_CHECKING, List, Dict, Set, Type, Optional
import Carte as crt

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ..Inventaire import Inventaire
    from .Item import Item_vu

class Inventaire_vu:
    def __init__(self, items:Set[Item_vu], equippement:Set[Item_vu]):
        self.items = items
        self.equippement = equippement

def voit_inventaire(inventaire:Inventaire) -> Inventaire_vu:
    return Inventaire_vu(
        items={voit_item(item) for item in inventaire.equippements}, # On ne voit que l'équippement
        equippement={voit_item(item) for item in inventaire.equippements},
    )

from .Item import voit_item