"""
Quelques effets de dégats.
"""

from __future__ import annotations
from typing import TYPE_CHECKING

# Imports des classes parentes
from ..timings import OnDebutTourAgissant, OnFinTourAgissant

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ....entitee.agissant.agissant import Agissant
    from ....commons.elements import Element

class Degats(OnDebutTourAgissant):
    """La classe des effets de dégats."""
    def __init__(self,responsable:Agissant,element:Element,degats:float):
        self.responsable = responsable
        self.element = element
        self.degats = degats

    def debut_tour(self, agissant: Agissant):
        agissant.subit(self.degats,self.element)

class Combustion(Degats, OnFinTourAgissant):
    """La classe des effets de combustion (brulure)."""
    def __init__(self,responsable:Agissant,element:Element,degats:float,reduction:float):
        Degats.__init__(self,responsable,element,degats)
        self.reduction = reduction

    def fin_tour(self,_agissant: Agissant):
        self.degats -= self.reduction

    def termine(self) -> bool:
        return self.degats <= 0
