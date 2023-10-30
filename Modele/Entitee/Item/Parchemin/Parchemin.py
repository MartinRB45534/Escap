"""Contient la classe Parchemin."""

from __future__ import annotations

# Imports des classes parentes
from ..item import Consommable

# Imports utilisés dans le code
from ....affichage import SKIN_PARCHEMIN

class Parchemin(Consommable):
    """La classe des consommables qui s'activent avec du mana."""

    @staticmethod
    def get_image():
        return SKIN_PARCHEMIN
