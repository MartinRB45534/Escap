"""
Contient les effets de soin, d'immunité, de purification, etc.
"""

from __future__ import annotations
from typing import TYPE_CHECKING

# Imports des classes parentes
from ..timings import OnFinTourAgissant

# Imports utilisés dans le code
from .maladies.maladie import Maladie
from .poison import Poison

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ....entitee.agissant.agissant import Agissant

class Antidote(OnFinTourAgissant):
    """Effet qui supprime les effets de poison de l'agissant."""
    def fin_tour(self, agissant:Agissant):
        for effet in agissant.effets:
            if isinstance(effet,Poison):
                agissant.effets.remove(effet)

class Medicament(OnFinTourAgissant):
    """Effet qui supprime les effets de maladie de l'agissant."""
    maladie: str
    def fin_tour(self, agissant:Agissant):
        for effet in agissant.effets:
            if isinstance(effet,Maladie):
                if effet.nom == self.maladie or effet.famille.nom == self.maladie:
                    agissant.effets.remove(effet)

class Purification(OnFinTourAgissant):
    """Effet qui supprime les effets de poison ou maladie de l'agissant"""
    def fin_tour(self, agissant:Agissant):
        for effet in agissant.effets:
            if isinstance(effet,(Maladie,Poison)):
                agissant.effets.remove(effet)

class Soin(OnFinTourAgissant):
    """Un effet de soin. Généralement placé sur l'agissant par une magie de soin, de soin de zone, ou d'auto-soin."""
    gain_pv:float
    def fin_tour(self, agissant:Agissant):
        agissant.soigne(self.gain_pv)

class Vaccin(OnFinTourAgissant):
    """Effet qui immunise l'agissant contre une maladie."""
    maladie: str
    immunite: float
    def fin_tour(self, agissant:Agissant):
        agissant.statistiques.set_non_affecte(self.maladie,self.immunite)
        agissant.statistiques.set_non_contagieux(self.maladie,self.immunite)
        agissant.statistiques.set_non_infectable(self.maladie,self.immunite)

class Immunite(OnFinTourAgissant):
    """Enchantement qui confère une immunité aux maladies, à condition de disposer de suffisamment de priorité."""
    superiorite:float
    def fin_tour(self, agissant:Agissant):
        for effet in agissant.effets :
            if isinstance(effet,Maladie):
                if effet.virulence + self.superiorite < agissant.priorite :
                    agissant.effets.remove(effet)
