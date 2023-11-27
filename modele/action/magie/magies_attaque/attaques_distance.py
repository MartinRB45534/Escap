"""
Contient les classes des magies qui créent une attaque à distance.
"""

from __future__ import annotations
from typing import TYPE_CHECKING, List
import carte as crt

# Imports des classes parentes
from ..magie import CibleCase, MagiesOffensives

# Imports utilisés dans le code
from ....effet import AttaqueCaseDelayee
from ....commons import Deplacement, Forme, Passage

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ....entitee.agissant.agissant import Agissant
    from ....systeme.skill.actif import Actif
    from ....commons.elements import Element

class MagieAttaqueDistance(CibleCase,MagiesOffensives):
    """Les magies qui créent une attaque à distance."""
    def __init__(self,skill:Actif,agissant:Agissant,gain_xp:float,cout_pm:float,portee:float,degats:float,element:Element,latence:float,niveau:int,cible:crt.Position=crt.POSITION_ABSENTE):
        CibleCase.__init__(self,skill,agissant,gain_xp,cout_pm,latence,niveau,cible)
        MagiesOffensives.__init__(self,skill,agissant,gain_xp,cout_pm,latence,niveau)
        self.cible = cible
        self.effets:List[AttaqueCaseDelayee] = []
        self.portee = portee
        self.degats = degats
        self.element = element

    def action(self):
        if self.cible == crt.POSITION_ABSENTE:
            self.interrompt()
        elif not self.effets:
            for position in self.agissant.labyrinthe.a_portee(self.cible,self.portee,Deplacement.MAGIQUE,Forme.CERCLE,Passage(True,True,True,False,True)):
                case = self.agissant.labyrinthe.get_case(position)
                effet = AttaqueCaseDelayee(self.agissant,self.degats,self.element,"distance")
                case.effets.add(effet)
                self.effets.append(effet)
        else:
            for effet in self.effets:
                effet.attente = False
