"""
Ce module contient les classes CoteDecalage et CotePosition.
"""

from __future__ import annotations
from typing import TYPE_CHECKING, Any

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from .position import Position
    from .decalage import Decalage
    from .direction import Direction

# Pas de classe parente

class CoteDecalage:
    """Un décalage et une direction, pour représenter un côté de case."""
    def __init__(self,emplacement: Decalage,direction:Direction):
        self.emplacement = emplacement
        self.direction=direction

    def __sub__(self,other:Any):
        emplacement = self.emplacement - other
        if isinstance(emplacement,Decalage):
            return CoteDecalage(emplacement,self.direction)
        return NotImplemented

    def __add__(self,other:Any):
        emplacement = self.emplacement + other
        if isinstance(emplacement,Decalage):
            return CoteDecalage(emplacement,self.direction)
        elif isinstance(emplacement,Position):
            return CotePosition(emplacement,self.direction)
        return NotImplemented

    def __radd__(self,other:Any):
        emplacement = other + self.emplacement
        if isinstance(emplacement,Decalage):
            return CoteDecalage(emplacement,self.direction)
        elif isinstance(emplacement,Position):
            return CotePosition(emplacement,self.direction)
        return NotImplemented

    def __eq__(self,other:Any):
        if isinstance(other,CoteDecalage):
            return self.emplacement == other.emplacement and self.direction == other.direction
        return NotImplemented

    def __hash__(self):
        return hash((self.emplacement,self.direction))

    def __str__(self):
        return f"Coté : {self.emplacement}, {self.direction}"

    def __repr__(self):
        return f"Coté : {self.emplacement}, {self.direction}"

    def oppose(self):
        """Le mur opposé à ce mur (sur la case voisine, dans la direction opposée)."""
        return CoteDecalage(self.emplacement+self.direction,self.direction.oppose)

class CotePosition:
    """Une position et une direction, pour représenter un côté de case."""
    def __init__(self,emplacement: Position,direction:Direction):
        self.emplacement = emplacement
        self.direction=direction

    def __sub__(self,other:Any):
        emplacement = self.emplacement - other
        if isinstance(emplacement,Decalage):
            return CoteDecalage(emplacement,self.direction)
        elif isinstance(emplacement,Position):
            return CotePosition(emplacement,self.direction)
        return NotImplemented

    def __add__(self,other:Any):
        emplacement = self.emplacement + other
        if isinstance(emplacement,Position):
            return CotePosition(emplacement,self.direction)
        return NotImplemented

    def __radd__(self,other:Any):
        emplacement = other + self.emplacement
        if isinstance(emplacement,Position):
            return CotePosition(emplacement,self.direction)
        return NotImplemented

    def __eq__(self,other:Any):
        if isinstance(other,CotePosition|CoteDecalage):
            return self.emplacement == other.emplacement and self.direction == other.direction
        return NotImplemented

    def __hash__(self):
        return hash((self.emplacement,self.direction))

    def __str__(self):
        return f"Coté : {self.emplacement}, {self.direction}"

    def __repr__(self):
        return f"Coté : {self.emplacement}, {self.direction}"

    def oppose(self):
        """Le mur opposé à ce mur (sur la case voisine, dans la direction opposée)."""
        return CotePosition(self.emplacement+self.direction,self.direction.oppose)

# Imports utilisés dans le code
from .decalage import Decalage
from .position import Position