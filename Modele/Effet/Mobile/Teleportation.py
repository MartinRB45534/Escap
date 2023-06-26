from __future__ import annotations
from typing import TYPE_CHECKING
import Carte as crt

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ...Entitee.Entitee import Mobile

# Imports des classes parentes
from .Mobile import Effet_mobile
from ..Effet import On_tick

class Teleportation(Effet_mobile, On_tick):
    """Effet qui déplace une entitée."""
    def __init__(self,mobile:Mobile,position:crt.Position):
        self.mobile = mobile
        self.position = position

    def action(self):
        self.mobile.position = self.position
