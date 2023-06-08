from __future__ import annotations

# Pas d'import pour les annotations

# Imports des classes parentes
from ..Equippement import Equipement

class Anoblisseur(Equipement):
    """La classe des équipements qui augmentent la priorité."""
    def __init__(self,taux_priorite:float):
        self.taux_priorite = taux_priorite

    def augmente_priorite(self,priorite:float):
        taux_priorite = self.taux_priorite
        for taux in self.taux_stats.values():
            taux_priorite *= taux
        return priorite * taux_priorite
