from __future__ import annotations

# Imports des classes parentes
from .agissant import EffetAgissant
from ..time_limited import TimeLimited

class EnchantementAgissant(TimeLimited, EffetAgissant):
    """Les enchantements qui affectent les agissant."""
