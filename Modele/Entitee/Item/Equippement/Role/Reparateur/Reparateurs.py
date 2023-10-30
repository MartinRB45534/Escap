"""Contient deux cas de réparateurs."""

from __future__ import annotations
from typing import TYPE_CHECKING
import carte as crt

# Imports des classes parentes
from .reparateur import Reparateur

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ......labyrinthe.labyrinthe import Labyrinthe

class PompeAPV(Reparateur): #Régénère une quantité fixe de pm
    """Régénère une quantité fixe de pv à chaque tour."""
    def __init__(self,labyrinthe:Labyrinthe,position:crt.Position,pv:float):
        Reparateur.__init__(self,labyrinthe,position)
        self.pv = pv

    def regen_pv(self,regen_pv:float):
        pv = self.pv
        for taux in self.taux_stats.values():
            pv *= taux
        return regen_pv + pv

class RenforceRegenPV(Reparateur): #Démultiplie l'efficacité de la régénération
    """Démultiplie l'efficacité de la régénération."""
    def __init__(self,labyrinthe:Labyrinthe,position:crt.Position,taux_pv:float):
        Reparateur.__init__(self,labyrinthe,position)
        self.taux_pv = taux_pv

    def regen_pv(self,regen_pv:float):
        taux_pv = self.taux_pv
        for taux in self.taux_stats.values():
            taux_pv *= taux
        return regen_pv * taux_pv
