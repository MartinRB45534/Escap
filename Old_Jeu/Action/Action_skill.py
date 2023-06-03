from __future__ import annotations
from typing import TYPE_CHECKING, List

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from Old_Jeu.Entitee.Agissant.Agissant import Agissant
    from Old_Jeu.Systeme.Skill.Actif import Actif
    from Old_Jeu.Effet.Effets_protection import Protection_bouclier
    from Old_Jeu.Entitee.Item.Item import Item
    from Old_Jeu.Entitee.Item.Equippement.Degainable.Bouclier.Bouclier import Bouclier
    from Old_Jeu.Labyrinthe.Structure_spatiale.Direction import Direction

# Imports des classes parentes
from Old_Jeu.Action.Action import Action, Action_parcellaire, Non_repetable

class Action_skill(Action):
    """
    Les actions provoquées par un skill.
    """
    def __init__(self,agissant:Agissant,latence:float,skill:Actif,xp:float):
        super().__init__(agissant,latence)
        self.skill = skill
        self.xp = xp

    def termine(self):
        """L'action est terminée."""
        self.skill.xp_new += self.xp
        return super().termine()



class Ramasse(Action_skill, Action_parcellaire, Non_repetable):
    """
    L'action de ramasser les items d'une case.
    """
    def __init__(self,agissant:Agissant,latences:List[float],skill:Actif,xp:float,items:List[Item]):
        Action_skill.__init__(self,agissant,sum(latences),skill,xp)
        self.latences = latences
        self.items = items

    def action(self):
        self.agissant.inventaire.ajoute(self.items[self.rempli-1])

class Derobe(Action_skill, Non_repetable):
    """
    L'action de dérober un item.
    """
    def __init__(self,agissant:Agissant,latence:float,skill:Actif,xp:float,item:Item,possesseur:Agissant):
        super().__init__(agissant,latence,skill,xp)
        self.item = item
        self.possesseur = possesseur

    def action(self):
        self.possesseur.inventaire.drop(ABSENT,self.item)
        self.agissant.inventaire.ajoute(self.item)

class Blocage(Action_skill):
    """
    L'action de bloquer avec un bouclier.
    """
    def __init__(self, agissant: Agissant, latence: float, skill: Actif, xp: float, taux: float, direction: Direction, bouclier: Bouclier):
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
    def __init__(self, agissant: Agissant, latence: float, skill: Actif, xp: float, taux: float, direction: Direction, bouclier: Bouclier, portee: int, propagation:str="C__S___"):
        super().__init__(agissant, latence, skill, xp, taux, direction, bouclier)
        self.portee = portee
        self.propagation = propagation

    def action(self):
        self.bouclier.taux_degats = self.taux
        position = self.agissant.position
        positions_touchees = self.agissant.controleur.get_pos_touches(position,self.portee,self.propagation,self.direction)
        for pos in positions_touchees:
            self.agissant.controleur.case_from_position(pos).effets.append(Protection_bouclier(1,self.bouclier,[dir for dir in DIRECTIONS]))

class Cree_item(Action_skill):
    """
    L'action de créer un item.
    """
    def __init__(self, agissant: Agissant, latence: float, skill: Actif, xp: float, item: Item):
        super().__init__(agissant, latence, skill, xp)
        self.item = item

    def action(self):
        self.agissant.inventaire.ajoute(self.item)

class Alchimie(Cree_item, Non_repetable):
    """
    L'action de créer un item par alchimie.
    """
    def __init__(self, agissant: Agissant, latence: float, skill: Actif, xp: float, item: Item, ingredients: List[Item]):
        super().__init__(agissant, latence, skill, xp, item)
        self.ingredients = ingredients

    def action(self):
        for item in self.ingredients:
            self.agissant.inventaire.drop(ABSENT,item)
        self.agissant.inventaire.ajoute(self.item)

# Imports utilisés dans le code
from Old_Jeu.Labyrinthe.Structure_spatiale.Direction import DIRECTIONS
from Old_Jeu.Labyrinthe.Structure_spatiale.Position import ABSENT