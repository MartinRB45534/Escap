"""
Contient la classe Poison.
"""

from __future__ import annotations
from typing import TYPE_CHECKING

# Imports des classes parentes
from ..timings import OnDebutTourAgissant
from ..agissant import EffetAgissant

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ....entitee.agissant.agissant import Agissant

class Poison(OnDebutTourAgissant, EffetAgissant):
    """La classe des effets d'empoisonnement."""
    def __init__(self,responsable:Agissant,degats_max:float,progression:float):
        self.responsable = responsable
        self.degats = 0
        self.progression = progression
        self.degats_max = degats_max

    def debut_tour(self,agissant:Agissant):
        agissant.statistiques.pv -= self.degats
        if self.degats < self.degats_max:
            self.degats += self.progression

    def termine(self) -> bool:
        return False
