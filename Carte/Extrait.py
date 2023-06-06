from __future__ import annotations
from typing import TYPE_CHECKING, Set
import networkx as nx

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from .Structure_spatiale.Position import Position

# Pas de classe parente

class Extrait(nx.MultiDiGraph):
    def __init__(self, exterieur:Set[Position], subgraph:nx.MultiDiGraph):
        super().__init__()
        self.add_nodes_from(subgraph.nodes(data=True))
        self.add_edges_from(subgraph.edges(data=True, keys=True))
        self.exterieur = exterieur