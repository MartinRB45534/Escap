"""
Contient la classe Poison.
"""

from __future__ import annotations
from typing import TYPE_CHECKING

# Imports des classes parentes
from ..timings import OnDebutTourAgissant

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ....entitee.agissant.agissant import Agissant

class Poison(OnDebutTourAgissant):
    """La classe des effets d'empoisonnement."""
    progression:float
    degats_max:float
    def __init__(self):
        self.degats = 0

    def debut_tour(self,agissant:Agissant):
        agissant.statistiques.pv -= self.degats # TODO : Utiliser la méthode de dégâts des statistiques
        if self.degats < self.degats_max:
            self.degats += self.progression

    def termine(self) -> bool:
        return False
