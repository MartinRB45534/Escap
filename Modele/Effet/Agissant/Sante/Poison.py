from __future__ import annotations
from typing import TYPE_CHECKING

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ....Entitee.Agissant.Agissant import Agissant

# Imports des classes parentes
from ...Effet import On_tick
from ..Agissant import Effet_agissant

class Poison(On_tick, Effet_agissant):
    """La classe des effets d'empoisonnement."""
    def __init__(self,agissant:Agissant,responsable:Agissant,degats_max:float,progression:float):
        self.agissant = agissant
        self.responsable = responsable
        self.degats = 0
        self.progression = progression
        self.degats_max = degats_max

    def action(self):
        self.agissant.statistiques.pv -= self.degats
        if self.degats < self.degats_max:
            self.degats += self.progression

    def execute(self):
        self.action()

    def termine(self) -> bool:
        return self.agissant.etat == Etats_agissants.MORT

# Imports utilisés dans le code
from ....Entitee.Agissant.Etats import Etats_agissants