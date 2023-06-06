from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Set
import networkx as nx

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from .Structure_spatiale.Position import Position
    from .Structure_spatiale.Direction import Direction
    from .Case import Case
    from .Mur import Mur
    from .Extrait import Extrait

class Labyrinthe(nx.MultiDiGraph): #Rarement Multi, mais ça arrive pour la case absente par exemple
    def __init__(self):
        super().__init__()
        self.position_case: dict[Position,Case] = {}
        self.add_case(CASE_ABSENTE)

    def add_case(self, case:Case, **attr):
        self.add_node(case.position, case=case, **attr)
        self.position_case[case.position] = case
        for direction in Direction:
            self.add_mur(case.position, case.position+direction, direction, Mur())

    def add_mur(self, u:Position, v:Position, direction:Direction, mur:Mur, **attr):
        if v not in self.position_case:
            self.add_case(Case(v))
        else:
            if v in self[u] and direction in self[u][v]:
                raise ValueError(f"Un mur existe déjà entre {u} et {v} dans la direction {direction}")
        self.add_edge(u, v, key=direction, mur=mur, **attr)

    def get_case(self, position:Position) -> Case:
        return self.position_case[position]
    
    def get_mur(self, u:Position, v:Position, direction:Direction) -> Mur:
        return self[u][v][direction]['mur']
    
    def get_mur_oppose(self, u:Position, v:Position, direction:Direction) -> Optional[Mur]:
        # On vérifie que le mur existe, que v n'est pas POSITION_ABSENTE, et qu'il n'y a qu'un seul mur entre v et u
        if direction in self[u][v] and v != POSITION_ABSENTE and len(self[u][v]) == 1:
            return self[v][u]["mur"]
        
    def extrait(self, positions:Set[Position]) -> Extrait:
        voisins:Set[Position] = {voisin for position in positions for voisin in self[position] if voisin not in positions}
        subgraph = super().subgraph(positions|voisins)
        return Extrait(voisins, subgraph)

from .Structure_spatiale.Direction import Direction
from .Mur import Mur
from .Case import Case
from .Extrait import Extrait
from .Absent import CASE_ABSENTE, POSITION_ABSENTE