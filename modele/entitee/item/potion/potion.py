"""Contient la classe Potion."""

from __future__ import annotations
from typing import TYPE_CHECKING

import carte as crt

# Imports des classes parentes
from ..item import Item

# Imports utilisés dans le code
from ....affichage import SKIN_POTION

if TYPE_CHECKING:
    from ....action import Boit

class Potion(Item):
    """La classe des consommables qui peuvent se boire
       (ne requièrent pas de mana pour être activés)."""
    def __init__(self, position: crt.Position, action_portee: Boit):
        Item.__init__(self, position)
        self.action_portee = action_portee

    def frappe(self):
        self.action_portee.eclabousse()
        Item.frappe(self)

    @staticmethod
    def get_image():
        return SKIN_POTION
