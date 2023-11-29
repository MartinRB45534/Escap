"""
Fichier contenant la classe de stockage des items.
"""

from __future__ import annotations

from ...stockage import StockageSurCategorie
from .parchemin import Parchemins
from .projectile import Projectiles

class Items(StockageSurCategorie):
    """Les informations des parchemins."""
    nom = "Items"
    elements = {
        "parchemin": Parchemins,
        "projectile": Projectiles
    }
