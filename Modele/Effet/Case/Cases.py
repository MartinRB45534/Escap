from __future__ import annotations
from typing import TYPE_CHECKING

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ...Labyrinthe.Case import Case

# Imports des classes parentes
from ...Effet import Evenement
from .Case import Effet_case

class Obscurite(Evenement, Effet_case):
    """Evenement d'obscurité."""
    def __init__(self,case:Case,duree:int,gain_opacite:float):
        self.case = case
        self.temps_restant = duree
        self.gain_opacite = gain_opacite

    def action(self): #La case affectée devient plus impénétrable à la lumière
        pass

class Blizzard(Evenement, Effet_case):
    """Evenement de blizzard."""
    def __init__(self,case:Case,duree:int,gain_latence:float):
        self.case = case
        self.temps_restant = duree
        self.gain_latence = gain_latence

    def action(self):
        occupants = self.case.items | {self.case.agissant} if self.case.agissant is not None else self.case.items
        for occupant in occupants :
            if occupant.action is not None:
                occupant.action.latence -= self.gain_latence
