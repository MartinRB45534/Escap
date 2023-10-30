"""Contient la classe ReparateurMagique."""

from __future__ import annotations

# Imports des classes parentes
from ...equippement import Equippement

class ReparateurMagique(Equippement):
    """La classe des équipements qui régénèrent les pm."""
    def regen_pm(self,regen_pm:float):
        """Renvoie la nouvelle régénération des pm."""
        return regen_pm
