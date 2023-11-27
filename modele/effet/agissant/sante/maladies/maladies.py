"""
Contient les classes des maladies.
"""

from __future__ import annotations
import random

# Pas d'imports utilisés uniquement dans les annotations

# Imports des classes parentes
from .maladie import Maladie
from ...statistiques import EffetStats
from ...timings import OnDebutTourAgissant

class Tirnogose(Maladie, OnDebutTourAgissant):
    """Maladie qui cause une perte progressive de PV. Peut se transmettre aux voisins."""

    def debut_tour(self, agissant: Agissant):
        agissant.statistiques.pv -= self.virulence

class Fibaluse(Maladie, EffetStats):
    """Maladie qui réduit les statistiques. Peut se transmettre aux voisins."""

    def modifie_stats(self, stat:float) -> float:
        return stat * (self.virulence)

class Ibsutiomialgie(Maladie, OnDebutTourAgissant):
    """Maladie qui peut causer une mort subite. Peut se transmettre aux voisins."""

    def debut_tour(self, agissant: Agissant):
        if self.immunite == 0 and random.random() < self.virulence :
            agissant.meurt()
