from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Iterator, Any
import carte as crt
import networkx as nx

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from .case import Case
    from .mur import Mur

# Pas de classe parente

class Extrait(crt.Extrait):
    """Un extrait du labyrinthe"""
    def __init__(self, exterieur:set[crt.Position], subgraph:nx.MultiDiGraph):
        nx.MultiDiGraph.__init__(self)
        self.add_nodes_from(subgraph.nodes(data=True))
        self.add_edges_from(subgraph.edges(data=True, keys=True))
        self.exterieur = exterieur
        self.position_case: dict[crt.Position,Case] = {}
        for position in self.nodes:
            if position not in self.exterieur:
                self.position_case[position] = self.nodes[position]['case']

    def __contains__(self, item:Any):
        if isinstance(item,crt.Position):
            return item in self.nodes and item not in self.exterieur and item is not crt.POSITION_ABSENTE
        return super().__contains__(item)
    
    def __iter__(self) -> Iterator[crt.Position]:
        return iter(self.nodes - self.exterieur)
    
    def get_case(self, position:crt.Position) -> Case:
        return self.position_case[position]
    
    def get_mur(self, u:crt.Position, direction:crt.Direction, v:Optional[crt.Position]=None) -> Mur:
        assert u in self
        if v is None:
            v = self.get_cible(u, direction)
        return self[u][v][direction]['mur']
    
    def get_mur_oppose(self, u:crt.Position, direction:crt.Direction, v:Optional[crt.Position]=None) -> Optional[Mur]:
        assert u in self
        if v is None:
            v = self.get_cible(u, direction)
        # On vérifie que le mur existe, que v n'est pas POSITION_ABSENTE, et qu'il n'y a qu'un seul mur entre v et u
        if direction in self[u][v] and len(self[v][u]) == 1:
            return self[v][u]["mur"]
        
    def get_cible(self, position:crt.Position, direction:crt.Direction) -> crt.Position:
        assert position in self
        # Il devrait exister un mur sortant de position dans la direction direction
        # Il ne mêne pas nécessairement à position+direction
        for voisin in self[position]:
            if direction in self[position][voisin]:
                return voisin
        raise ValueError(f"La position {position} n'a pas de mur dans la direction {direction}")
