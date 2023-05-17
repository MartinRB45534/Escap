from __future__ import annotations
from typing import TYPE_CHECKING, List

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from Jeu.Entitee.Agissant.Agissant import Agissant
    from Jeu.Systeme.Skill import Skill_intrasec
    from Jeu.Entitee.Item.Item import Item

# Imports des classes parentes
from Jeu.Action.Action import Action

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

class Ramasse(Action_skill):
    """
    L'action de ramasser les items d'une case.
    """
    def __init__(self,agissant:Agissant,latence:float,skill:Skill_intrasec,xp:float,items:List[Item]):
        super().__init__(agissant,latence,skill,xp)
        self.items = items

    def termine(self):
        super().termine()
        for item in self.items:
            self.agissant.inventaire.ajoute(item)
