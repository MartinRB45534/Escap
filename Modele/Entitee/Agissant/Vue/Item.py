"""Contient la classe ItemVu."""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import carte as crt

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from .agissant import AgissantVu
    from ....action.action import Action
    from ...item.item import Item
    from ....commons.etats_item import EtatsItems

class ItemVu:
    """Un item vu par un agissant."""
    def __init__(self, etat:Optional[EtatsItems]=None, priorite:Optional[float]=None, action:Optional[Action]=None, lanceur:Optional[AgissantVu]=None, direction:Optional[crt.Direction]=None, poids:Optional[float]=None, frottements:Optional[float]=None, hauteur:Optional[float]=None, nom:Optional[str]=None):
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
    """Transforme un item en item vu."""
    return ItemVu(
        nom=item.nom
    )
