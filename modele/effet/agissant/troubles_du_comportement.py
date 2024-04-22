"""
Quelques effets qui peuvent être appliqués à un agissant, et qui modifient son comportement.
"""

from __future__ import annotations
from typing import TYPE_CHECKING
import random

# Imports des classes parentes
from .timings import OnPostActionAgissant, OnPostDecisionAgissant

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ...entitee.agissant.agissant import Agissant

class Confusion(OnPostDecisionAgissant):
    """Les effets qui provoque des erreurs de direction."""
    taux_erreur:float
    def post_decision(self, agissant: Agissant):
        # On vérifie que l'agissant a une action, avec une direction
        agissant.confus(self.taux_erreur)

class PochesTrouees(OnPostActionAgissant):
    """L'effet qui fait droper des items involontairement."""
    taux_drop:float
    def post_action(self, agissant: Agissant) -> None:
        if random.random() < self.taux_drop :
            agissant.inventaire.drop_random(agissant.labyrinthe.position_case[agissant.position])
