"""Effet qui déplace une entitée."""

from __future__ import annotations
from typing import TYPE_CHECKING
import carte as crt

from .mobile import EffetMobile

if TYPE_CHECKING:
    from ...entitee.entitee import Mobile

class Teleportation(EffetMobile):
    """Effet qui déplace une entitée."""
    def __init__(self,position:crt.Position):
        EffetMobile.__init__(self)
        self.position = position

    def deplace(self,mobile:Mobile):
        """Déplace l'entitée."""
        mobile.position = self.position
