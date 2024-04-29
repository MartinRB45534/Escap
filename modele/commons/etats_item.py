"""
Fichier contenant l'énumération des états des items.
"""

from enum import StrEnum

class EtatsItems(StrEnum):
    """Enumération des états des items."""
    INTACT = "INTACT" # Item en bon état
    BRISE = "BRISE" # Item brisé (à évacuer bientôt)
    UTILISE = "UTILISE" # Item en cours d'utilisation