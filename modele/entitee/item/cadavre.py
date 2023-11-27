"""Contient la classe Cadavre."""

from __future__ import annotations
from typing import TYPE_CHECKING
import carte as crt

# Imports des classes parentes
from .item import Item

# Imports utilisés dans le code
from ...affichage import SKIN_CADAVRE

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ..agissant.agissant import Agissant

class Cadavre(Item):
    """Les restes d'un agissant. Peut être ressuscité ou réanimé. Certains monstres se vendent aussi à bon prix."""
    def __init__(self,agissant:Agissant,position:crt.Position=crt.POSITION_ABSENTE):
        Item.__init__(self,agissant.labyrinthe,position)
        self.poids = 1
        self.agissant = agissant

    @staticmethod
    def get_image():
        return SKIN_CADAVRE
