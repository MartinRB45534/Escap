"""Contient la classe Parchemin."""

from __future__ import annotations
from typing import TYPE_CHECKING

import carte as crt

# Imports des classes parentes
from ..item import Item

# Imports utilisés dans le code
from ....affichage import SKIN_PARCHEMIN

if TYPE_CHECKING:
    from ....action import Lit, Magie

class Parchemin(Item):
    """La classe des consommables qui s'activent avec du mana."""
    action_portee: Lit|Magie
    def __init__(self, position: crt.Position):
        Item.__init__(self, position)

    @staticmethod
    def get_image():
        return SKIN_PARCHEMIN
