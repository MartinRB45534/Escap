"""Contient deux cas de réparateurs."""

from __future__ import annotations

# Imports des classes parentes
from .reparateur import Reparateur

class PompeAPV(Reparateur): #Régénère une quantité fixe de pm
    """Régénère une quantité fixe de pv à chaque tour."""
    pv:float

    def regen_pv(self,regen_pv:float):
        pv = self.pv
        for taux in self.taux_stats.values():
            pv *= taux
        return regen_pv + pv

class RenforceRegenPV(Reparateur): #Démultiplie l'efficacité de la régénération
    """Démultiplie l'efficacité de la régénération."""
    taux_pv:float

    def regen_pv(self,regen_pv:float):
        taux_pv = self.taux_pv
        for taux in self.taux_stats.values():
            taux_pv *= taux
        return regen_pv * taux_pv
