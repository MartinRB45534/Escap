from __future__ import annotations

# Pas d'import pour les annotations

# Imports des classes parentes
from .Reparateur import Reparateur

class Pompe_a_pv(Reparateur): #Régénère une quantité fixe de pm
    def __init__(self,pv:float):
        self.pv = pv

    def regen_pv(self,regen_pv:float):
        pv = self.pv
        for taux in self.taux_stats.values():
            pv *= taux
        return regen_pv + pv

class Renforce_regen_pv(Reparateur): #Démultiplie l'efficacité de la régénération
    def __init__(self,taux_pv:float):
        self.taux_pv = taux_pv

    def regen_pv(self,regen_pv:float):
        taux_pv = self.taux_pv
        for taux in self.taux_stats.values():
            taux_pv *= taux
        return regen_pv * taux_pv
