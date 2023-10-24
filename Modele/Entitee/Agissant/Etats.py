from enum import Enum

class EtatsAgissants(Enum):
    """Les états des agissants. Pour l'instant juste mort et vivant ?"""
    VIVANT = "VIVANT"
    MORT = "MORT"