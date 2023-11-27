from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import networkx as nx
import carte as crt

# Import de la classe parente
from ....labyrinthe.extrait import Extrait

# Imports utilisés dans le code
from .case import voit_case, CasePasVue
from .mur import voit_mur

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from .case import CaseVue
    from .mur import MurVu

class Vue(Extrait):
    """Un extrait de labyrinthe vu par un agissant."""
    def __init__(self, exterieur:set[crt.Position], subgraph:nx.MultiDiGraph, position_case:dict[crt.Position,CaseVue]):
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
    """Transforme un extrait en vue."""
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
