from __future__ import annotations
from typing import TYPE_CHECKING, List, Optional
import Carte as crt

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ..Entitee.Agissant.Agissant import Agissant
    from ..Entitee.Item.Equippement.Degainable.Degainable import Arme
    from ..Systeme.Skill.Actif import Actif
    from ..Systeme.Elements import Element

# Imports des classes parentes
from ..Action.Action_skill import Action_skill
from ..Action.Action import Action_final, Action_parcellaire

class Attaque(Action_skill):
    """
    L'action d'attaquer.
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

    def action(self):
        degats = self.agissant.force*self.taux*self.agissant.affinite(self.element)
        position = self.agissant.position
        zone = self.agissant.labyrinthe.a_portee(position,self.portee,self.deplacement,self.forme,self.passage,self.direction)
        for position in zone:
            self.agissant.labyrinthe.get_case(position).effets.add(Attaque_case(self.agissant,degats,self.element,self.distance,self.direction))

class Attaque_final(Action_final,Attaque):
    """
    Une attaque qui se fait à la fin de la latence.
    """
    # L'attaque la plus courante, correspond aussi au stomp

class Attaque_arme(Attaque):
    """
    L'action d'attaquer avec une arme.
    """
    def __init__(self,agissant:Agissant,latence:float,skill:Actif,xp:float,taux:float,direction:crt.Direction,arme:Arme,deplacement:Deplacement,forme:Forme,passage:Passage,distance:str="contact"):
        Attaque.__init__(self,agissant,latence,skill,xp,taux,direction,arme.portee,arme.element,deplacement,forme,passage,distance)
        self.arme = arme

    def action(self):
        element,tranchant,portee = self.arme.get_stats_attaque()
        degats = self.agissant.force*self.taux*self.agissant.affinite(element)*tranchant
        position = self.agissant.position
        zone = self.agissant.labyrinthe.a_portee(position,portee,self.deplacement,self.forme,self.passage,self.direction)
        for position in zone:
            self.agissant.labyrinthe.get_case(position).effets.add(Attaque_case(self.agissant,degats,element,self.distance,self.direction))

class Attaque_arme_final(Action_final,Attaque_arme):
    """
    Une attaque avec une arme qui se fait à la fin de la latence.
    """
    # L'attaque avec une arme la plus courante (correspond aux attaques de base à l'épée et la lance)

class Attaque_multiple(Action_parcellaire,Attaque_arme): # Les attaques sans arme ne peuvent pas être multiples
    """
    Une attaque complexe avec plusieurs coups.
    """
    def __init__(self,agissant:Agissant,latences:List[float],skill:Actif,xp:float,taux:List[float],directions:List[crt.Direction],arme:Arme,deplacement:Deplacement,formes:List[Forme],passage:Passage,distance:str="contact"):
        Action_skill.__init__(self,agissant,sum(latences),skill,xp)
        self.latences = latences
        self.taux = taux
        self.directions = directions
        self.deplacement = deplacement
        self.formes = formes
        self.passage = passage
        self.distance = distance
        self.arme = arme

    def action(self):
        element,tranchant,portee = self.arme.get_stats_attaque()
        degats = self.agissant.force*self.taux[self.rempli]*self.agissant.affinite(element)*tranchant
        position = self.agissant.position
        zone = self.agissant.labyrinthe.a_portee(position,portee,self.deplacement,self.formes[self.rempli],self.passage,self.directions[self.rempli])
        for position in zone:
            self.agissant.labyrinthe.get_case(position).effets.add(Attaque_case(self.agissant,degats,element,self.distance,self.directions[self.rempli]))

# Imports utilisés dans le code
from ..Effet.Attaque.Attaque import Attaque_case
from ..Labyrinthe.Deplacement import Deplacement
from ..Labyrinthe.Forme import Forme
from ..Labyrinthe.Passage import Passage