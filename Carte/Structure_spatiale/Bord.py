from __future__ import annotations
from typing import TYPE_CHECKING, List, Iterator

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from .Position import Position
    from .Decalage import Decalage
    from .Cote import Cote_position, Cote_decalage

# Pas de classe parente

# Valeurs par défaut des paramètres
from .Decalage import Decalage

class Bord:
    """Représente les limites d'un espace"""
    def __init__(self,emplacement: Position|Decalage):
        self.emplacement = emplacement

    def __contains__(self,item):
        if item is None:
            return False
        if isinstance(item,Cote_position|Cote_decalage):
            return (item.direction == Direction.HAUT and item.emplacement.y == 0 and 0 <= item.emplacement.x < self.emplacement.x) or (item.direction == Direction.BAS and item.emplacement.y == self.emplacement.y-1 and 0 <= item.emplacement.x < self.emplacement.x) or (item.direction == Direction.GAUCHE and item.emplacement.x == 0 and 0 <= item.emplacement.y < self.emplacement.y) or (item.direction == Direction.DROITE and item.emplacement.x == self.emplacement.x-1 and 0 <= item.emplacement.y < self.emplacement.y)
        return NotImplemented

    def __iter__(self):
        for i in range(self.emplacement.x):
            yield Cote_decalage(Decalage(i,0),Direction.HAUT)
            yield Cote_decalage(Decalage(i,self.emplacement.y-1),Direction.BAS)
        for j in range(self.emplacement.y):
            yield Cote_decalage(Decalage(0,j),Direction.GAUCHE)
            yield Cote_decalage(Decalage(self.emplacement.x-1,j),Direction.DROITE)

class Bord_dec(Bord):
    """Un bord, décalé dans l'espace"""
    def __init__(self,position:Position,emplacement:Decalage=Decalage(1,1),entrees:List[Cote_decalage]=[]):
        self.position = position
        self.emplacement = emplacement
        self.entrees = entrees

    def __contains__(self,item):
        if item is None:
            return False
        if isinstance(item,Cote_position|Cote_decalage):
            item_pat = item-self.position
            return (Bord.__contains__(self,item_pat) and not item_pat in self.entrees) #/!\ Jamais utilisé !?
        return NotImplemented

    def __iter__(self) -> Iterator[Cote_position]:
        for cote_pat in Bord.__iter__(self):
            if not cote_pat in self.entrees:
                cote = cote_pat + self.position
                yield cote

class Bord_pat(Bord_dec):
    """Représente les bords d'un pattern"""
    def __contains__(self,item):
        if item is None:
            return False
        if isinstance(item,Cote_position|Cote_decalage):
            item_pat = item-self.position
            item_opp = item_pat.oppose()
            return (Bord.__contains__(self,item_pat) or Bord.__contains__(self,item_opp)) and not (item_pat in self.entrees or item_opp in self.entrees)
        return NotImplemented

    def __iter__(self):
        for cote_pat in Bord.__iter__(self):
            if not cote_pat in self.entrees:
                cote = cote_pat + self.position
                yield cote
                yield cote.oppose()

class Bord_lab(Bord):
    """Représente les différents bords (bords réels, bords de patterns) d'un labyrinthe"""
    def __init__(self,emplacement:Position|Decalage,bords_interieurs:List[Bord_pat]):
        self.emplacement = emplacement
        self.bords_interieurs = bords_interieurs

    def __contains__(self, item):
        if Bord.__contains__(self,item):
            return True
        for bord in self.bords_interieurs:
            if item in bord:
                return True
        return False

    def __iter__(self):
        """
        Ici la difficulté est de ne pas repasser au même mur plusieurs fois.
        Idées :
            Accepter de passer plusieurs fois par le même mur (risque de causer des bugs (effets doubles, etc.))
            Parcourir tout le labyrinthe en renvoyant tout ce qui est in self (temps de calcul accru sur les gros labyrinthes)
            Garder en mémoire les murs déjà passés (utilisation de la mémoire accrue (contraire au principe des itérateurs))
            Déduire les endroits où l'on est déjà passé
        """
        for cote in Bord.__iter__(self):
            yield cote
        for i in range(len(self.bords_interieurs)):
            for cote in self.bords_interieurs[i]:
                if not Bord.__contains__(self,cote):
                    passe=False
                    for j in range(i):
                        if cote in self.bords_interieurs[j]:
                            passe=True
                            break
                    if not passe:
                        yield cote

# Imports utilisés dans le code
from .Direction import Direction
from .Cote import Cote_decalage, Cote_position