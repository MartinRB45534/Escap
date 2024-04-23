"""
Contient l'effets de soin placé sur une case.
"""

from __future__ import annotations
from typing import TYPE_CHECKING

# Imports des classes parentes
from .timings import OnPostActionCase

# Imports utilisés dans le code
from ..agissant.sante.soins import Soin

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ...entitee.agissant.agissant import Agissant
    from ...labyrinthe.case import Case

class SoinCase(OnPostActionCase):
    """Un effet de soin. À répercuter sur les occupants éventuels de la case."""
    def __init__(self,soin:type[Soin], responsable: Agissant, cible:str="alliés"):
        self.soin = soin
        self.responsable = responsable
        self.cible = cible

    def post_action(self, case:Case):
        cible_potentielle = case.agissant
        if cible_potentielle is not None:
            if not self.responsable: #Pas de responsable. Sérieusement ?
                cible_potentielle.effets.add(self.soin())
            else:
                esprit = self.responsable.esprit
                if not esprit: #Pas d'esprit ? Sérieusement ?
                    cible_potentielle.effets.add(self.soin())
                elif self.cible == "alliés" and cible_potentielle in esprit.corps:
                    cible_potentielle.effets.add(self.soin())
                elif self.cible == "neutres" and not cible_potentielle in esprit.corps:
                    cible_potentielle.effets.add(self.soin())
