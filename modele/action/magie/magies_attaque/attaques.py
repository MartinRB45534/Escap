"""
Contient les classes des magies d'attaque au corp à corp.
"""

from __future__ import annotations
from typing import TYPE_CHECKING
import carte as crt

# Imports des classes parentes
from ..magie import ActionMagieDirigee, ActionMagiesOffensives, CibleCase

# Imports utilisés dans le code
from ....effet import AttaqueCase, AttaqueCaseDelayee
from ....commons import Element

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ....entitee.agissant.agissant import Agissant
    from ....systeme import Actif, Magie
    from ....commons import Deplacement
    from ....commons import Forme
    from ....commons import Passage

class ActionMagieAttaque(ActionMagiesOffensives):
    """Les magies qui créent une attaque."""
    def __init__(self,skill:Actif,magie:Magie,agissant:Agissant,gain_xp:float,cout_pm:float,portee:float,degats:float,element:Element,deplacement:Deplacement,forme:Forme,passage:Passage,latence:float,taux_perce:float,inverse:bool):
        ActionMagiesOffensives.__init__(self,skill,magie,agissant,gain_xp,cout_pm,latence)
        self.portee = portee
        self.degats = degats
        self.element = element
        self.deplacement = deplacement
        self.forme = forme
        self.passage = passage
        self.direction = None
        self.taux_perce = taux_perce
        self.inverse = inverse

    def action(self):
        for case in self.agissant.labyrinthe.a_portee(self.agissant.position,self.portee,self.deplacement,self.forme,self.passage):
            case = self.agissant.labyrinthe.get_case(case)
            case.effets.add(AttaqueCase(self.agissant,self.degats,self.element,self.direction,self.taux_perce,self.inverse))

class ActionMagieAttaqueDistance(CibleCase,ActionMagieAttaque):
    """Les magies qui créent une attaque à distance."""
    def __init__(self,skill:Actif,magie:Magie,agissant:Agissant,gain_xp:float,cout_pm:float,portee:float,degats:float,element:Element,deplacement:Deplacement,forme:Forme,passage:Passage,latence:float,taux_perce:float,inverse:bool):
        CibleCase.__init__(self,skill,magie,agissant,gain_xp,cout_pm,latence)
        ActionMagieAttaque.__init__(self,skill,magie,agissant,gain_xp,cout_pm,portee,degats,element,deplacement,forme,passage,latence,taux_perce,inverse)
        self.effets:list[AttaqueCaseDelayee] = []

    def action(self):
        if self.cible == crt.POSITION_ABSENTE:
            self.interrompt()
        elif not self.effets:
            for position in self.agissant.labyrinthe.a_portee(self.cible,self.portee,self.deplacement,self.forme,self.passage):
                case = self.agissant.labyrinthe.get_case(position)
                effet = AttaqueCaseDelayee(self.agissant,self.degats,self.element,self.direction,self.taux_perce,self.inverse)
                case.effets.add(effet)
                self.effets.append(effet)
        else:
            for effet in self.effets:
                effet.attente = False

class ActionMagieAttaqueDirigee(ActionMagieDirigee,ActionMagieAttaque):
    """Les magies qui créent une attaque au corp à corp dirigée."""
    def __init__(self,skill:Actif,magie:Magie,agissant:Agissant,gain_xp:float,cout_pm:float,portee:float,degats:float,element:Element,deplacement:Deplacement,forme:Forme,passage:Passage,latence:float,taux_perce:float,inverse:bool):
        ActionMagieDirigee.__init__(self,skill,magie,agissant,gain_xp,cout_pm,latence)
        ActionMagieAttaque.__init__(self,skill,magie,agissant,gain_xp,cout_pm,portee,degats,element,deplacement,forme,passage,latence,taux_perce,inverse)

    def action(self):
        if self.direction is None:
            self.interrompt()
        else:
            for case in self.agissant.labyrinthe.a_portee(self.agissant.position,self.portee,self.deplacement,self.forme,self.passage,self.direction):
                case = self.agissant.labyrinthe.get_case(case)
                case.effets.add(AttaqueCase(self.agissant,self.degats,self.element,self.direction,self.taux_perce,self.inverse))

class ActionMagieAttaqueDistanceDirigee(ActionMagieAttaqueDirigee,ActionMagieAttaqueDistance):
    """Les magies qui créent une attaque à distance dirigée."""
    def __init__(self,skill:Actif,magie:Magie,agissant:Agissant,gain_xp:float,cout_pm:float,portee:float,degats:float,element:Element,deplacement:Deplacement,forme:Forme,passage:Passage,latence:float,taux_perce:float,inverse:bool):
        ActionMagieAttaqueDirigee.__init__(self,skill,magie,agissant,gain_xp,cout_pm,portee,degats,element,deplacement,forme,passage,latence,taux_perce,inverse)
        ActionMagieAttaqueDistance.__init__(self,skill,magie,agissant,gain_xp,cout_pm,portee,degats,element,deplacement,forme,passage,latence,taux_perce,inverse)

    def action(self):
        if self.direction is None:
            self.interrompt()
        elif self.cible == crt.POSITION_ABSENTE:
            self.interrompt()
        elif not self.effets:
            for position in self.agissant.labyrinthe.a_portee(self.cible,self.portee,self.deplacement,self.forme,self.passage,self.direction):
                case = self.agissant.labyrinthe.get_case(position)
                effet = AttaqueCaseDelayee(self.agissant,self.degats,self.element,self.direction,self.taux_perce,self.inverse)
                case.effets.add(effet)
                self.effets.append(effet)
        else:
            for effet in self.effets:
                effet.attente = False