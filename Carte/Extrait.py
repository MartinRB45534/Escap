from __future__ import annotations
from typing import TYPE_CHECKING, Set, Optional, Iterator
import networkx as nx

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from .Structure_spatiale.Position import Position
    from .Structure_spatiale.Direction import Direction
    from .Case import Case
    from .Mur import Mur

# Pas de classe parente

class Extrait(nx.MultiDiGraph):
    def __init__(self, exterieur:Set[Position], subgraph:nx.MultiDiGraph):
        super().__init__()
        self.add_nodes_from(subgraph.nodes(data=True))
        self.add_edges_from(subgraph.edges(data=True, keys=True))
        self.exterieur = exterieur
        self.position_case: dict[Position,Case] = {}
        for position in self.nodes:
            if position not in self.exterieur:
                self.position_case[position] = self.nodes[position]['case']

    def __contains__(self, item):
        if isinstance(item,Position):
            return item in self.nodes and item not in self.exterieur and item is not POSITION_ABSENTE
        return super().__contains__(item)
    
    def __iter__(self) -> Iterator[Position]:
        return iter(self.nodes - self.exterieur)
    
    def get_case(self, position:Position) -> Case:
        return self.position_case[position]
    
    def get_mur(self, u:Position, direction:Direction, v:Optional[Position]=None) -> Mur:
        assert u in self
        if v is None:
            v = self.get_cible(u, direction)
        return self[u][v][direction]['mur']
    
    def get_mur_oppose(self, u:Position, direction:Direction, v:Optional[Position]=None) -> Optional[Mur]:
        assert u in self
        if v is None:
            v = self.get_cible(u, direction)
        # On vérifie que le mur existe, que v n'est pas POSITION_ABSENTE, et qu'il n'y a qu'un seul mur entre v et u
        if direction in self[u][v] and len(self[v][u]) == 1:
            return self[v][u]["mur"]
        
    def get_cible(self, position:Position, direction:Direction) -> Position:
        assert position in self
        # Il devrait exister un mur sortant de position dans la direction direction
        # Il ne mêne pas nécessairement à position+direction
        for voisin in self[position]:
            if direction in self[position][voisin]:
                return voisin
        raise ValueError(f"La position {position} n'a pas de mur dans la direction {direction}")
    
from .Structure_spatiale.Absent import POSITION_ABSENTE