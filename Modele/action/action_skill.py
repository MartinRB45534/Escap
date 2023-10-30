"""
Les classes de base des actions liées à un skill,
ainsi que quelques actions spécifiques.
"""

from __future__ import annotations
from typing import TYPE_CHECKING, List
import carte as crt

# Imports des classes parentes
from .action import Action, ActionParcellaire, NonRepetable

# Imports utilisés dans le code
from ..effet import ProtectionCaseBouclier

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ..entitee.agissant.agissant import Agissant
    from ..systeme.skill.actif import Actif
    from ..entitee.item.item import Item
    from ..entitee.item.equippement.degainable.bouclier.bouclier import Bouclier
    from ..commons import Deplacement
    from ..commons import Forme
    from ..commons import Passage

class ActionSkill(Action):
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



class Ramasse(ActionSkill, ActionParcellaire, NonRepetable):
    """
    L'action de ramasser les items d'une case.
    """
    def __init__(self,agissant:Agissant,latences:List[float],skill:Actif,xp:float,items:List[Item]):
        ActionSkill.__init__(self,agissant,sum(latences),skill,xp)
        ActionParcellaire.__init__(self,agissant,latences)
        NonRepetable.__init__(self,agissant,sum(latences))
        self.items = items

    def action(self):
        self.agissant.inventaire.ajoute(self.items[self.rempli-1])

class Derobe(ActionSkill, NonRepetable):
    """
    L'action de dérober un item.
    """
    def __init__(self,agissant:Agissant,latence:float,skill:Actif,xp:float,item:Item,possesseur:Agissant):
        super().__init__(agissant,latence,skill,xp)
        self.item = item
        self.possesseur = possesseur

    def action(self):
        self.possesseur.inventaire.drop(self.item)
        self.agissant.inventaire.ajoute(self.item)

class Blocage(ActionSkill):
    """
    L'action de bloquer avec un bouclier.
    """
    def __init__(self, agissant: Agissant, latence: float, skill: Actif, xp: float, taux: float, direction: crt.Direction, bouclier: Bouclier):
        super().__init__(agissant, latence, skill, xp)
        self.taux = taux
        self.direction = direction
        self.bouclier = bouclier

    def action(self):
        self.bouclier.taux_degats = self.taux
        self.agissant.labyrinthe.get_case(self.agissant.position).effets.add(ProtectionCaseBouclier(1,self.bouclier,[dir for dir in crt.Direction]))

class BlocageZone(Blocage):
    """
    L'action de bloquer avec un bouclier sur une zone.
    """
    def __init__(self, agissant: Agissant, latence: float, skill: Actif, xp: float, taux: float, direction: crt.Direction, bouclier: Bouclier, portee: int, deplacement: Deplacement, forme: Forme, passage: Passage):
        super().__init__(agissant, latence, skill, xp, taux, direction, bouclier)
        self.portee = portee
        self.deplacement = deplacement
        self.forme = forme
        self.passage = passage

    def action(self):
        self.bouclier.taux_degats = self.taux
        position = self.agissant.position
        zone = self.agissant.labyrinthe.a_portee(position,self.portee,self.deplacement,self.forme,self.passage)
        for pos in zone:
            self.agissant.labyrinthe.get_case(pos).effets.add(ProtectionCaseBouclier(1,self.bouclier,[dir for dir in crt.Direction]))

class CreeItem(ActionSkill):
    """
    L'action de créer un item.
    """
    def __init__(self, agissant: Agissant, latence: float, skill: Actif, xp: float, item: Item):
        super().__init__(agissant, latence, skill, xp)
        self.item = item

    def action(self):
        self.agissant.inventaire.ajoute(self.item)

class Alchimie(CreeItem, NonRepetable):
    """
    L'action de créer un item par alchimie.
    """
    def __init__(self, agissant: Agissant, latence: float, skill: Actif, xp: float, item: Item, ingredients: List[Item]):
        super().__init__(agissant, latence, skill, xp, item)
        self.ingredients = ingredients

    def action(self):
        for item in self.ingredients:
            self.agissant.inventaire.drop(item)
        self.agissant.inventaire.ajoute(self.item)
