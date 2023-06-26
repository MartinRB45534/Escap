from __future__ import annotations

# Pas d'imports utilisés uniquement dans les annotations

# Imports des classes parentes
from ..Case import Effet_case
from ...Effet import On_tick

class Aura(Effet_case, On_tick):
    """Effet qui est placé sur une case."""
