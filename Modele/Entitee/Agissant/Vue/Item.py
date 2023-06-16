from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import Carte as crt

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from .Agissant import Agissant_vu
    from ....Action.Action import Action
    from ...Item.Item import Item
    from ...Item.Etats import Etats_items

class Item_vu:
    def __init__(self, etat:Optional[Etats_items]=None, priorite:Optional[float]=None, action:Optional[Action]=None, lanceur:Optional[Agissant_vu]=None, direction:Optional[crt.Direction]=None, poids:Optional[float]=None, frottements:Optional[float]=None, hauteur:Optional[float]=None, nom:Optional[str]=None):
        self.etat = etat
        self.priorite = priorite
        self.action = action
        self.lanceur = lanceur
        self.direction = direction
        self.poids = poids
        self.frottements = frottements
        self.hauteur = hauteur
        self.nom = nom

def voit_item(item:Item):
    return Item_vu(
        nom=item.nom
    )