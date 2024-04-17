"""Contient deux cas de réparateurs magiques."""

from __future__ import annotations

# Imports des classes parentes
from .reparateur_magique import ReparateurMagique

class PompeAPM(ReparateurMagique): #Régénère une quantité fixe de pm
    """Régénère une quantité fixe de pm à chaque tour."""
    pm:float

    def regen_pm(self,regen_pm:float):
        pm = self.pm
        for taux in self.taux_stats.values():
            pm *= taux
        return regen_pm + pm

class RenforceRegenPM(ReparateurMagique): #Démultiplie l'efficacité de la régénération
    """Démultiplie l'efficacité de la régénération."""
    taux_pm:float

    def regen_pm(self,regen_pm:float):
        taux_pm = self.taux_pm
        for taux in self.taux_stats.values():
            taux_pm *= taux
        return regen_pm * taux_pm
