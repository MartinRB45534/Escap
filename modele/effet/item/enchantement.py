from __future__ import annotations

# Imports des classes parentes
from .item import EffetItem
from ..time_limited import TimeLimited

class EnchantementItem(TimeLimited, EffetItem):
    """Les enchantements qui affectent les items."""
