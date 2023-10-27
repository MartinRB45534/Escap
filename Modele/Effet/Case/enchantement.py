"""
Les enchantements de cases.
"""

from .case import EffetCase
from ..timings import Enchantement

class EnchantementCase(EffetCase,Enchantement):
    """Un effet (temporaire) qui enchante un item."""
    def __init__(self,temps_restant:float):
        Enchantement.__init__(self,temps_restant)
        EffetCase.__init__(self)