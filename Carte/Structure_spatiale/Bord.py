"""
Contient toutes les classes permettant de représenter les bords d'un espace.
"""

from __future__ import annotations
from types import NotImplementedType
from typing import TYPE_CHECKING, List, Any
from .decalage import Decalage

if TYPE_CHECKING:
    from .position import Position
    from .cote import CotePosition, CoteDecalage

class Bord:
    """Représente les limites d'un espace"""
    def __init__(self,emplacement: Position|Decalage):
        self.emplacement = emplacement

    def __contains__(self,item:Any):
        if item is None:
            return False
        if isinstance(item,CotePosition|CoteDecalage):
            return (item.direction == Direction.HAUT and item.emplacement.y == 0 and 0 <= item.emplacement.x < self.emplacement.x) or (item.direction == Direction.BAS and item.emplacement.y == self.emplacement.y-1 and 0 <= item.emplacement.x < self.emplacement.x) or (item.direction == Direction.GAUCHE and item.emplacement.x == 0 and 0 <= item.emplacement.y < self.emplacement.y) or (item.direction == Direction.DROITE and item.emplacement.x == self.emplacement.x-1 and 0 <= item.emplacement.y < self.emplacement.y)
        return NotImplemented

    def __iter__(self):
        for i in range(self.emplacement.x):
            yield CoteDecalage(Decalage(i,0),Direction.HAUT)
            yield CoteDecalage(Decalage(i,self.emplacement.y-1),Direction.BAS)
        for j in range(self.emplacement.y):
            yield CoteDecalage(Decalage(0,j),Direction.GAUCHE)
            yield CoteDecalage(Decalage(self.emplacement.x-1,j),Direction.DROITE)

class BordDec(Bord):
    """Un bord, décalé dans l'espace"""
    def __init__(self,position:Position,emplacement:Decalage=Decalage(1,1),entrees:List[CoteDecalage]=[]):
        super().__init__(emplacement)
        self.position = position
        self.entrees = entrees

    def __contains__(self,item:Any):
        if item is None:
            return False
        if isinstance(item,CotePosition|CoteDecalage):
            item_pat = item-self.position
            return (Bord.__contains__(self,item_pat) and not item_pat in self.entrees) #/!\ Jamais utilisé !?
        return NotImplemented

    def __iter__(self):
        for cote_pat in Bord.__iter__(self):
            if not cote_pat in self.entrees:
                cote = cote_pat + self.position
                yield cote

class BordPat(BordDec):
    """Représente les bords d'un pattern"""
    def __contains__(self,item:Any):
        if item is None:
            return False
        if isinstance(item,CotePosition|CoteDecalage):
            item_pat = item-self.position
            if isinstance(item_pat,NotImplementedType):
                raise NotImplementedError
            item_opp = item_pat.oppose()
            return (Bord.__contains__(self,item_pat) or Bord.__contains__(self,item_opp)) and not (item_pat in self.entrees or item_opp in self.entrees)
        return NotImplemented

    def __iter__(self):
        for cote_pat in Bord.__iter__(self):
            if not cote_pat in self.entrees:
                cote = cote_pat + self.position
                if isinstance(cote,NotImplementedType):
                    raise NotImplementedError
                yield cote
                yield cote.oppose()

class BordLab(Bord):
    """Représente les différents bords (bords réels, bords de patterns) d'un labyrinthe"""
    def __init__(self,emplacement:Position|Decalage,bords_interieurs:List[BordPat]):
        super().__init__(emplacement)
        self.bords_interieurs = bords_interieurs

    def __contains__(self, item:Any):
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
        for i, bord in enumerate(self.bords_interieurs):
            for cote in bord:
                assert isinstance(cote,CoteDecalage)
                if not Bord.__contains__(self,cote):
                    passe=False
                    for j in range(i):
                        if cote in self.bords_interieurs[j]:
                            passe=True
                            break
                    if not passe:
                        yield cote

# Imports utilisés dans le code
from .direction import Direction
from .cote import CoteDecalage, CotePosition
