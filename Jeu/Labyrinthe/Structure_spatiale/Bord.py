from Jeu.Labyrinthe.Structure_spatiale.Cote import *

class Bord:
    """Représente les limites d'un espace"""
    def __init__(self,emplacement):
        self.emplacement = emplacement

    def __contains__(self,item):
        if item is None:
            return False
        if isinstance(item,Cote):
            if NB_DIRECTIONS == 4:
                return (item.direction == HAUT and item.emplacement.y == 0) or (item.direction == BAS and item.emplacement.y == self.emplacement.y-1) or (item.direction == GAUCHE and item.emplacement.x == 0) or (item.direction == DROITE and item.emplacement.x == self.emplacement.x-1)
        return NotImplemented

    def __iter__(self):
        for i in range(self.emplacement.x):
            yield Cote(Decalage(i,0),HAUT)
            yield Cote(Decalage(i,self.emplacement.y-1),BAS)
        for j in range(self.emplacement.y):
            yield Cote(Decalage(0,j),GAUCHE)
            yield Cote(Decalage(self.emplacement.x-1,j),DROITE)