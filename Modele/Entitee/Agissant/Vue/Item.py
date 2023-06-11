from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import Carte as crt

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from .Agissant import Agissant_vu
    from ...Item.Item import Item

class Item_vu:
    def __init__(self, etat:str, priorite:float, lanceur:Optional[Agissant_vu], direction:Optional[crt.Direction], poids:float, frottements:float, hauteur:float, nom:str):
        self.etat = etat
        self.priorite = priorite
        self.lanceur = lanceur
        self.direction = direction
        self.poids = poids
        self.frottements = frottements
        self.hauteur = hauteur
        self.nom = nom

def voit_item(item:Item):
    return Item_vu(
        item.etat,
        item.priorite,
        voit_agissant(item.lanceur) if item.lanceur else None,
        item.direction,
        item.poids,
        item.frottements,
        item.hauteur,
        item.nom
    )

from .Agissant import voit_agissant