from __future__ import annotations

# Pas d'import pour les annotations

# Pas de classe parente

# Variables de classe
from Jeu.Constantes import NB_DIRECTIONS

class Angle:
    directions = NB_DIRECTIONS
    def __init__(self,angle: int):
        self.angle = angle%self.directions

    def __add__(self,other):
        if isinstance(other,Angle):
            return Angle(self.angle+other.angle)
        else:
            return NotImplemented #Vraiment une bonne idée ?

    def __radd__(self,other):
        if isinstance(other,Angle): #Ne devrait pas pouvoir arriver
            return Angle(other.angle+self.angle)
        else:
            return NotImplemented #Vraiment une bonne idée ?

    def __sub__(self,other):
        if isinstance(other,Angle):
            return Angle(self.angle-other.angle)
        else:
            return NotImplemented #Vraiment une bonne idée ?

    def __rsub__(self,other):
        if isinstance(other,Angle): #Ne devrait pas pouvoir arriver
            return Angle(other.angle-self.angle)
        else:
            return NotImplemented #Vraiment une bonne idée ?

    def __mul__(self,other):
        if isinstance(other,int):
            return Angle(self.angle*other)
        else:
            return NotImplemented

    def __rmul__(self,other):
        if isinstance(other,int):
            return Angle(other*self.angle)
        else:
            return NotImplemented

    def __eq__(self, other):
        if isinstance(other,Angle):
            return self.angle == other.angle
        return NotImplemented

    def oppose(self):
        return self - self.directions//2

    def __str__(self):
        return f"Angle : {self.angle}"

    def __repr__(self):
        return f"Angle : {self.angle}"

CLOCK_WISE=Angle(1)
COUNTER_CLOCK_WISE=Angle(-1)