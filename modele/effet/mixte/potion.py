"""
Contient la classes des effets mixtes (effets d'agissants qui peuvent séjourner sur une case (pour les potions brisées au sol)).
"""

from __future__ import annotations
from typing import TYPE_CHECKING

# Imports des classes parentes
from ..agissant import EffetAgissant
from ..case import OnPostActionCase

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ...labyrinthe import Case

class EffetMixte(OnPostActionCase, EffetAgissant):
    """Effet qui peut séjourner sur une case."""
    on_case = False
    portee:float
    duree_max:float
    def __init__(self):
        self.duree = self.duree_max

    def post_action(self, case: Case):
        """L'effet est appelé après les actions de la case."""
        agissant_potentiel = case.agissant
        if agissant_potentiel:
            agissant_potentiel.effets.add(self)
            case.effets.remove(self)
            self.on_case = False
        self.duree -= 1

    def termine(self) -> bool:
        if self.on_case:
            return self.duree <= 0
        return True
