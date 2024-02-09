"""
Sert à définir les différents éléments du jeu.
"""

from enum import StrEnum

class Element(StrEnum):
    """Contient les quatre éléments."""
    TERRE = "Terre"
    FEU = "Feu"
    GLACE = "Glace"
    OMBRE = "Ombre"
