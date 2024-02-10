"""
Fichier contenant la classe de stockage des items.
"""

from __future__ import annotations

from ...stockage import StockageSurCategorie
from .parchemin import Parchemins
from .projectile import Projectiles
from .arme import Armes
from .bouclier import Boucliers
from .equippement import Equippements

class Items(StockageSurCategorie):
    """Les informations des parchemins."""
    nom = "Items"
    elements = {
        "parchemin": Parchemins,
        "projectile": Projectiles,
        "arme": Armes,
        "bouclier": Boucliers,
        "equippement": Equippements,
    }
