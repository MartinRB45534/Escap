from __future__ import annotations
from typing import Any
import Carte as crt

# Pas d'import utilisé uniquement dans les annotations

class Vision_position:
    """
    Quelques positions que la classe crt.Position ne peut pas représenter :
    - les positions inconnues (différentes de la position absente)
    - les positions d'espaces (quand on suppose qu'un agissant est dans un ensemble de cases donné)
    - les positions multiples (quand on suppose qu'un agissant est sur l'une de plusieurs positions possibles)
    """
    # Ces positions ne permettent pas l'accès aux propriétés habituelles de Position

class Position_inconnue(Vision_position):
    """
    On sait que l'entitée est quelque part, mais on n'a pas la moindre idée où.
    """
    def __init__(self):
        pass

    def __eq__(self,other:Any):
        if isinstance(other,crt.Position|Vision_position):
            return False # On n'est même pas égal à une autre position inconnue
        return NotImplemented
    
    def __hash__(self):
        return hash("Position_inconnue")
    
    def __contains__(self,item:Any):
        if isinstance(item,crt.Position|Vision_position):
            return False # On ne peut pas être contenu dans une position connue
        return False
    
    def __str__(self):
        return "Position inconnue"
    
    def __repr__(self):
        return "Position_inconnue()"
    
POSITION_INCONNUE = Position_inconnue() # On ne crée qu'une seule instance de Position_inconnue

class Position_espace(Vision_position):
    """
    On sait que l'entitée est dans un ensemble de cases donné.
    """
    def __init__(self,espace:set[crt.Position]):
        self.espace = espace

    def __eq__(self,other:Any):
        if isinstance(other,Position_espace):
            return bool(self.espace & other.espace) # On est égal à une autre position d'espace si les deux espaces se croisent
        return NotImplemented
    
    def __hash__(self):
        return hash((self.espace))
    
    def __contains__(self,item:Any):
        if isinstance(item,crt.Position):
            return item in self.espace or any(item in position for position in self.espace)
        elif isinstance(item,Position_espace):
            return bool(self.espace & item.espace)
        elif isinstance(item,Position_multiple):
            return any(position in self for position in item.positions)
    
    def __str__(self):
        return f"Position espace : {self.espace}"
    
    def __repr__(self):
        return f"Position_espace({self.espace})"
    
    def __iter__(self):
        return iter(self.espace)
    
class Position_multiple(Vision_position):
    """
    On sait que l'entitée est sur l'une de plusieurs positions possibles.
    """
    def __init__(self,positions:set[crt.Position]):
        self.positions = positions

    def __eq__(self,other:Any):
        return False
    
    def __hash__(self):
        return hash((self.positions))
    
    def __contains__(self,item:Any):
        return any(item in position for position in self.positions)
    
    def __str__(self):
        return f"Position multiple : {self.positions}"
    
    def __repr__(self):
        return f"Position_multiple({self.positions})"
    
    def __iter__(self):
        return iter(self.positions)