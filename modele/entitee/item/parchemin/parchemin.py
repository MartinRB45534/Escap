"""Contient la classe Parchemin."""

from __future__ import annotations
from typing import TYPE_CHECKING

# Imports des classes parentes
from ..item import Item

# Imports utilisés dans le code
from ....affichage import SKIN_PARCHEMIN

if TYPE_CHECKING:
    from ....action import Impregne, Magie

class Parchemin(Item):
    """La classe des consommables qui s'activent avec du mana."""
    action_portee: Magie|None
    impregne: type[Impregne]|None

    @staticmethod
    def get_image():
        return SKIN_PARCHEMIN
