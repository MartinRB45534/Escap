from enum import Enum

class Direction:
    """La classe utilisée pour les directions (dans l'affichage comme le jeu)"""

class Direction_aff(Enum,Direction):
    """Les directions pour l'affichage"""
    UP = "Up"
    DOWN = "Down"
    LEFT = "Left"
    RIGHT = "Right"
    IN = "In"
    OUT = "Out"
    NEXT = "Next"
    PREVIOUS = "Previous"