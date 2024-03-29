from __future__ import annotations

# Pas d'imports pour les annotations

# Imports des classes parentes
from ..agissant import Agissant

class Support_lointain(Agissant):
    """Les agissants qui combattent loin de la ligne de front."""

    def comporte_distance(self,degats:float=0):
        if (self.statistiques.pv-degats)/self.statistiques.pv_max >= 0.7:
            return 2
        else:
            return 3

    def veut_attaquer(self,degats:float=0):
        return (self.statistiques.pv+degats) <= self.statistiques.pv_max and (self.statistiques.pv-degats)/self.statistiques.pv_max >= 0.7

    def veut_fuir(self,degats:float=0):
        return (self.statistiques.pv+degats)/self.statistiques.pv_max < 0.7
