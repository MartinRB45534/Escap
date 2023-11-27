"""Les effets liés aux magies à coût variable."""

from __future__ import annotations
from typing import TYPE_CHECKING

# Imports des classes parentes
from .agissant import EffetAgissant
from .timings import OnDebutTourAgissant, TimeLimitedAgissant

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ...entitee.agissant.agissant import Agissant

class InvestissementMana(TimeLimitedAgissant,OnDebutTourAgissant):
    """Le joueur met du mana de côté, et en a plus après !"""
    def __init__(self,temps_restant:float,mana:float):
        TimeLimitedAgissant.__init__(self,temps_restant)
        self.mana = mana

    def debut_tour(self,agissant:Agissant):
        if self.termine():
            agissant.statistiques.pm += self.mana

class ReserveMana(EffetAgissant):
    """Effet qui correspond à une réserve de mana pour le joueur qui peut piocher dedans lorsqu'il en a besoin, mais ce mana n'est pas compté dans le calcul de son mana max."""
    def __init__(self,agissant:Agissant,mana:float):
        self.agissant = agissant
        self.mana = mana

    def paye(self,mana:float):
        """Paye le mana."""
        self.mana -= mana

    def termine(self):
        return self.mana <= 0
