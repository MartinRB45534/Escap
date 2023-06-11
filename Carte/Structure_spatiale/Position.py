from __future__ import annotations
from typing import TYPE_CHECKING, Any
from warnings import warn

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from .Etage import Etage

# Pas de classe parente

class Position:
    def __init__(self,etage:Etage,x:int,y:int):
        self.etage=etage #Doit être un chaine de caractères
        self.x=x
        self.y=y

    def __add__(self,other:Any):
        if isinstance(other,Decalage):
            return New_pos(self.etage,self.x+other.x,self.y+other.y)
        return NotImplemented

    def __radd__(self,other:Any):
        if isinstance(other,Decalage):
            return New_pos(self.etage,other.x+self.x,other.y+self.y)
        return NotImplemented

    def __sub__(self,other:Any):
        if isinstance(other,Position):
            if other in self:
                return Decalage(self.x-other.x,self.y-other.y)
            else:
                warn(f"On ne peut pas soustraire {other} à {self} car les étages diffèrent.")
                return NotImplemented
        elif isinstance(other,Decalage):
            return New_pos(self.etage,self.x-other.x,self.y-other.y)
        return NotImplemented

    def __rsub__(self,other:Any):
        if isinstance(other,Position): #Ne devrait pas pouvoir arriver
            if other in self:
                return Decalage(other.x-self.x,other.y-self.y)
            else:
                warn(f"On ne peut pas soustraire {self} à {other} car les étages diffèrent.")
                return NotImplemented
        return NotImplemented

    def __eq__(self,other:Any):
        if isinstance(other,Position):
            return self.etage == other.etage and self.x == other.x and self.y == other.y
        return NotImplemented

    def __hash__(self):
        return hash((self.etage, self.x, self.y))


    def __contains__(self,item:Any): #Ce n'est pas exactement l'usage normal de in, mais en l'occurence pos1 in pos2 est vrai si les deux positions sont au même étage
        return isinstance(item,Position) and item in self.etage

    def __str__(self):
        return f"Position : {self.etage}, {self.x}, {self.y}"

    def __repr__(self):
        return f"Position : {self.etage}, {self.x}, {self.y}"

    def __iter__(self):
        for i in range(self.y):
            for j in range(self.x):
                yield New_pos(self.etage,j,i)

    def to_decalage(self):
        return Decalage(self.x,self.y)
    
def New_pos(etage:Etage,x:int,y:int) -> Position:
    return etage.get_pos(x,y)

# Imports utilisés dans le code
from .Decalage import Decalage