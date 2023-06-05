from __future__ import annotations
import Affichage
# Pas d'import pour les annotations

# Imports des classes parentes
from enum import IntEnum

class Direction(IntEnum,Affichage.Direction):
    HAUT = 0
    DROITE = 1
    BAS = 2
    GAUCHE = 3

    @property
    def angle(self):
        return self.value*90

    def __index__(self):
        return self.value
    
    @property
    def decalage(self):
        return Decalage([0,1,0,-1][self],[-1,0,1,0][self])

    def __add__(self,other):
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

    def __radd__(self,other):
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

    def __sub__(self,other):
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

    def __rsub__(self,other):
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

    def __mul__(self,other):
        if isinstance(other,int):
            return self.decalage*other
        else:
            return NotImplemented

    def __rmul__(self,other):
        if isinstance(other,int):
            return other*self.decalage
        else:
            return NotImplemented

    @property
    def oppose(self):
        return self+HALF_TURN

    def __str__(self):
        return f"Direction : {self.name}"

    def __repr__(self):
        return f"Direction : {self.name}"

# Imports utilisés dans le code
from .Position import Position
from .Decalage import Decalage
from .Direction import Direction
from .Angle import Angle, HALF_TURN