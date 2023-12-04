"""
Les auras sont des effets qui sont placés sur une case.
"""

from __future__ import annotations
from typing import TYPE_CHECKING

# Imports des classes parentes
from ..case import EffetCase

if TYPE_CHECKING:
    from ....entitee.agissant.agissant import Agissant

class Aura(EffetCase):
    """Effet qui est placé sur une case."""
    def __init__(self, responsable: Agissant):
        EffetCase.__init__(self)
        self.priorite = 0
        self.responsable = responsable
