"""Contient deux cas de réparateurs magiques."""

from __future__ import annotations
from typing import TYPE_CHECKING
import carte as crt

# Imports des classes parentes
from .reparateur_magique import ReparateurMagique

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ......labyrinthe.labyrinthe import Labyrinthe

class PompeAPM(ReparateurMagique): #Régénère une quantité fixe de pm
    """Régénère une quantité fixe de pm à chaque tour."""
    def __init__(self,labyrinthe:Labyrinthe,position:crt.Position,pm:float):
        ReparateurMagique.__init__(self,labyrinthe,position)
        self.pm = pm

    def regen_pm(self,regen_pm:float):
        pm = self.pm
        for taux in self.taux_stats.values():
            pm *= taux
        return regen_pm + pm

class RenforceRegenPM(ReparateurMagique): #Démultiplie l'efficacité de la régénération
    """Démultiplie l'efficacité de la régénération."""
    def __init__(self,labyrinthe:Labyrinthe,position:crt.Position,taux_pm:float):
        ReparateurMagique.__init__(self,labyrinthe,position)
        self.taux_pm = taux_pm

    def regen_pm(self,regen_pm:float):
        taux_pm = self.taux_pm
        for taux in self.taux_stats.values():
            taux_pm *= taux
        return regen_pm * taux_pm
