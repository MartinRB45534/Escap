"""
Le fichier pour stocker les informations des magies.
"""

from __future__ import annotations

from ..stockage import StockageCategorieNivelee

from .attaque import MagieAttaqueNivele
from .boost import MagieBoostNivele
from .protection import MagieProtectionNivelee
from .projectile import MagieProjectileNivelee
from .soins import MagieSoinNivelee, MagieResurectionNivele, MagieReanimationNivele
from .enchantement import MagieEnchantementAgissantNivele, MagieEnchantementItemNivele
from .economie import MagieReserveNivelee, MagieInvestissementNivelee
from .divers import MagieBlizzardNivelee, MagieObscuriteNivelee, MagieInstakillNivelee, MagieTeleportationNivelee

class Magies(StockageCategorieNivelee):
    """Les informations des magies."""
    nom = "Magies"
    titre_nouveau = "Nouvelle magie"
    description = "Les magies puevent être lancées contre du mana pour obtenit divers effets."
    avertissement = "Il existe déjà une magie avec ce nom !"
    elements = {
        "MagieAttaqueNivele": MagieAttaqueNivele,
        "MagieBoostNivele": MagieBoostNivele,
        "MagieProtectionNivelee": MagieProtectionNivelee,
        "MagieSoinNivelee": MagieSoinNivelee,
        "MagieResurectionNivele": MagieResurectionNivele,
        "MagieReanimationNivele": MagieReanimationNivele,
        "MagieEnchantementAgissantNivele": MagieEnchantementAgissantNivele,
        "MagieEnchantementItemNivele": MagieEnchantementItemNivele,
        "MagieProjectileNivelee": MagieProjectileNivelee,
        "MagieReserveNivelee": MagieReserveNivelee,
        "MagieInvestissementNivelee": MagieInvestissementNivelee,
        "MagieBlizzardNivelee": MagieBlizzardNivelee,
        "MagieObscuriteNivelee": MagieObscuriteNivelee,
        "MagieInstakillNivelee": MagieInstakillNivelee,
        "MagieTeleportationNivelee": MagieTeleportationNivelee
    }
