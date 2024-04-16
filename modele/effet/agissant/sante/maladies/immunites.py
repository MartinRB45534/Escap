"""
Les effets qui affectent les maladies des agissants.
"""

from __future__ import annotations
from typing import TYPE_CHECKING

# Imports des classes parentes
from ...agissant import EffetAgissant

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from .maladie import Maladie, FamilleMaladie

class EffetImmuniteMaladie(EffetAgissant):
    """Les effets qui permettent à un agissant de résister à une maladie."""
    def __init__(self, maladie:type[Maladie]|FamilleMaladie, priorite:float):
        self.maladie = maladie
        self.priorite = priorite

class EffetNonContagieux(EffetImmuniteMaladie):
    """Les effets qui empêchent un agissant de transmettre une maladie."""

class EffetNonInfectable(EffetImmuniteMaladie):
    """Les effets qui empêchent un agissant d'attraper une maladie."""

class EffetNonAffecte(EffetImmuniteMaladie):
    """Les effets qui empêchent une maladie d'avoir un effet sur un agissant."""
