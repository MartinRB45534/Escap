from __future__ import annotations

# Pas d'import pour les annotations

# Imports des classes parentes
from Old_Jeu.Entitee.Item.Equippement.Equippement import Equipement

class Accelerateur(Equipement):
    """La classe des équipements qui augmentent la vitesse."""
    def __init__(self,taux_vitesse:float):
        self.taux_vitesse = taux_vitesse

    def augmente_vitesse(self,vitesse:float):
        taux_vitesse = self.taux_vitesse
        for taux in self.taux_stats.values():
            taux_vitesse *= taux
        return vitesse * taux_vitesse
