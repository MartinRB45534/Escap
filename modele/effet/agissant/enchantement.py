"""
Les enchantements d'agissants.
"""

from .agissant import EffetAgissant
from ..enchantement import Enchantement

class EnchantementAgissant(EffetAgissant,Enchantement):
    """Un effet (temporaire) qui enchante un item."""
    def __init__(self,temps_restant:float):
        Enchantement.__init__(self,temps_restant)
        EffetAgissant.__init__(self)