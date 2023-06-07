from __future__ import annotations
from typing import TYPE_CHECKING, List, Tuple, Optional, Set, Iterator, Literal, Self

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ..Labyrinthe.Structure_spatiale.Position import Position
    from ..Labyrinthe.Structure_spatiale.Decalage import Decalage
    from ..Labyrinthe.Structure_spatiale.Direction import Direction
    from ..Labyrinthe.Structure_spatiale.Cote import Cote_position,Cote_decalage
    from ..Labyrinthe.Vue import Representation_case
    from ..Labyrinthe.Case import Case
    from ..Entitee.Agissant.Agissant import Agissant
    from ..Entitee.Item.Item import Item
    from ..Entitee.Decors.Decor import Decors

# Import des classes parentes
from ..Labyrinthe.Structure_spatiale.Espace import Espace

class Vue(Espace):
    """Une représentation simplifiée d'un labyrinthe"""
    def __init__(self,ID:str,matrice:List[List],decalage:Decalage):
        self.id = ID
        self.matrice_cases = matrice
        self.decalage = decalage

    def __getitem__(self,key:Position|Decalage|Cote_position|Cote_decalage|tuple):
        if isinstance(key,tuple):
            return self.matrice_cases[key[0]][key[1]]
        elif isinstance(key,Position):
            if key.lab != self.id:
                raise ValueError("La position n'est pas dans l'étage")
            return self.matrice_cases[key.x][key.y]
        elif isinstance(key,Decalage):
            return self.matrice_cases[key.x][key.y]
        if isinstance(key,Cote_position|Cote_decalage):
            return self[key.emplacement][key.direction]
        return NotImplemented

    def __setitem__(self,key:Position|Decalage|Cote_position|Cote_decalage|tuple,value):
        if isinstance(key,tuple):
            self[key[0]][key[1]] = value
        elif isinstance(key,Position):
            if key.lab != self.id:
                raise ValueError("La position n'est pas dans l'étage")
            self.matrice_cases[key.x][key.y] = value
        elif isinstance(key,Decalage):
            self.matrice_cases[key.x][key.y] = value
        if isinstance(key,Cote_position|Cote_decalage):
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
        elif isinstance(item,Cote_position):
            return item.emplacement in self
        return NotImplemented
    
    def __iter__(self) -> Iterator:
        for decalage in self.decalage:
            yield self[decalage]

    def case_from_tuple(self,tuple:Tuple[int,int]):
        return self.matrice_cases[tuple[0]][tuple[1]]
    
    def mur_from_tuple(self,tuple:Tuple[int,int,Direction]):
        return self.matrice_cases[tuple[0]][tuple[1]][tuple[2]]
    
    def case_from_position(self,position:Position|Decalage):
        return self.matrice_cases[position.x][position.y]

    def mur_from_cote(self,cote:Cote_position|Cote_decalage):
        return self.matrice_cases[cote.emplacement.x][cote.emplacement.y][cote.direction]


class Representation_case:
    """Regroupe les informations sur une case qui seront envoyées à l'agissant"""
    def __init__(self,case:Case,clarte:float,code:int,cibles:List[List[Position|Literal[False]]],agissant:Optional[Agissant],decors:Optional[Decors],items:Set[Item],effets:List[List[int]],repoussante:bool):
        self.case = case #La position de la case
        self.clarte = clarte #La clarté, qui vient d'être calculée pour l'agissant
        self.oubli = 0 #Pour le décompte de l'oubli
        self.trajets = {"dangerosite":[],"importance":[]}
        self.visitee = False #Pour savoir si la case a déjà été visitée
        self.code = code #Le code correspondant aux auras et autres effets
        self.cibles = cibles #Les murs et leur traversabilité pour l'agissant
        self.agissant = agissant #L'éventuel agissant sur la case
        self.decors = decors #L'éventuel décor de la case
        self.items = items #Les éventuels items sur la case
        self.effets = effets #Pour stocker les effets (attaques delayées)
        self.repoussante = repoussante #Si la case est repoussante

    def oublie(self, oubli:int):
        """Pour oublier les cases visitées il y a trop longtemps"""
        self.trajets = {"dangerosite":[],"importance":[]}
        self.effets = []
        self.repoussante = False
        if self.oubli > 1:
            self.oubli = min(oubli, self.oubli-1)
        elif self.oubli > 0:
            self.clarte = 0
            self.oubli = 0
            self.code = 0
            self.cibles:List[List[Position|Literal[False]]] = [[False,False,False,False,False],[False,False,False,False,False],[False,False,False,False,False],[False,False,False,False,False]]
            self.agissant = None
            self.decors = None
            self.items = set()
            return True
        return False
    
    def update(self, other:Self):
        self.oubli = other.oubli
        self.code = other.code
        self.cibles = other.cibles
        self.agissant = other.agissant
        self.decors = other.decors
        self.items = other.items
        self.effets = other.effets
        self.repoussante = other.repoussante
    
    def __getitem__(self,key:Tuple[str,int]) -> float:
        trajet = self.trajets.get(key[0],[])
        if len(trajet) > key[1] and -len(trajet) <= key[1] :
            return trajet[key[1]]
        return 0

    def __setitem__(self,key:Tuple[str,int],value:float):
        if key[0] not in self.trajets:
            self.trajets[key[0]] = []
        if len(self.trajets[key[0]]) <= key[1]:
            self.trajets[key[0]] += [0]*(key[1]-len(self.trajets[key[0]])+1)
        self.trajets[key[0]][key[1]] = value

class Representation_vue(Vue):
    """Une représentation simplifiée d'un labyrinthe"""
    def __init__(self, ID: str, matrice: List[List[Representation_case]], decalage: Decalage):
        self.id = ID
        self.matrice_cases = matrice
        self.decalage = decalage
        
    def __contains__(self,item:Position|Decalage|Cote_position|Cote_decalage|tuple|None):
        if item is None:
            return False
        elif isinstance(item,Position):
            return item.lab == self.id and 0<=item.x<self.decalage.x and 0<=item.y<self.decalage.y
        elif isinstance(item,Decalage):
            return 0<=item.x<self.decalage.x and 0<=item.y<self.decalage.y
        elif isinstance(item,Cote_position|Cote_decalage):
            return item.emplacement in self
        return NotImplemented
    
    def __iter__(self) -> Iterator[Representation_case]:
        for decalage in self.decalage:
            yield self[decalage]

    def case_from_tuple(self,tuple:Tuple[int,int]) -> Representation_case:
        return self.matrice_cases[tuple[0]][tuple[1]]
    
    def mur_from_tuple(self,tuple:Tuple[int,int,Direction]) -> List[Position|Literal[False]]:
        return self.matrice_cases[tuple[0]][tuple[1]].cibles[tuple[2]]
    
    def case_from_position(self,position:Position) -> Representation_case:
        if position.lab != self.id:
            raise ValueError("La position n'est pas au bon étage")
        return self.matrice_cases[position.x][position.y]
    
    def case_from_decalage(self,decalage:Decalage) -> Representation_case:
        return self.matrice_cases[decalage.x][decalage.y]

    def mur_from_cote(self,cote:Cote_position|Cote_decalage) -> List[Position|Literal[False]]:
        if isinstance(cote,Cote_position) and cote.emplacement.lab != self.id:
            raise ValueError("Le coté n'est pas au bon étage")
        return self.matrice_cases[cote.emplacement.x][cote.emplacement.y].cibles[cote.direction]

class Vues(dict[str,Representation_vue]):
    """Un dictionnaire qui contient des objets Representation_vue"""
    def __contains__(self,item):
        if item is None:
            return False
        elif isinstance(item,Position):
            return item.lab in self and item in self[item.lab]
        elif isinstance(item,Cote_position):
            return item.emplacement in self
        else:
            return dict.__contains__(self,item)

    def __iter__(self) -> Iterator[Representation_case]:
        for vue in self.values():
            for case in vue:
                yield case

    def case_from_tuple(self,tuple:Tuple[str,int,int]) -> Representation_case:
        return self[tuple[0]].case_from_tuple(tuple[1:])
    
    def mur_from_tuple(self,tuple:Tuple[str,int,int,Direction]) -> List[Position|Literal[False]]:
        return self[tuple[0]].mur_from_tuple(tuple[1:])
    
    def case_from_position(self,position:Position) -> Representation_case:
        return self[position.lab].case_from_position(position)

    def mur_from_cote(self,cote:Cote_position) -> List[Position|Literal[False]]:
        return self[cote.emplacement.lab].mur_from_cote(cote)
    
# Imports utilisés dans le code
from ..Labyrinthe.Structure_spatiale.Decalage import Decalage
from ..Labyrinthe.Structure_spatiale.Position import Position
from ..Labyrinthe.Structure_spatiale.Cote import Cote_position, Cote_decalage