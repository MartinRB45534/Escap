"""
Ce fichier contient la classe Labyrinthe, qui représente un labyrinthe.
"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Set, Any, Dict
import networkx as nx

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from .structure_spatiale.position import Position
    from .structure_spatiale.direction import Direction
    from .structure_spatiale.etage import Etage
    from .case import Case
    from .mur import Mur
    from .extrait import Extrait

class Labyrinthe(nx.MultiDiGraph): #Rarement Multi, mais ça arrive pour la case absente par exemple
    """Classe représentant un labyrinthe."""
    def __init__(self):
        super().__init__()
        self.position_case: dict[Position,Case] = {}
        self.etages: dict[Etage,nx.Graph] = {}
        self.add_case(CASE_ABSENTE)

    def __contains__(self, item:Any):
        if isinstance(item,Position):
            return item in self.nodes and item is not POSITION_ABSENTE
        return super().__contains__(item)

    def add_case(self, case:Case, **attr:Dict[str,Any]):
        """Ajoute une case au labyrinthe."""
        self.add_node(case.position, case=case, **attr)
        self.position_case[case.position] = case
        for direction in Direction:
            self.add_mur(case.position, case.position+direction, direction, Mur())
        if case.position.etage not in self.etages:
            self.etages[case.position.etage] = nx.Graph()
        self.etages[case.position.etage].add_node(case.position)
        for direction in Direction:
            if case.position+direction in case.position.etage:
                self.etages[case.position.etage].add_edge(case.position, case.position+direction, key=direction)

    def add_mur(self, u:Position, v:Position, direction:Direction, mur:Mur, **attr:Dict[str,Any]):
        """Ajoute un mur entre deux cases."""
        if v not in self.position_case:
            self.add_case(Case(v))
        else:
            if v in self[u] and direction in self[u][v]:
                raise ValueError(f"Un mur existe déjà entre {u} et {v} dans la direction {direction}")
        self.add_edge(u, v, key=direction, mur=mur, **attr)

    def get_case(self, position:Position) -> Case:
        """Renvoie la case à la position donnée."""
        return self.position_case[position]
    
    def get_mur(self, u:Position, direction:Direction, v:Optional[Position]=None) -> Mur:
        """Renvoie le mur entre u et v dans la direction direction."""
        if v is None:
            v = self.get_cible(u, direction)
        return self[u][v][direction]['mur']
    
    def get_mur_oppose(self, u:Position, direction:Direction, v:Optional[Position]=None) -> Optional[Mur]:
        """Renvoie le mur entre v et u dans la direction opposée à direction, ou None si ce mur n'existe pas."""
        if v is None:
            v = self.get_cible(u, direction)
        # On vérifie que le mur existe, que v n'est pas POSITION_ABSENTE, et qu'il n'y a qu'un seul mur entre v et u
        if direction in self[u][v] and len(self[v][u]) == 1:
            return self[v][u]["mur"]
        
    def get_cible(self, position:Position, direction:Direction) -> Position:
        """Renvoie la position voisine de position dans la direction direction."""
        # Il devrait exister un mur sortant de position dans la direction direction
        # Il ne mêne pas nécessairement à position+direction
        for voisin in self[position]:
            if direction in self[position][voisin]:
                return voisin
        raise ValueError(f"La position {position} n'a pas de mur dans la direction {direction}")
        
    def extrait(self, positions:Set[Position]) -> Extrait:
        """Renvoie un extrait du labyrinthe contenant les positions données."""
        voisins:Set[Position] = {voisin for position in positions for voisin in self[position] if voisin not in positions}
        subgraph = super().subgraph(positions|voisins)
        return Extrait(voisins, subgraph)

from .structure_spatiale.direction import Direction
from .mur import Mur
from .case import Case
from .extrait import Extrait
from .absent import CASE_ABSENTE, POSITION_ABSENTE
