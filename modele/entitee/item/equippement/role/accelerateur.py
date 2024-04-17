"""Contient la classe Accelerateur."""

from __future__ import annotations

# Imports des classes parentes
from ..equippement import Equippement

class Accelerateur(Equippement):
    """La classe des équipements qui augmentent la vitesse."""
    taux_vitesse:float

    def augmente_vitesse(self,vitesse:float):
        """Augmente la vitesse."""
        taux_vitesse = self.taux_vitesse
        for taux in self.taux_stats.values():
            taux_vitesse *= taux
        return vitesse * taux_vitesse
