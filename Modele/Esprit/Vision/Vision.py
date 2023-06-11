from __future__ import annotations
from typing import TYPE_CHECKING, Set
import Carte as crt
import networkx as nx

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ...Labyrinthe.Extrait import Extrait
    from ...Entitee.Agissant.Vue.Vue import Vue

class Vision(Extrait):
    def __init__(self, vues:Set[Vue], tour:int):
        nx.MultiDiGraph.__init__(self)
        self.position_case:dict[crt.Position, Vision_case] = {}
        self.exterieur:Set[crt.Position] = set()
        self.voit(vues, tour)

    def voit(self, vues:Set[Vue], tour:int):
        for vue in vues:
            

    def get_case(self, position:crt.Position) -> Vision_case:
        return self.position_case[position]


# Imports utilisés dans le code
from .Case import Vision_case