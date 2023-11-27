"""
Contient les classes des magies d'attaque au corp à corp.
"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import carte as crt

# Imports des classes parentes
from ..magie import MagieDirigee,MagiesOffensives

# Imports utilisés dans le code
from ....effet import AttaqueCase
from ....commons import Element

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ....entitee.agissant.agissant import Agissant
    from ....systeme.skill.actif import Actif
    from ....commons import Deplacement
    from ....commons import Forme
    from ....commons import Passage

class MagieAttaqueCorpACorp(MagiesOffensives):
    """Les magies qui créent une attaque au corp à corp."""
    def __init__(self,skill:Actif,agissant:Agissant,gain_xp:float,cout_pm:float,portee:float,degats:float,element:Element,deplacement:Deplacement,forme:Forme,passage:Passage,latence:float,niveau:int):
        MagiesOffensives.__init__(self,skill,agissant,gain_xp,cout_pm,latence,niveau)
        self.portee = portee
        self.degats = degats
        self.element = element
        self.deplacement = deplacement
        self.forme = forme
        self.passage = passage

    def action(self):
        for case in self.agissant.labyrinthe.a_portee(self.agissant.position,self.portee,self.deplacement,self.forme,self.passage):
            case = self.agissant.labyrinthe.get_case(case)
            case.effets.add(AttaqueCase(self.agissant,self.degats,self.element,"proximité"))

class MagieAttaqueCorpACorpDirigee(MagieDirigee,MagieAttaqueCorpACorp):
    """Les magies qui créent une attaque au corp à corp dirigée."""
    def __init__(self,skill:Actif,agissant:Agissant,direction:Optional[crt.Direction],gain_xp:float,cout_pm:float,portee:float,degats:float,element:Element,deplacement:Deplacement,forme:Forme,passage:Passage,latence:float,niveau:int):
        MagieDirigee.__init__(self,skill,agissant,gain_xp,cout_pm,latence,direction,niveau)
        MagieAttaqueCorpACorp.__init__(self,skill,agissant,gain_xp,cout_pm,portee,degats,element,deplacement,forme,passage,latence,niveau)

    def action(self):
        if self.direction is None:
            self.interrompt()
        else:
            for case in self.agissant.labyrinthe.a_portee(self.agissant.position,self.portee,self.deplacement,self.forme,self.passage,self.direction):
                case = self.agissant.labyrinthe.get_case(case)
                case.effets.add(AttaqueCase(self.agissant,self.degats,self.element,"proximité",self.direction))

class MagiePurification(MagieAttaqueCorpACorp):
    """La magie qui crée un effet de purification sur un agissant."""
    def action(self):
        for case in self.agissant.labyrinthe.a_portee(self.agissant.position,self.portee,self.deplacement,self.forme,self.passage):
            case = self.agissant.labyrinthe.get_case(case)
            case.effets.add(AttaqueCase(self.agissant,self.degats,Element.OMBRE,"proximité",inverse=True))
