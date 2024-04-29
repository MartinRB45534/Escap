"""
Fichier contenant l'énumération des états des decors.
"""

from enum import StrEnum

class EtatsDecors(StrEnum):
    """Les états des decors. Intact ou écrasé."""
    INTACT = "INTACT" # Decor en bon état
    ECRASE = "ECRASE" # Decor écrasé (on peut passer dessus, mais plus interragir avec)
