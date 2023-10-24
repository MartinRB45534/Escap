from __future__ import annotations

from Modele.labyrinthe.case import Case

# Pas d'imports utilisés uniquement dans les annotations

# Imports des classes parentes
from ..case import Effet_case
from ...effet import OnTick

class Aura(Effet_case, OnTick):
    """Effet qui est placé sur une case."""
    def __init__(self, case: Case, niveau: int):
        self.case = case
        self.niveau = niveau
        self.priorite = 0
        self.responsable = NOONE

# Imports utilisés dans le code
from ....entitee.agissant.agissant import NOONE
