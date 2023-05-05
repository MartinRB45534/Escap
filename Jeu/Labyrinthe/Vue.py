# from typing import Any
from typing import Any, Dict, Iterator, Literal, Tuple
from Jeu.Labyrinthe.Structure_spatiale.Espace import *
from Jeu.Labyrinthe.Structure_spatiale.Espace import Decalage, List

class Vue(Espace):
    """Une représentation simplifiée d'un labyrinthe"""
    def __init__(self,ID:str,matrice:List[List],decalage:Decalage):
        self.id = ID
        self.matrice_cases = matrice
        self.decalage = decalage

    def __getitem__(self,key:Position|Decalage|Cote|tuple):
        if isinstance(key,tuple):
            return self.matrice_cases[key[0]][key[1]]
        elif isinstance(key,Position):
            if key.lab != self.id:
                raise ValueError("La position n'est pas dans l'étage")
            return self.matrice_cases[key.x][key.y]
        elif isinstance(key,Decalage):
            return self.matrice_cases[key.x][key.y]
        if isinstance(key,Cote):
            return self[key.emplacement][key.direction]
        return NotImplemented

    def __setitem__(self,key:Position|Decalage|Cote|tuple,value):
        if isinstance(key,tuple):
            self[key[0]][key[1]] = value
        elif isinstance(key,Position):
            if key.lab != self.id:
                raise ValueError("La position n'est pas dans l'étage")
            self.matrice_cases[key.x][key.y] = value
        elif isinstance(key,Decalage):
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
    
    def __iter__(self) -> Iterator:
        for decalage in self.decalage:
            yield self[decalage]

class Representation_case:
    """Regroupe les informations sur une case qui seront envoyées à l'agissant"""
    def __init__(self,position:Position,clarte:float,code:int,cibles:List[Position|Literal[False]],effets:List[List[int]],repoussante:bool):
        self.position = position #La position de la case
        self.clarte = clarte #La clarté, qui vient d'être calculée pour l'agissant
        self.oubli = 0 #Pour le décompte de l'oubli
        # self.trajets = [0, #Pour les trajets (importance des ennemis), en contournant les agissants
        #                 0, #Pour les trajets (importance des ennemis), en traversant les agissants
        #                 0, #Pour les trajets (dangerosité), en contournant les agissants
        #                 0, #Pour les trajets (dangerosité), en traversant les agissants
        #                 0, #Pour les autres trajets (pour calculer de façon unique, effacé avant chaque calcul)
        #                 False]
        self.trajets = {}
        self.visitee = False #Pour savoir si la case a déjà été visitée
        self.code = code #Le code correspondant aux auras et autres effets
        self.cibles = cibles #Les murs et leur traversabilité pour l'agissant
        self.entitees = [] #Pour stocker les entitées
        self.effets = effets #Pour stocker les effets (attaques delayées)
        self.repoussante = repoussante #Si la case est repoussante

    def oublie(self, oubli:int):
        """Pour oublier les cases visitées il y a trop longtemps"""
        self.trajets = {}
        self.effets = []
        self.repoussante = False
        if self.oubli > 1:
            self.oubli = min(oubli, self.oubli-1)
        elif self.oubli > 0:
            self.clarte = 0
            self.oubli = 0
            self.code = 0
            self.cibles = [[False,False,False,False,False],[False,False,False,False,False],[False,False,False,False,False],[False,False,False,False,False]]
            self.entitees = []
            return True
        return False

    def __getitem__(self,key:str|Tuple[str,int]|Tuple[int|Direction,int]) -> int:
        if isinstance(key,str):
            return self.trajets.get(key,[])
        elif isinstance(key,tuple):
            if isinstance(key[0],str):
                trajet = self.trajets.get(key[0],[])
                if len(trajet) > key[1]:
                    return trajet[key[1]]
                return 0
            elif isinstance(key[0],(int,Direction)):
                return self.trajets[key[0]][key[1]]
        return NotImplemented

    def __setitem__(self,key:str|Tuple[str,int],value:int):
        if isinstance(key,str):
            self.trajets[key] = value
        elif isinstance(key,tuple):
            if key[0] not in self:
                self.trajets[key[0]] = []
            if len(self.trajets[key[0]]) <= key[1]:
                self.trajets[key[0]] += [0]*(key[1]-len(self.trajets[key[0]])+1)
            self.trajets[key[0]][key[1]] = value
        else:
            return NotImplemented
        
    def __contains__(self,item:str):
        return item in self.trajets

class Representation_vue(Vue):
    """Une représentation simplifiée d'un labyrinthe"""
    def __init__(self, ID: str, matrice: List[List[Representation_case]], decalage: Decalage):
        super().__init__(ID, matrice, decalage)

    def __getitem__(self,key:Position|Decalage|Cote|tuple) -> Representation_case:
        if isinstance(key,tuple):
            return self.matrice_cases[key[0]][key[1]]
        elif isinstance(key,Position):
            if key.lab != self.id:
                raise ValueError("La position n'est pas dans l'étage")
            return self.matrice_cases[key.x][key.y]
        elif isinstance(key,Decalage):
            return self.matrice_cases[key.x][key.y]
        if isinstance(key,Cote):
            return self[key.emplacement][key.direction]
        return NotImplemented
    
    def __setitem__(self,key:Position|Decalage|Cote|tuple,value:Representation_case):
        if isinstance(key,tuple):
            self[key[0]][key[1]] = value
        elif isinstance(key,Position):
            if key.lab != self.id:
                raise ValueError("La position n'est pas dans l'étage")
            self.matrice_cases[key.x][key.y] = value
        elif isinstance(key,Decalage):
            self.matrice_cases[key.x][key.y] = value
        if isinstance(key,Cote):
            self[key.emplacement][key.direction] = value
        else:
            return NotImplemented
        
    def __contains__(self,item:Position|Decalage|Cote|tuple):
        if item is None:
            return False
        elif isinstance(item,Position):
            return item.lab == self.id and 0<=item.x<self.decalage.x and 0<=item.y<self.decalage.y
        elif isinstance(item,Decalage):
            return 0<=item.x<self.decalage.x and 0<=item.y<self.decalage.y
        elif isinstance(item,Cote):
            return item.emplacement in self
        return NotImplemented
    
    def __iter__(self) -> Iterator[Representation_case]:
        for decalage in self.decalage:
            yield self[decalage]

class Vues(dict[str,Representation_vue]):
    """Un dictionnaire qui contient des objets Representation_vue"""
    def __getitem__(self,key) -> Representation_vue|Representation_case:
        if isinstance(key,tuple):
            return self[key[0]][key[1]]
        elif isinstance(key,str):
            return dict.__getitem__(self,key)
        elif isinstance(key,Position):
            return self[key.lab][key]
        if isinstance(key,Cote):
            return self[key.emplacement][key.direction]
        return NotImplemented

    def __setitem__(self,key,value:Representation_vue):
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

    def __iter__(self) -> Iterator[Representation_case]:
        for vue in self.values():
            for case in vue:
                yield case