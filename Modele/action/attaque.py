"""
Les skills d'attaque physique.
"""

from __future__ import annotations
from typing import TYPE_CHECKING, List
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
    def __init__(self,agissant:Agissant,latence:float,skill:Actif,xp:float,taux:float,direction:crt.Direction,portee:int,element:Element,deplacement:Deplacement,forme:Forme,passage:Passage,distance:str="contact"):
        super().__init__(agissant,latence,skill,xp)
        self.taux = taux
        self.direction = direction
        self.portee = portee
        self.element = element
        self.deplacement = deplacement
        self.forme = forme
        self.passage = passage
        self.distance = distance

    def dope(self,dopage:Dopage):
        self.taux = dopage.dope(self.taux)

    def action(self):
        degats = self.agissant.force*self.taux*self.agissant.affinite(self.element)
        position = self.agissant.position
        zone = self.agissant.labyrinthe.a_portee(position,self.portee,self.deplacement,self.forme,self.passage,self.direction)
        for position in zone:
            self.agissant.labyrinthe.get_case(position).effets.add(AttaqueCase(self.agissant,degats,self.element,self.distance,self.direction))

class AttaqueFinal(ActionFinal,AttaqueSimple):
    """
    Une attaque qui se fait à la fin de la latence.
    """
    # L'attaque la plus courante, correspond aussi au stomp

class AttaqueArme(Attaque):
    """
    L'action d'attaquer avec une arme.
    """
    def __init__(self,agissant:Agissant,latence:float,skill:Actif,xp:float,arme:Arme):
        Attaque.__init__(self,agissant,latence,skill,xp)
        self.arme = arme

class AttaqueArmeSimple(AttaqueArme,AttaqueSimple):
    """
    Une attaque avec une arme qui n'inflige qu'un seul coup.
    """
    def __init__(self,agissant:Agissant,latence:float,skill:Actif,xp:float,taux:float,direction:crt.Direction,arme:Arme,deplacement:Deplacement,forme:Forme,passage:Passage,distance:str="contact"):
        AttaqueSimple.__init__(self,agissant,latence,skill,xp,taux,direction,arme.portee,arme.element,deplacement,forme,passage,distance)
        AttaqueArme.__init__(self,agissant,latence,skill,xp,arme)

    def action(self):
        element,tranchant,portee = self.arme.get_stats_attaque()
        degats = self.agissant.force*self.taux*self.agissant.affinite(element)*tranchant
        position = self.agissant.position
        zone = self.agissant.labyrinthe.a_portee(position,portee,self.deplacement,self.forme,self.passage,self.direction)
        for position in zone:
            self.agissant.labyrinthe.get_case(position).effets.add(AttaqueCase(self.agissant,degats,element,self.distance,self.direction))

class AttaqueArmeFinal(ActionFinal,AttaqueArmeSimple):
    """
    Une attaque avec une arme qui se fait à la fin de la latence.
    """
    # L'attaque avec une arme la plus courante (correspond aux attaques de base à l'épée et la lance)

class AttaqueMultiple(ActionParcellaire,AttaqueArme): # Les attaques sans arme ne peuvent pas être multiples
    """
    Une attaque complexe avec plusieurs coups.
    """
    def __init__(self,agissant:Agissant,latences:List[float],skill:Actif,xp:float,taux:List[float],directions:List[crt.Direction],arme:Arme,deplacement:Deplacement,formes:List[Forme],passage:Passage,distance:str="contact"):
        ActionParcellaire.__init__(self,agissant,latences)
        AttaqueArme.__init__(self,agissant,sum(latences),skill,xp,arme)
        self.taux = taux
        self.directions = directions
        self.portee = arme.portee
        self.element = arme.element
        self.deplacement = deplacement
        self.formes = formes
        self.passage = passage
        self.distance = distance

    def dope(self,dopage:Dopage):
        self.taux = [dopage.dope(taux) for taux in self.taux]

    def action(self):
        element,tranchant,portee = self.arme.get_stats_attaque()
        degats = self.agissant.force*self.taux[self.rempli]*self.agissant.affinite(element)*tranchant
        position = self.agissant.position
        zone = self.agissant.labyrinthe.a_portee(position,portee,self.deplacement,self.formes[self.rempli],self.passage,self.directions[self.rempli])
        for position in zone:
            self.agissant.labyrinthe.get_case(position).effets.add(AttaqueCase(self.agissant,degats,element,self.distance,self.directions[self.rempli]))
