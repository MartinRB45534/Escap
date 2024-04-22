"""
Les enchantements des items.
"""

from __future__ import annotations

# Imports des classes parentes
from .enchantement import EnchantementItem
from .items import EffetPortee, EffetTranchant, EffetBombe

class EnchantementArme(EnchantementItem, EffetTranchant, EffetPortee):
    """Enchantement qui modifie les statistiques d'une arme (en positif ou négatif)."""
    gain_force: float
    gain_portee: float

    def modifie_portee(self, portee: float) -> float:
        return portee + self.gain_portee

    def modifie_tranchant(self, tranchant: float) -> float:
        return tranchant + self.gain_force

class EnchantementBombe(EnchantementItem, EffetBombe):
    """Enchantement qui confère des propriétés explosives à un item."""


enchantements_items: dict[str, type[EnchantementItem]] = {
    "renforcement": EnchantementArme,
    "bombe": EnchantementBombe
}
"""
nom -> type[EnchantementItem]
"""
