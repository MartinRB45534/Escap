from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Set
import carte as crt
import networkx as nx

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from .case import CaseVue, CasePasVue
    from .mur import MurVu

# Import de la classe parente
from ....labyrinthe.Extrait import Extrait

class Vue(Extrait):
    def __init__(self, exterieur:Set[crt.Position], subgraph:nx.MultiDiGraph, position_case:dict[crt.Position,CaseVue]):
        nx.MultiDiGraph.__init__(self)
        self.add_nodes_from(subgraph.nodes(data=True))
        self.add_edges_from(subgraph.edges(data=True, keys=True))
        self.exterieur = exterieur
        self.position_case: dict[crt.Position,CaseVue] = position_case

    def get_case(self, position:crt.Position) -> CaseVue:
        return self.position_case[position]
    
    def get_mur(self, u:crt.Position, direction:crt.Direction, v:Optional[crt.Position]=None) -> MurVu:
        mur = super().get_mur(u, direction, v)
        assert isinstance(mur, MurVu)
        return mur
    
    def get_mur_oppose(self, u:crt.Position, direction:crt.Direction, v:Optional[crt.Position]=None) -> Optional[MurVu]:
        mur = super().get_mur_oppose(u, direction, v)
        if mur is not None:
            assert isinstance(mur, MurVu)
        return mur

def voit_vue(extrait: Extrait) -> Vue:
    subgraph = nx.MultiDiGraph(extrait)
    position_case = {position: voit_case(case) for position, case in extrait.position_case.items()}
    for position in extrait:
        subgraph.nodes[position]['case'] = position_case[position]
    for position in extrait.exterieur:
        subgraph.nodes[position]['case'] = CasePasVue(position)
    for u,v, direction in subgraph.edges:
        subgraph[u][v][direction]['mur'] = voit_mur(subgraph[u][v][direction]['mur'])
    return Vue(
        extrait.exterieur,
        subgraph,
        position_case,
    )

from .case import voit_case
from .mur import voit_mur