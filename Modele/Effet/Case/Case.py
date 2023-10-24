from __future__ import annotations
from typing import TYPE_CHECKING

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ...labyrinthe.case import Case

# Imports des classes parentes
from ..effet import Effet

class Effet_case(Effet):
    """Effet qui est placé sur une case."""
    def __init__(self, case:Case):
        self.case = case
