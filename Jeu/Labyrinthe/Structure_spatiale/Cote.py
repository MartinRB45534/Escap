from Jeu.Labyrinthe.Structure_spatiale.Direction import *

class Cote_decalage:
    def __init__(self,emplacement: Decalage,direction:Direction):
        self.emplacement = emplacement
        self.direction=direction

    def __sub__(self,other):
        emplacement = self.emplacement - other
        if isinstance(emplacement,Decalage):
            return Cote_decalage(emplacement,self.direction)
        return NotImplemented

    def __add__(self,other):
        emplacement = self.emplacement + other
        if isinstance(emplacement,Decalage):
            return Cote_decalage(emplacement,self.direction)
        return NotImplemented

    def __radd__(self,other):
        emplacement = other + self.emplacement
        if isinstance(emplacement,Decalage):
            return Cote_decalage(emplacement,self.direction)
        return NotImplemented

    def __eq__(self,other):
        if isinstance(other,Cote_decalage):
            return self.emplacement == other.emplacement and self.direction == other.direction
        return False

    def __str__(self):
        return f"Coté : {self.emplacement}, {self.direction}"

    def __repr__(self):
        return f"Coté : {self.emplacement}, {self.direction}"

    def oppose(self):
        return Cote_decalage(self.emplacement+self.direction,self.direction.oppose())
    
class Cote_position:
    def __init__(self,emplacement: Position,direction:Direction):
        self.emplacement = emplacement
        self.direction=direction

    def __sub__(self,other):
        emplacement = self.emplacement - other
        if isinstance(emplacement,Position):
            return Cote_position(emplacement,self.direction)
        return NotImplemented

    def __add__(self,other):
        emplacement = self.emplacement + other
        if isinstance(emplacement,Position):
            return Cote_position(emplacement,self.direction)
        return NotImplemented

    def __radd__(self,other):
        emplacement = other + self.emplacement
        if isinstance(emplacement,Position):
            return Cote_position(emplacement,self.direction)
        return NotImplemented

    def __eq__(self,other):
        if isinstance(other,Cote_position|Cote_decalage):
            return self.emplacement == other.emplacement and self.direction == other.direction
        return False

    def __str__(self):
        return f"Coté : {self.emplacement}, {self.direction}"

    def __repr__(self):
        return f"Coté : {self.emplacement}, {self.direction}"

    def oppose(self):
        return Cote_position(self.emplacement+self.direction,self.direction.oppose())