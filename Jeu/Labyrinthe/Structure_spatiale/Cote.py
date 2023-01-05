from typing import Union
from Jeu.Labyrinthe.Structure_spatiale.Direction import *

class Cote:
    def __init__(self,emplacement: Union[Position,Decalage],direction:Direction):
        self.emplacement = emplacement
        self.direction=direction

    def __sub__(self,other):
        emplacement = self.emplacement - other
        if isinstance(emplacement,(Decalage,Position)):
            return Cote(emplacement,self.direction)
        return NotImplemented

    def __add__(self,other):
        emplacement = self.emplacement + other
        if isinstance(emplacement,(Decalage,Position)):
            return Cote(emplacement,self.direction)
        return NotImplemented

    def __radd__(self,other):
        emplacement = other + self.emplacement
        if isinstance(emplacement,(Decalage,Position)):
            return Cote(emplacement,self.direction)
        return NotImplemented

    def __eq__(self,other):
        if isinstance(other,Cote):
            return self.emplacement == other.emplacement and self.direction == other.direction
        return False

    def __str__(self):
        return f"Coté : {self.emplacement}, {self.direction}"

    def __repr__(self):
        return f"Coté : {self.emplacement}, {self.direction}"

    def oppose(self):
        return Cote(self.emplacement+self.direction,self.direction.oppose())