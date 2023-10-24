"""
Sert à définir les différents éléments du jeu.
"""

from enum import Enum

class Element(Enum):
    """Contient les quatre éléments."""
    TERRE = "Terre"
    FEU = "Feu"
    GLACE = "Glace"
    OMBRE = "Ombre"
