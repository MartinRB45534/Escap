from __future__ import annotations
from typing import TYPE_CHECKING

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ...Entitee.Entitee import Mobile

# Imports des classes parentes
from ..Effet import Effet

class Effet_mobile(Effet):
    """Effet qui est placé sur une case."""
    def __init__(self, mobile:Mobile):
        self.mobile = mobile
