"""
Ce fichier contient les directions utilisées dans l'affichage et le jeu.
"""

from enum import Enum

class Direction:
    """La classe utilisée pour les directions (dans l'affichage comme le jeu)"""

class DirectionAff(Direction,Enum):
    """Les directions pour l'affichage"""
    UP = "Up"
    DOWN = "Down"
    LEFT = "Left"
    RIGHT = "Right"
    IN = "In"
    OUT = "Out"
    NEXT = "Next"
    PREVIOUS = "Previous"

    @property
    def oppose(self):
        """Renvoie la direction opposée"""
        if self == DirectionAff.UP:
            return DirectionAff.DOWN
        elif self == DirectionAff.DOWN:
            return DirectionAff.UP
        elif self == DirectionAff.LEFT:
            return DirectionAff.RIGHT
        elif self == DirectionAff.RIGHT:
            return DirectionAff.LEFT
        elif self == DirectionAff.IN:
            return DirectionAff.OUT
        elif self == DirectionAff.OUT:
            return DirectionAff.IN
        elif self == DirectionAff.NEXT:
            return DirectionAff.PREVIOUS
        elif self == DirectionAff.PREVIOUS:
            return DirectionAff.NEXT
        else:
            raise ValueError("La direction n'est pas valide")
