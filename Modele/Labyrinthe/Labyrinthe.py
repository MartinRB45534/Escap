from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Set
import networkx as nx
import carte as crt

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from .case import Case
    from .mur import Mur, MurImpassable
    from ..entitee.entitee import Mobile
    from .deplacement import Deplacement
    from .forme import Forme
    from .passage import Passage
    from .extrait import Extrait

class Labyrinthe(crt.Labyrinthe):
    """Le labyrinthe"""
    def __init__(self):
        super().__init__()
        self.position_case: dict[crt.Position,Case] = {}
        self.add_case(CASE_ABSENTE)

    def __contains__(self, item):
        if isinstance(item,crt.Position):
            return item in self.nodes and item is not crt.POSITION_ABSENTE
        return super().__contains__(item)

    def add_case(self, case:Case, **attr):
        self.add_node(case.position, case=case, **attr)
        self.position_case[case.position] = case
        for direction in crt.Direction:
            self.add_mur(case.position, case.position+direction, direction, MurImpassable(1))
        if case.position.etage not in self.etages: # Représente les étages physiques (pour tout ce qui ignore les murs et les téléporteurs)
            self.etages[case.position.etage] = nx.Graph()
        self.etages[case.position.etage].add_node(case.position)
        for direction in crt.Direction:
            if case.position+direction in case.position.etage:
                self.etages[case.position.etage].add_edge(case.position, case.position+direction, key=direction)

    def add_mur(self, u:crt.Position, v:crt.Position, direction:crt.Direction, mur:Mur, **attr):
        if v not in self.position_case:
            self.add_case(Case(v))
        else:
            if v in self[u] and direction in self[u][v]:
                raise ValueError(f"Un mur existe déjà entre {u} et {v} dans la direction {direction}")
        self.add_edge(u, v, key=direction, mur=mur, **attr)

    def get_case(self, position:crt.Position) -> Case:
        return self.position_case[position]

    def get_mur(self, u:crt.Position, direction:crt.Direction, v:Optional[crt.Position]=None) -> Mur:
        if v is None:
            v = self.get_cible(u, direction)
        return self[u][v][direction]['mur']

    def get_mur_oppose(self, u:crt.Position, direction:crt.Direction, v:Optional[crt.Position]=None) -> Optional[Mur]:
        if v is None:
            v = self.get_cible(u, direction)
        # On vérifie que le mur existe, que v n'est pas POSITION_ABSENTE, et qu'il n'y a qu'un seul mur entre v et u
        if direction in self[u][v] and len(self[v][u]) == 1:
            return self[v][u]["mur"]

    def get_cible(self, position:crt.Position, direction:crt.Direction) -> crt.Position:
        # Il devrait exister un mur sortant de position dans la direction direction
        # Il ne mêne pas nécessairement à position+direction
        for voisin in self[position]:
            if direction in self[position][voisin]:
                return voisin
        raise ValueError(f"La position {position} n'a pas de mur dans la direction {direction}")

    def extrait(self, positions:Set[crt.Position]) -> Extrait:
        voisins:Set[crt.Position] = {voisin for position in positions for voisin in self[position] if voisin not in positions}
        subgraph = super().subgraph(positions|voisins)
        return Extrait(voisins, subgraph)

    def veut_passer(self,intrus:Mobile,direction:crt.Direction):
        """Fonction qui tente de faire passer une entitée.
           Se réfère à la case compétente, qui gère tout."""
        position = intrus.get_position()
        if position is crt.POSITION_ABSENTE:
            raise Exception("L'entitée n'a pas de position")
        cible = self.get_cible(position,direction)
        if self.get_mur(position,direction,cible).peut_passer(intrus):
            if self.get_case(cible).arrive(intrus):
                intrus.set_position(cible)
                self.get_case(position).part(intrus)

    #Découvrons le déroulé d'un tour, avec Labyrinthe-ni :
    def debut_tour(self): #On commence le tour
        for position in self.nodes:
            self.position_case[position].debut_tour()

    def pseudo_debut_tour(self): #On commence le tour
        for position in self.nodes:
            self.position_case[position].pseudo_debut_tour()

    def post_action(self): #On agit sur les actions en suspens (les attaques en particulier)
        for position in self.nodes:
            self.position_case[position].post_action()

    def fin_tour(self):
        for position in self.nodes:
            self.position_case[position].fin_tour()
    #Et c'est la fin du tour !

    def a_portee(self,position:crt.Position,portee:float,deplacement:Deplacement,forme:Forme,passage:Passage,direction:Optional[crt.Direction]=None,obscurite:bool=False) -> crt.Extrait:
        """Fonction qui renvoie les positions à portée de la position donnée"""
        # On crée un graphe temporaire
        if deplacement == Deplacement.SPATIAL:
            graphe = self.etages[position.etage] # Les déplacements spatiaux ne peuvent se faire que sur le même étage
        elif deplacement == Deplacement.MAGIQUE:
            graphe = self.copy() # Les déplacements magiques peuvent se faire sur tous les étages
        else:
            raise ValueError(f"Le déplacement {deplacement} n'est pas reconnu")
        # On retire les murs qu'on ne peut pas passer
        for u in graphe.nodes:
            for dir in crt.Direction:
                if forme == Forme.DEMI_CERCLE:
                    if direction is None:
                        raise ValueError("La forme DEMI_CERCLE nécessite une direction")
                    if deplacement == Deplacement.MAGIQUE:
                        raise ValueError("La forme DEMI_CERCLE n'est pas compatible avec le déplacement MAGIQUE pour le moment")
                    if dir == direction.oppose:
                        graphe.remove_edge(u,self.get_cible(u,dir))
                        continue
                v = self.get_cible(u,dir)
                if not self.get_mur(u,dir,v).passage(passage):
                    graphe.remove_edge(u,v)
        if obscurite:
            # On met les poids sur les arêtes
            for u,v in graphe.edges:
                graphe[u][v]["poids"] = self.position_case[u].get_opacite()
            # Puisqu'ego_graph ne prend pas de float pour la portée, on va augmenter portee à l'entier supérieur et mettre la différence dans le poid des arrêtes de la position de départ
            for v in graphe[position]:
                graphe[position][v]["poids"] += portee - int(portee)
            portee = int(portee) + 1
        # On calcule les positions à portée
        return self.extrait(nx.ego_graph(graphe,position,int(portee), distance="poids" if obscurite else None).nodes)

# Imports utilisés dans le code
from .absent import CASE_ABSENTE
from .extrait import Extrait
