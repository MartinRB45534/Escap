from __future__ import annotations

from Modele.Labyrinthe.Case import Case

# Pas d'imports utilisés uniquement dans les annotations

# Imports des classes parentes
from ..Case import Effet_case
from ...Effet import On_tick

class Aura(Effet_case, On_tick):
    """Effet qui est placé sur une case."""
    def __init__(self, case: Case, niveau: int):
        self.case = case
        self.niveau = niveau
        self.priorite = 0
        self.responsable = NOONE

# Imports utilisés dans le code
from ....Entitee.Agissant.Agissant import NOONE
