"""Contient la classe Direction, qui permet de représenter les directions sur une grille."""

from __future__ import annotations
from typing import Any
from enum import IntEnum
import affichage as af

class Direction(af.Direction,IntEnum):
    """Classe représentant une direction sur la carte."""
    HAUT = 0
    DROITE = 1
    BAS = 2
    GAUCHE = 3

    @property
    def angle(self):
        """L'angle de cette direction, en degrés par rapport à la verticale, dans le sens horaire."""
        return self.value*90

    def __index__(self):
        return self.value
    
    @property
    def decalage(self):
        """Le décalage correspondant à un déplacement d'une case dans cette direction"""
        return Decalage([0,1,0,-1][self],[-1,0,1,0][self])

    def __add__(self,other:Any):
        if isinstance(other,Direction):
            return self.decalage+other
        elif isinstance(other,Angle):
            return Direction(self.value+other)
        elif isinstance(other,int):
            return Direction(self.value+other)
        elif isinstance(other,(Decalage,Position)):
            return self.decalage+other
        else:
            return NotImplemented #Vraiment une bonne idée ?

    def __radd__(self,other:Any):
        if isinstance(other,Direction): #Ne devrait pas pouvoir arriver
            return other+self.decalage
        elif isinstance(other,Angle):
            return Direction(other+self.value)
        elif isinstance(other,int):
            return Direction(other+self.value)
        elif isinstance(other,(Decalage,Position)):
            return other+self.decalage
        else:
            return NotImplemented #Vraiment une bonne idée ?

    def __sub__(self,other:Any):
        if isinstance(other,Direction): #Ne devrait théoriquement pas être utilisé
            return self.decalage-other
        elif isinstance(other,Angle):
            return Direction(self.value-other)
        elif isinstance(other,int):
            return Direction(self.value-other)
        elif isinstance(other,(Decalage,Position)): #Encore un truc qui ne devrait jamais servir !
            return self.decalage-other
        else:
            return NotImplemented #Vraiment une bonne idée ?

    def __rsub__(self,other:Any):
        if isinstance(other,Direction): #Ne devrait pas pouvoir arriver
            return other-self.decalage
        elif isinstance(other,Angle):
            return Direction(other-self.value)
        elif isinstance(other,int):
            return Direction(other-self.value)
        elif isinstance(other,(Decalage,Position)): #Ne devrait pas être utilisé non plus
            return other-self.decalage
        else:
            return NotImplemented #Vraiment une bonne idée ?

    def __mul__(self,other:Any):
        if isinstance(other,int):
            return self.decalage*other
        else:
            return NotImplemented

    def __rmul__(self,other:Any):
        if isinstance(other,int):
            return other*self.decalage
        else:
            return NotImplemented

    @property
    def oppose(self) -> Direction:
        """La direction opposée à cette direction."""
        return self+HALF_TURN

    def __str__(self):
        return f"Direction : {self.name}"

    def __repr__(self):
        return f"Direction : {self.name}"

# Imports utilisés dans le code
from .position import Position
from .decalage import Decalage
from .angle import Angle, HALF_TURN
