"""
Les enchantements d'items.
"""

from .item import EffetItem
from ..timings import Enchantement

class EnchantementItem(EffetItem,Enchantement):
    """Un effet (temporaire) qui enchante un item."""
    def __init__(self,temps_restant:float):
        Enchantement.__init__(self,temps_restant)
        EffetItem.__init__(self)