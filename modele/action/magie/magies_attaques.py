"""
Contient les classes des magies d'attaque au corp à corp.
"""

from __future__ import annotations
from typing import TYPE_CHECKING
import carte as crt

# Imports des classes parentes
from .magie import Magie, MagieDirigee, CibleCase

# Imports utilisés dans le code
from ...effet import AttaqueCase, AttaqueCaseDelayee
from ...commons import Element

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ...commons import Deplacement
    from ...commons import Forme
    from ...commons import Passage

class MagieAttaque(Magie):
    """Les magies qui créent une attaque."""
    portee: float
    degats: float
    element: Element
    deplacement: Deplacement
    forme: Forme
    passage: Passage
    direction: crt.Direction|None
    taux_perce: float
    inverse: bool

    def action(self):
        for case in self.agissant.labyrinthe.a_portee(self.agissant.position,self.portee,self.deplacement,self.forme,self.passage):
            case = self.agissant.labyrinthe.get_case(case)
            case.effets.add(AttaqueCase(self.agissant,self.degats,self.element,self.direction,self.taux_perce,self.inverse))

class MagieAttaqueDistance(CibleCase,MagieAttaque):
    """Les magies qui créent une attaque à distance."""
    effets:list[AttaqueCaseDelayee] = []

    def action(self):
        if self.cible == crt.POSITION_ABSENTE:
            self.interrompt()
        elif not self.effets:
            self.effets = [] # On ne veut pas que les effets soient partagés entre les instances
            for position in self.agissant.labyrinthe.a_portee(self.cible,self.portee,self.deplacement,self.forme,self.passage):
                case = self.agissant.labyrinthe.get_case(position)
                effet = AttaqueCaseDelayee(self.agissant,self.degats,self.element,self.direction,self.taux_perce,self.inverse)
                case.effets.add(effet)
                self.effets.append(effet)
        else:
            for effet in self.effets:
                effet.attente = False

class MagieAttaqueDirigee(MagieDirigee,MagieAttaque):
    """Les magies qui créent une attaque au corp à corp dirigée."""
    def action(self):
        if self.direction is None:
            self.interrompt()
        else:
            for case in self.agissant.labyrinthe.a_portee(self.agissant.position,self.portee,self.deplacement,self.forme,self.passage,self.direction):
                case = self.agissant.labyrinthe.get_case(case)
                case.effets.add(AttaqueCase(self.agissant,self.degats,self.element,self.direction,self.taux_perce,self.inverse))

class MagieAttaqueDistanceDirigee(MagieAttaqueDirigee,MagieAttaqueDistance):
    """Les magies qui créent une attaque à distance dirigée."""
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
