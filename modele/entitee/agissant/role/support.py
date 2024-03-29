from __future__ import annotations

# Pas d'imports pour les annotations

# Imports des classes parentes
from ..agissant import Agissant

class Support(Agissant):
    """Les agissants qui combattent proche de la ligne de front.""" #Ils auront un "agit en vue" ou assimilé selon leur type de combat

    def comporte_distance(self,degats:float=0):
        if (self.statistiques.pv-degats)/self.statistiques.pv_max >= 0.4:
            return 1
        else:
            return 3

    def veut_attaquer(self,degats:float=0):
        return (self.statistiques.pv+degats)/self.statistiques.pv_max < 0.7 and (self.statistiques.pv-degats)/self.statistiques.pv_max >= 0.4

    def veut_fuir(self,degats:float=0):
        return (self.statistiques.pv+degats)/self.statistiques.pv_max < 0.4
