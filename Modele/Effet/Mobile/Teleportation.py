"""Effet qui déplace une entitée."""

from __future__ import annotations
from typing import TYPE_CHECKING
import carte as crt

from .mobile import EffetMobile
from ..effet import OnTick

if TYPE_CHECKING:
    from ...entitee.entitee import Mobile

class Teleportation(EffetMobile, OnTick):
    """Effet qui déplace une entitée."""
    def __init__(self,mobile:Mobile,position:crt.Position):
        self.mobile = mobile
        self.position = position

    def action(self):
        self.mobile.position = self.position
