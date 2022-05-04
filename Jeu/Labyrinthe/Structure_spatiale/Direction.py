from Jeu.Constantes import NB_DIRECTIONS
from Jeu.Labyrinthe.Structure_spatiale.Position import *

# global NB_DIRECTIONS
# NB_DIRECTIONS = 4

class Direction:
    directions = NB_DIRECTIONS
    def __init__(self,direction):
        self.direction = direction

    def __index__(self):
        return self.direction

    def __add__(self,other):
        if isinstance(other,Direction): #Ne devrait théoriquement pas être utilisé
            return Direction((self.direction+other.direction)%self.directions)
        elif isinstance(other,int):
            return Direction((self.direction+other)%self.directions)
        elif isinstance(other,(Decalage,Position)):
            return self.to_decalage()+other
        else:
            return NotImplemented #Vraiment une bonne idée ?

    def __radd__(self,other):
        if isinstance(other,Direction): #Ne devrait pas pouvoir arriver
            return Direction((other.direction+self.direction)%self.directions)
        elif isinstance(other,int):
            return Direction((other+self.direction)%self.directions)
        elif isinstance(other,(Decalage,Position)):
            return other+self.to_decalage()
        else:
            return NotImplemented #Vraiment une bonne idée ?

    def __sub__(self,other):
        if isinstance(other,Direction): #Ne devrait théoriquement pas être utilisé
            return Direction((self.direction-other.direction)%self.directions)
        elif isinstance(other,int):
            return Direction((self.direction-other)%self.directions)
        elif isinstance(other,(Decalage,Position)): #Encore un truc qui ne devrait jamais servir !
            return self.to_decalage()-other
        else:
            return NotImplemented #Vraiment une bonne idée ?

    def __rsub__(self,other):
        if isinstance(other,Direction): #Ne devrait pas pouvoir arriver
            return Direction((other.direction-self.direction)%self.directions)
        elif isinstance(other,int):
            return Direction((other-self.direction)%self.directions)
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

#Essayer de ne plus utiliser ceux-ci ?
# global HAUT
HAUT=Direction(0)
# global DROITE
DROITE=Direction(1)
# global BAS
BAS=Direction(2)
# global GAUCHE
GAUCHE=Direction(3)