"""
Fichier contenant l'énumération des formes de propagation (surtout utilisé pour les attaques)
"""

from enum import Enum

class Forme(Enum):
    """Enumération des formes de propagation."""
    CERCLE = "CERCLE"
    DEMI_CERCLE = "DEMI_CERCLE"
