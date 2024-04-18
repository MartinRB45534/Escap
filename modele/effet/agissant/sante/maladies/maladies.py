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
    def modifie_affinite(self, affinite: float, elements: Element) -> float:
        if elements in self.elements:
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

class TirgnonoseFibaluse(Tirgnonose, Fibaluse):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale)."""

class TirgnonoseFibaluseForce(TirgnonoseFibaluse, FibaluseForce):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force."""

class TirgnonoseFibaluseVision(TirgnonoseFibaluse, FibaluseVision):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vision."""

class TirgnonoseFibalusePv(TirgnonoseFibaluse, FibalusePv):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa régénération de PV."""

class TirgnonoseFibalusePm(TirgnonoseFibaluse, FibalusePm):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa régénération de PM."""

class TirgnonoseFibaluseVitesse(TirgnonoseFibaluse, FibaluseVitesse):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vitesse."""

class TirgnonoseFibaluseAffinite(TirgnonoseFibaluse, FibaluseAffinite):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant son affinité à un élément."""

class TirgnonoseIbsutiomialgie(Tirgnonose, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et peut le tuer de façon subite (ibsute)."""

class FibaluseIbsutiomialgie(Fibaluse, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant et peut le tuer de façon subite (ibsute)."""

class FibaluseForceVision(FibaluseForce, FibaluseVision):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force et sa vision."""

class FibaluseForcePv(FibaluseForce, FibalusePv):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force et sa régénération de PV."""

class FibaluseForcePm(FibaluseForce, FibalusePm):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force et sa régénération de PM."""

class FibaluseForceVitesse(FibaluseForce, FibaluseVitesse):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force et sa vitesse."""

class FibaluseForceAffinite(FibaluseForce, FibaluseAffinite):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force et son affinité à un élément."""

class FibaluseForceIbsutiomialgie(FibaluseForce, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force et peut le tuer de façon subite (ibsute)."""

class FibaluseVisionPv(FibaluseVision, FibalusePv):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vision et sa régénération de PV."""

class FibaluseVisionPm(FibaluseVision, FibalusePm):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vision et sa régénération de PM."""

class FibaluseVisionVitesse(FibaluseVision, FibaluseVitesse):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vision et sa vitesse."""

class FibaluseVisionAffinite(FibaluseVision, FibaluseAffinite):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vision et son affinité à un élément."""

class FibaluseVisionIbsutiomialgie(FibaluseVision, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vision et peut le tuer de façon subite (ibsute)."""

class FibalusePvPm(FibalusePv, FibalusePm):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa régénération de PV et de PM."""

class FibalusePvVitesse(FibalusePv, FibaluseVitesse):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa régénération de PV et sa vitesse."""

class FibalusePvAffinite(FibalusePv, FibaluseAffinite):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa régénération de PV et son affinité à un élément."""

class FibalusePvIbsutiomialgie(FibalusePv, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa régénération de PV et peut le tuer de façon subite (ibsute)."""

class FibalusePmVitesse(FibalusePm, FibaluseVitesse):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa régénération de PM et sa vitesse."""

class FibalusePmAffinite(FibalusePm, FibaluseAffinite):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa régénération de PM et son affinité à un élément."""

class FibalusePmIbsutiomialgie(FibalusePm, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa régénération de PM et peut le tuer de façon subite (ibsute)."""

class FibaluseVitesseAffinite(FibaluseVitesse, FibaluseAffinite):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vitesse et son affinité à un élément."""

class FibaluseVitesseIbsutiomialgie(FibaluseVitesse, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vitesse et peut le tuer de façon subite (ibsute)."""

class FibaluseAffiniteIbsutiomialgie(FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseIbsutiomialgie(TirgnonoseFibaluse, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseForceVision(Tirgnonose, FibaluseForce, FibaluseVision):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force et sa vision."""

class TirgnonoseFibaluseForcePv(Tirgnonose, FibaluseForce, FibalusePv):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force et sa régénération de PV."""

class TirgnonoseFibaluseForcePm(Tirgnonose, FibaluseForce, FibalusePm):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force et sa régénération de PM."""

class TirgnonoseFibaluseForceVitesse(Tirgnonose, FibaluseForce, FibaluseVitesse):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force et sa vitesse."""

class TirgnonoseFibaluseForceAffinite(Tirgnonose, FibaluseForce, FibaluseAffinite):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force et son affinité à un élément."""

class TirgnonoseFibaluseForceIbsutiomialgie(Tirgnonose, FibaluseForce, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseVisionPv(Tirgnonose, FibaluseVision, FibalusePv):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vision et sa régénération de PV."""

class TirgnonoseFibaluseVisionPm(Tirgnonose, FibaluseVision, FibalusePm):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vision et sa régénération de PM."""

class TirgnonoseFibaluseVisionVitesse(Tirgnonose, FibaluseVision, FibaluseVitesse):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vision et sa vitesse."""

class TirgnonoseFibaluseVisionAffinite(Tirgnonose, FibaluseVision, FibaluseAffinite):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vision et son affinité à un élément."""

class TirgnonoseFibaluseVisionIbsutiomialgie(Tirgnonose, FibaluseVision, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vision et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibalusePvPm(Tirgnonose, FibalusePv, FibalusePm):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa régénération de PV et de PM."""

class TirgnonoseFibalusePvVitesse(Tirgnonose, FibalusePv, FibaluseVitesse):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa régénération de PV et sa vitesse."""

class TirgnonoseFibalusePvAffinite(Tirgnonose, FibalusePv, FibaluseAffinite):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa régénération de PV et son affinité à un élément."""

class TirgnonoseFibalusePvIbsutiomialgie(Tirgnonose, FibalusePv, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa régénération de PV et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibalusePmVitesse(Tirgnonose, FibalusePm, FibaluseVitesse):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa régénération de PM et sa vitesse."""

class TirgnonoseFibalusePmAffinite(Tirgnonose, FibalusePm, FibaluseAffinite):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa régénération de PM et son affinité à un élément."""

class TirgnonoseFibalusePmIbsutiomialgie(Tirgnonose, FibalusePm, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa régénération de PM et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseVitesseAffinite(Tirgnonose, FibaluseVitesse, FibaluseAffinite):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vitesse et son affinité à un élément."""

class TirgnonoseFibaluseVitesseIbsutiomialgie(Tirgnonose, FibaluseVitesse, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vitesse et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseAffiniteIbsutiomialgie(Tirgnonose, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class FibaluseForceVisionPv(FibaluseForce, FibaluseVision, FibalusePv):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vision et sa régénération de PV."""

class FibaluseForceVisionPm(FibaluseForce, FibaluseVision, FibalusePm):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vision et sa régénération de PM."""

class FibaluseForceVisionVitesse(FibaluseForce, FibaluseVision, FibaluseVitesse):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vision et sa vitesse."""

class FibaluseForceVisionAffinite(FibaluseForce, FibaluseVision, FibaluseAffinite):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vision et son affinité à un élément."""

class FibaluseForceVisionIbsutiomialgie(FibaluseForce, FibaluseVision, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vision et peut le tuer de façon subite (ibsute)."""

class FibaluseForcePvPm(FibaluseForce, FibalusePv, FibalusePm):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa régénération de PV et de PM."""

class FibaluseForcePvVitesse(FibaluseForce, FibalusePv, FibaluseVitesse):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa régénération de PV et sa vitesse."""

class FibaluseForcePvAffinite(FibaluseForce, FibalusePv, FibaluseAffinite):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa régénération de PV et son affinité à un élément."""

class FibaluseForcePvIbsutiomialgie(FibaluseForce, FibalusePv, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa régénération de PV et peut le tuer de façon subite (ibsute)."""

class FibaluseForcePmVitesse(FibaluseForce, FibalusePm, FibaluseVitesse):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa régénération de PM et sa vitesse."""

class FibaluseForcePmAffinite(FibaluseForce, FibalusePm, FibaluseAffinite):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa régénération de PM et son affinité à un élément."""

class FibaluseForcePmIbsutiomialgie(FibaluseForce, FibalusePm, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa régénération de PM et peut le tuer de façon subite (ibsute)."""

class FibaluseForceVitesseAffinite(FibaluseForce, FibaluseVitesse, FibaluseAffinite):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vitesse et son affinité à un élément."""

class FibaluseForceVitesseIbsutiomialgie(FibaluseForce, FibaluseVitesse, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vitesse et peut le tuer de façon subite (ibsute)."""

class FibaluseForceAffiniteIbsutiomialgie(FibaluseForce, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class FibaluseVisionPvPm(FibaluseVision, FibalusePv, FibalusePm):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vision, sa régénération de PV et de PM."""

class FibaluseVisionPvVitesse(FibaluseVision, FibalusePv, FibaluseVitesse):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vision, sa régénération de PV et sa vitesse."""

class FibaluseVisionPvAffinite(FibaluseVision, FibalusePv, FibaluseAffinite):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vision, sa régénération de PV et son affinité à un élément."""

class FibaluseVisionPvIbsutiomialgie(FibaluseVision, FibalusePv, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vision, sa régénération de PV et peut le tuer de façon subite (ibsute)."""

class FibaluseVisionPmVitesse(FibaluseVision, FibalusePm, FibaluseVitesse):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vision, sa régénération de PM et sa vitesse."""

class FibaluseVisionPmAffinite(FibaluseVision, FibalusePm, FibaluseAffinite):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vision, sa régénération de PM et son affinité à un élément."""

class FibaluseVisionPmIbsutiomialgie(FibaluseVision, FibalusePm, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vision, sa régénération de PM et peut le tuer de façon subite (ibsute)."""

class FibaluseVisionVitesseAffinite(FibaluseVision, FibaluseVitesse, FibaluseAffinite):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vision, sa vitesse et son affinité à un élément."""

class FibaluseVisionVitesseIbsutiomialgie(FibaluseVision, FibaluseVitesse, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vision, sa vitesse et peut le tuer de façon subite (ibsute)."""

class FibaluseVisionAffiniteIbsutiomialgie(FibaluseVision, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vision, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class FibalusePvPmVitesse(FibalusePv, FibalusePm, FibaluseVitesse):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa régénération de PV, de PM et sa vitesse."""

class FibalusePvPmAffinite(FibalusePv, FibalusePm, FibaluseAffinite):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa régénération de PV, de PM et son affinité à un élément."""

class FibalusePvPmIbsutiomialgie(FibalusePv, FibalusePm, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa régénération de PV, de PM et peut le tuer de façon subite (ibsute)."""

class FibalusePvVitesseAffinite(FibalusePv, FibaluseVitesse, FibaluseAffinite):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa régénération de PV, sa vitesse et son affinité à un élément."""

class FibalusePvVitesseIbsutiomialgie(FibalusePv, FibaluseVitesse, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa régénération de PV, sa vitesse et peut le tuer de façon subite (ibsute)."""

class FibalusePvAffiniteIbsutiomialgie(FibalusePv, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa régénération de PV, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class FibalusePmVitesseAffinite(FibalusePm, FibaluseVitesse, FibaluseAffinite):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa régénération de PM, sa vitesse et son affinité à un élément."""

class FibalusePmVitesseIbsutiomialgie(FibalusePm, FibaluseVitesse, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa régénération de PM, sa vitesse et peut le tuer de façon subite (ibsute)."""

class FibalusePmAffiniteIbsutiomialgie(FibalusePm, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa régénération de PM, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class FibaluseVitesseAffiniteIbsutiomialgie(FibaluseVitesse, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vitesse, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseForceVisionPv(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePv):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vision et sa régénération de PV."""

class TirgnonoseFibaluseForceVisionPm(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePm):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vision et sa régénération de PM."""

class TirgnonoseFibaluseForceVisionVitesse(Tirgnonose, FibaluseForce, FibaluseVision, FibaluseVitesse):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vision et sa vitesse."""

class TirgnonoseFibaluseForceVisionAffinite(Tirgnonose, FibaluseForce, FibaluseVision, FibaluseAffinite):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vision et son affinité à un élément."""

class TirgnonoseFibaluseForceVisionIbsutiomialgie(Tirgnonose, FibaluseForce, FibaluseVision, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vision et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseForcePvPm(Tirgnonose, FibaluseForce, FibalusePv, FibalusePm):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa régénération de PV et de PM."""

class TirgnonoseFibaluseForcePvVitesse(Tirgnonose, FibaluseForce, FibalusePv, FibaluseVitesse):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa régénération de PV et sa vitesse."""

class TirgnonoseFibaluseForcePvAffinite(Tirgnonose, FibaluseForce, FibalusePv, FibaluseAffinite):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa régénération de PV et son affinité à un élément."""

class TirgnonoseFibaluseForcePvIbsutiomialgie(Tirgnonose, FibaluseForce, FibalusePv, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa régénération de PV et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseForcePmVitesse(Tirgnonose, FibaluseForce, FibalusePm, FibaluseVitesse):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa régénération de PM et sa vitesse."""

class TirgnonoseFibaluseForcePmAffinite(Tirgnonose, FibaluseForce, FibalusePm, FibaluseAffinite):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa régénération de PM et son affinité à un élément."""

class TirgnonoseFibaluseForcePmIbsutiomialgie(Tirgnonose, FibaluseForce, FibalusePm, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa régénération de PM et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseForceVitesseAffinite(Tirgnonose, FibaluseForce, FibaluseVitesse, FibaluseAffinite):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vitesse et son affinité à un élément."""

class TirgnonoseFibaluseForceVitesseIbsutiomialgie(Tirgnonose, FibaluseForce, FibaluseVitesse, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vitesse et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseForceAffiniteIbsutiomialgie(Tirgnonose, FibaluseForce, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseVisionPvPm(Tirgnonose, FibaluseVision, FibalusePv, FibalusePm):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vision, sa régénération de PV et de PM."""

class TirgnonoseFibaluseVisionPvVitesse(Tirgnonose, FibaluseVision, FibalusePv, FibaluseVitesse):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vision, sa régénération de PV et sa vitesse."""

class TirgnonoseFibaluseVisionPvAffinite(Tirgnonose, FibaluseVision, FibalusePv, FibaluseAffinite):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vision, sa régénération de PV et son affinité à un élément."""

class TirgnonoseFibaluseVisionPvIbsutiomialgie(Tirgnonose, FibaluseVision, FibalusePv, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vision, sa régénération de PV et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseVisionPmVitesse(Tirgnonose, FibaluseVision, FibalusePm, FibaluseVitesse):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vision, sa régénération de PM et sa vitesse."""

class TirgnonoseFibaluseVisionPmAffinite(Tirgnonose, FibaluseVision, FibalusePm, FibaluseAffinite):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vision, sa régénération de PM et son affinité à un élément."""

class TirgnonoseFibaluseVisionPmIbsutiomialgie(Tirgnonose, FibaluseVision, FibalusePm, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vision, sa régénération de PM et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseVisionVitesseAffinite(Tirgnonose, FibaluseVision, FibaluseVitesse, FibaluseAffinite):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vision, sa vitesse et son affinité à un élément."""

class TirgnonoseFibaluseVisionVitesseIbsutiomialgie(Tirgnonose, FibaluseVision, FibaluseVitesse, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vision, sa vitesse et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseVisionAffiniteIbsutiomialgie(Tirgnonose, FibaluseVision, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vision, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibalusePvPmVitesse(Tirgnonose, FibalusePv, FibalusePm, FibaluseVitesse):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa régénération de PV, de PM et sa vitesse."""

class TirgnonoseFibalusePvPmAffinite(Tirgnonose, FibalusePv, FibalusePm, FibaluseAffinite):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa régénération de PV, de PM et son affinité à un élément."""

class TirgnonoseFibalusePvPmIbsutiomialgie(Tirgnonose, FibalusePv, FibalusePm, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa régénération de PV, de PM et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibalusePvVitesseAffinite(Tirgnonose, FibalusePv, FibaluseVitesse, FibaluseAffinite):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa régénération de PV, sa vitesse et son affinité à un élément."""

class TirgnonoseFibalusePvVitesseIbsutiomialgie(Tirgnonose, FibalusePv, FibaluseVitesse, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa régénération de PV, sa vitesse et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibalusePvAffiniteIbsutiomialgie(Tirgnonose, FibalusePv, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa régénération de PV, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibalusePmVitesseAffinite(Tirgnonose, FibalusePm, FibaluseVitesse, FibaluseAffinite):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa régénération de PM, sa vitesse et son affinité à un élément."""

class TirgnonoseFibalusePmVitesseIbsutiomialgie(Tirgnonose, FibalusePm, FibaluseVitesse, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa régénération de PM, sa vitesse et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibalusePmAffiniteIbsutiomialgie(Tirgnonose, FibalusePm, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa régénération de PM, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseVitesseAffiniteIbsutiomialgie(Tirgnonose, FibaluseVitesse, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vitesse, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class FibaluseForceVisionPvPm(FibaluseForce, FibaluseVision, FibalusePv, FibalusePm):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vision, sa régénération de PV et de PM."""

class FibaluseForceVisionPvVitesse(FibaluseForce, FibaluseVision, FibalusePv, FibaluseVitesse):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vision, sa régénération de PV et sa vitesse."""

class FibaluseForceVisionPvAffinite(FibaluseForce, FibaluseVision, FibalusePv, FibaluseAffinite):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vision, sa régénération de PV et son affinité à un élément."""

class FibaluseForceVisionPvIbsutiomialgie(FibaluseForce, FibaluseVision, FibalusePv, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vision, sa régénération de PV et peut le tuer de façon subite (ibsute)."""

class FibaluseForceVisionPmVitesse(FibaluseForce, FibaluseVision, FibalusePm, FibaluseVitesse):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vision, sa régénération de PM et sa vitesse."""

class FibaluseForceVisionPmAffinite(FibaluseForce, FibaluseVision, FibalusePm, FibaluseAffinite):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vision, sa régénération de PM et son affinité à un élément."""

class FibaluseForceVisionPmIbsutiomialgie(FibaluseForce, FibaluseVision, FibalusePm, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vision, sa régénération de PM et peut le tuer de façon subite (ibsute)."""

class FibaluseForceVisionVitesseAffinite(FibaluseForce, FibaluseVision, FibaluseVitesse, FibaluseAffinite):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vision, sa vitesse et son affinité à un élément."""

class FibaluseForceVisionVitesseIbsutiomialgie(FibaluseForce, FibaluseVision, FibaluseVitesse, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vision, sa vitesse et peut le tuer de façon subite (ibsute)."""

class FibaluseForceVisionAffiniteIbsutiomialgie(FibaluseForce, FibaluseVision, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vision, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class FibaluseForcePvPmVitesse(FibaluseForce, FibalusePv, FibalusePm, FibaluseVitesse):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa régénération de PV, de PM et sa vitesse."""

class FibaluseForcePvPmAffinite(FibaluseForce, FibalusePv, FibalusePm, FibaluseAffinite):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa régénération de PV, de PM et son affinité à un élément."""

class FibaluseForcePvPmIbsutiomialgie(FibaluseForce, FibalusePv, FibalusePm, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa régénération de PV, de PM et peut le tuer de façon subite (ibsute)."""

class FibaluseForcePvVitesseAffinite(FibaluseForce, FibalusePv, FibaluseVitesse, FibaluseAffinite):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa régénération de PV, sa vitesse et son affinité à un élément."""

class FibaluseForcePvVitesseIbsutiomialgie(FibaluseForce, FibalusePv, FibaluseVitesse, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa régénération de PV, sa vitesse et peut le tuer de façon subite (ibsute)."""

class FibaluseForcePvAffiniteIbsutiomialgie(FibaluseForce, FibalusePv, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa régénération de PV, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class FibaluseForcePmVitesseAffinite(FibaluseForce, FibalusePm, FibaluseVitesse, FibaluseAffinite):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa régénération de PM, sa vitesse et son affinité à un élément."""

class FibaluseForcePmVitesseIbsutiomialgie(FibaluseForce, FibalusePm, FibaluseVitesse, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa régénération de PM, sa vitesse et peut le tuer de façon subite (ibsute)."""

class FibaluseForcePmAffiniteIbsutiomialgie(FibaluseForce, FibalusePm, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa régénération de PM, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class FibaluseForceVitesseAffiniteIbsutiomialgie(FibaluseForce, FibaluseVitesse, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vitesse, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class FibaluseVisionPvPmVitesse(FibaluseVision, FibalusePv, FibalusePm, FibaluseVitesse):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vision, sa régénération de PV, de PM et sa vitesse."""

class FibaluseVisionPvPmAffinite(FibaluseVision, FibalusePv, FibalusePm, FibaluseAffinite):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vision, sa régénération de PV, de PM et son affinité à un élément."""

class FibaluseVisionPvPmIbsutiomialgie(FibaluseVision, FibalusePv, FibalusePm, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vision, sa régénération de PV, de PM et peut le tuer de façon subite (ibsute)."""

class FibaluseVisionPvVitesseAffinite(FibaluseVision, FibalusePv, FibaluseVitesse, FibaluseAffinite):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vision, sa régénération de PV, sa vitesse et son affinité à un élément."""

class FibaluseVisionPvVitesseIbsutiomialgie(FibaluseVision, FibalusePv, FibaluseVitesse, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vision, sa régénération de PV, sa vitesse et peut le tuer de façon subite (ibsute)."""

class FibaluseVisionPvAffiniteIbsutiomialgie(FibaluseVision, FibalusePv, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vision, sa régénération de PV, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class FibaluseVisionPmVitesseAffinite(FibaluseVision, FibalusePm, FibaluseVitesse, FibaluseAffinite):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vision, sa régénération de PM, sa vitesse et son affinité à un élément."""

class FibaluseVisionPmVitesseIbsutiomialgie(FibaluseVision, FibalusePm, FibaluseVitesse, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vision, sa régénération de PM, sa vitesse et peut le tuer de façon subite (ibsute)."""

class FibaluseVisionPmAffiniteIbsutiomialgie(FibaluseVision, FibalusePm, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vision, sa régénération de PM, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class FibaluseVisionVitesseAffiniteIbsutiomialgie(FibaluseVision, FibaluseVitesse, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vision, sa vitesse, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class FibalusePvPmVitesseAffinite(FibalusePv, FibalusePm, FibaluseVitesse, FibaluseAffinite):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa régénération de PV, de PM, sa vitesse et son affinité à un élément."""

class FibalusePvPmVitesseIbsutiomialgie(FibalusePv, FibalusePm, FibaluseVitesse, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa régénération de PV, de PM, sa vitesse et peut le tuer de façon subite (ibsute)."""

class FibalusePvPmAffiniteIbsutiomialgie(FibalusePv, FibalusePm, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa régénération de PV, de PM, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class FibalusePvVitesseAffiniteIbsutiomialgie(FibalusePv, FibaluseVitesse, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa régénération de PV, sa vitesse, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class FibalusePmVitesseAffiniteIbsutiomialgie(FibalusePm, FibaluseVitesse, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa régénération de PM, sa vitesse, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseForceVisionPvPm(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePv, FibalusePm):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vision, sa régénération de PV et de PM."""

class TirgnonoseFibaluseForceVisionPvVitesse(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePv, FibaluseVitesse):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vision, sa régénération de PV et sa vitesse."""

class TirgnonoseFibaluseForceVisionPvAffinite(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePv, FibaluseAffinite):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vision, sa régénération de PV et son affinité à un élément."""

class TirgnonoseFibaluseForceVisionPvIbsutiomialgie(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePv, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vision, sa régénération de PV et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseForceVisionPmVitesse(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePm, FibaluseVitesse):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vision, sa régénération de PM et sa vitesse."""

class TirgnonoseFibaluseForceVisionPmAffinite(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePm, FibaluseAffinite):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vision, sa régénération de PM et son affinité à un élément."""

class TirgnonoseFibaluseForceVisionPmIbsutiomialgie(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePm, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vision, sa régénération de PM et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseForceVisionVitesseAffinite(Tirgnonose, FibaluseForce, FibaluseVision, FibaluseVitesse, FibaluseAffinite):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vision, sa vitesse et son affinité à un élément."""

class TirgnonoseFibaluseForceVisionVitesseIbsutiomialgie(Tirgnonose, FibaluseForce, FibaluseVision, FibaluseVitesse, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vision, sa vitesse et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseForceVisionAffiniteIbsutiomialgie(Tirgnonose, FibaluseForce, FibaluseVision, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vision, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseForcePvPmVitesse(Tirgnonose, FibaluseForce, FibalusePv, FibalusePm, FibaluseVitesse):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa régénération de PV, de PM et sa vitesse."""

class TirgnonoseFibaluseForcePvPmAffinite(Tirgnonose, FibaluseForce, FibalusePv, FibalusePm, FibaluseAffinite):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa régénération de PV, de PM et son affinité à un élément."""

class TirgnonoseFibaluseForcePvPmIbsutiomialgie(Tirgnonose, FibaluseForce, FibalusePv, FibalusePm, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa régénération de PV, de PM et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseForcePvVitesseAffinite(Tirgnonose, FibaluseForce, FibalusePv, FibaluseVitesse, FibaluseAffinite):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa régénération de PV, sa vitesse et son affinité à un élément."""

class TirgnonoseFibaluseForcePvVitesseIbsutiomialgie(Tirgnonose, FibaluseForce, FibalusePv, FibaluseVitesse, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa régénération de PV, sa vitesse et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseForcePvAffiniteIbsutiomialgie(Tirgnonose, FibaluseForce, FibalusePv, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa régénération de PV, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseForcePmVitesseAffinite(Tirgnonose, FibaluseForce, FibalusePm, FibaluseVitesse, FibaluseAffinite):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa régénération de PM, sa vitesse et son affinité à un élément."""

class TirgnonoseFibaluseForcePmVitesseIbsutiomialgie(Tirgnonose, FibaluseForce, FibalusePm, FibaluseVitesse, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa régénération de PM, sa vitesse et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseForcePmAffiniteIbsutiomialgie(Tirgnonose, FibaluseForce, FibalusePm, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa régénération de PM, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseForceVitesseAffiniteIbsutiomialgie(Tirgnonose, FibaluseForce, FibaluseVitesse, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vitesse, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseVisionPvPmVitesse(Tirgnonose, FibaluseVision, FibalusePv, FibalusePm, FibaluseVitesse):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vision, sa régénération de PV, de PM et sa vitesse."""

class TirgnonoseFibaluseVisionPvPmAffinite(Tirgnonose, FibaluseVision, FibalusePv, FibalusePm, FibaluseAffinite):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vision, sa régénération de PV, de PM et son affinité à un élément."""

class TirgnonoseFibaluseVisionPvPmIbsutiomialgie(Tirgnonose, FibaluseVision, FibalusePv, FibalusePm, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vision, sa régénération de PV, de PM et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseVisionPvVitesseAffinite(Tirgnonose, FibaluseVision, FibalusePv, FibaluseVitesse, FibaluseAffinite):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vision, sa régénération de PV, sa vitesse et son affinité à un élément."""

class TirgnonoseFibaluseVisionPvVitesseIbsutiomialgie(Tirgnonose, FibaluseVision, FibalusePv, FibaluseVitesse, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vision, sa régénération de PV, sa vitesse et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseVisionPvAffiniteIbsutiomialgie(Tirgnonose, FibaluseVision, FibalusePv, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vision, sa régénération de PV, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseVisionPmVitesseAffinite(Tirgnonose, FibaluseVision, FibalusePm, FibaluseVitesse, FibaluseAffinite):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vision, sa régénération de PM, sa vitesse et son affinité à un élément."""

class TirgnonoseFibaluseVisionPmVitesseIbsutiomialgie(Tirgnonose, FibaluseVision, FibalusePm, FibaluseVitesse, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vision, sa régénération de PM, sa vitesse et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseVisionPmAffiniteIbsutiomialgie(Tirgnonose, FibaluseVision, FibalusePm, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vision, sa régénération de PM, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseVisionVitesseAffiniteIbsutiomialgie(Tirgnonose, FibaluseVision, FibaluseVitesse, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vision, sa vitesse, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibalusePvPmVitesseAffinite(Tirgnonose, FibalusePv, FibalusePm, FibaluseVitesse, FibaluseAffinite):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa régénération de PV, de PM, sa vitesse et son affinité à un élément."""

class TirgnonoseFibalusePvPmVitesseIbsutiomialgie(Tirgnonose, FibalusePv, FibalusePm, FibaluseVitesse, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa régénération de PV, de PM, sa vitesse et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibalusePvPmAffiniteIbsutiomialgie(Tirgnonose, FibalusePv, FibalusePm, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa régénération de PV, de PM, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibalusePvVitesseAffiniteIbsutiomialgie(Tirgnonose, FibalusePv, FibaluseVitesse, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa régénération de PV, sa vitesse, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibalusePmVitesseAffiniteIbsutiomialgie(Tirgnonose, FibalusePm, FibaluseVitesse, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa régénération de PM, sa vitesse, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class FibaluseForceVisionPvPmVitesse(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePv, FibalusePm, FibaluseVitesse):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vision, sa régénération de PV, de PM et sa vitesse."""

class FibaluseForceVisionPvPmAffinite(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePv, FibalusePm, FibaluseAffinite):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vision, sa régénération de PV, de PM et son affinité à un élément."""

class FibaluseForceVisionPvPmIbsutiomialgie(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePv, FibalusePm, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vision, sa régénération de PV, de PM et peut le tuer de façon subite (ibsute)."""

class FibaluseForceVisionPvVitesseAffinite(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePv, FibaluseVitesse, FibaluseAffinite):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vision, sa régénération de PV, sa vitesse et son affinité à un élément."""

class FibaluseForceVisionPvVitesseIbsutiomialgie(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePv, FibaluseVitesse, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vision, sa régénération de PV, sa vitesse et peut le tuer de façon subite (ibsute)."""

class FibaluseForceVisionPvAffiniteIbsutiomialgie(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePv, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vision, sa régénération de PV, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class FibaluseForceVisionPmVitesseAffinite(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePm, FibaluseVitesse, FibaluseAffinite):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vision, sa régénération de PM, sa vitesse et son affinité à un élément."""

class FibaluseForceVisionPmVitesseIbsutiomialgie(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePm, FibaluseVitesse, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vision, sa régénération de PM, sa vitesse et peut le tuer de façon subite (ibsute)."""

class FibaluseForceVisionPmAffiniteIbsutiomialgie(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePm, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vision, sa régénération de PM, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class FibaluseForceVisionVitesseAffiniteIbsutiomialgie(Tirgnonose, FibaluseForce, FibaluseVision, FibaluseVitesse, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vision, sa vitesse, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class FibaluseForcePvPmVitesseAffinite(Tirgnonose, FibaluseForce, FibalusePv, FibalusePm, FibaluseVitesse, FibaluseAffinite):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa régénération de PV, de PM, sa vitesse et son affinité à un élément."""

class FibaluseForcePvPmVitesseIbsutiomialgie(Tirgnonose, FibaluseForce, FibalusePv, FibalusePm, FibaluseVitesse, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa régénération de PV, de PM, sa vitesse et peut le tuer de façon subite (ibsute)."""

class FibaluseForcePvPmAffiniteIbsutiomialgie(Tirgnonose, FibaluseForce, FibalusePv, FibalusePm, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa régénération de PV, de PM, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class FibaluseForcePvVitesseAffiniteIbsutiomialgie(Tirgnonose, FibaluseForce, FibalusePv, FibaluseVitesse, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa régénération de PV, sa vitesse, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class FibaluseForcePmVitesseAffiniteIbsutiomialgie(Tirgnonose, FibaluseForce, FibalusePm, FibaluseVitesse, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa régénération de PM, sa vitesse, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class FibaluseVisionPvPmVitesseAffinite(Tirgnonose, FibaluseVision, FibalusePv, FibalusePm, FibaluseVitesse, FibaluseAffinite):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vision, sa régénération de PV, de PM, sa vitesse et son affinité à un élément."""

class FibaluseVisionPvPmVitesseIbsutiomialgie(Tirgnonose, FibaluseVision, FibalusePv, FibalusePm, FibaluseVitesse, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vision, sa régénération de PV, de PM, sa vitesse et peut le tuer de façon subite (ibsute)."""

class FibaluseVisionPvPmAffiniteIbsutiomialgie(Tirgnonose, FibaluseVision, FibalusePv, FibalusePm, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vision, sa régénération de PV, de PM, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class FibaluseVisionPvVitesseAffiniteIbsutiomialgie(Tirgnonose, FibaluseVision, FibalusePv, FibaluseVitesse, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vision, sa régénération de PV, sa vitesse, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class FibaluseVisionPmVitesseAffiniteIbsutiomialgie(Tirgnonose, FibaluseVision, FibalusePm, FibaluseVitesse, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vision, sa régénération de PM, sa vitesse, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class FibalusePvPmVitesseAffiniteIbsutiomialgie(Tirgnonose, FibalusePv, FibalusePm, FibaluseVitesse, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa régénération de PV, de PM, sa vitesse, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseForceVisionPvPmVitesse(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePv, FibalusePm, FibaluseVitesse):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vision, sa régénération de PV, de PM et sa vitesse."""

class TirgnonoseFibaluseForceVisionPvPmAffinite(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePv, FibalusePm, FibaluseAffinite):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vision, sa régénération de PV, de PM et son affinité à un élément."""

class TirgnonoseFibaluseForceVisionPvPmIbsutiomialgie(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePv, FibalusePm, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vision, sa régénération de PV, de PM et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseForceVisionPvVitesseAffinite(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePv, FibaluseVitesse, FibaluseAffinite):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vision, sa régénération de PV, sa vitesse et son affinité à un élément."""

class TirgnonoseFibaluseForceVisionPvVitesseIbsutiomialgie(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePv, FibaluseVitesse, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vision, sa régénération de PV, sa vitesse et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseForceVisionPvAffiniteIbsutiomialgie(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePv, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vision, sa régénération de PV, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseForceVisionPmVitesseAffinite(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePm, FibaluseVitesse, FibaluseAffinite):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vision, sa régénération de PM, sa vitesse et son affinité à un élément."""

class TirgnonoseFibaluseForceVisionPmVitesseIbsutiomialgie(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePm, FibaluseVitesse, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vision, sa régénération de PM, sa vitesse et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseForceVisionPmAffiniteIbsutiomialgie(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePm, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vision, sa régénération de PM, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseForceVisionVitesseAffiniteIbsutiomialgie(Tirgnonose, FibaluseForce, FibaluseVision, FibaluseVitesse, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vision, sa vitesse, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseForcePvPmVitesseAffinite(Tirgnonose, FibaluseForce, FibalusePv, FibalusePm, FibaluseVitesse, FibaluseAffinite):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa régénération de PV, de PM, sa vitesse et son affinité à un élément."""

class TirgnonoseFibaluseForcePvPmVitesseIbsutiomialgie(Tirgnonose, FibaluseForce, FibalusePv, FibalusePm, FibaluseVitesse, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa régénération de PV, de PM, sa vitesse et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseForcePvPmAffiniteIbsutiomialgie(Tirgnonose, FibaluseForce, FibalusePv, FibalusePm, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa régénération de PV, de PM, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseForcePvVitesseAffiniteIbsutiomialgie(Tirgnonose, FibaluseForce, FibalusePv, FibaluseVitesse, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa régénération de PV, sa vitesse, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseForcePmVitesseAffiniteIbsutiomialgie(Tirgnonose, FibaluseForce, FibalusePm, FibaluseVitesse, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa régénération de PM, sa vitesse, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseVisionPvPmVitesseAffinite(Tirgnonose, FibaluseVision, FibalusePv, FibalusePm, FibaluseVitesse, FibaluseAffinite):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vision, sa régénération de PV, de PM, sa vitesse et son affinité à un élément."""

class TirgnonoseFibaluseVisionPvPmVitesseIbsutiomialgie(Tirgnonose, FibaluseVision, FibalusePv, FibalusePm, FibaluseVitesse, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vision, sa régénération de PV, de PM, sa vitesse et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseVisionPvPmAffiniteIbsutiomialgie(Tirgnonose, FibaluseVision, FibalusePv, FibalusePm, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vision, sa régénération de PV, de PM, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseVisionPvVitesseAffiniteIbsutiomialgie(Tirgnonose, FibaluseVision, FibalusePv, FibaluseVitesse, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vision, sa régénération de PV, sa vitesse, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseVisionPmVitesseAffiniteIbsutiomialgie(Tirgnonose, FibaluseVision, FibalusePm, FibaluseVitesse, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vision, sa régénération de PM, sa vitesse, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibalusePvPmVitesseAffiniteIbsutiomialgie(Tirgnonose, FibalusePv, FibalusePm, FibaluseVitesse, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa régénération de PV, de PM, sa vitesse, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class FibaluseForceVisionPvPmVitesseAffinite(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePv, FibalusePm, FibaluseVitesse, FibaluseAffinite):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vision, sa régénération de PV, de PM, sa vitesse et son affinité à un élément."""

class FibaluseForceVisionPvPmVitesseIbsutiomialgie(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePv, FibalusePm, FibaluseVitesse, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vision, sa régénération de PV, de PM, sa vitesse et peut le tuer de façon subite (ibsute)."""

class FibaluseForceVisionPvPmAffiniteIbsutiomialgie(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePv, FibalusePm, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vision, sa régénération de PV, de PM, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class FibaluseForceVisionPvVitesseAffiniteIbsutiomialgie(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePv, FibaluseVitesse, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vision, sa régénération de PV, sa vitesse, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class FibaluseForceVisionPmVitesseAffiniteIbsutiomialgie(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePm, FibaluseVitesse, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vision, sa régénération de PM, sa vitesse, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class FibaluseForcePvPmVitesseAffiniteIbsutiomialgie(Tirgnonose, FibaluseForce, FibalusePv, FibalusePm, FibaluseVitesse, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa régénération de PV, de PM, sa vitesse, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class FibaluseVisionPvPmVitesseAffiniteIbsutiomialgie(Tirgnonose, FibaluseVision, FibalusePv, FibalusePm, FibaluseVitesse, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vision, sa régénération de PV, de PM, sa vitesse, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseForceVisionPvPmVitesseAffinite(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePv, FibalusePm, FibaluseVitesse, FibaluseAffinite):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vision, sa régénération de PV, de PM, sa vitesse et son affinité à un élément."""

class TirgnonoseFibaluseForceVisionPvPmVitesseIbsutiomialgie(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePv, FibalusePm, FibaluseVitesse, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vision, sa régénération de PV, de PM, sa vitesse et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseForceVisionPvPmAffiniteIbsutiomialgie(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePv, FibalusePm, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vision, sa régénération de PV, de PM, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseForceVisionPvVitesseAffiniteIbsutiomialgie(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePv, FibaluseVitesse, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vision, sa régénération de PV, sa vitesse, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseForceVisionPmVitesseAffiniteIbsutiomialgie(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePm, FibaluseVitesse, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vision, sa régénération de PM, sa vitesse, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseForcePvPmVitesseAffiniteIbsutiomialgie(Tirgnonose, FibaluseForce, FibalusePv, FibalusePm, FibaluseVitesse, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa régénération de PV, de PM, sa vitesse, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseVisionPvPmVitesseAffiniteIbsutiomialgie(Tirgnonose, FibaluseVision, FibalusePv, FibalusePm, FibaluseVitesse, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vision, sa régénération de PV, de PM, sa vitesse, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class FibaluseForceVisionPvPmVitesseAffiniteIbsutiomialgie(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePv, FibalusePm, FibaluseVitesse, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vision, sa régénération de PV, de PM, sa vitesse, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseForceVisionPvPmVitesseAffiniteIbsutiomialgie(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePv, FibalusePm, FibaluseVitesse, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vision, sa régénération de PV, de PM, sa vitesse, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

maladies: dict[tuple[bool, bool, bool, bool, bool, bool, bool, bool, bool], type[Maladie]] = {
    (False, False, False, False, False, False, False, False, False): Maladie,
    (True, False, False, False, False, False, False, False, False): Tirgnonose,
    (False, True, False, False, False, False, False, False, False): Fibaluse,
    (True, True, False, False, False, False, False, False, False): TirgnonoseFibaluse,
    (False, False, True, False, False, False, False, False, False): FibaluseForce,
    (True, False, True, False, False, False, False, False, False): TirgnonoseFibaluseForce,
    (False, True, True, False, False, False, False, False, False): Maladie,
    (True, True, True, False, False, False, False, False, False): Maladie,
    (False, False, False, True, False, False, False, False, False): FibaluseVision,
    (True, False, False, True, False, False, False, False, False): TirgnonoseFibaluseVision,
    (False, True, False, True, False, False, False, False, False): Maladie,
    (True, True, False, True, False, False, False, False, False): Maladie,
    (False, False, True, True, False, False, False, False, False): FibaluseForceVision,
    (True, False, True, True, False, False, False, False, False): TirgnonoseFibaluseForceVision,
    (False, True, True, True, False, False, False, False, False): Maladie,
    (True, True, True, True, False, False, False, False, False): Maladie,
    (False, False, False, False, True, False, False, False, False): FibalusePv,
    (True, False, False, False, True, False, False, False, False): TirgnonoseFibalusePv,
    (False, True, False, False, True, False, False, False, False): Maladie,
    (True, True, False, False, True, False, False, False, False): Maladie,
    (False, False, True, False, True, False, False, False, False): FibaluseForcePv,
    (True, False, True, False, True, False, False, False, False): TirgnonoseFibaluseForcePv,
    (False, True, True, False, True, False, False, False, False): Maladie,
    (True, True, True, False, True, False, False, False, False): Maladie,
    (False, False, False, True, True, False, False, False, False): FibaluseVisionPv,
    (True, False, False, True, True, False, False, False, False): TirgnonoseFibaluseVisionPv,
    (False, True, False, True, True, False, False, False, False): Maladie,
    (True, True, False, True, True, False, False, False, False): Maladie,
    (False, False, True, True, True, False, False, False, False): FibaluseForceVisionPv,
    (True, False, True, True, True, False, False, False, False): TirgnonoseFibaluseForceVisionPv,
    (False, True, True, True, True, False, False, False, False): Maladie,
    (True, True, True, True, True, False, False, False, False): Maladie,
    (False, False, False, False, False, True, False, False, False): FibalusePm,
    (True, False, False, False, False, True, False, False, False): TirgnonoseFibalusePm,
    (False, True, False, False, False, True, False, False, False): Maladie,
    (True, True, False, False, False, True, False, False, False): Maladie,
    (False, False, True, False, False, True, False, False, False): FibaluseForcePm,
    (True, False, True, False, False, True, False, False, False): TirgnonoseFibaluseForcePm,
    (False, True, True, False, False, True, False, False, False): Maladie,
    (True, True, True, False, False, True, False, False, False): Maladie,
    (False, False, False, True, False, True, False, False, False): FibaluseVisionPm,
    (True, False, False, True, False, True, False, False, False): TirgnonoseFibaluseVisionPm,
    (False, True, False, True, False, True, False, False, False): Maladie,
    (True, True, False, True, False, True, False, False, False): Maladie,
    (False, False, True, True, False, True, False, False, False): FibaluseForceVisionPm,
    (True, False, True, True, False, True, False, False, False): TirgnonoseFibaluseForceVisionPm,
    (False, True, True, True, False, True, False, False, False): Maladie,
    (True, True, True, True, False, True, False, False, False): Maladie,
    (False, False, False, False, True, True, False, False, False): FibalusePvPm,
    (True, False, False, False, True, True, False, False, False): TirgnonoseFibalusePvPm,
    (False, True, False, False, True, True, False, False, False): Maladie,
    (True, True, False, False, True, True, False, False, False): Maladie,
    (False, False, True, False, True, True, False, False, False): FibaluseForcePvPm,
    (True, False, True, False, True, True, False, False, False): TirgnonoseFibaluseForcePvPm,
    (False, True, True, False, True, True, False, False, False): Maladie,
    (True, True, True, False, True, True, False, False, False): Maladie,
    (False, False, False, True, True, True, False, False, False): FibaluseVisionPvPm,
    (True, False, False, True, True, True, False, False, False): TirgnonoseFibaluseVisionPvPm,
    (False, True, False, True, True, True, False, False, False): Maladie,
    (True, True, False, True, True, True, False, False, False): Maladie,
    (False, False, True, True, True, True, False, False, False): FibaluseForceVisionPvPm,
    (True, False, True, True, True, True, False, False, False): TirgnonoseFibaluseForceVisionPvPm,
    (False, True, True, True, True, True, False, False, False): Maladie,
    (True, True, True, True, True, True, False, False, False): Maladie,
    (False, False, False, False, False, False, True, False, False): FibaluseVitesse,
    (True, False, False, False, False, False, True, False, False): TirgnonoseFibaluseVitesse,
    (False, True, False, False, False, False, True, False, False): Maladie,
    (True, True, False, False, False, False, True, False, False): Maladie,
    (False, False, True, False, False, False, True, False, False): FibaluseForceVitesse,
    (True, False, True, False, False, False, True, False, False): TirgnonoseFibaluseForceVitesse,
    (False, True, True, False, False, False, True, False, False): Maladie,
    (True, True, True, False, False, False, True, False, False): Maladie,
    (False, False, False, True, False, False, True, False, False): FibaluseVisionVitesse,
    (True, False, False, True, False, False, True, False, False): TirgnonoseFibaluseVisionVitesse,
    (False, True, False, True, False, False, True, False, False): Maladie,
    (True, True, False, True, False, False, True, False, False): Maladie,
    (False, False, True, True, False, False, True, False, False): FibaluseForceVisionVitesse,
    (True, False, True, True, False, False, True, False, False): TirgnonoseFibaluseForceVisionVitesse,
    (False, True, True, True, False, False, True, False, False): Maladie,
    (True, True, True, True, False, False, True, False, False): Maladie,
    (False, False, False, False, True, False, True, False, False): FibalusePvVitesse,
    (True, False, False, False, True, False, True, False, False): TirgnonoseFibalusePvVitesse,
    (False, True, False, False, True, False, True, False, False): Maladie,
    (True, True, False, False, True, False, True, False, False): Maladie,
    (False, False, True, False, True, False, True, False, False): FibaluseForcePvVitesse,
    (True, False, True, False, True, False, True, False, False): TirgnonoseFibaluseForcePvVitesse,
    (False, True, True, False, True, False, True, False, False): Maladie,
    (True, True, True, False, True, False, True, False, False): Maladie,
    (False, False, False, True, True, False, True, False, False): FibaluseVisionPvVitesse,
    (True, False, False, True, True, False, True, False, False): TirgnonoseFibaluseVisionPvVitesse,
    (False, True, False, True, True, False, True, False, False): Maladie,
    (True, True, False, True, True, False, True, False, False): Maladie,
    (False, False, True, True, True, False, True, False, False): FibaluseForceVisionPvVitesse,
    (True, False, True, True, True, False, True, False, False): TirgnonoseFibaluseForceVisionPvVitesse,
    (False, True, True, True, True, False, True, False, False): Maladie,
    (True, True, True, True, True, False, True, False, False): Maladie,
    (False, False, False, False, False, True, True, False, False): FibalusePmVitesse,
    (True, False, False, False, False, True, True, False, False): TirgnonoseFibalusePmVitesse,
    (False, True, False, False, False, True, True, False, False): Maladie,
    (True, True, False, False, False, True, True, False, False): Maladie,
    (False, False, True, False, False, True, True, False, False): FibaluseForcePmVitesse,
    (True, False, True, False, False, True, True, False, False): TirgnonoseFibaluseForcePmVitesse,
    (False, True, True, False, False, True, True, False, False): Maladie,
    (True, True, True, False, False, True, True, False, False): Maladie,
    (False, False, False, True, False, True, True, False, False): FibaluseVisionPmVitesse,
    (True, False, False, True, False, True, True, False, False): TirgnonoseFibaluseVisionPmVitesse,
    (False, True, False, True, False, True, True, False, False): Maladie,
    (True, True, False, True, False, True, True, False, False): Maladie,
    (False, False, True, True, False, True, True, False, False): FibaluseForceVisionPmVitesse,
    (True, False, True, True, False, True, True, False, False): TirgnonoseFibaluseForceVisionPmVitesse,
    (False, True, True, True, False, True, True, False, False): Maladie,
    (True, True, True, True, False, True, True, False, False): Maladie,
    (False, False, False, False, True, True, True, False, False): FibalusePvPmVitesse,
    (True, False, False, False, True, True, True, False, False): TirgnonoseFibalusePvPmVitesse,
    (False, True, False, False, True, True, True, False, False): Maladie,
    (True, True, False, False, True, True, True, False, False): Maladie,
    (False, False, True, False, True, True, True, False, False): FibaluseForcePvPmVitesse,
    (True, False, True, False, True, True, True, False, False): TirgnonoseFibaluseForcePvPmVitesse,
    (False, True, True, False, True, True, True, False, False): Maladie,
    (True, True, True, False, True, True, True, False, False): Maladie,
    (False, False, False, True, True, True, True, False, False): FibaluseVisionPvPmVitesse,
    (True, False, False, True, True, True, True, False, False): TirgnonoseFibaluseVisionPvPmVitesse,
    (False, True, False, True, True, True, True, False, False): Maladie,
    (True, True, False, True, True, True, True, False, False): Maladie,
    (False, False, True, True, True, True, True, False, False): FibaluseForceVisionPvPmVitesse,
    (True, False, True, True, True, True, True, False, False): TirgnonoseFibaluseForceVisionPvPmVitesse,
    (False, True, True, True, True, True, True, False, False): Maladie,
    (True, True, True, True, True, True, True, False, False): Maladie,
    (False, False, False, False, False, False, False, True, False): FibaluseAffinite,
    (True, False, False, False, False, False, False, True, False): TirgnonoseFibaluseAffinite,
    (False, True, False, False, False, False, False, True, False): Maladie,
    (True, True, False, False, False, False, False, True, False): Maladie,
    (False, False, True, False, False, False, False, True, False): FibaluseForceAffinite,
    (True, False, True, False, False, False, False, True, False): TirgnonoseFibaluseForceAffinite,
    (False, True, True, False, False, False, False, True, False): Maladie,
    (True, True, True, False, False, False, False, True, False): Maladie,
    (False, False, False, True, False, False, False, True, False): FibaluseVisionAffinite,
    (True, False, False, True, False, False, False, True, False): TirgnonoseFibaluseVisionAffinite,
    (False, True, False, True, False, False, False, True, False): Maladie,
    (True, True, False, True, False, False, False, True, False): Maladie,
    (False, False, True, True, False, False, False, True, False): FibaluseForceVisionAffinite,
    (True, False, True, True, False, False, False, True, False): TirgnonoseFibaluseForceVisionAffinite,
    (False, True, True, True, False, False, False, True, False): Maladie,
    (True, True, True, True, False, False, False, True, False): Maladie,
    (False, False, False, False, True, False, False, True, False): FibalusePvAffinite,
    (True, False, False, False, True, False, False, True, False): TirgnonoseFibalusePvAffinite,
    (False, True, False, False, True, False, False, True, False): Maladie,
    (True, True, False, False, True, False, False, True, False): Maladie,
    (False, False, True, False, True, False, False, True, False): FibaluseForcePvAffinite,
    (True, False, True, False, True, False, False, True, False): TirgnonoseFibaluseForcePvAffinite,
    (False, True, True, False, True, False, False, True, False): Maladie,
    (True, True, True, False, True, False, False, True, False): Maladie,
    (False, False, False, True, True, False, False, True, False): FibaluseVisionPvAffinite,
    (True, False, False, True, True, False, False, True, False): TirgnonoseFibaluseVisionPvAffinite,
    (False, True, False, True, True, False, False, True, False): Maladie,
    (True, True, False, True, True, False, False, True, False): Maladie,
    (False, False, True, True, True, False, False, True, False): FibaluseForceVisionPvAffinite,
    (True, False, True, True, True, False, False, True, False): TirgnonoseFibaluseForceVisionPvAffinite,
    (False, True, True, True, True, False, False, True, False): Maladie,
    (True, True, True, True, True, False, False, True, False): Maladie,
    (False, False, False, False, False, True, False, True, False): FibalusePmAffinite,
    (True, False, False, False, False, True, False, True, False): TirgnonoseFibalusePmAffinite,
    (False, True, False, False, False, True, False, True, False): Maladie,
    (True, True, False, False, False, True, False, True, False): Maladie,
    (False, False, True, False, False, True, False, True, False): FibaluseForcePmAffinite,
    (True, False, True, False, False, True, False, True, False): TirgnonoseFibaluseForcePmAffinite,
    (False, True, True, False, False, True, False, True, False): Maladie,
    (True, True, True, False, False, True, False, True, False): Maladie,
    (False, False, False, True, False, True, False, True, False): FibaluseVisionPmAffinite,
    (True, False, False, True, False, True, False, True, False): TirgnonoseFibaluseVisionPmAffinite,
    (False, True, False, True, False, True, False, True, False): Maladie,
    (True, True, False, True, False, True, False, True, False): Maladie,
    (False, False, True, True, False, True, False, True, False): FibaluseForceVisionPmAffinite,
    (True, False, True, True, False, True, False, True, False): TirgnonoseFibaluseForceVisionPmAffinite,
    (False, True, True, True, False, True, False, True, False): Maladie,
    (True, True, True, True, False, True, False, True, False): Maladie,
    (False, False, False, False, True, True, False, True, False): FibalusePvPmAffinite,
    (True, False, False, False, True, True, False, True, False): TirgnonoseFibalusePvPmAffinite,
    (False, True, False, False, True, True, False, True, False): Maladie,
    (True, True, False, False, True, True, False, True, False): Maladie,
    (False, False, True, False, True, True, False, True, False): FibaluseForcePvPmAffinite,
    (True, False, True, False, True, True, False, True, False): TirgnonoseFibaluseForcePvPmAffinite,
    (False, True, True, False, True, True, False, True, False): Maladie,
    (True, True, True, False, True, True, False, True, False): Maladie,
    (False, False, False, True, True, True, False, True, False): FibaluseVisionPvPmAffinite,
    (True, False, False, True, True, True, False, True, False): TirgnonoseFibaluseVisionPvPmAffinite,
    (False, True, False, True, True, True, False, True, False): Maladie,
    (True, True, False, True, True, True, False, True, False): Maladie,
    (False, False, True, True, True, True, False, True, False): FibaluseForceVisionPvPmAffinite,
    (True, False, True, True, True, True, False, True, False): TirgnonoseFibaluseForceVisionPvPmAffinite,
    (False, True, True, True, True, True, False, True, False): Maladie,
    (True, True, True, True, True, True, False, True, False): Maladie,
    (False, False, False, False, False, False, True, True, False): FibaluseVitesseAffinite,
    (True, False, False, False, False, False, True, True, False): TirgnonoseFibaluseVitesseAffinite,
    (False, True, False, False, False, False, True, True, False): Maladie,
    (True, True, False, False, False, False, True, True, False): Maladie,
    (False, False, True, False, False, False, True, True, False): FibaluseForceVitesseAffinite,
    (True, False, True, False, False, False, True, True, False): TirgnonoseFibaluseForceVitesseAffinite,
    (False, True, True, False, False, False, True, True, False): Maladie,
    (True, True, True, False, False, False, True, True, False): Maladie,
    (False, False, False, True, False, False, True, True, False): FibaluseVisionVitesseAffinite,
    (True, False, False, True, False, False, True, True, False): TirgnonoseFibaluseVisionVitesseAffinite,
    (False, True, False, True, False, False, True, True, False): Maladie,
    (True, True, False, True, False, False, True, True, False): Maladie,
    (False, False, True, True, False, False, True, True, False): FibaluseForceVisionVitesseAffinite,
    (True, False, True, True, False, False, True, True, False): TirgnonoseFibaluseForceVisionVitesseAffinite,
    (False, True, True, True, False, False, True, True, False): Maladie,
    (True, True, True, True, False, False, True, True, False): Maladie,
    (False, False, False, False, True, False, True, True, False): FibalusePvVitesseAffinite,
    (True, False, False, False, True, False, True, True, False): TirgnonoseFibalusePvVitesseAffinite,
    (False, True, False, False, True, False, True, True, False): Maladie,
    (True, True, False, False, True, False, True, True, False): Maladie,
    (False, False, True, False, True, False, True, True, False): FibaluseForcePvVitesseAffinite,
    (True, False, True, False, True, False, True, True, False): TirgnonoseFibaluseForcePvVitesseAffinite,
    (False, True, True, False, True, False, True, True, False): Maladie,
    (True, True, True, False, True, False, True, True, False): Maladie,
    (False, False, False, True, True, False, True, True, False): FibaluseVisionPvVitesseAffinite,
    (True, False, False, True, True, False, True, True, False): TirgnonoseFibaluseVisionPvVitesseAffinite,
    (False, True, False, True, True, False, True, True, False): Maladie,
    (True, True, False, True, True, False, True, True, False): Maladie,
    (False, False, True, True, True, False, True, True, False): FibaluseForceVisionPvVitesseAffinite,
    (True, False, True, True, True, False, True, True, False): TirgnonoseFibaluseForceVisionPvVitesseAffinite,
    (False, True, True, True, True, False, True, True, False): Maladie,
    (True, True, True, True, True, False, True, True, False): Maladie,
    (False, False, False, False, False, True, True, True, False): FibalusePmVitesseAffinite,
    (True, False, False, False, False, True, True, True, False): TirgnonoseFibalusePmVitesseAffinite,
    (False, True, False, False, False, True, True, True, False): Maladie,
    (True, True, False, False, False, True, True, True, False): Maladie,
    (False, False, True, False, False, True, True, True, False): FibaluseForcePmVitesseAffinite,
    (True, False, True, False, False, True, True, True, False): TirgnonoseFibaluseForcePmVitesseAffinite,
    (False, True, True, False, False, True, True, True, False): Maladie,
    (True, True, True, False, False, True, True, True, False): Maladie,
    (False, False, False, True, False, True, True, True, False): FibaluseVisionPmVitesseAffinite,
    (True, False, False, True, False, True, True, True, False): TirgnonoseFibaluseVisionPmVitesseAffinite,
    (False, True, False, True, False, True, True, True, False): Maladie,
    (True, True, False, True, False, True, True, True, False): Maladie,
    (False, False, True, True, False, True, True, True, False): FibaluseForceVisionPmVitesseAffinite,
    (True, False, True, True, False, True, True, True, False): TirgnonoseFibaluseForceVisionPmVitesseAffinite,
    (False, True, True, True, False, True, True, True, False): Maladie,
    (True, True, True, True, False, True, True, True, False): Maladie,
    (False, False, False, False, True, True, True, True, False): FibalusePvPmVitesseAffinite,
    (True, False, False, False, True, True, True, True, False): TirgnonoseFibalusePvPmVitesseAffinite,
    (False, True, False, False, True, True, True, True, False): Maladie,
    (True, True, False, False, True, True, True, True, False): Maladie,
    (False, False, True, False, True, True, True, True, False): FibaluseForcePvPmVitesseAffinite,
    (True, False, True, False, True, True, True, True, False): TirgnonoseFibaluseForcePvPmVitesseAffinite,
    (False, True, True, False, True, True, True, True, False): Maladie,
    (True, True, True, False, True, True, True, True, False): Maladie,
    (False, False, False, True, True, True, True, True, False): FibaluseVisionPvPmVitesseAffinite,
    (True, False, False, True, True, True, True, True, False): TirgnonoseFibaluseVisionPvPmVitesseAffinite,
    (False, True, False, True, True, True, True, True, False): Maladie,
    (True, True, False, True, True, True, True, True, False): Maladie,
    (False, False, True, True, True, True, True, True, False): FibaluseForceVisionPvPmVitesseAffinite,
    (True, False, True, True, True, True, True, True, False): TirgnonoseFibaluseForceVisionPvPmVitesseAffinite,
    (False, True, True, True, True, True, True, True, False): Maladie,
    (True, True, True, True, True, True, True, True, False): Maladie,
    (False, False, False, False, False, False, False, False, True): Ibsutiomialgie,
    (True, False, False, False, False, False, False, False, True): TirgnonoseIbsutiomialgie,
    (False, True, False, False, False, False, False, False, True): FibaluseIbsutiomialgie,
    (True, True, False, False, False, False, False, False, True): TirgnonoseFibaluseIbsutiomialgie,
    (False, False, True, False, False, False, False, False, True): FibaluseForceIbsutiomialgie,
    (True, False, True, False, False, False, False, False, True): TirgnonoseFibaluseForceIbsutiomialgie,
    (False, True, True, False, False, False, False, False, True): Maladie,
    (True, True, True, False, False, False, False, False, True): Maladie,
    (False, False, False, True, False, False, False, False, True): FibaluseVisionIbsutiomialgie,
    (True, False, False, True, False, False, False, False, True): TirgnonoseFibaluseVisionIbsutiomialgie,
    (False, True, False, True, False, False, False, False, True): Maladie,
    (True, True, False, True, False, False, False, False, True): Maladie,
    (False, False, True, True, False, False, False, False, True): FibaluseForceVisionIbsutiomialgie,
    (True, False, True, True, False, False, False, False, True): TirgnonoseFibaluseForceVisionIbsutiomialgie,
    (False, True, True, True, False, False, False, False, True): Maladie,
    (True, True, True, True, False, False, False, False, True): Maladie,
    (False, False, False, False, True, False, False, False, True): FibalusePvIbsutiomialgie,
    (True, False, False, False, True, False, False, False, True): TirgnonoseFibalusePvIbsutiomialgie,
    (False, True, False, False, True, False, False, False, True): Maladie,
    (True, True, False, False, True, False, False, False, True): Maladie,
    (False, False, True, False, True, False, False, False, True): FibaluseForcePvIbsutiomialgie,
    (True, False, True, False, True, False, False, False, True): TirgnonoseFibaluseForcePvIbsutiomialgie,
    (False, True, True, False, True, False, False, False, True): Maladie,
    (True, True, True, False, True, False, False, False, True): Maladie,
    (False, False, False, True, True, False, False, False, True): FibaluseVisionPvIbsutiomialgie,
    (True, False, False, True, True, False, False, False, True): TirgnonoseFibaluseVisionPvIbsutiomialgie,
    (False, True, False, True, True, False, False, False, True): Maladie,
    (True, True, False, True, True, False, False, False, True): Maladie,
    (False, False, True, True, True, False, False, False, True): FibaluseForceVisionPvIbsutiomialgie,
    (True, False, True, True, True, False, False, False, True): TirgnonoseFibaluseForceVisionPvIbsutiomialgie,
    (False, True, True, True, True, False, False, False, True): Maladie,
    (True, True, True, True, True, False, False, False, True): Maladie,
    (False, False, False, False, False, True, False, False, True): FibalusePmIbsutiomialgie,
    (True, False, False, False, False, True, False, False, True): TirgnonoseFibalusePmIbsutiomialgie,
    (False, True, False, False, False, True, False, False, True): Maladie,
    (True, True, False, False, False, True, False, False, True): Maladie,
    (False, False, True, False, False, True, False, False, True): FibaluseForcePmIbsutiomialgie,
    (True, False, True, False, False, True, False, False, True): TirgnonoseFibaluseForcePmIbsutiomialgie,
    (False, True, True, False, False, True, False, False, True): Maladie,
    (True, True, True, False, False, True, False, False, True): Maladie,
    (False, False, False, True, False, True, False, False, True): FibaluseVisionPmIbsutiomialgie,
    (True, False, False, True, False, True, False, False, True): TirgnonoseFibaluseVisionPmIbsutiomialgie,
    (False, True, False, True, False, True, False, False, True): Maladie,
    (True, True, False, True, False, True, False, False, True): Maladie,
    (False, False, True, True, False, True, False, False, True): FibaluseForceVisionPmIbsutiomialgie,
    (True, False, True, True, False, True, False, False, True): TirgnonoseFibaluseForceVisionPmIbsutiomialgie,
    (False, True, True, True, False, True, False, False, True): Maladie,
    (True, True, True, True, False, True, False, False, True): Maladie,
    (False, False, False, False, True, True, False, False, True): FibalusePvPmIbsutiomialgie,
    (True, False, False, False, True, True, False, False, True): TirgnonoseFibalusePvPmIbsutiomialgie,
    (False, True, False, False, True, True, False, False, True): Maladie,
    (True, True, False, False, True, True, False, False, True): Maladie,
    (False, False, True, False, True, True, False, False, True): FibaluseForcePvPmIbsutiomialgie,
    (True, False, True, False, True, True, False, False, True): TirgnonoseFibaluseForcePvPmIbsutiomialgie,
    (False, True, True, False, True, True, False, False, True): Maladie,
    (True, True, True, False, True, True, False, False, True): Maladie,
    (False, False, False, True, True, True, False, False, True): FibaluseVisionPvPmIbsutiomialgie,
    (True, False, False, True, True, True, False, False, True): TirgnonoseFibaluseVisionPvPmIbsutiomialgie,
    (False, True, False, True, True, True, False, False, True): Maladie,
    (True, True, False, True, True, True, False, False, True): Maladie,
    (False, False, True, True, True, True, False, False, True): FibaluseForceVisionPvPmIbsutiomialgie,
    (True, False, True, True, True, True, False, False, True): TirgnonoseFibaluseForceVisionPvPmIbsutiomialgie,
    (False, True, True, True, True, True, False, False, True): Maladie,
    (True, True, True, True, True, True, False, False, True): Maladie,
    (False, False, False, False, False, False, True, False, True): FibaluseVitesseIbsutiomialgie,
    (True, False, False, False, False, False, True, False, True): TirgnonoseFibaluseVitesseIbsutiomialgie,
    (False, True, False, False, False, False, True, False, True): Maladie,
    (True, True, False, False, False, False, True, False, True): Maladie,
    (False, False, True, False, False, False, True, False, True): FibaluseForceVitesseIbsutiomialgie,
    (True, False, True, False, False, False, True, False, True): TirgnonoseFibaluseForceVitesseIbsutiomialgie,
    (False, True, True, False, False, False, True, False, True): Maladie,
    (True, True, True, False, False, False, True, False, True): Maladie,
    (False, False, False, True, False, False, True, False, True): FibaluseVisionVitesseIbsutiomialgie,
    (True, False, False, True, False, False, True, False, True): TirgnonoseFibaluseVisionVitesseIbsutiomialgie,
    (False, True, False, True, False, False, True, False, True): Maladie,
    (True, True, False, True, False, False, True, False, True): Maladie,
    (False, False, True, True, False, False, True, False, True): FibaluseForceVisionVitesseIbsutiomialgie,
    (True, False, True, True, False, False, True, False, True): TirgnonoseFibaluseForceVisionVitesseIbsutiomialgie,
    (False, True, True, True, False, False, True, False, True): Maladie,
    (True, True, True, True, False, False, True, False, True): Maladie,
    (False, False, False, False, True, False, True, False, True): FibalusePvVitesseIbsutiomialgie,
    (True, False, False, False, True, False, True, False, True): TirgnonoseFibalusePvVitesseIbsutiomialgie,
    (False, True, False, False, True, False, True, False, True): Maladie,
    (True, True, False, False, True, False, True, False, True): Maladie,
    (False, False, True, False, True, False, True, False, True): FibaluseForcePvVitesseIbsutiomialgie,
    (True, False, True, False, True, False, True, False, True): TirgnonoseFibaluseForcePvVitesseIbsutiomialgie,
    (False, True, True, False, True, False, True, False, True): Maladie,
    (True, True, True, False, True, False, True, False, True): Maladie,
    (False, False, False, True, True, False, True, False, True): FibaluseVisionPvVitesseIbsutiomialgie,
    (True, False, False, True, True, False, True, False, True): TirgnonoseFibaluseVisionPvVitesseIbsutiomialgie,
    (False, True, False, True, True, False, True, False, True): Maladie,
    (True, True, False, True, True, False, True, False, True): Maladie,
    (False, False, True, True, True, False, True, False, True): FibaluseForceVisionPvVitesseIbsutiomialgie,
    (True, False, True, True, True, False, True, False, True): TirgnonoseFibaluseForceVisionPvVitesseIbsutiomialgie,
    (False, True, True, True, True, False, True, False, True): Maladie,
    (True, True, True, True, True, False, True, False, True): Maladie,
    (False, False, False, False, False, True, True, False, True): FibalusePmVitesseIbsutiomialgie,
    (True, False, False, False, False, True, True, False, True): TirgnonoseFibalusePmVitesseIbsutiomialgie,
    (False, True, False, False, False, True, True, False, True): Maladie,
    (True, True, False, False, False, True, True, False, True): Maladie,
    (False, False, True, False, False, True, True, False, True): FibaluseForcePmVitesseIbsutiomialgie,
    (True, False, True, False, False, True, True, False, True): TirgnonoseFibaluseForcePmVitesseIbsutiomialgie,
    (False, True, True, False, False, True, True, False, True): Maladie,
    (True, True, True, False, False, True, True, False, True): Maladie,
    (False, False, False, True, False, True, True, False, True): FibaluseVisionPmVitesseIbsutiomialgie,
    (True, False, False, True, False, True, True, False, True): TirgnonoseFibaluseVisionPmVitesseIbsutiomialgie,
    (False, True, False, True, False, True, True, False, True): Maladie,
    (True, True, False, True, False, True, True, False, True): Maladie,
    (False, False, True, True, False, True, True, False, True): FibaluseForceVisionPmVitesseIbsutiomialgie,
    (True, False, True, True, False, True, True, False, True): TirgnonoseFibaluseForceVisionPmVitesseIbsutiomialgie,
    (False, True, True, True, False, True, True, False, True): Maladie,
    (True, True, True, True, False, True, True, False, True): Maladie,
    (False, False, False, False, True, True, True, False, True): FibalusePvPmVitesseIbsutiomialgie,
    (True, False, False, False, True, True, True, False, True): TirgnonoseFibalusePvPmVitesseIbsutiomialgie,
    (False, True, False, False, True, True, True, False, True): Maladie,
    (True, True, False, False, True, True, True, False, True): Maladie,
    (False, False, True, False, True, True, True, False, True): FibaluseForcePvPmVitesseIbsutiomialgie,
    (True, False, True, False, True, True, True, False, True): TirgnonoseFibaluseForcePvPmVitesseIbsutiomialgie,
    (False, True, True, False, True, True, True, False, True): Maladie,
    (True, True, True, False, True, True, True, False, True): Maladie,
    (False, False, False, True, True, True, True, False, True): FibaluseVisionPvPmVitesseIbsutiomialgie,
    (True, False, False, True, True, True, True, False, True): TirgnonoseFibaluseVisionPvPmVitesseIbsutiomialgie,
    (False, True, False, True, True, True, True, False, True): Maladie,
    (True, True, False, True, True, True, True, False, True): Maladie,
    (False, False, True, True, True, True, True, False, True): FibaluseForceVisionPvPmVitesseIbsutiomialgie,
    (True, False, True, True, True, True, True, False, True): TirgnonoseFibaluseForceVisionPvPmVitesseIbsutiomialgie,
    (False, True, True, True, True, True, True, False, True): Maladie,
    (True, True, True, True, True, True, True, False, True): Maladie,
    (False, False, False, False, False, False, False, True, True): FibaluseAffiniteIbsutiomialgie,
    (True, False, False, False, False, False, False, True, True): TirgnonoseFibaluseAffiniteIbsutiomialgie,
    (False, True, False, False, False, False, False, True, True): Maladie,
    (True, True, False, False, False, False, False, True, True): Maladie,
    (False, False, True, False, False, False, False, True, True): FibaluseForceAffiniteIbsutiomialgie,
    (True, False, True, False, False, False, False, True, True): TirgnonoseFibaluseForceAffiniteIbsutiomialgie,
    (False, True, True, False, False, False, False, True, True): Maladie,
    (True, True, True, False, False, False, False, True, True): Maladie,
    (False, False, False, True, False, False, False, True, True): FibaluseVisionAffiniteIbsutiomialgie,
    (True, False, False, True, False, False, False, True, True): TirgnonoseFibaluseVisionAffiniteIbsutiomialgie,
    (False, True, False, True, False, False, False, True, True): Maladie,
    (True, True, False, True, False, False, False, True, True): Maladie,
    (False, False, True, True, False, False, False, True, True): FibaluseForceVisionAffiniteIbsutiomialgie,
    (True, False, True, True, False, False, False, True, True): TirgnonoseFibaluseForceVisionAffiniteIbsutiomialgie,
    (False, True, True, True, False, False, False, True, True): Maladie,
    (True, True, True, True, False, False, False, True, True): Maladie,
    (False, False, False, False, True, False, False, True, True): FibalusePvAffiniteIbsutiomialgie,
    (True, False, False, False, True, False, False, True, True): TirgnonoseFibalusePvAffiniteIbsutiomialgie,
    (False, True, False, False, True, False, False, True, True): Maladie,
    (True, True, False, False, True, False, False, True, True): Maladie,
    (False, False, True, False, True, False, False, True, True): FibaluseForcePvAffiniteIbsutiomialgie,
    (True, False, True, False, True, False, False, True, True): TirgnonoseFibaluseForcePvAffiniteIbsutiomialgie,
    (False, True, True, False, True, False, False, True, True): Maladie,
    (True, True, True, False, True, False, False, True, True): Maladie,
    (False, False, False, True, True, False, False, True, True): FibaluseVisionPvAffiniteIbsutiomialgie,
    (True, False, False, True, True, False, False, True, True): TirgnonoseFibaluseVisionPvAffiniteIbsutiomialgie,
    (False, True, False, True, True, False, False, True, True): Maladie,
    (True, True, False, True, True, False, False, True, True): Maladie,
    (False, False, True, True, True, False, False, True, True): FibaluseForceVisionPvAffiniteIbsutiomialgie,
    (True, False, True, True, True, False, False, True, True): TirgnonoseFibaluseForceVisionPvAffiniteIbsutiomialgie,
    (False, True, True, True, True, False, False, True, True): Maladie,
    (True, True, True, True, True, False, False, True, True): Maladie,
    (False, False, False, False, False, True, False, True, True): FibalusePmAffiniteIbsutiomialgie,
    (True, False, False, False, False, True, False, True, True): TirgnonoseFibalusePmAffiniteIbsutiomialgie,
    (False, True, False, False, False, True, False, True, True): Maladie,
    (True, True, False, False, False, True, False, True, True): Maladie,
    (False, False, True, False, False, True, False, True, True): FibaluseForcePmAffiniteIbsutiomialgie,
    (True, False, True, False, False, True, False, True, True): TirgnonoseFibaluseForcePmAffiniteIbsutiomialgie,
    (False, True, True, False, False, True, False, True, True): Maladie,
    (True, True, True, False, False, True, False, True, True): Maladie,
    (False, False, False, True, False, True, False, True, True): FibaluseVisionPmAffiniteIbsutiomialgie,
    (True, False, False, True, False, True, False, True, True): TirgnonoseFibaluseVisionPmAffiniteIbsutiomialgie,
    (False, True, False, True, False, True, False, True, True): Maladie,
    (True, True, False, True, False, True, False, True, True): Maladie,
    (False, False, True, True, False, True, False, True, True): FibaluseForceVisionPmAffiniteIbsutiomialgie,
    (True, False, True, True, False, True, False, True, True): TirgnonoseFibaluseForceVisionPmAffiniteIbsutiomialgie,
    (False, True, True, True, False, True, False, True, True): Maladie,
    (True, True, True, True, False, True, False, True, True): Maladie,
    (False, False, False, False, True, True, False, True, True): FibalusePvPmAffiniteIbsutiomialgie,
    (True, False, False, False, True, True, False, True, True): TirgnonoseFibalusePvPmAffiniteIbsutiomialgie,
    (False, True, False, False, True, True, False, True, True): Maladie,
    (True, True, False, False, True, True, False, True, True): Maladie,
    (False, False, True, False, True, True, False, True, True): FibaluseForcePvPmAffiniteIbsutiomialgie,
    (True, False, True, False, True, True, False, True, True): TirgnonoseFibaluseForcePvPmAffiniteIbsutiomialgie,
    (False, True, True, False, True, True, False, True, True): Maladie,
    (True, True, True, False, True, True, False, True, True): Maladie,
    (False, False, False, True, True, True, False, True, True): FibaluseVisionPvPmAffiniteIbsutiomialgie,
    (True, False, False, True, True, True, False, True, True): TirgnonoseFibaluseVisionPvPmAffiniteIbsutiomialgie,
    (False, True, False, True, True, True, False, True, True): Maladie,
    (True, True, False, True, True, True, False, True, True): Maladie,
    (False, False, True, True, True, True, False, True, True): FibaluseForceVisionPvPmAffiniteIbsutiomialgie,
    (True, False, True, True, True, True, False, True, True): TirgnonoseFibaluseForceVisionPvPmAffiniteIbsutiomialgie,
    (False, True, True, True, True, True, False, True, True): Maladie,
    (True, True, True, True, True, True, False, True, True): Maladie,
    (False, False, False, False, False, False, True, True, True): FibaluseVitesseAffiniteIbsutiomialgie,
    (True, False, False, False, False, False, True, True, True): TirgnonoseFibaluseVitesseAffiniteIbsutiomialgie,
    (False, True, False, False, False, False, True, True, True): Maladie,
    (True, True, False, False, False, False, True, True, True): Maladie,
    (False, False, True, False, False, False, True, True, True): FibaluseForceVitesseAffiniteIbsutiomialgie,
    (True, False, True, False, False, False, True, True, True): TirgnonoseFibaluseForceVitesseAffiniteIbsutiomialgie,
    (False, True, True, False, False, False, True, True, True): Maladie,
    (True, True, True, False, False, False, True, True, True): Maladie,
    (False, False, False, True, False, False, True, True, True): FibaluseVisionVitesseAffiniteIbsutiomialgie,
    (True, False, False, True, False, False, True, True, True): TirgnonoseFibaluseVisionVitesseAffiniteIbsutiomialgie,
    (False, True, False, True, False, False, True, True, True): Maladie,
    (True, True, False, True, False, False, True, True, True): Maladie,
    (False, False, True, True, False, False, True, True, True): FibaluseForceVisionVitesseAffiniteIbsutiomialgie,
    (True, False, True, True, False, False, True, True, True): TirgnonoseFibaluseForceVisionVitesseAffiniteIbsutiomialgie,
    (False, True, True, True, False, False, True, True, True): Maladie,
    (True, True, True, True, False, False, True, True, True): Maladie,
    (False, False, False, False, True, False, True, True, True): FibalusePvVitesseAffiniteIbsutiomialgie,
    (True, False, False, False, True, False, True, True, True): TirgnonoseFibalusePvVitesseAffiniteIbsutiomialgie,
    (False, True, False, False, True, False, True, True, True): Maladie,
    (True, True, False, False, True, False, True, True, True): Maladie,
    (False, False, True, False, True, False, True, True, True): FibaluseForcePvVitesseAffiniteIbsutiomialgie,
    (True, False, True, False, True, False, True, True, True): TirgnonoseFibaluseForcePvVitesseAffiniteIbsutiomialgie,
    (False, True, True, False, True, False, True, True, True): Maladie,
    (True, True, True, False, True, False, True, True, True): Maladie,
    (False, False, False, True, True, False, True, True, True): FibaluseVisionPvVitesseAffiniteIbsutiomialgie,
    (True, False, False, True, True, False, True, True, True): TirgnonoseFibaluseVisionPvVitesseAffiniteIbsutiomialgie,
    (False, True, False, True, True, False, True, True, True): Maladie,
    (True, True, False, True, True, False, True, True, True): Maladie,
    (False, False, True, True, True, False, True, True, True): FibaluseForceVisionPvVitesseAffiniteIbsutiomialgie,
    (True, False, True, True, True, False, True, True, True): TirgnonoseFibaluseForceVisionPvVitesseAffiniteIbsutiomialgie,
    (False, True, True, True, True, False, True, True, True): Maladie,
    (True, True, True, True, True, False, True, True, True): Maladie,
    (False, False, False, False, False, True, True, True, True): FibalusePmVitesseAffiniteIbsutiomialgie,
    (True, False, False, False, False, True, True, True, True): TirgnonoseFibalusePmVitesseAffiniteIbsutiomialgie,
    (False, True, False, False, False, True, True, True, True): Maladie,
    (True, True, False, False, False, True, True, True, True): Maladie,
    (False, False, True, False, False, True, True, True, True): FibaluseForcePmVitesseAffiniteIbsutiomialgie,
    (True, False, True, False, False, True, True, True, True): TirgnonoseFibaluseForcePmVitesseAffiniteIbsutiomialgie,
    (False, True, True, False, False, True, True, True, True): Maladie,
    (True, True, True, False, False, True, True, True, True): Maladie,
    (False, False, False, True, False, True, True, True, True): FibaluseVisionPmVitesseAffiniteIbsutiomialgie,
    (True, False, False, True, False, True, True, True, True): TirgnonoseFibaluseVisionPmVitesseAffiniteIbsutiomialgie,
    (False, True, False, True, False, True, True, True, True): Maladie,
    (True, True, False, True, False, True, True, True, True): Maladie,
    (False, False, True, True, False, True, True, True, True): FibaluseForceVisionPmVitesseAffiniteIbsutiomialgie,
    (True, False, True, True, False, True, True, True, True): TirgnonoseFibaluseForceVisionPmVitesseAffiniteIbsutiomialgie,
    (False, True, True, True, False, True, True, True, True): Maladie,
    (True, True, True, True, False, True, True, True, True): Maladie,
    (False, False, False, False, True, True, True, True, True): FibalusePvPmVitesseAffiniteIbsutiomialgie,
    (True, False, False, False, True, True, True, True, True): TirgnonoseFibalusePvPmVitesseAffiniteIbsutiomialgie,
    (False, True, False, False, True, True, True, True, True): Maladie,
    (True, True, False, False, True, True, True, True, True): Maladie,
    (False, False, True, False, True, True, True, True, True): FibaluseForcePvPmVitesseAffiniteIbsutiomialgie,
    (True, False, True, False, True, True, True, True, True): TirgnonoseFibaluseForcePvPmVitesseAffiniteIbsutiomialgie,
    (False, True, True, False, True, True, True, True, True): Maladie,
    (True, True, True, False, True, True, True, True, True): Maladie,
    (False, False, False, True, True, True, True, True, True): FibaluseVisionPvPmVitesseAffiniteIbsutiomialgie,
    (True, False, False, True, True, True, True, True, True): TirgnonoseFibaluseVisionPvPmVitesseAffiniteIbsutiomialgie,
    (False, True, False, True, True, True, True, True, True): Maladie,
    (True, True, False, True, True, True, True, True, True): Maladie,
    (False, False, True, True, True, True, True, True, True): FibaluseForceVisionPvPmVitesseAffiniteIbsutiomialgie,
    (True, False, True, True, True, True, True, True, True): TirgnonoseFibaluseForceVisionPvPmVitesseAffiniteIbsutiomialgie,
    (False, True, True, True, True, True, True, True, True): Maladie,
    (True, True, True, True, True, True, True, True, True): Maladie,
}
"""
(tirgnonose, fibaluse, force, vision, pv, pm, vitesse, affinite, ibsutiomialgie) -> maladie correspondante
"""
