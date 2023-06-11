from enum import Enum

class Direction:
    """La classe utilisée pour les directions (dans l'affichage comme le jeu)"""

class Direction_aff(Direction,Enum):
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
        if self == Direction_aff.UP:
            return Direction_aff.DOWN
        elif self == Direction_aff.DOWN:
            return Direction_aff.UP
        elif self == Direction_aff.LEFT:
            return Direction_aff.RIGHT
        elif self == Direction_aff.RIGHT:
            return Direction_aff.LEFT
        elif self == Direction_aff.IN:
            return Direction_aff.OUT
        elif self == Direction_aff.OUT:
            return Direction_aff.IN
        elif self == Direction_aff.NEXT:
            return Direction_aff.PREVIOUS
        elif self == Direction_aff.PREVIOUS:
            return Direction_aff.NEXT
        else:
            raise ValueError("La direction n'est pas valide")