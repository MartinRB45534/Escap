from __future__ import annotations

# Pas d'import pour les annotations

# Imports des classes parentes
from ...equippement import Equippement

class Reparateur(Equippement):
    """La classe des équipements qui régénèrent les pv."""
    def regen_pv(self,regen_pv:float):
        return regen_pv
