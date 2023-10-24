from __future__ import annotations

# Pas d'imports pour les annotations

# Imports des classes parentes
from .bourrin import Bourrin

class Dps(Bourrin):
    """Les agissants chargé d'infliger les dégats."""

    def comporte_distance(self,degats:float=0):
        if (self.statistiques.pv-degats)/self.statistiques.pv_max > 0.3:
            return 0
        else:
            return 3

    def veut_attaquer(self,degats:float=0):
        return (self.statistiques.pv+degats)/self.statistiques.pv_max > 0.3 #Appliquer un multiplicateur aux dégats en fonction des moyens de défense du DPS
