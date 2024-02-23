"""Contient la classe Cle."""

from __future__ import annotations
import carte as crt

# Imports des classes parentes
from .item import Item

# Imports utilisés dans le code
from ...affichage import SKIN_CLE

class Cle(Item):
    """La classe des items qui ouvrent les portes (et les coffres ?)."""
    def __init__(self,position:crt.Position,codes:set[str]):
        Item.__init__(self,position)
        self.codes = codes

    def get_codes(self):
        """Renvoie les codes de la clef."""
        return self.codes

    @staticmethod
    def get_image():
        return SKIN_CLE
