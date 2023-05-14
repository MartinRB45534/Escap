from __future__ import annotations

# Pas d'import pour les annotations

# Pas de classe parente

# Variables de classe
from Jeu.Constantes import NB_DIRECTIONS

class Position:
    def __init__(self,lab:str,x:int,y:int):
        self.lab=lab #Doit être un chaine de caractères
        self.x=x
        self.y=y

    def __add__(self,other):
        if isinstance(other,Decalage):
            return Position(self.lab,self.x+other.x,self.y+other.y)
        return NotImplemented

    def __radd__(self,other):
        if isinstance(other,Decalage):
            return Position(self.lab,other.x+self.x,other.y+self.y)
        return NotImplemented

    def __sub__(self,other):
        if isinstance(other,Position):
            if other in self:
                return Decalage(self.x-other.x,self.y-other.y)
            else:
                print(f"On ne peut pas soustraire {other} à {self} car les étages diffèrent.")
                return NotImplemented
        elif isinstance(other,Decalage):
            return Position(self.lab,self.x-other.x,self.y-other.y)
        return NotImplemented

    def __rsub__(self,other):
        if isinstance(other,Position): #Ne devrait pas pouvoir arriver
            if other in self:
                return Decalage(other.x-self.x,other.y-self.y)
            else:
                print(f"On ne peut pas soustraire {self} à {other} car les étages diffèrent.")
                return NotImplemented
        return NotImplemented

    def __eq__(self,other):
        if isinstance(other,Position):
            return self.lab == other.lab and self.x == other.x and self.y == other.y
        return False

    def __hash__(self):
        return hash((self.lab, self.x, self.y))


    def __contains__(self,item): #Ce n'est pas exactement l'usage normal de in, mais en l'occurence pos1 in pos2 est vrai si les deux positions sont au même étage
        if isinstance(item,Position):
            return self.lab == item.lab
        return False

    def __str__(self):
        return f"Position : {self.lab}, {self.x}, {self.y}"

    def __repr__(self):
        return f"Position : {self.lab}, {self.x}, {self.y}"

    def __iter__(self):
        for i in range(self.y):
            for j in range(self.x):
                yield Position(self.lab,j,i)

    def to_decalage(self):
        return Decalage(self.x,self.y)
    
class Nowhere(Position):
    def __init__(self):
        self.lab="Nowhere"
        self.x=0
        self.y=0

ABSENT = Nowhere()

# Imports utilisés dans le code
from Jeu.Labyrinthe.Structure_spatiale.Decalage import Decalage