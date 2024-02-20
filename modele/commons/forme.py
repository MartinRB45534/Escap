"""
Fichier contenant l'énumération des formes de propagation (surtout utilisé pour les attaques)
"""

from enum import StrEnum

class Forme(StrEnum):
    """Enumération des formes de propagation."""
    CERCLE = "CERCLE"
    DEMI_CERCLE = "DEMI_CERCLE"
