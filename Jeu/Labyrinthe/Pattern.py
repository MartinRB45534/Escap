# from Jeu.Constantes import *
# from Jeu.Effet.Effets import *
from Jeu.Labyrinthe.Case import *
from Jeu.Labyrinthe.Structure_spatiale.Espace import *

class Pattern(Espace):
    def __init__(self,position:Position,decalage:Decalage,entrees:List[Cote_decalage]=[],codes:List[str]=[],vide=True):
        self.position = position
        self.decalage = decalage
        self.matrice_cases = [[Decalage(i,j) for j in range(decalage.y)] for i in range(decalage.x)]
        self.bord = Bord_pat(position,decalage,entrees)
        self.entrees = entrees
        self.codes = codes
        self.vide = vide

    # def __getitem__(self,key):
    #     if isinstance(key,tuple):
    #         return self[key[0]][key[1]]
    #     elif isinstance(key,Decalage):
    #         return self.matrice_cases[key.x][key.y]
    #     elif isinstance(key,Position):
    #         return self[key-self.position]
    #     if isinstance(key,Cote_decalage|Cote_position):
    #         return self[key.emplacement][key.direction]
    #     else:
    #         return NotImplemented

    def __contains__(self,item):
        if item is None:
            return False
        elif isinstance(item,Position):
            return item-self.position in self
        elif isinstance(item,Decalage):
            return 0<=item.x<self.decalage.x and 0<=item.y<self.decalage.y
        elif isinstance(item,Cote_decalage|Cote_position):
            return item.emplacement in self
        return NotImplemented

    def __iter__(self):
        for decalage in self.decalage:
            yield self.position + decalage
