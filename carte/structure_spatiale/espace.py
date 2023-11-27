"""
Ce fichier contient la classe Espace, qui représente un élément de l'espace (un étage de labyrinthe, une salle d'un étage, etc.).
"""

from __future__ import annotations
from typing import TYPE_CHECKING, Any

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from .decalage import Decalage

# Pas de classe parente

class Espace:
    """La classe qui représente un élément de l'espace (un étage de labyrinthe, une salle d'un étage, etc.)"""
    def __init__(self,decalage: Decalage):
        self.decalage = decalage
        self.matrice_cases = [[Decalage(i,j) for j in range(decalage.y)] for i in range(decalage.x)]
        self.bord = Bord(self.decalage)

    def __getitem__(self,key:Any):
        if isinstance(key,Decalage):
            return self.matrice_cases[key.x][key.y]
        return NotImplemented

    # def __setitem__(self,key,value):
    #     if isinstance(key,tuple):
    #         self[key[0]][key[1]] = value
    #     if isinstance(key,CoteDecalage):
    #         self[key.emplacement][key.direction] = value
    #     if isinstance(key,Decalage):
    #         self.matrice_cases[key.x][key.y] = value
    #     else:
    #         return NotImplemented

    def __contains__(self,item:Any):
        if item is None:
            return False
        elif isinstance(item,Decalage):
            return 0<=item.x<self.decalage.x and 0<=item.y<self.decalage.y
        elif isinstance(item,CoteDecalage):
            return item.emplacement in self
        return NotImplemented

    def __iter__(self):
        for decalage in self.decalage:
            yield self[decalage]

# Imports utilisés dans le code
from .bord import Bord
from .cote import CoteDecalage
from .decalage import Decalage
