"""Contient la classe Oeuf."""

from __future__ import annotations
from typing import TYPE_CHECKING
import carte as crt

# Imports des classes parentes
from .item import Item

# Imports utilisés dans le code
from ...affichage import SKIN_OEUF

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ...entitee.agissant.agissant import Agissant

class Oeuf(Item):
    """Un item qui transporte un agissant. Va éclore avec le temps."""
    def __init__(self,agissant:Agissant,position:crt.Position):
        Item.__init__(self,position)
        self.agissant = agissant

    @staticmethod
    def get_image():
        return SKIN_OEUF
