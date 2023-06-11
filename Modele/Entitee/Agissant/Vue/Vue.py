from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Set
import Carte as crt
import networkx as nx

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from .Case import Case_vue
    from .Mur import Mur_vu

# Import de la classe parente
from ....Labyrinthe.Extrait import Extrait

class Vue(Extrait):
    def __init__(self, exterieur:Set[crt.Position], subgraph:nx.MultiDiGraph, position_case:dict[crt.Position,Case_vue]):
        nx.MultiDiGraph.__init__(self)
        self.add_nodes_from(subgraph.nodes(data=True))
        self.add_edges_from(subgraph.edges(data=True, keys=True))
        self.exterieur = exterieur
        self.position_case: dict[crt.Position,Case_vue] = position_case

    def get_case(self, position:crt.Position) -> Case_vue:
        return self.position_case[position]
    
    def get_mur(self, u:crt.Position, direction:crt.Direction, v:Optional[crt.Position]=None) -> Mur_vu:
        mur = super().get_mur(u, direction, v)
        assert isinstance(mur, Mur_vu)
        return mur
    
    def get_mur_oppose(self, u:crt.Position, direction:crt.Direction, v:Optional[crt.Position]=None) -> Optional[Mur_vu]:
        mur = super().get_mur_oppose(u, direction, v)
        if mur is not None:
            assert isinstance(mur, Mur_vu)
        return mur

def voit_vue(extrait: Extrait) -> Vue:
    subgraph = nx.MultiDiGraph(extrait)
    for position in subgraph.nodes:
        subgraph.nodes[position]['case'] = voit_case(subgraph.nodes[position]['case'])
    for u,v, direction in subgraph.edges:
        subgraph[u][v][direction]['mur'] = voit_mur(subgraph[u][v][direction]['mur'])
    return Vue(
        extrait.exterieur,
        subgraph,
        {position: voit_case(case) for position, case in extrait.position_case.items()}
    )

from .Case import voit_case
from .Mur import voit_mur