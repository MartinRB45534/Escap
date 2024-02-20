"""Définition de l'énumération Deplacement."""

from enum import StrEnum

class Deplacement(StrEnum):
    """Enumération des types de déplacement."""
    SPATIAL = "SPATIAL"
    MAGIQUE = "MAGIQUE"
