"""
Ce fichier contient la classe Extrait, qui représente un extrait de labyrinthe.
"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Iterator, Any
import networkx as nx
    
from .structure_spatiale.absent import POSITION_ABSENTE

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from .structure_spatiale.position import Position
    from .structure_spatiale.direction import Direction
    from .mur import Mur

# Pas de classe parente

class Extrait(nx.MultiDiGraph):
    """Classe représentant un extrait de labyrinthe."""
    def __init__(self, exterieur:set[Position], subgraph:nx.MultiDiGraph):
        super().__init__() # type: ignore
        self.add_nodes_from(subgraph.nodes(data=True)) # type: ignore
        self.add_edges_from(subgraph.edges(data=True, keys=True)) # type: ignore
        self.exterieur = exterieur
        self.nodes:set[Position] # type: ignore # C'est faux mais ça appaise les linters

    def __contains__(self, item:Any): 
        return item in self.nodes and item not in self.exterieur and item is not POSITION_ABSENTE

    def __iter__(self) -> Iterator[Position]:
        return iter(self.nodes - self.exterieur) # type: ignore

    def get_mur(self, u:Position, direction:Direction, v:Optional[Position]=None) -> Mur:
        """Renvoie le mur entre u et v dans la direction direction."""
        assert u in self
        if v is None:
            v = self.get_cible(u, direction)
        return self[u][v][direction]['mur'] # type: ignore

    def get_mur_oppose(self, u:Position, direction:Direction, v:Optional[Position]=None) -> Optional[Mur]:
        """Renvoie le mur opposé à celui entre u et v dans la direction direction."""
        assert u in self
        if v is None:
            v = self.get_cible(u, direction)
        # On vérifie que le mur existe, que v n'est pas POSITION_ABSENTE, et qu'il n'y a qu'un seul mur entre v et u
        if direction in self[u][v] and len(self[v][u]) == 1: # type: ignore
            return self[v][u]["mur"] # type: ignore
        
    def get_cible(self, position:Position, direction:Direction) -> Position:
        """Renvoie la position voisine de position dans la direction direction."""
        assert position in self
        # Il devrait exister un mur sortant de position dans la direction direction
        # Il ne mêne pas nécessairement à position+direction
        for voisin in self[position]: # type: ignore
            if direction in self[position][voisin]: # type: ignore
                return voisin # type: ignore
        raise ValueError(f"La position {position} n'a pas de mur dans la direction {direction}")
