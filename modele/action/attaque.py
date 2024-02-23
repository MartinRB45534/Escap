"""
Les skills d'attaque physique.
"""

from __future__ import annotations
from typing import TYPE_CHECKING
import carte as crt

# Imports des classes parentes
from ..action.action_skill import ActionSkill
from ..action.action import ActionFinal, ActionParcellaire

# Imports utilisés dans le code
from ..effet import AttaqueCase
from ..commons import Deplacement, Forme, Passage

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ..effet.agissant.agissants import Dopage
    from ..entitee.agissant.agissant import Agissant
    from ..entitee.item.equippement.degainable.degainable import Arme
    from ..systeme.skill.actif import Actif
    from ..commons.elements import Element

class Attaque(ActionSkill):
    """
    L'action d'attaquer.
    """
    def dope(self,dopage:Dopage):
        """Dope l'attaque."""

class AttaqueSimple(Attaque):
    """
    Une attaque qui n'inflige qu'un seul coup.
    """
    taux:float
    direction:crt.Direction
    portee:float
    element:Element
    deplacement:Deplacement
    forme:Forme
    passage:Passage
    def __init__(self, agissant: Agissant, skill: Actif):
        Attaque.__init__(self, agissant, skill)

    def dope(self,dopage:Dopage):
        self.taux = dopage.dope(self.taux)

    def action(self):
        degats = self.agissant.force*self.taux*self.agissant.affinite(self.element)
        position = self.agissant.position
        zone = self.agissant.labyrinthe.a_portee(
            position,self.portee,self.deplacement,self.forme,self.passage,self.direction)
        for position in zone:
            self.agissant.labyrinthe.get_case(position).effets.add(
                AttaqueCase(self.agissant,degats,self.element,self.direction))

class AttaqueFinal(ActionFinal,AttaqueSimple):
    """
    Une attaque qui se fait à la fin de la latence.
    """
    def __init__(self, agissant: Agissant, skill: Actif, latence: float, xp: float, taux: float,
                 direction: crt.Direction, portee: float, element: Element,
                 deplacement: Deplacement, forme: Forme, passage: Passage):
        ActionFinal.__init__(self, agissant)
        AttaqueSimple.__init__(self, agissant, skill)
        self.latence_max = latence
        self.xp = xp
        self.taux = taux
        self.direction = direction
        self.portee = portee
        self.element = element
        self.deplacement = deplacement
        self.forme = forme
        self.passage = passage

class AttaqueMultiple(ActionParcellaire,Attaque):
    """
    Une attaque complexe avec plusieurs coups.
    """
    def __init__(self, agissant: Agissant, skill: Actif, latences: list[float], xp: float,
                 taux: list[float], directions: list[crt.Direction], portees: list[float],
                 element: Element, deplacement: Deplacement, formes: list[Forme],
                 passages: list[Passage]):
        ActionParcellaire.__init__(self, agissant)
        Attaque.__init__(self, agissant, skill)
        self.latence_max = sum(latences)
        self.latences = latences
        self.xp = xp
        self.taux = taux
        self.directions = directions
        self.portees = portees
        self.element = element
        self.deplacement = deplacement
        self.formes = formes
        self.passages = passages

    def dope(self,dopage:Dopage):
        self.taux = [dopage.dope(taux) for taux in self.taux]

    def action(self):
        degats = self.agissant.force*self.taux[self.rempli]*self.agissant.affinite(self.element)
        position = self.agissant.position
        zone = self.agissant.labyrinthe.a_portee(
            position,self.portees[self.rempli],self.deplacement,
            self.formes[self.rempli],self.passages[self.rempli],
            self.directions[self.rempli])
        for position in zone:
            self.agissant.labyrinthe.get_case(position).effets.add(
                AttaqueCase(self.agissant,degats,self.element,self.directions[self.rempli]))

class AttaqueArme(Attaque):
    """
    L'action d'attaquer avec une arme.
    """
    arme:Arme
    def __init__(self,agissant:Agissant,skill:Actif):
        Attaque.__init__(self,agissant,skill)

class AttaqueArmeSimple(AttaqueArme,AttaqueSimple):
    """
    Une attaque avec une arme qui n'inflige qu'un seul coup.
    """
    def __init__(self,agissant:Agissant,skill:Actif):
        AttaqueSimple.__init__(self,agissant,skill)
        AttaqueArme.__init__(self,agissant,skill)

    def action(self):
        element,tranchant,portee = self.arme.get_stats_attaque()
        degats = self.agissant.force*self.taux*self.agissant.affinite(element)*tranchant
        position = self.agissant.position
        zone = self.agissant.labyrinthe.a_portee(position,portee,self.deplacement,self.forme,self.passage,self.direction)
        for position in zone:
            self.agissant.labyrinthe.get_case(position).effets.add(AttaqueCase(self.agissant,degats,element,self.direction))

class AttaqueArmeFinal(ActionFinal,AttaqueArmeSimple):
    """
    Une attaque avec une arme qui se fait à la fin de la latence.
    """
    def __init__(self,agissant:Agissant,latence:float,skill:Actif,xp:float,taux:float,direction:crt.Direction,arme:Arme,deplacement:Deplacement,forme:Forme,passage:Passage):
        ActionFinal.__init__(self,agissant)
        AttaqueArmeSimple.__init__(self,agissant,skill)
        self.latence_max = latence
        self.xp = xp
        self.taux = taux
        self.direction = direction
        self.arme = arme
        self.deplacement = deplacement
        self.forme = forme
        self.passage = passage

class AttaqueArmeMultiple(ActionParcellaire,AttaqueArme):
    """
    Une attaque complexe avec plusieurs coups.
    """
    def __init__(self,agissant:Agissant,latences:list[float],skill:Actif,xp:float,taux:list[float],directions:list[crt.Direction],arme:Arme,deplacement:Deplacement,formes:list[Forme],passage:Passage):
        ActionParcellaire.__init__(self,agissant)
        AttaqueArme.__init__(self,agissant,skill)
        self.latence_max = sum(latences)
        self.latences = latences
        self.xp = xp
        self.arme = arme
        self.taux = taux
        self.directions = directions
        self.portee = arme.portee
        self.element = arme.element
        self.deplacement = deplacement
        self.formes = formes
        self.passage = passage

    def dope(self,dopage:Dopage):
        self.taux = [dopage.dope(taux) for taux in self.taux]

    def action(self):
        element,tranchant,portee = self.arme.get_stats_attaque()
        degats = self.agissant.force*self.taux[self.rempli]*self.agissant.affinite(element)*tranchant
        position = self.agissant.position
        zone = self.agissant.labyrinthe.a_portee(position,portee,self.deplacement,self.formes[self.rempli],self.passage,self.directions[self.rempli])
        for position in zone:
            self.agissant.labyrinthe.get_case(position).effets.add(AttaqueCase(self.agissant,degats,element,self.directions[self.rempli]))

attaques: dict[tuple[bool, bool], type[Attaque]] = {
    (False, False): AttaqueFinal,
    (False, True): AttaqueMultiple,
    (True, False): AttaqueArmeFinal,
    (True, True): AttaqueArmeMultiple
}
"""
(arme, multiple) -> attaque
"""
