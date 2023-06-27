from __future__ import annotations
from typing import TYPE_CHECKING

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ....Entitee.Agissant.Agissant import Agissant
    from ....Systeme.Elements import Element

# Imports des classes parentes
from ...Effet import On_tick, One_shot
from ..Agissant import Effet_agissant

class Degats(One_shot, Effet_agissant):
    """La classe des effets de dégats."""
    def __init__(self,agissant:Agissant,responsable:Agissant,element:Element,degats:float):
        self.agissant = agissant
        self.responsable = responsable
        self.element = element
        self.degats = degats

    def action(self):
        pass

class Combustion(On_tick, Effet_agissant):
    """La classe des effets de combustion (brulure)."""
    def __init__(self,agissant:Agissant,responsable:Agissant,element:Element,degats:float,reduction:float):
        self.agissant = agissant
        self.responsable = responsable
        self.element = element
        self.degats = degats
        self.reduction = reduction

    def action(self):
        self.degats -= self.reduction

    def execute(self):
        self.action()

    def termine(self) -> bool:
        return self.degats <= 0