"""
Module contenant les effets qui sont placés sur une case.
"""

from __future__ import annotations
from typing import TYPE_CHECKING

from ..effet import Effet

if TYPE_CHECKING:
    from ...entitee.entitee import Mobile

class EffetMobile(Effet):
    """Effet qui est placé sur une case."""
    def __init__(self, mobile:Mobile):
        self.mobile = mobile
