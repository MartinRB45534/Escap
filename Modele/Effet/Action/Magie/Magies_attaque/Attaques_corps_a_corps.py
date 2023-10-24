from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import carte as crt

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from .....entitee.agissant.agissant import Agissant
    from .....systeme.skill.actif import Actif
    from .....systeme.elements import Element

# Imports des classes parentes
from ...magie.magie import Magie,Magie_dirigee,Magies_offensives

class Magie_attaque_corp_a_corp(Magies_offensives):
    """Les magies qui créent une attaque au corp à corp."""
    def __init__(self,skill:Actif,agissant:Agissant,gain_xp:float,cout_pm:float,portee:float,degats:float,element:Element,deplacement:Deplacement,forme:Forme,passage:Passage,latence:float,niveau:int):
        Magie.__init__(self,skill,agissant,gain_xp,cout_pm,latence,niveau)
        self.portee = portee
        self.degats = degats
        self.element = element
        self.deplacement = deplacement
        self.forme = forme
        self.passage = passage

    def action(self):
        for case in self.agissant.labyrinthe.a_portee(self.agissant.position,self.portee,self.deplacement,self.forme,self.passage):
            self.agissant.labyrinthe.get_case(case).effets.add(AttaqueCase(self.agissant,self.degats,self.element,"proximité"))

class Magie_attaque_corp_a_corp_dirigee(Magie_dirigee,Magie_attaque_corp_a_corp):
    def __init__(self,skill:Actif,agissant:Agissant,direction:Optional[crt.Direction],gain_xp:float,cout_pm:float,portee:float,degats:float,element:Element,deplacement:Deplacement,forme:Forme,passage:Passage,propagation:str,latence:float,niveau:int):
        Magie_attaque_corp_a_corp.__init__(self,skill,agissant,gain_xp,cout_pm,portee,degats,element,deplacement,forme,passage,latence,niveau)
        self.direction = direction

    def action(self):
        if self.direction is None:
            self.interrompt()
        else:
            for case in self.agissant.labyrinthe.a_portee(self.agissant.position,self.portee,self.deplacement,self.forme,self.passage,self.direction):
                self.agissant.labyrinthe.get_case(case).effets.add(AttaqueCase(self.agissant,self.degats,self.element,"proximité",self.direction))

class Magie_purification(Magie_attaque_corp_a_corp):
    """La magie qui crée un effet de purification sur un agissant."""
    nom = "magie purification"
    def action(self):
        for case in self.agissant.labyrinthe.a_portee(self.agissant.position,self.portee,self.deplacement,self.forme,self.passage):
            self.agissant.labyrinthe.get_case(case).effets.add(Attaque_lumineuse_case(self.agissant,self.degats))

# Imports utilisés dans le code
from ....attaque.attaque import AttaqueCase,Attaque_lumineuse_case
from .....labyrinthe.deplacement import Deplacement
from .....labyrinthe.forme import Forme
from .....labyrinthe.passage import Passage