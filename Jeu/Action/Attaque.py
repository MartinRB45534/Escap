from __future__ import annotations
from typing import TYPE_CHECKING, List

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from Jeu.Entitee.Agissant.Agissant import Agissant
    from Jeu.Entitee.Item.Equippement.Degainable.Degainable import Arme
    from Jeu.Systeme.Skill import Skill_intrasec
    from Jeu.Entitee.Item.Item import Item
    from Jeu.Labyrinthe.Structure_spatiale.Direction import Direction

# Imports des classes parentes
from Jeu.Action.Action_skill import Action_skill

# Valeurs par défaut des paramètres
from Jeu.Constantes import TERRE

class Attaque(Action_skill):
    """
    L'action d'attaquer.
    """
    def __init__(self,agissant:Agissant,latence:float,skill:Skill_intrasec,xp:float,taux:float,direction:Direction,portee:int,element:int=TERRE,propagation:str="C__S___",distance:str="contact"):
        super().__init__(agissant,latence,skill,xp)
        self.taux = taux
        self.direction = direction
        self.portee = portee
        self.element = element
        self.propagation = propagation
        self.distance = distance

    def termine(self):
        super().termine()
        force,affinite = self.agissant.get_stats_attaque(self.element)
        degats = force*self.taux*affinite
        position = self.agissant.position
        positions_touchees = self.agissant.controleur.get_pos_touches(position,self.portee,self.propagation,self.direction,"alliés",self.agissant)
        for position in positions_touchees:
            self.agissant.controleur.case_from_position(position).effets.append(Attaque_case(self.agissant,degats,self.element,self.distance,self.direction))

class Attaque_arme(Attaque):
    """
    L'action d'attaquer avec une arme.
    """
    def __init__(self,agissant:Agissant,latence:float,skill:Skill_intrasec,xp:float,taux:float,direction:Direction,arme:Arme,propagation:str="C__S___",distance:str="contact"):
        Action_skill.__init__(self,agissant,latence,skill,xp)
        self.taux = taux
        self.direction = direction
        self.propagation = propagation
        self.distance = distance
        self.arme = arme

    def termine(self):
        super().termine()
        element,tranchant,portee = self.arme.get_stats_attaque()
        force,affinite = self.agissant.get_stats_attaque(element)
        degats = force*self.taux*affinite*tranchant
        position = self.agissant.position
        positions_touchees = self.agissant.controleur.get_pos_touches(position,portee,self.propagation,self.direction,"alliés",self.agissant)
        for position in positions_touchees:
            self.agissant.controleur.case_from_position(position).effets.append(Attaque_case(self.agissant,degats,element,self.distance,self.direction))

class Attaque_multiple(Attaque_arme): # Les attaques sans arme ne peuvent pas être multiples
    """
    Une attaque complexe avec plusieurs coups.
    """
    def __init__(self,agissant:Agissant,latences:List[float],skill:Skill_intrasec,xp:float,taux:List[float],directions:List[Direction],arme:Arme,propagations:List[str]=["C__S___"],distance:str="contact"):
        Action_skill.__init__(self,agissant,sum(latences),skill,xp)
        self.latences = latences
        self.taux = taux
        self.directions = directions
        self.propagations = propagations
        self.distance = distance
        self.arme = arme

    def execute(self):
        self.latence += self.get_vitesse()
        while sum(self.latences[:len(self.latences)-len(self.directions)]) <= self.latence:
            element,tranchant,portee = self.arme.get_stats_attaque()
            force,affinite = self.agissant.get_stats_attaque(element)
            degats = force*self.taux[0]*affinite*tranchant
            position = self.agissant.position
            positions_touchees = self.agissant.controleur.get_pos_touches(position,portee,self.propagations[0],self.directions[0],"alliés",self.agissant)
            for position in positions_touchees:
                self.agissant.controleur.case_from_position(position).effets.append(Attaque_case(self.agissant,degats,element,self.distance,self.directions[0]))
            self.taux.pop(0)
            self.directions.pop(0)
            self.propagations.pop(0)
        if self.latence >= sum(self.latences):
            self.termine()
            return True
        return False
    
    def termine(self):
        Action_skill.termine(self)



# Imports utilisés dans le code
from Jeu.Effet.Attaque.Attaque import Attaque_case