# from typing import Any
from typing import Any, Dict
from Jeu.Labyrinthe.Structure_spatiale.Espace import *

class Vue(Espace):
    """Une représentation simplifiée d'un labyrinthe"""
    def __init__(self,ID:str,matrice:List[List],decalage:Decalage):
        self.id = ID
        self.matrice_cases = matrice
        self.decalage = decalage

    def __getitem__(self,key):
        if isinstance(key,tuple):
            return self.matrice_cases[key[0]][key[1]]
        elif isinstance(key,(Decalage,Position)):
            return self.matrice_cases[key.x][key.y]
        if isinstance(key,Cote):
            return self[key.emplacement][key.direction]
        return NotImplemented

    def __setitem__(self,key,value):
        if isinstance(key,tuple):
            self[key[0]][key[1]] = value
        elif isinstance(key,(Decalage,Position)):
            self.matrice_cases[key.x][key.y] = value
        if isinstance(key,Cote):
            self[key.emplacement][key.direction] = value
        else:
            return NotImplemented

    def __contains__(self,item):
        if item is None:
            return False
        elif isinstance(item,Position):
            return item.lab == self.id and 0<=item.x<self.decalage.x and 0<=item.y<self.decalage.y
        elif isinstance(item,Decalage):
            return 0<=item.x<self.decalage.x and 0<=item.y<self.decalage.y
        elif isinstance(item,Cote):
            return item.emplacement in self
        return NotImplemented

class Vues(dict):
    """Un dictionnaire qui contient des objets Vue"""
    def __getitem__(self,key) -> Vue|Any:
        if isinstance(key,tuple):
            return self[key[0]][key[1]]
        elif isinstance(key,str):
            return dict.__getitem__(self,key)
        elif isinstance(key,Position):
            return self[key.lab][key]
        if isinstance(key,Cote):
            return self[key.emplacement][key.direction]
        return NotImplemented

    def __setitem__(self,key,value):
        if isinstance(key,tuple):
            self[key[0]][key[1]] = value
        elif isinstance(key,str):
            return dict.__setitem__(self,key,value)
        elif isinstance(key,Position):
            self[key.lab][key] = value
        if isinstance(key,Cote):
            self[key.emplacement][key.direction] = value
        else:
            return NotImplemented

    def __contains__(self,item):
        if item is None:
            return False
        elif isinstance(item,Position):
            return item.lab in self and item in self[item.lab]
        elif isinstance(item,Cote):
            return item.emplacement in self
        else:
            return dict.__contains__(self,item)

    def __iter__(self):
        for vue in self.values():
            for case in vue:
                yield case