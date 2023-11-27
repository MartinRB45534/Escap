"""Ce module contient la classe Labyrinthe, qui représente le labyrinthe du jeu."""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Set, Any, Dict, Type
import networkx as nx
import carte as crt

# Imports utilisés dans le code
from .absent import CASE_ABSENTE
from .case import Case
from .extrait import Extrait
from .mur import MurImpassable, MurPlein

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from .mur import Mur
    from ..effet.case.aura.auras import AuraPermanente
    from ..entitee.agissant.agissant import Agissant
    from ..entitee.item.item import Item
    from ..commons import Deplacement, Forme, Passage

class Labyrinthe(crt.Labyrinthe):
    """Le labyrinthe"""
    def __init__(self):
        super().__init__()
        self.position_case: Dict[crt.Position,Case] = {}
        self.add_case(CASE_ABSENTE)

    def __contains__(self, item: Any):
        if isinstance(item,crt.Position):
            return item in self.nodes and item is not crt.POSITION_ABSENTE
        return super().__contains__(item)
    
    def ajoute_etage(self, etage:crt.Etage, aura:Type[AuraPermanente], opacite:int, niveau:int, responsable:Agissant):
        """Ajoute un étage au labyrinthe."""
        for position in etage.positions:
            self.add_case(Case(position, aura, opacite, niveau, responsable))
            for direction in crt.Direction:
                if position+direction in etage:
                    self.add_mur(position, position+direction, direction, MurPlein(niveau))
                    self.etages[position.etage].add_edge(position, position+direction, key=direction) #type: ignore
                else:
                    self.add_mur(position, crt.POSITION_ABSENTE, direction, MurImpassable(10))

    def add_case(self, case:Case, **attr:Dict[str,Any]):
        """Ajoute une case au labyrinthe."""
        self.add_node(case.position, case=case, **attr) #type: ignore
        self.position_case[case.position] = case
        if case.position.etage not in self.etages: # Représente les étages physiques (pour tout ce qui ignore les murs et les téléporteurs)
            self.etages[case.position.etage] = nx.Graph()
        self.etages[case.position.etage].add_node(case.position) #type: ignore

    def add_mur(self, u:crt.Position, v:crt.Position, direction:crt.Direction, mur:Mur, **attr:Dict[str,Any]): #type: ignore
        """Ajoute un mur entre deux cases."""
        if v not in self.position_case:
            raise ValueError(f"La case {v} n'existe pas")
        else:
            if v in self[u] and direction in self[u][v]:
                raise ValueError(f"Un mur existe déjà entre {u} et {v} dans la direction {direction}")
        self.add_edge(u, v, key=direction, mur=mur, **attr) #type: ignore

    def get_case(self, position:crt.Position) -> Case:
        """Renvoie la case à la position donnée"""
        return self.position_case[position]

    def get_mur(self, u:crt.Position, direction:crt.Direction, v:Optional[crt.Position]=None) -> Mur:
        """Renvoie le mur entre u et v dans la direction direction."""
        if v is None:
            v = self.get_cible(u, direction)
        elif v not in self[u]:
            raise ValueError(f"La position {v} n'est pas voisine de {u}")
        return self[u][v][direction]['mur'] #type: ignore

    def get_mur_oppose(self, u:crt.Position, direction:crt.Direction, v:Optional[crt.Position]=None) -> Optional[Mur]:
        if v is None:
            v = self.get_cible(u, direction)
        # On vérifie que le mur existe, que v n'est pas POSITION_ABSENTE, et qu'il n'y a qu'un seul mur entre v et u
        if direction in self[u][v] and len(self[v][u]) == 1: #type: ignore
            return self[v][u]["mur"] #type: ignore

    def get_cible(self, position:crt.Position, direction:crt.Direction) -> crt.Position:
        # Il devrait exister un mur sortant de position dans la direction direction
        # Il ne mêne pas nécessairement à position+direction
        for voisin in self[position]: #type: ignore
            if direction in self[position][voisin]: #type: ignore
                return voisin #type: ignore
        raise ValueError(f"La position {position} n'a pas de mur dans la direction {direction}")

    def extrait(self, positions:Set[crt.Position]) -> Extrait:
        voisins:Set[crt.Position] = {voisin for position in positions for voisin in self[position] if voisin not in positions} #type: ignore
        subgraph = super().subgraph(positions|voisins) # type: ignore
        return Extrait(voisins, subgraph) # type: ignore

    def agissant_veut_passer(self,intrus:Agissant,direction:crt.Direction):
        """Fonction qui tente de faire passer une entitée.
           Se réfère à la case compétente, qui gère tout."""
        position = intrus.get_position()
        if position is crt.POSITION_ABSENTE:
            raise ValueError("L'entitée n'a pas de position")
        cible = self.get_cible(position,direction)
        if self.get_mur(position,direction,cible).peut_passer(intrus):
            if self.get_case(cible).agissant_arrive(intrus):
                intrus.set_position(cible)
                self.get_case(position).agissant = None

    def item_veut_passer(self,intrus:Item,direction:crt.Direction):
        """Fonction qui tente de faire passer une entitée.
           Se réfère à la case compétente, qui gère tout."""
        position = intrus.get_position()
        if position is crt.POSITION_ABSENTE:
            raise ValueError("L'entitée n'a pas de position")
        cible = self.get_cible(position,direction)
        if self.get_mur(position,direction,cible).peut_passer(intrus):
            if self.get_case(cible).item_arrive(intrus):
                intrus.set_position(cible)
                self.get_case(position).items.remove(intrus)

    #Découvrons le déroulé d'un tour, avec Labyrinthe-ni :
    def debut_tour(self): #On commence le tour
        """Fonction qui s'exécute au début du tour."""
        for position in self.nodes:
            self.position_case[position].debut_tour()

    def pseudo_debut_tour(self): #On commence le tour
        """Un faux début de tour"""
        for position in self.nodes:
            self.position_case[position].pseudo_debut_tour()

    def post_action(self): #On agit sur les actions en suspens (les attaques en particulier)
        """Fonction qui s'exécute après les actions."""
        for position in self.nodes:
            self.position_case[position].post_action()

    def fin_tour(self):
        """Fonction qui s'exécute à la fin du tour."""
        for position in self.nodes:
            self.position_case[position].fin_tour()
    #Et c'est la fin du tour !

    def a_portee(self,position:crt.Position,portee:float,deplacement:Deplacement,forme:Forme,passage:Passage,direction:Optional[crt.Direction]=None,obscurite:bool=False) -> crt.Extrait:
        """Fonction qui renvoie les positions à portée de la position donnée"""
        # On crée un graphe temporaire
        if deplacement == Deplacement.SPATIAL:
            graphe = self.etages[position.etage].copy() # Les déplacements spatiaux ne peuvent se faire que sur le même étage
        elif deplacement == Deplacement.MAGIQUE:
            graphe = self.copy() # Les déplacements magiques peuvent se faire sur tous les étages
        else:
            raise ValueError(f"Le déplacement {deplacement} n'est pas reconnu")
        # On retire les murs qu'on ne peut pas passer
        for u in graphe.nodes: #type: ignore
            for dir_ in crt.Direction:
                if forme == Forme.DEMI_CERCLE:
                    if direction is None:
                        raise ValueError("La forme DEMI_CERCLE nécessite une direction")
                    if deplacement == Deplacement.MAGIQUE:
                        raise ValueError("La forme DEMI_CERCLE n'est pas compatible avec le déplacement MAGIQUE pour le moment")
                    if dir_ == direction.oppose:
                        graphe.remove_edge(u,self.get_cible(u,dir_)) # type: ignore
                        continue
                v = self.get_cible(u,dir_) # type: ignore
                if not self.get_mur(u,dir_,v).passage(passage): # type: ignore
                    graphe.remove_edge(u,v) # type: ignore
        if obscurite:
            # On met les poids sur les arêtes
            for u,v in graphe.edges: # type: ignore
                graphe[u][v]["poids"] = self.position_case[u].get_opacite() # type: ignore
            # Puisqu'ego_graph ne prend pas de float pour la portée, on va augmenter portee à l'entier supérieur et mettre la différence dans le poid des arrêtes de la position de départ
            for v in graphe[position]: # type: ignore
                graphe[position][v]["poids"] += portee - int(portee) # type: ignore
            portee = int(portee) + 1
        # On calcule les positions à portée
        return self.extrait(nx.ego_graph(graphe,position,int(portee), distance="poids" if obscurite else None).nodes) # type: ignore

NOWHERE = Labyrinthe()
"""Le labyrinthe vide."""