from enum import Enum

class Etats_agissants(Enum):
    """Les états des agissants. Pour l'instant juste mort et vivant ?"""
    VIVANT = "VIVANT"
    MORT = "MORT"