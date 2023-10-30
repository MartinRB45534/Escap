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
    def fin_tour(self, agissant:Agissant):
        for effet in agissant.effets:
            if isinstance(effet,Maladie): # Créer des médicaments différents selon les maladies ?
                agissant.effets.remove(effet)

class Purification(OnFinTourAgissant):
    """Effet qui supprime les effets de poison ou maladie de l'agissant"""
    def fin_tour(self, agissant:Agissant):
        for effet in agissant.effets:
            if isinstance(effet,(Maladie,Poison)):
                agissant.effets.remove(effet)

class Soin(OnFinTourAgissant):
    """Un effet de soin. Généralement placé sur l'agissant par une magie de soin, de soin de zone, ou d'auto-soin."""
    def __init__(self,responsable:Agissant,gain_pv:float):
        self.responsable = responsable
        self.gain_pv = gain_pv

    def fin_tour(self, agissant:Agissant):
        agissant.soigne(self.gain_pv)

class Immunite(OnFinTourAgissant):
    """Enchantement qui confère une immunité aux maladies, à condition de disposer de suffisamment de priorité."""
    def __init__(self,superiorite:float):
        self.superiorite = superiorite

    def fin_tour(self, agissant:Agissant):
        for effet in agissant.effets :
            if isinstance(effet,Maladie):
                if effet.virulence + self.superiorite < agissant.priorite :
                    agissant.effets.remove(effet)