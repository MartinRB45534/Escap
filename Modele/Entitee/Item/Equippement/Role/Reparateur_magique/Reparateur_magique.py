from __future__ import annotations

# Pas d'import pour les annotations

# Imports des classes parentes
from ...equippement import Equippement

class Reparateur_magique(Equippement):
    """La classe des équipements qui régénèrent les pm."""
    def regen_pm(self,regen_pm:float):
        return regen_pm
