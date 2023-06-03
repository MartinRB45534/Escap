from __future__ import annotations

# Pas d'import pour les annotations

# Pas de classe parente

# Variables de classe
from Old_Jeu.Constantes import NB_DIRECTIONS

class Direction:
    directions = NB_DIRECTIONS
    def __init__(self,direction: int):
        self.direction = direction%self.directions

    def __index__(self):
        return self.direction

    def __add__(self,other):
        if isinstance(other,Direction):
            return self.to_decalage()+other
        elif isinstance(other,Angle):
            return Direction(self.direction+other)
        elif isinstance(other,int):
            return Direction(self.direction+other)
        elif isinstance(other,(Decalage,Position)):
            return self.to_decalage()+other
        else:
            return NotImplemented #Vraiment une bonne idée ?

    def __radd__(self,other):
        if isinstance(other,Direction): #Ne devrait pas pouvoir arriver
            return other+self.to_decalage()
        elif isinstance(other,Angle):
            return Direction(other+self.direction)
        elif isinstance(other,int):
            return Direction(other+self.direction)
        elif isinstance(other,(Decalage,Position)):
            return other+self.to_decalage()
        else:
            return NotImplemented #Vraiment une bonne idée ?

    def __sub__(self,other):
        if isinstance(other,Direction): #Ne devrait théoriquement pas être utilisé
            return self.to_decalage()-other
        elif isinstance(other,Angle):
            return Direction(self.direction-other)
        elif isinstance(other,int):
            return Direction(self.direction-other)
        elif isinstance(other,(Decalage,Position)): #Encore un truc qui ne devrait jamais servir !
            return self.to_decalage()-other
        else:
            return NotImplemented #Vraiment une bonne idée ?

    def __rsub__(self,other):
        if isinstance(other,Direction): #Ne devrait pas pouvoir arriver
            return other-self.to_decalage()
        elif isinstance(other,Angle):
            return Direction(other-self.direction)
        elif isinstance(other,int):
            return Direction(other-self.direction)
        elif isinstance(other,(Decalage,Position)): #Ne devrait pas être utilisé non plus
            return other-self.to_decalage()
        else:
            return NotImplemented #Vraiment une bonne idée ?

    def __mul__(self,other):
        if isinstance(other,int):
            return self.to_decalage()*other
        else:
            return NotImplemented

    def __rmul__(self,other):
        if isinstance(other,int):
            return other*self.to_decalage()
        else:
            return NotImplemented

    def __eq__(self, other):
        if isinstance(other,Direction):
            return self.direction == other.direction
        elif isinstance(other,Decalage):
            return self.to_decalage() == other
        return NotImplemented
    
    def __hash__(self) -> int:
        return hash(self.direction)

    def to_decalage(self):
        if self.directions == 4:
            return Decalage([0,1,0,-1][self],[-1,0,1,0][self])
        else:
            return NotImplemented

    def oppose(self):
        return self - self.directions//2

    def __str__(self):
        return f"Direction : {self.direction}"

    def __repr__(self):
        return f"Direction : {self.direction}"

if NB_DIRECTIONS==4:
    HAUT=Direction(0)
    DROITE=Direction(1)
    BAS=Direction(2)
    GAUCHE=Direction(3)
DIRECTIONS = [Direction(i) for i in range(Direction.directions)]

# Imports utilisés dans le code
from Old_Jeu.Labyrinthe.Structure_spatiale.Position import Position
from Old_Jeu.Labyrinthe.Structure_spatiale.Decalage import Decalage
from Old_Jeu.Labyrinthe.Structure_spatiale.Direction import Direction
from Old_Jeu.Labyrinthe.Structure_spatiale.Angle import Angle