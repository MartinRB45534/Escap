"""
Contient les classes des maladies.
"""

from __future__ import annotations
from typing import TYPE_CHECKING

import random

# Imports des classes parentes
from .maladie import Maladie
from ...statistiques import EffetStats, EffetForce, EffetVision, EffetPv, EffetPm, EffetVitesse, EffetAffinites
from ...timings import OnDebutTourAgissant

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from .....entitee import Agissant
    from .....commons import Element

class Tirgnonose(Maladie, OnDebutTourAgissant):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant."""
    def debut_tour(self, agissant: Agissant):
        agissant.statistiques.blesse(self._virulence)

class Fibaluse(Maladie, EffetStats):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant toutes ses stats."""
    def modifie_stats(self, stat: float) -> float:
        return max(0, stat - self._virulence)

class FibaluseForce(Fibaluse, EffetForce):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force."""
    def modifie_force(self, force: float) -> float:
        return max(0, force - self._virulence)

class FibaluseVision(Fibaluse, EffetVision):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vision."""
    def modifie_vision(self, vision: float) -> float:
        return max(0, vision - self._virulence)

class FibalusePv(Fibaluse, EffetPv):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa régénération de PV."""
    def modifie_pv(self, pv: float) -> float:
        return max(0, pv - self._virulence)

class FibalusePm(Fibaluse, EffetPm):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa régénération de PM."""
    def modifie_pm(self, pm: float) -> float:
        return max(0, pm - self._virulence)

class FibaluseVitesse(Fibaluse, EffetVitesse):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vitesse."""
    def modifie_vitesse(self, vitesse: float) -> float:
        return max(0, vitesse - self._virulence)

class FibaluseAffinite(Fibaluse, EffetAffinites):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant son affinité à un élément."""
    elements: set[Element]
    def modifie_affinite(self, affinite: float, element: Element) -> float:
        if element in self.elements:
            return max(0, affinite - self._virulence)
        return affinite

class Ibsutiomialgie(Maladie, OnDebutTourAgissant):
    """Une maladie qui peut tuer l'agissant de façon subite (ibsute)."""
    def __init__(self):
        Maladie.__init__(self)
        OnDebutTourAgissant.__init__(self)
        self.debut = True

    def debut_tour(self, agissant: Agissant):
        if self.debut:
            self.debut = False
            if random.random() < self.virulence:
                agissant.statistiques.blesse(agissant.statistiques.pv)
