from __future__ import annotations
from typing import TYPE_CHECKING, Set, Optional, Dict
import Carte as crt
import networkx as nx

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ...Labyrinthe.Extrait import Extrait
    from ...Entitee.Agissant.Agissant import Agissant
    from ...Entitee.Agissant.Vue.Vue import Vue
    from ...Entitee.Agissant.Vue.Case import Case_vue, Case_pas_vue
    from ...Entitee.Agissant.Vue.Agissant import Agissant_vu
    from .Agissant import Vision_agissant
    from .Case import Vision_case
    from .Mur import Vision_mur

class Vision(Extrait):
    def __init__(self, vues:Set[Vue], tour:int):
        nx.MultiDiGraph.__init__(self)
        self.position_case:dict[crt.Position, Vision_case] = {}
        self.exterieur:Set[crt.Position] = set()
        self.corps:Set[Agissant] = set() # Nos corps nous donnent accès à toutes leurs infos
        self.neutres:Dict[int,Vision_agissant] = {} # On ne sait des neutres que ce que l'on voit
        self.ennemis:Dict[int,Vision_agissant] = {} # On ne sait des ennemis que ce que l'on voit
        self.voit(vues, tour)

    def voit(self, vues:Set[Vue], tour:int):
        for vue in vues:
            for position in vue:
                self.voit_case(vue.get_case(position), tour)

        for vue in vues:
            for position in vue.exterieur:
                if position not in self:
                    self.exterieur.add(position)
                    self.add_node(position, case=Case_pas_vue(position))

        for vue in vues:
            for u,v, direction in vue.edges:
                if (u,v,direction) not in self.edges:
                    self.add_edge(u,v,direction, mur=vue.get_mur(u, direction, v))
                else:
                    self.get_mur(u, direction, v).voit(vue.get_mur(u, direction, v), tour)

    def voit_case(self, case:Case_vue, tour:int):
        if case.position in self:
            self.get_case(case.position).voit(case, tour)
        else:
            self.position_case[case.position] = Vision_case(case, tour)
            self.add_node(case.position, case=self.get_case(case.position))
        if case.agissant is not None:
            self.voit_agissant(case.agissant, tour)
        
    def voit_agissant(self, agissant:Agissant_vu, tour:int):
        if agissant.ID not in {agissant.ID for agissant in self.corps}: # Les corps nous donnent leurs infos en direct
            if agissant.ID in self.ennemis:
                self.ennemis[agissant.ID].voit(agissant, tour)
            elif agissant.ID in self.neutres:
                self.neutres[agissant.ID].voit(agissant, tour)
            else:
                self.neutres[agissant.ID] = Vision_agissant(agissant, tour, self)

    def get_case(self, position:crt.Position) -> Vision_case:
        return self.position_case[position]
    
    def get_mur(self, u:crt.Position, direction:crt.Direction, v:Optional[crt.Position]=None) -> Vision_mur:
        assert u in self
        if v is None:
            v = self.get_cible(u, direction)
        return self[u][v][direction]['mur']
    
    def get_mur_oppose(self, u:crt.Position, direction:crt.Direction, v:Optional[crt.Position]=None) -> Optional[Vision_mur]:
        assert u in self
        if v is None:
            v = self.get_cible(u, direction)
        # On vérifie que le mur existe, que v n'est pas POSITION_ABSENTE, et qu'il n'y a qu'un seul mur entre v et u
        if direction in self[u][v] and len(self[v][u]) == 1:
            return self[v][u]["mur"]


# Imports utilisés dans le code
from .Agissant import Vision_agissant
from .Case import Vision_case
from ...Entitee.Agissant.Vue.Case import Case_pas_vue