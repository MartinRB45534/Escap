from __future__ import annotations

# Pas d'imports utilisés uniquement dans les annotations

# Imports des classes parentes
from .maladie import Maladie
from ...statistiques import Effet_stats

class Tirnogose(Maladie):
    """Maladie qui cause une perte progressive de PV. Peut se transmettre aux voisins."""

    def action(self):
        self.agissant.statistiques.pv -= self.virulence
        self.immunite += 1

class Fibaluse(Maladie, Effet_stats):
    """Maladie qui réduit les statistiques. Peut se transmettre aux voisins."""

    def action(self):
        self.immunite += 1

    def modifie_stats(self, stat:float) -> float:
        return stat * (self.virulence)

class Ibsutiomialgie(Maladie):
    """Maladie qui peut causer une mort subite. Peut se transmettre aux voisins."""

    def action(self):
        if self.immunite == 0 and random.random() < self.virulence :
            self.agissant.meurt()
        self.immunite += 1

# Imports utilisés dans le code
import random