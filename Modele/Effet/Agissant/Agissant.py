from __future__ import annotations
from typing import TYPE_CHECKING

# Imports des classes parentes
from ..effet import Effet
from ..timings import TimeLimited

if TYPE_CHECKING:
    from ...entitee.agissant.agissant import Agissant

class EffetAgissant(Effet):
    """Effet qui est placé sur un agissant."""

class TimeLimitedAgissant(TimeLimited):
    """Un TimeLimited qui a quelque chose à faire, sur un agissant"""
    def action(self,agissant:Agissant):
        """Une action exécutée sur un agissant."""
