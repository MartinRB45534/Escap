from __future__ import annotations
from typing import TYPE_CHECKING, List

from Jeu.Entitee.Agissant.Agissant import Agissant
from Jeu.Systeme.Skill import Skill_intrasec

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from Jeu.Entitee.Agissant.Agissant import Agissant
    from Jeu.Systeme.Skill import Skill_intrasec
    from Jeu.Effet.Effets_protection import Protection_bouclier
    from Jeu.Entitee.Item.Item import Item
    from Jeu.Entitee.Item.Equippement.Degainable.Bouclier.Bouclier import Bouclier
    from Jeu.Labyrinthe.Structure_spatiale.Direction import Direction

# Imports des classes parentes
from Jeu.Action.Action import Action, Action_parcellaire

class Action_skill(Action):
    """
    Les actions provoquées par un skill.
    """
    def __init__(self,agissant:Agissant,latence:float,skill:Skill_intrasec,xp:float):
        super().__init__(agissant,latence)
        self.skill = skill
        self.xp = xp

    def termine(self):
        """L'action est terminée."""
        self.skill.xp_new += self.xp

class Ramasse(Action_skill,Action_parcellaire):
    """
    L'action de ramasser les items d'une case.
    """
    def __init__(self,agissant:Agissant,latences:List[float],skill:Skill_intrasec,xp:float,items:List[Item]):
        Action_skill.__init__(self,agissant,sum(latences),skill,xp)
        self.latences = latences
        self.items = items

    def action(self):
        self.agissant.inventaire.ajoute(self.items[self.rempli-1])

class Blocage(Action_skill):
    """
    L'action de bloquer avec un bouclier.
    """
    def __init__(self, agissant: Agissant, latence: float, skill: Skill_intrasec, xp: float, taux: float, direction: Direction, bouclier: Bouclier):
        super().__init__(agissant, latence, skill, xp)
        self.taux = taux
        self.direction = direction
        self.bouclier = bouclier

    def action(self):
        self.bouclier.taux_degats = self.taux
        self.agissant.controleur.case_from_position(self.agissant.position).effets.append(Protection_bouclier(1,self.bouclier,[dir for dir in DIRECTIONS]))

class Blocage_zone(Blocage):
    """
    L'action de bloquer avec un bouclier sur une zone.
    """
    def __init__(self, agissant: Agissant, latence: float, skill: Skill_intrasec, xp: float, taux: float, direction: Direction, bouclier: Bouclier, portee: int, propagation:str="C__S___"):
        super().__init__(agissant, latence, skill, xp, taux, direction, bouclier)
        self.portee = portee
        self.propagation = propagation

    def action(self):
        self.bouclier.taux_degats = self.taux
        position = self.agissant.position
        positions_touchees = self.agissant.controleur.get_pos_touches(position,self.portee,self.propagation,self.direction)
        for pos in positions_touchees:
            self.agissant.controleur.case_from_position(pos).effets.append(Protection_bouclier(1,self.bouclier,[dir for dir in DIRECTIONS]))

# Imports utilisés dans le code
from Jeu.Labyrinthe.Structure_spatiale.Direction import DIRECTIONS