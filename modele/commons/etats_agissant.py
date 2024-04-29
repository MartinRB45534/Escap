"""
Fichier contenant l'énumération des états des agissants.
"""

from enum import StrEnum

class EtatsAgissants(StrEnum):
    """Les états des agissants. Pour l'instant juste mort et vivant ?"""
    VIVANT = "VIVANT" # Agissant en vie
    MORT = "MORT" # Agissant mort (on devrait voir un item de cadavre à la place)
