"""
Un angle représente un décalage de direction sur la carte.
"""

from __future__ import annotations
from typing import Any

# Pas d'import pour les annotations

# Pas de classe parente

class Angle:
    """Un angle de direction."""
    def __init__(self,angle: int):
        self.angle = angle%4

    def __add__(self,other:Any):
        if isinstance(other,Angle):
            return Angle(self.angle+other.angle)
        else:
            return NotImplemented #Vraiment une bonne idée ?

    def __radd__(self,other:Any):
        if isinstance(other,Angle): #Ne devrait pas pouvoir arriver
            return Angle(other.angle+self.angle)
        else:
            return NotImplemented #Vraiment une bonne idée ?

    def __sub__(self,other:Any):
        if isinstance(other,Angle):
            return Angle(self.angle-other.angle)
        else:
            return NotImplemented #Vraiment une bonne idée ?

    def __rsub__(self,other:Any):
        if isinstance(other,Angle): #Ne devrait pas pouvoir arriver
            return Angle(other.angle-self.angle)
        else:
            return NotImplemented #Vraiment une bonne idée ?

    def __mul__(self,other:Any):
        if isinstance(other,int):
            return Angle(self.angle*other)
        else:
            return NotImplemented

    def __rmul__(self,other:Any):
        if isinstance(other,int):
            return Angle(other*self.angle)
        else:
            return NotImplemented

    def __eq__(self, other:Any):
        if isinstance(other,Angle):
            return self.angle == other.angle
        return NotImplemented

    @property
    def oppose(self):
        """L'angle opposé à cet angle."""
        return self + HALF_TURN

    def __str__(self):
        return f"Angle : {self.angle}"

    def __repr__(self):
        return f"Angle : {self.angle}"

CLOCK_WISE=Angle(1)
COUNTER_CLOCK_WISE=Angle(-1)
HALF_TURN=Angle(2)
