"""
Fichier contenant l'énumération des catégories d'armes.
"""

from enum import StrEnum

class CategoriesArmes(StrEnum):
    """Enumération des catégories d'armes."""
    EPEE = "Épée"
    LANCE = "Lance"
    AUTRE = "Autre"
