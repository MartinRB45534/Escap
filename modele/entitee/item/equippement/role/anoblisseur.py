"""Contient la classe Anoblisseur."""

from __future__ import annotations

# Imports des classes parentes
from ..equippement import Equippement

class Anoblisseur(Equippement):
    """La classe des équipements qui augmentent la priorité."""
    taux_priorite:float

    def augmente_priorite(self,priorite:float):
        """Augmente la priorité."""
        taux_priorite = self.taux_priorite
        for taux in self.taux_stats.values():
            taux_priorite *= taux
        return priorite * taux_priorite
