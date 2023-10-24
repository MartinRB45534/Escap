from __future__ import annotations
from typing import TYPE_CHECKING

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ...entitee.agissant.agissant import Agissant

# Imports des classes parentes
from ..effet import Effet

class Effet_agissant(Effet):
    """Effet qui est placé sur un agissant."""
    def __init__(self, agissant:Agissant):
        self.agissant = agissant
