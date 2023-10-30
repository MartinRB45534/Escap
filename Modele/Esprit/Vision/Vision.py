from __future__ import annotations
from typing import TYPE_CHECKING, Set, Optional, Dict, Self
import carte as crt
import networkx as nx

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ...entitee.agissant.agissant import Agissant
    from ...entitee.agissant.vue.vue import Vue
    from ...entitee.agissant.vue.case import CaseVue, CasePasVue
    from ...entitee.agissant.vue.agissant import AgissantVu
    from .agissant import VisionAgissant
    from .case import VisionCase
    from .mur import VisionMur

# Import des classes parentes
from ...labyrinthe.extrait import Extrait

class Vision(Extrait):
    def __init__(self, vues:Set[Vue], tour:int):
        nx.MultiDiGraph.__init__(self)
        self.position_case:dict[crt.Position, VisionCase] = {}
        self.exterieur:Set[crt.Position] = set()
        self.corps:Set[Agissant] = set() # Nos corps nous donnent accès à toutes leurs infos
        self.neutres:Dict[int,VisionAgissant] = {} # On ne sait des neutres que ce que l'on voit
        self.ennemis:Dict[int,VisionAgissant] = {} # On ne sait des ennemis que ce que l'on voit
        self.voit(vues, tour)

    def voit(self, vues:Set[Vue], tour:int):
        for vue in vues:
            for position in vue:
                self.voit_case(vue.get_case(position), tour)

        for vue in vues:
            for position in vue.exterieur:
                if position not in self:
                    self.exterieur.add(position)
                    self.add_node(position, case=CasePasVue(position))

        for vue in vues:
            for u,v, direction in vue.edges:
                if (u,v,direction) not in self.edges:
                    self.add_edge(u,v,direction, mur=vue.get_mur(u, direction, v))
                else:
                    self.get_mur(u, direction, v).voit(vue.get_mur(u, direction, v), tour)

    def voit_case(self, case:CaseVue, tour:int):
        if case.position in self:
            self.get_case(case.position).voit(case, tour)
        else:
            self.position_case[case.position] = VisionCase(case, tour)
            self.add_node(case.position, case=self.get_case(case.position))
        if case.agissant is not None:
            self.voit_agissant(case.agissant, tour)
        
    def voit_agissant(self, agissant:AgissantVu, tour:int):
        if agissant.id not in {agissant.id for agissant in self.corps}: # Les corps nous donnent leurs infos en direct
            if agissant.id in self.ennemis:
                self.ennemis[agissant.id].voit(agissant, tour)
            elif agissant.id in self.neutres:
                self.neutres[agissant.id].voit(agissant, tour)
            else:
                self.neutres[agissant.id] = VisionAgissant(agissant, tour, self)

    def get_case(self, position:crt.Position) -> VisionCase:
        return self.position_case[position]
    
    def get_mur(self, u:crt.Position, direction:crt.Direction, v:Optional[crt.Position]=None) -> VisionMur:
        assert u in self
        if v is None:
            v = self.get_cible(u, direction)
        return self[u][v][direction]['mur']
    
    def get_mur_oppose(self, u:crt.Position, direction:crt.Direction, v:Optional[crt.Position]=None) -> Optional[VisionMur]:
        assert u in self
        if v is None:
            v = self.get_cible(u, direction)
        # On vérifie que le mur existe, que v n'est pas POSITION_ABSENTE, et qu'il n'y a qu'un seul mur entre v et u
        if direction in self[u][v] and len(self[v][u]) == 1:
            return self[v][u]["mur"]

    def merge(self, vision:Self):
        pass # TODO

# Imports utilisés dans le code
from .agissant import VisionAgissant
from .case import VisionCase
from ...entitee.agissant.vue.case import CasePasVue
