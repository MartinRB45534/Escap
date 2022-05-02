from Jeu.Labyrinthe.Structure_spatiale.Bord import *

class Espace:
    """La classe qui représente un élément de l'espace (un étage de labyrinthe, une salle d'un étage, etc.)"""
    def __init__(self,decalage):
        self.decalage = decalage
        self.matrice_cases = [[Decalage(i,j) for j in range(decalage.y)] for i in range(decalage.x)]
        self.bord = Bord(self.decalage)

    def __getitem__(self,key):
        if isinstance(key,tuple):
            return self[key[0]][key[1]]
        if isinstance(key,Cote):
            return self[key.emplacement][key.direction]
        if isinstance(key,Decalage):
            return self.matrice_cases[key.x][key.y]
        return NotImplemented

    def __setitem__(self,key,value):
        if isinstance(key,tuple):
            self[key[0]][key[1]] = value
        if isinstance(key,Cote):
            self[key.emplacement][key.direction] = value
        if isinstance(key,Decalage):
            self.matrice_cases[key.x][key.y] = value
        else:
            return NotImplemented

    def __contains__(self,item):
        if item is None:
            return False
        elif isinstance(item,Decalage):
            return 0<=item.x<self.decalage.x and 0<=item.y<self.decalage.y
        elif isinstance(item,Cote):
            return item.emplacement in self
        return NotImplemented

    def __iter__(self):
        for decalage in self.decalage:
            yield self[decalage]