"""
Fichier contenant la classe de stockage des items.
"""

from __future__ import annotations

from ...stockage import StockageSurCategorie
from .parchemin import Parchemins
from .projectile import Projectiles
from .potion import Potions
from .arme import Armes
from .bouclier import Boucliers
from .equippement import Equippements
from .ingredient import Ingredients

class Items(StockageSurCategorie):
    """Les informations des items."""
    nom = "Items"
    elements = {
        "parchemin": Parchemins,
        "potions": Potions,
        "projectile": Projectiles,
        "arme": Armes,
        "bouclier": Boucliers,
        "equippement": Equippements,
        "ingredient": Ingredients,
    }
