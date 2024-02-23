"""
Les items sont des entitées inanimées qui peuvent être ramassées, lancées, etc.
"""

from __future__ import annotations
import carte as crt

# Imports des classes parentes
from .item import Item

# Imports utilisés dans le code
from ...affichage import SKIN_INGREDIENT

class Ingredient(Item):
    """La classe des ingrédients d'alchimie."""
    def __init__(self, position:crt.Position):
        Item.__init__(self,position)

    def get_classe(self):
        """Se limite aux catégories de l'inventaire."""
        return Ingredient

    @staticmethod
    def get_image():
        return SKIN_INGREDIENT
