"""
Ce fichier contient la classe Labyrinthe, qui représente un labyrinthe.
"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Set, Any, Dict
import networkx as nx

from .structure_spatiale.direction import Direction
from .mur import Mur
from .extrait import Extrait
from .absent import POSITION_ABSENTE

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from .structure_spatiale.etage import Etage
    from .structure_spatiale.position import Position

class Labyrinthe(nx.MultiDiGraph): #Rarement Multi, mais ça arrive pour la case absente par exemple
    """Classe représentant un labyrinthe."""
    def __init__(self):
        super().__init__() # type: ignore
        self.etages: Dict[Etage,nx.Graph] = {}
        self.add_pos(POSITION_ABSENTE)
        self.nodes:Set[Position] # type: ignore # C'est faux mais ça appaise les linters

    def __contains__(self, item:Any) -> bool:
        return item in self.nodes and item is not POSITION_ABSENTE

    def add_pos(self, position:Position, **attr:Dict[str,Any]):
        """Ajoute une case au labyrinthe."""
        self.add_node(position, **attr) #type: ignore
        if position.etage not in self.etages:
            self.etages[position.etage] = nx.Graph()
        self.etages[position.etage].add_node(position) #type: ignore
        for direction in Direction:
            if position+direction in position.etage:
                self.add_wal(position, position+direction, direction)

    def add_wal(self, u:Position, v:Position, direction:Direction, **attr:Dict[str,Any]):
        """Ajoute un mur entre deux cases."""
        if v not in self.nodes:
            self.add_pos(v)
        else:
            if v in self[u] and direction in self[u][v]:
                raise ValueError(f"Un mur existe déjà entre {u} et {v} dans la direction {direction}")
        self.add_edge(u, v, key=direction, **attr) #type: ignore
    
    def get_mur(self, u:Position, direction:Direction, v:Optional[Position]=None) -> Mur:
        """Renvoie le mur entre u et v dans la direction direction."""
        if v is None:
            v = self.get_cible(u, direction)
        return self[u][v][direction]['mur'] #type: ignore
    
    def get_mur_oppose(self, u:Position, direction:Direction, v:Optional[Position]=None) -> Optional[Mur]:
        """Renvoie le mur entre v et u dans la direction opposée à direction, ou None si ce mur n'existe pas."""
        if v is None:
            v = self.get_cible(u, direction)
        # On vérifie que le mur existe, que v n'est pas POSITION_ABSENTE, et qu'il n'y a qu'un seul mur entre v et u
        if direction in self[u][v] and len(self[v][u]) == 1: #type: ignore
            return self[v][u]["mur"] #type: ignore
        
    def get_cible(self, position:Position, direction:Direction) -> Position:
        """Renvoie la position voisine de position dans la direction direction."""
        # Il devrait exister un mur sortant de position dans la direction direction
        # Il ne mêne pas nécessairement à position+direction
        for voisin in self[position]: #type: ignore
            if direction in self[position][voisin]: #type: ignore
                return voisin #type: ignore
        raise ValueError(f"La position {position} n'a pas de mur dans la direction {direction}")
        
    def extrait(self, positions:Set[Position]) -> Extrait:
        """Renvoie un extrait du labyrinthe contenant les positions données."""
        voisins:Set[Position] = {voisin for position in positions for voisin in self[position] if voisin not in positions} #type: ignore
        subgraph = super().subgraph(positions|voisins) # type: ignore
        return Extrait(voisins, subgraph) # type: ignore
