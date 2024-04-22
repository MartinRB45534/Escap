"""
Contient les classes des maladies mixtes (qui affectent aussi les cases).
"""

from __future__ import annotations

# Imports des classes parentes
from .maladie_mixte import MaladieMixte
from ..agissant import Maladie, Tirgnonose, Fibaluse, FibaluseForce, FibaluseVision, FibalusePv, FibalusePm, FibaluseVitesse, FibaluseAffinite, Ibsutiomialgie

class TirgnonoseMixte(Tirgnonose, MaladieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant, et qui peut survivre sur une case."""

class FibaluseMixte(Fibaluse, MaladieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant toutes ses stats, et qui peut survivre sur une case."""

class FibaluseForceMixte(FibaluseForce, MaladieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, et qui peut survivre sur une case."""

class FibaluseVisionMixte(FibaluseVision, MaladieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vision, et qui peut survivre sur une case."""

class FibalusePvMixte(FibalusePv, MaladieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa régénération de PV, et qui peut survivre sur une case."""

class FibalusePmMixte(FibalusePm, MaladieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa régénération de PM, et qui peut survivre sur une case."""

class FibaluseVitesseMixte(FibaluseVitesse, MaladieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vitesse, et qui peut survivre sur une case."""

class FibaluseAffiniteMixte(FibaluseAffinite, MaladieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant son affinité à un élément, et qui peut survivre sur une case."""

class IbsutiomialgieMixte(Ibsutiomialgie, MaladieMixte):
    """Une maladie qui peut tuer l'agissant de façon subite (ibsute), et qui peut survivre sur une case."""
    def __init__(self):
        Ibsutiomialgie.__init__(self)
        MaladieMixte.__init__(self)

class TirgnonoseFibaluse(Tirgnonose, Fibaluse):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale)."""

class TirgnonoseFibaluseMixte(Tirgnonose, Fibaluse, MaladieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale), et qui peut survivre sur une case."""

class TirgnonoseFibaluseForce(TirgnonoseFibaluse, FibaluseForce):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force."""

class TirgnonoseFibaluseForceMixte(TirgnonoseFibaluse, FibaluseForce, MaladieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, et qui peut survivre sur une case."""

class TirgnonoseFibaluseVision(TirgnonoseFibaluse, FibaluseVision):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vision."""

class TirgnonoseFibaluseVisionMixte(TirgnonoseFibaluse, FibaluseVision, MaladieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vision, et qui peut survivre sur une case."""

class TirgnonoseFibalusePv(TirgnonoseFibaluse, FibalusePv):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa régénération de PV."""

class TirgnonoseFibalusePvMixte(TirgnonoseFibaluse, FibalusePv, MaladieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa régénération de PV, et qui peut survivre sur une case."""

class TirgnonoseFibalusePm(TirgnonoseFibaluse, FibalusePm):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa régénération de PM."""

class TirgnonoseFibalusePmMixte(TirgnonoseFibaluse, FibalusePm, MaladieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa régénération de PM, et qui peut survivre sur une case."""

class TirgnonoseFibaluseVitesse(TirgnonoseFibaluse, FibaluseVitesse):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vitesse."""

class TirgnonoseFibaluseVitesseMixte(TirgnonoseFibaluse, FibaluseVitesse, MaladieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vitesse, et qui peut survivre sur une case."""

class TirgnonoseFibaluseAffinite(TirgnonoseFibaluse, FibaluseAffinite):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant son affinité à un élément."""

class TirgnonoseFibaluseAffiniteMixte(TirgnonoseFibaluse, FibaluseAffinite, MaladieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant son affinité à un élément, et qui peut survivre sur une case."""

class TirgnonoseIbsutiomialgie(Tirgnonose, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et peut le tuer de façon subite (ibsute)."""

class TirgnonoseIbsutiomialgieMixte(Tirgnonose, IbsutiomialgieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class FibaluseIbsutiomialgie(Fibaluse, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant et peut le tuer de façon subite (ibsute)."""

class FibaluseIbsutiomialgieMixte(Fibaluse, IbsutiomialgieMixte):
    """Une maladie qui rend faible (fibale) l'agissant et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class FibaluseForceVision(FibaluseForce, FibaluseVision):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force et sa vision."""

class FibaluseForceVisionMixte(FibaluseForce, FibaluseVision, MaladieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force et sa vision, et qui peut survivre sur une case."""

class FibaluseForcePv(FibaluseForce, FibalusePv):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force et sa régénération de PV."""

class FibaluseForcePvMixte(FibaluseForce, FibalusePv, MaladieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force et sa régénération de PV, et qui peut survivre sur une case."""

class FibaluseForcePm(FibaluseForce, FibalusePm):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force et sa régénération de PM."""

class FibaluseForcePmMixte(FibaluseForce, FibalusePm, MaladieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force et sa régénération de PM, et qui peut survivre sur une case."""

class FibaluseForceVitesse(FibaluseForce, FibaluseVitesse):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force et sa vitesse."""

class FibaluseForceVitesseMixte(FibaluseForce, FibaluseVitesse, MaladieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force et sa vitesse, et qui peut survivre sur une case."""

class FibaluseForceAffinite(FibaluseForce, FibaluseAffinite):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force et son affinité à un élément."""

class FibaluseForceAffiniteMixte(FibaluseForce, FibaluseAffinite, MaladieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force et son affinité à un élément, et qui peut survivre sur une case."""

class FibaluseForceIbsutiomialgie(FibaluseForce, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force et peut le tuer de façon subite (ibsute)."""

class FibaluseForceIbsutiomialgieMixte(FibaluseForce, IbsutiomialgieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class FibaluseVisionPv(FibaluseVision, FibalusePv):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vision et sa régénération de PV."""

class FibaluseVisionPvMixte(FibaluseVision, FibalusePv, MaladieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vision et sa régénération de PV, et qui peut survivre sur une case."""

class FibaluseVisionPm(FibaluseVision, FibalusePm):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vision et sa régénération de PM."""

class FibaluseVisionPmMixte(FibaluseVision, FibalusePm, MaladieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vision et sa régénération de PM, et qui peut survivre sur une case."""

class FibaluseVisionVitesse(FibaluseVision, FibaluseVitesse):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vision et sa vitesse."""

class FibaluseVisionVitesseMixte(FibaluseVision, FibaluseVitesse, MaladieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vision et sa vitesse, et qui peut survivre sur une case."""

class FibaluseVisionAffinite(FibaluseVision, FibaluseAffinite):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vision et son affinité à un élément."""

class FibaluseVisionAffiniteMixte(FibaluseVision, FibaluseAffinite, MaladieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vision et son affinité à un élément, et qui peut survivre sur une case."""

class FibaluseVisionIbsutiomialgie(FibaluseVision, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vision et peut le tuer de façon subite (ibsute)."""

class FibaluseVisionIbsutiomialgieMixte(FibaluseVision, IbsutiomialgieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vision et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class FibalusePvPm(FibalusePv, FibalusePm):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa régénération de PV et de PM."""

class FibalusePvPmMixte(FibalusePv, FibalusePm, MaladieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa régénération de PV et de PM, et qui peut survivre sur une case."""

class FibalusePvVitesse(FibalusePv, FibaluseVitesse):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa régénération de PV et sa vitesse."""

class FibalusePvVitesseMixte(FibalusePv, FibaluseVitesse, MaladieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa régénération de PV et sa vitesse, et qui peut survivre sur une case."""

class FibalusePvAffinite(FibalusePv, FibaluseAffinite):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa régénération de PV et son affinité à un élément."""

class FibalusePvAffiniteMixte(FibalusePv, FibaluseAffinite, MaladieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa régénération de PV et son affinité à un élément, et qui peut survivre sur une case."""

class FibalusePvIbsutiomialgie(FibalusePv, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa régénération de PV et peut le tuer de façon subite (ibsute)."""

class FibalusePvIbsutiomialgieMixte(FibalusePv, IbsutiomialgieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa régénération de PV et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class FibalusePmVitesse(FibalusePm, FibaluseVitesse):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa régénération de PM et sa vitesse."""

class FibalusePmVitesseMixte(FibalusePm, FibaluseVitesse, MaladieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa régénération de PM et sa vitesse, et qui peut survivre sur une case."""

class FibalusePmAffinite(FibalusePm, FibaluseAffinite):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa régénération de PM et son affinité à un élément."""

class FibalusePmAffiniteMixte(FibalusePm, FibaluseAffinite, MaladieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa régénération de PM et son affinité à un élément, et qui peut survivre sur une case."""

class FibalusePmIbsutiomialgie(FibalusePm, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa régénération de PM et peut le tuer de façon subite (ibsute)."""

class FibalusePmIbsutiomialgieMixte(FibalusePm, IbsutiomialgieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa régénération de PM et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class FibaluseVitesseAffinite(FibaluseVitesse, FibaluseAffinite):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vitesse et son affinité à un élément."""

class FibaluseVitesseAffiniteMixte(FibaluseVitesse, FibaluseAffinite, MaladieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vitesse et son affinité à un élément, et qui peut survivre sur une case."""

class FibaluseVitesseIbsutiomialgie(FibaluseVitesse, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vitesse et peut le tuer de façon subite (ibsute)."""

class FibaluseVitesseIbsutiomialgieMixte(FibaluseVitesse, IbsutiomialgieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vitesse et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class FibaluseAffiniteIbsutiomialgie(FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class FibaluseAffiniteIbsutiomialgieMixte(FibaluseAffinite, IbsutiomialgieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant son affinité à un élément et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class TirgnonoseFibaluseIbsutiomialgie(TirgnonoseFibaluse, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseIbsutiomialgieMixte(TirgnonoseFibaluse, IbsutiomialgieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class TirgnonoseFibaluseForceVision(Tirgnonose, FibaluseForce, FibaluseVision):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force et sa vision."""

class TirgnonoseFibaluseForceVisionMixte(Tirgnonose, FibaluseForce, FibaluseVision, MaladieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force et sa vision, et qui peut survivre sur une case."""

class TirgnonoseFibaluseForcePv(Tirgnonose, FibaluseForce, FibalusePv):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force et sa régénération de PV."""

class TirgnonoseFibaluseForcePvMixte(Tirgnonose, FibaluseForce, FibalusePv, MaladieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force et sa régénération de PV, et qui peut survivre sur une case."""

class TirgnonoseFibaluseForcePm(Tirgnonose, FibaluseForce, FibalusePm):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force et sa régénération de PM."""

class TirgnonoseFibaluseForcePmMixte(Tirgnonose, FibaluseForce, FibalusePm, MaladieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force et sa régénération de PM, et qui peut survivre sur une case."""

class TirgnonoseFibaluseForceVitesse(Tirgnonose, FibaluseForce, FibaluseVitesse):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force et sa vitesse."""

class TirgnonoseFibaluseForceVitesseMixte(Tirgnonose, FibaluseForce, FibaluseVitesse, MaladieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force et sa vitesse, et qui peut survivre sur une case."""

class TirgnonoseFibaluseForceAffinite(Tirgnonose, FibaluseForce, FibaluseAffinite):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force et son affinité à un élément."""

class TirgnonoseFibaluseForceAffiniteMixte(Tirgnonose, FibaluseForce, FibaluseAffinite, MaladieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force et son affinité à un élément, et qui peut survivre sur une case."""

class TirgnonoseFibaluseForceIbsutiomialgie(Tirgnonose, FibaluseForce, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseForceIbsutiomialgieMixte(Tirgnonose, FibaluseForce, IbsutiomialgieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class TirgnonoseFibaluseVisionPv(Tirgnonose, FibaluseVision, FibalusePv):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vision et sa régénération de PV."""

class TirgnonoseFibaluseVisionPvMixte(Tirgnonose, FibaluseVision, FibalusePv, MaladieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vision et sa régénération de PV, et qui peut survivre sur une case."""

class TirgnonoseFibaluseVisionPm(Tirgnonose, FibaluseVision, FibalusePm):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vision et sa régénération de PM."""

class TirgnonoseFibaluseVisionPmMixte(Tirgnonose, FibaluseVision, FibalusePm, MaladieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vision et sa régénération de PM, et qui peut survivre sur une case."""

class TirgnonoseFibaluseVisionVitesse(Tirgnonose, FibaluseVision, FibaluseVitesse):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vision et sa vitesse."""

class TirgnonoseFibaluseVisionVitesseMixte(Tirgnonose, FibaluseVision, FibaluseVitesse, MaladieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vision et sa vitesse, et qui peut survivre sur une case."""

class TirgnonoseFibaluseVisionAffinite(Tirgnonose, FibaluseVision, FibaluseAffinite):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vision et son affinité à un élément."""

class TirgnonoseFibaluseVisionAffiniteMixte(Tirgnonose, FibaluseVision, FibaluseAffinite, MaladieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vision et son affinité à un élément, et qui peut survivre sur une case."""

class TirgnonoseFibaluseVisionIbsutiomialgie(Tirgnonose, FibaluseVision, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vision et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseVisionIbsutiomialgieMixte(Tirgnonose, FibaluseVision, IbsutiomialgieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vision et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class TirgnonoseFibalusePvPm(Tirgnonose, FibalusePv, FibalusePm):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa régénération de PV et de PM."""

class TirgnonoseFibalusePvPmMixte(Tirgnonose, FibalusePv, FibalusePm, MaladieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa régénération de PV et de PM, et qui peut survivre sur une case."""

class TirgnonoseFibalusePvVitesse(Tirgnonose, FibalusePv, FibaluseVitesse):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa régénération de PV et sa vitesse."""

class TirgnonoseFibalusePvVitesseMixte(Tirgnonose, FibalusePv, FibaluseVitesse, MaladieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa régénération de PV et sa vitesse, et qui peut survivre sur une case."""

class TirgnonoseFibalusePvAffinite(Tirgnonose, FibalusePv, FibaluseAffinite):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa régénération de PV et son affinité à un élément."""

class TirgnonoseFibalusePvAffiniteMixte(Tirgnonose, FibalusePv, FibaluseAffinite, MaladieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa régénération de PV et son affinité à un élément, et qui peut survivre sur une case."""

class TirgnonoseFibalusePvIbsutiomialgie(Tirgnonose, FibalusePv, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa régénération de PV et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibalusePvIbsutiomialgieMixte(Tirgnonose, FibalusePv, IbsutiomialgieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa régénération de PV et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class TirgnonoseFibalusePmVitesse(Tirgnonose, FibalusePm, FibaluseVitesse):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa régénération de PM et sa vitesse."""

class TirgnonoseFibalusePmVitesseMixte(Tirgnonose, FibalusePm, FibaluseVitesse, MaladieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa régénération de PM et sa vitesse, et qui peut survivre sur une case."""

class TirgnonoseFibalusePmAffinite(Tirgnonose, FibalusePm, FibaluseAffinite):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa régénération de PM et son affinité à un élément."""

class TirgnonoseFibalusePmAffiniteMixte(Tirgnonose, FibalusePm, FibaluseAffinite, MaladieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa régénération de PM et son affinité à un élément, et qui peut survivre sur une case."""

class TirgnonoseFibalusePmIbsutiomialgie(Tirgnonose, FibalusePm, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa régénération de PM et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibalusePmIbsutiomialgieMixte(Tirgnonose, FibalusePm, IbsutiomialgieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa régénération de PM et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class TirgnonoseFibaluseVitesseAffinite(Tirgnonose, FibaluseVitesse, FibaluseAffinite):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vitesse et son affinité à un élément."""

class TirgnonoseFibaluseVitesseAffiniteMixte(Tirgnonose, FibaluseVitesse, FibaluseAffinite, MaladieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vitesse et son affinité à un élément, et qui peut survivre sur une case."""

class TirgnonoseFibaluseVitesseIbsutiomialgie(Tirgnonose, FibaluseVitesse, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vitesse et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseVitesseIbsutiomialgieMixte(Tirgnonose, FibaluseVitesse, IbsutiomialgieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vitesse et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class TirgnonoseFibaluseAffiniteIbsutiomialgie(Tirgnonose, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseAffiniteIbsutiomialgieMixte(Tirgnonose, FibaluseAffinite, IbsutiomialgieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant son affinité à un élément et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class FibaluseForceVisionPv(FibaluseForce, FibaluseVision, FibalusePv):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vision et sa régénération de PV."""

class FibaluseForceVisionPvMixte(FibaluseForce, FibaluseVision, FibalusePv, MaladieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vision et sa régénération de PV, et qui peut survivre sur une case."""

class FibaluseForceVisionPm(FibaluseForce, FibaluseVision, FibalusePm):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vision et sa régénération de PM."""

class FibaluseForceVisionPmMixte(FibaluseForce, FibaluseVision, FibalusePm, MaladieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vision et sa régénération de PM, et qui peut survivre sur une case."""

class FibaluseForceVisionVitesse(FibaluseForce, FibaluseVision, FibaluseVitesse):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vision et sa vitesse."""

class FibaluseForceVisionVitesseMixte(FibaluseForce, FibaluseVision, FibaluseVitesse, MaladieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vision et sa vitesse, et qui peut survivre sur une case."""

class FibaluseForceVisionAffinite(FibaluseForce, FibaluseVision, FibaluseAffinite):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vision et son affinité à un élément."""

class FibaluseForceVisionAffiniteMixte(FibaluseForce, FibaluseVision, FibaluseAffinite, MaladieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vision et son affinité à un élément, et qui peut survivre sur une case."""

class FibaluseForceVisionIbsutiomialgie(FibaluseForce, FibaluseVision, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vision et peut le tuer de façon subite (ibsute)."""

class FibaluseForceVisionIbsutiomialgieMixte(FibaluseForce, FibaluseVision, IbsutiomialgieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vision et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class FibaluseForcePvPm(FibaluseForce, FibalusePv, FibalusePm):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa régénération de PV et de PM."""

class FibaluseForcePvPmMixte(FibaluseForce, FibalusePv, FibalusePm, MaladieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa régénération de PV et de PM, et qui peut survivre sur une case."""

class FibaluseForcePvVitesse(FibaluseForce, FibalusePv, FibaluseVitesse):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa régénération de PV et sa vitesse."""

class FibaluseForcePvVitesseMixte(FibaluseForce, FibalusePv, FibaluseVitesse, MaladieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa régénération de PV et sa vitesse, et qui peut survivre sur une case."""

class FibaluseForcePvAffinite(FibaluseForce, FibalusePv, FibaluseAffinite):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa régénération de PV et son affinité à un élément."""

class FibaluseForcePvAffiniteMixte(FibaluseForce, FibalusePv, FibaluseAffinite, MaladieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa régénération de PV et son affinité à un élément, et qui peut survivre sur une case."""

class FibaluseForcePvIbsutiomialgie(FibaluseForce, FibalusePv, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa régénération de PV et peut le tuer de façon subite (ibsute)."""

class FibaluseForcePvIbsutiomialgieMixte(FibaluseForce, FibalusePv, IbsutiomialgieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa régénération de PV et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class FibaluseForcePmVitesse(FibaluseForce, FibalusePm, FibaluseVitesse):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa régénération de PM et sa vitesse."""

class FibaluseForcePmVitesseMixte(FibaluseForce, FibalusePm, FibaluseVitesse, MaladieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa régénération de PM et sa vitesse, et qui peut survivre sur une case."""

class FibaluseForcePmAffinite(FibaluseForce, FibalusePm, FibaluseAffinite):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa régénération de PM et son affinité à un élément."""

class FibaluseForcePmAffiniteMixte(FibaluseForce, FibalusePm, FibaluseAffinite, MaladieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa régénération de PM et son affinité à un élément, et qui peut survivre sur une case."""

class FibaluseForcePmIbsutiomialgie(FibaluseForce, FibalusePm, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa régénération de PM et peut le tuer de façon subite (ibsute)."""

class FibaluseForcePmIbsutiomialgieMixte(FibaluseForce, FibalusePm, IbsutiomialgieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa régénération de PM et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class FibaluseForceVitesseAffinite(FibaluseForce, FibaluseVitesse, FibaluseAffinite):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vitesse et son affinité à un élément."""

class FibaluseForceVitesseAffiniteMixte(FibaluseForce, FibaluseVitesse, FibaluseAffinite, MaladieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vitesse et son affinité à un élément, et qui peut survivre sur une case."""

class FibaluseForceVitesseIbsutiomialgie(FibaluseForce, FibaluseVitesse, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vitesse et peut le tuer de façon subite (ibsute)."""

class FibaluseForceVitesseIbsutiomialgieMixte(FibaluseForce, FibaluseVitesse, IbsutiomialgieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vitesse et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class FibaluseForceAffiniteIbsutiomialgie(FibaluseForce, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class FibaluseForceAffiniteIbsutiomialgieMixte(FibaluseForce, FibaluseAffinite, IbsutiomialgieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, son affinité à un élément et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class FibaluseVisionPvPm(FibaluseVision, FibalusePv, FibalusePm):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vision, sa régénération de PV et de PM."""

class FibaluseVisionPvPmMixte(FibaluseVision, FibalusePv, FibalusePm, MaladieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vision, sa régénération de PV et de PM, et qui peut survivre sur une case."""

class FibaluseVisionPvVitesse(FibaluseVision, FibalusePv, FibaluseVitesse):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vision, sa régénération de PV et sa vitesse."""

class FibaluseVisionPvVitesseMixte(FibaluseVision, FibalusePv, FibaluseVitesse, MaladieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vision, sa régénération de PV et sa vitesse, et qui peut survivre sur une case."""

class FibaluseVisionPvAffinite(FibaluseVision, FibalusePv, FibaluseAffinite):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vision, sa régénération de PV et son affinité à un élément."""

class FibaluseVisionPvAffiniteMixte(FibaluseVision, FibalusePv, FibaluseAffinite, MaladieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vision, sa régénération de PV et son affinité à un élément, et qui peut survivre sur une case."""

class FibaluseVisionPvIbsutiomialgie(FibaluseVision, FibalusePv, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vision, sa régénération de PV et peut le tuer de façon subite (ibsute)."""

class FibaluseVisionPvIbsutiomialgieMixte(FibaluseVision, FibalusePv, IbsutiomialgieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vision, sa régénération de PV et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class FibaluseVisionPmVitesse(FibaluseVision, FibalusePm, FibaluseVitesse):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vision, sa régénération de PM et sa vitesse."""

class FibaluseVisionPmVitesseMixte(FibaluseVision, FibalusePm, FibaluseVitesse, MaladieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vision, sa régénération de PM et sa vitesse, et qui peut survivre sur une case."""

class FibaluseVisionPmAffinite(FibaluseVision, FibalusePm, FibaluseAffinite):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vision, sa régénération de PM et son affinité à un élément."""

class FibaluseVisionPmAffiniteMixte(FibaluseVision, FibalusePm, FibaluseAffinite, MaladieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vision, sa régénération de PM et son affinité à un élément, et qui peut survivre sur une case."""

class FibaluseVisionPmIbsutiomialgie(FibaluseVision, FibalusePm, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vision, sa régénération de PM et peut le tuer de façon subite (ibsute)."""

class FibaluseVisionPmIbsutiomialgieMixte(FibaluseVision, FibalusePm, IbsutiomialgieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vision, sa régénération de PM et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class FibaluseVisionVitesseAffinite(FibaluseVision, FibaluseVitesse, FibaluseAffinite):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vision, sa vitesse et son affinité à un élément."""

class FibaluseVisionVitesseAffiniteMixte(FibaluseVision, FibaluseVitesse, FibaluseAffinite, MaladieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vision, sa vitesse et son affinité à un élément, et qui peut survivre sur une case."""

class FibaluseVisionVitesseIbsutiomialgie(FibaluseVision, FibaluseVitesse, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vision, sa vitesse et peut le tuer de façon subite (ibsute)."""

class FibaluseVisionVitesseIbsutiomialgieMixte(FibaluseVision, FibaluseVitesse, IbsutiomialgieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vision, sa vitesse et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class FibaluseVisionAffiniteIbsutiomialgie(FibaluseVision, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vision, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class FibaluseVisionAffiniteIbsutiomialgieMixte(FibaluseVision, FibaluseAffinite, IbsutiomialgieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vision, son affinité à un élément et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class FibalusePvPmVitesse(FibalusePv, FibalusePm, FibaluseVitesse):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa régénération de PV, de PM et sa vitesse."""

class FibalusePvPmVitesseMixte(FibalusePv, FibalusePm, FibaluseVitesse, MaladieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa régénération de PV, de PM et sa vitesse, et qui peut survivre sur une case."""

class FibalusePvPmAffinite(FibalusePv, FibalusePm, FibaluseAffinite):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa régénération de PV, de PM et son affinité à un élément."""

class FibalusePvPmAffiniteMixte(FibalusePv, FibalusePm, FibaluseAffinite, MaladieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa régénération de PV, de PM et son affinité à un élément, et qui peut survivre sur une case."""

class FibalusePvPmIbsutiomialgie(FibalusePv, FibalusePm, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa régénération de PV, de PM et peut le tuer de façon subite (ibsute)."""

class FibalusePvPmIbsutiomialgieMixte(FibalusePv, FibalusePm, IbsutiomialgieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa régénération de PV, de PM et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class FibalusePvVitesseAffinite(FibalusePv, FibaluseVitesse, FibaluseAffinite):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa régénération de PV, sa vitesse et son affinité à un élément."""

class FibalusePvVitesseAffiniteMixte(FibalusePv, FibaluseVitesse, FibaluseAffinite, MaladieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa régénération de PV, sa vitesse et son affinité à un élément, et qui peut survivre sur une case."""

class FibalusePvVitesseIbsutiomialgie(FibalusePv, FibaluseVitesse, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa régénération de PV, sa vitesse et peut le tuer de façon subite (ibsute)."""

class FibalusePvVitesseIbsutiomialgieMixte(FibalusePv, FibaluseVitesse, IbsutiomialgieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa régénération de PV, sa vitesse et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class FibalusePvAffiniteIbsutiomialgie(FibalusePv, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa régénération de PV, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class FibalusePvAffiniteIbsutiomialgieMixte(FibalusePv, FibaluseAffinite, IbsutiomialgieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa régénération de PV, son affinité à un élément et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class FibalusePmVitesseAffinite(FibalusePm, FibaluseVitesse, FibaluseAffinite):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa régénération de PM, sa vitesse et son affinité à un élément."""

class FibalusePmVitesseAffiniteMixte(FibalusePm, FibaluseVitesse, FibaluseAffinite, MaladieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa régénération de PM, sa vitesse et son affinité à un élément, et qui peut survivre sur une case."""

class FibalusePmVitesseIbsutiomialgie(FibalusePm, FibaluseVitesse, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa régénération de PM, sa vitesse et peut le tuer de façon subite (ibsute)."""

class FibalusePmVitesseIbsutiomialgieMixte(FibalusePm, FibaluseVitesse, IbsutiomialgieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa régénération de PM, sa vitesse et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class FibalusePmAffiniteIbsutiomialgie(FibalusePm, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa régénération de PM, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class FibalusePmAffiniteIbsutiomialgieMixte(FibalusePm, FibaluseAffinite, IbsutiomialgieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa régénération de PM, son affinité à un élément et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class FibaluseVitesseAffiniteIbsutiomialgie(FibaluseVitesse, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vitesse, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class FibaluseVitesseAffiniteIbsutiomialgieMixte(FibaluseVitesse, FibaluseAffinite, IbsutiomialgieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vitesse, son affinité à un élément et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class TirgnonoseFibaluseForceVisionPv(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePv):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vision et sa régénération de PV."""

class TirgnonoseFibaluseForceVisionPvMixte(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePv, MaladieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vision et sa régénération de PV, et qui peut survivre sur une case."""

class TirgnonoseFibaluseForceVisionPm(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePm):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vision et sa régénération de PM."""

class TirgnonoseFibaluseForceVisionPmMixte(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePm, MaladieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vision et sa régénération de PM, et qui peut survivre sur une case."""

class TirgnonoseFibaluseForceVisionVitesse(Tirgnonose, FibaluseForce, FibaluseVision, FibaluseVitesse):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vision et sa vitesse."""

class TirgnonoseFibaluseForceVisionVitesseMixte(Tirgnonose, FibaluseForce, FibaluseVision, FibaluseVitesse, MaladieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vision et sa vitesse, et qui peut survivre sur une case."""

class TirgnonoseFibaluseForceVisionAffinite(Tirgnonose, FibaluseForce, FibaluseVision, FibaluseAffinite):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vision et son affinité à un élément."""

class TirgnonoseFibaluseForceVisionAffiniteMixte(Tirgnonose, FibaluseForce, FibaluseVision, FibaluseAffinite, MaladieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vision et son affinité à un élément, et qui peut survivre sur une case."""

class TirgnonoseFibaluseForceVisionIbsutiomialgie(Tirgnonose, FibaluseForce, FibaluseVision, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vision et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseForceVisionIbsutiomialgieMixte(Tirgnonose, FibaluseForce, FibaluseVision, IbsutiomialgieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vision et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class TirgnonoseFibaluseForcePvPm(Tirgnonose, FibaluseForce, FibalusePv, FibalusePm):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa régénération de PV et de PM."""

class TirgnonoseFibaluseForcePvPmMixte(Tirgnonose, FibaluseForce, FibalusePv, FibalusePm, MaladieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa régénération de PV et de PM, et qui peut survivre sur une case."""

class TirgnonoseFibaluseForcePvVitesse(Tirgnonose, FibaluseForce, FibalusePv, FibaluseVitesse):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa régénération de PV et sa vitesse."""

class TirgnonoseFibaluseForcePvVitesseMixte(Tirgnonose, FibaluseForce, FibalusePv, FibaluseVitesse, MaladieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa régénération de PV et sa vitesse, et qui peut survivre sur une case."""

class TirgnonoseFibaluseForcePvAffinite(Tirgnonose, FibaluseForce, FibalusePv, FibaluseAffinite):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa régénération de PV et son affinité à un élément."""

class TirgnonoseFibaluseForcePvAffiniteMixte(Tirgnonose, FibaluseForce, FibalusePv, FibaluseAffinite, MaladieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa régénération de PV et son affinité à un élément, et qui peut survivre sur une case."""

class TirgnonoseFibaluseForcePvIbsutiomialgie(Tirgnonose, FibaluseForce, FibalusePv, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa régénération de PV et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseForcePvIbsutiomialgieMixte(Tirgnonose, FibaluseForce, FibalusePv, IbsutiomialgieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa régénération de PV et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class TirgnonoseFibaluseForcePmVitesse(Tirgnonose, FibaluseForce, FibalusePm, FibaluseVitesse):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa régénération de PM et sa vitesse."""

class TirgnonoseFibaluseForcePmVitesseMixte(Tirgnonose, FibaluseForce, FibalusePm, FibaluseVitesse, MaladieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa régénération de PM et sa vitesse, et qui peut survivre sur une case."""

class TirgnonoseFibaluseForcePmAffinite(Tirgnonose, FibaluseForce, FibalusePm, FibaluseAffinite):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa régénération de PM et son affinité à un élément."""

class TirgnonoseFibaluseForcePmAffiniteMixte(Tirgnonose, FibaluseForce, FibalusePm, FibaluseAffinite, MaladieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa régénération de PM et son affinité à un élément, et qui peut survivre sur une case."""

class TirgnonoseFibaluseForcePmIbsutiomialgie(Tirgnonose, FibaluseForce, FibalusePm, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa régénération de PM et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseForcePmIbsutiomialgieMixte(Tirgnonose, FibaluseForce, FibalusePm, IbsutiomialgieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa régénération de PM et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class TirgnonoseFibaluseForceVitesseAffinite(Tirgnonose, FibaluseForce, FibaluseVitesse, FibaluseAffinite):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vitesse et son affinité à un élément."""

class TirgnonoseFibaluseForceVitesseAffiniteMixte(Tirgnonose, FibaluseForce, FibaluseVitesse, FibaluseAffinite, MaladieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vitesse et son affinité à un élément, et qui peut survivre sur une case."""

class TirgnonoseFibaluseForceVitesseIbsutiomialgie(Tirgnonose, FibaluseForce, FibaluseVitesse, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vitesse et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseForceVitesseIbsutiomialgieMixte(Tirgnonose, FibaluseForce, FibaluseVitesse, IbsutiomialgieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vitesse et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class TirgnonoseFibaluseForceAffiniteIbsutiomialgie(Tirgnonose, FibaluseForce, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseForceAffiniteIbsutiomialgieMixte(Tirgnonose, FibaluseForce, FibaluseAffinite, IbsutiomialgieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, son affinité à un élément et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class TirgnonoseFibaluseVisionPvPm(Tirgnonose, FibaluseVision, FibalusePv, FibalusePm):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vision, sa régénération de PV et de PM."""

class TirgnonoseFibaluseVisionPvPmMixte(Tirgnonose, FibaluseVision, FibalusePv, FibalusePm, MaladieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vision, sa régénération de PV et de PM, et qui peut survivre sur une case."""

class TirgnonoseFibaluseVisionPvVitesse(Tirgnonose, FibaluseVision, FibalusePv, FibaluseVitesse):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vision, sa régénération de PV et sa vitesse."""

class TirgnonoseFibaluseVisionPvVitesseMixte(Tirgnonose, FibaluseVision, FibalusePv, FibaluseVitesse, MaladieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vision, sa régénération de PV et sa vitesse, et qui peut survivre sur une case."""

class TirgnonoseFibaluseVisionPvAffinite(Tirgnonose, FibaluseVision, FibalusePv, FibaluseAffinite):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vision, sa régénération de PV et son affinité à un élément."""

class TirgnonoseFibaluseVisionPvAffiniteMixte(Tirgnonose, FibaluseVision, FibalusePv, FibaluseAffinite, MaladieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vision, sa régénération de PV et son affinité à un élément, et qui peut survivre sur une case."""

class TirgnonoseFibaluseVisionPvIbsutiomialgie(Tirgnonose, FibaluseVision, FibalusePv, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vision, sa régénération de PV et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseVisionPvIbsutiomialgieMixte(Tirgnonose, FibaluseVision, FibalusePv, IbsutiomialgieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vision, sa régénération de PV et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class TirgnonoseFibaluseVisionPmVitesse(Tirgnonose, FibaluseVision, FibalusePm, FibaluseVitesse):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vision, sa régénération de PM et sa vitesse."""

class TirgnonoseFibaluseVisionPmVitesseMixte(Tirgnonose, FibaluseVision, FibalusePm, FibaluseVitesse, MaladieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vision, sa régénération de PM et sa vitesse, et qui peut survivre sur une case."""

class TirgnonoseFibaluseVisionPmAffinite(Tirgnonose, FibaluseVision, FibalusePm, FibaluseAffinite):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vision, sa régénération de PM et son affinité à un élément."""

class TirgnonoseFibaluseVisionPmAffiniteMixte(Tirgnonose, FibaluseVision, FibalusePm, FibaluseAffinite, MaladieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vision, sa régénération de PM et son affinité à un élément, et qui peut survivre sur une case."""

class TirgnonoseFibaluseVisionPmIbsutiomialgie(Tirgnonose, FibaluseVision, FibalusePm, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vision, sa régénération de PM et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseVisionPmIbsutiomialgieMixte(Tirgnonose, FibaluseVision, FibalusePm, IbsutiomialgieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vision, sa régénération de PM et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class TirgnonoseFibaluseVisionVitesseAffinite(Tirgnonose, FibaluseVision, FibaluseVitesse, FibaluseAffinite):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vision, sa vitesse et son affinité à un élément."""

class TirgnonoseFibaluseVisionVitesseAffiniteMixte(Tirgnonose, FibaluseVision, FibaluseVitesse, FibaluseAffinite, MaladieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vision, sa vitesse et son affinité à un élément, et qui peut survivre sur une case."""

class TirgnonoseFibaluseVisionVitesseIbsutiomialgie(Tirgnonose, FibaluseVision, FibaluseVitesse, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vision, sa vitesse et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseVisionVitesseIbsutiomialgieMixte(Tirgnonose, FibaluseVision, FibaluseVitesse, IbsutiomialgieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vision, sa vitesse et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class TirgnonoseFibaluseVisionAffiniteIbsutiomialgie(Tirgnonose, FibaluseVision, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vision, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseVisionAffiniteIbsutiomialgieMixte(Tirgnonose, FibaluseVision, FibaluseAffinite, IbsutiomialgieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vision, son affinité à un élément et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class TirgnonoseFibalusePvPmVitesse(Tirgnonose, FibalusePv, FibalusePm, FibaluseVitesse):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa régénération de PV, de PM et sa vitesse."""

class TirgnonoseFibalusePvPmVitesseMixte(Tirgnonose, FibalusePv, FibalusePm, FibaluseVitesse, MaladieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa régénération de PV, de PM et sa vitesse, et qui peut survivre sur une case."""

class TirgnonoseFibalusePvPmAffinite(Tirgnonose, FibalusePv, FibalusePm, FibaluseAffinite):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa régénération de PV, de PM et son affinité à un élément."""

class TirgnonoseFibalusePvPmAffiniteMixte(Tirgnonose, FibalusePv, FibalusePm, FibaluseAffinite, MaladieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa régénération de PV, de PM et son affinité à un élément, et qui peut survivre sur une case."""

class TirgnonoseFibalusePvPmIbsutiomialgie(Tirgnonose, FibalusePv, FibalusePm, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa régénération de PV, de PM et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibalusePvPmIbsutiomialgieMixte(Tirgnonose, FibalusePv, FibalusePm, IbsutiomialgieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa régénération de PV, de PM et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class TirgnonoseFibalusePvVitesseAffinite(Tirgnonose, FibalusePv, FibaluseVitesse, FibaluseAffinite):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa régénération de PV, sa vitesse et son affinité à un élément."""

class TirgnonoseFibalusePvVitesseAffiniteMixte(Tirgnonose, FibalusePv, FibaluseVitesse, FibaluseAffinite, MaladieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa régénération de PV, sa vitesse et son affinité à un élément, et qui peut survivre sur une case."""

class TirgnonoseFibalusePvVitesseIbsutiomialgie(Tirgnonose, FibalusePv, FibaluseVitesse, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa régénération de PV, sa vitesse et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibalusePvVitesseIbsutiomialgieMixte(Tirgnonose, FibalusePv, FibaluseVitesse, IbsutiomialgieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa régénération de PV, sa vitesse et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class TirgnonoseFibalusePvAffiniteIbsutiomialgie(Tirgnonose, FibalusePv, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa régénération de PV, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibalusePvAffiniteIbsutiomialgieMixte(Tirgnonose, FibalusePv, FibaluseAffinite, IbsutiomialgieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa régénération de PV, son affinité à un élément et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class TirgnonoseFibalusePmVitesseAffinite(Tirgnonose, FibalusePm, FibaluseVitesse, FibaluseAffinite):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa régénération de PM, sa vitesse et son affinité à un élément."""

class TirgnonoseFibalusePmVitesseAffiniteMixte(Tirgnonose, FibalusePm, FibaluseVitesse, FibaluseAffinite, MaladieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa régénération de PM, sa vitesse et son affinité à un élément, et qui peut survivre sur une case."""

class TirgnonoseFibalusePmVitesseIbsutiomialgie(Tirgnonose, FibalusePm, FibaluseVitesse, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa régénération de PM, sa vitesse et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibalusePmVitesseIbsutiomialgieMixte(Tirgnonose, FibalusePm, FibaluseVitesse, IbsutiomialgieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa régénération de PM, sa vitesse et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class TirgnonoseFibalusePmAffiniteIbsutiomialgie(Tirgnonose, FibalusePm, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa régénération de PM, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibalusePmAffiniteIbsutiomialgieMixte(Tirgnonose, FibalusePm, FibaluseAffinite, IbsutiomialgieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa régénération de PM, son affinité à un élément et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class TirgnonoseFibaluseVitesseAffiniteIbsutiomialgie(Tirgnonose, FibaluseVitesse, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vitesse, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseVitesseAffiniteIbsutiomialgieMixte(Tirgnonose, FibaluseVitesse, FibaluseAffinite, IbsutiomialgieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vitesse, son affinité à un élément et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class FibaluseForceVisionPvPm(FibaluseForce, FibaluseVision, FibalusePv, FibalusePm):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vision, sa régénération de PV et de PM."""

class FibaluseForceVisionPvPmMixte(FibaluseForce, FibaluseVision, FibalusePv, FibalusePm, MaladieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vision, sa régénération de PV et de PM, et qui peut survivre sur une case."""

class FibaluseForceVisionPvVitesse(FibaluseForce, FibaluseVision, FibalusePv, FibaluseVitesse):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vision, sa régénération de PV et sa vitesse."""

class FibaluseForceVisionPvVitesseMixte(FibaluseForce, FibaluseVision, FibalusePv, FibaluseVitesse, MaladieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vision, sa régénération de PV et sa vitesse, et qui peut survivre sur une case."""

class FibaluseForceVisionPvAffinite(FibaluseForce, FibaluseVision, FibalusePv, FibaluseAffinite):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vision, sa régénération de PV et son affinité à un élément."""

class FibaluseForceVisionPvAffiniteMixte(FibaluseForce, FibaluseVision, FibalusePv, FibaluseAffinite, MaladieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vision, sa régénération de PV et son affinité à un élément, et qui peut survivre sur une case."""

class FibaluseForceVisionPvIbsutiomialgie(FibaluseForce, FibaluseVision, FibalusePv, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vision, sa régénération de PV et peut le tuer de façon subite (ibsute)."""

class FibaluseForceVisionPvIbsutiomialgieMixte(FibaluseForce, FibaluseVision, FibalusePv, IbsutiomialgieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vision, sa régénération de PV et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class FibaluseForceVisionPmVitesse(FibaluseForce, FibaluseVision, FibalusePm, FibaluseVitesse):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vision, sa régénération de PM et sa vitesse."""

class FibaluseForceVisionPmVitesseMixte(FibaluseForce, FibaluseVision, FibalusePm, FibaluseVitesse, MaladieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vision, sa régénération de PM et sa vitesse, et qui peut survivre sur une case."""

class FibaluseForceVisionPmAffinite(FibaluseForce, FibaluseVision, FibalusePm, FibaluseAffinite):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vision, sa régénération de PM et son affinité à un élément."""

class FibaluseForceVisionPmAffiniteMixte(FibaluseForce, FibaluseVision, FibalusePm, FibaluseAffinite, MaladieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vision, sa régénération de PM et son affinité à un élément, et qui peut survivre sur une case."""

class FibaluseForceVisionPmIbsutiomialgie(FibaluseForce, FibaluseVision, FibalusePm, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vision, sa régénération de PM et peut le tuer de façon subite (ibsute)."""

class FibaluseForceVisionPmIbsutiomialgieMixte(FibaluseForce, FibaluseVision, FibalusePm, IbsutiomialgieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vision, sa régénération de PM et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class FibaluseForceVisionVitesseAffinite(FibaluseForce, FibaluseVision, FibaluseVitesse, FibaluseAffinite):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vision, sa vitesse et son affinité à un élément."""

class FibaluseForceVisionVitesseAffiniteMixte(FibaluseForce, FibaluseVision, FibaluseVitesse, FibaluseAffinite, MaladieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vision, sa vitesse et son affinité à un élément, et qui peut survivre sur une case."""

class FibaluseForceVisionVitesseIbsutiomialgie(FibaluseForce, FibaluseVision, FibaluseVitesse, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vision, sa vitesse et peut le tuer de façon subite (ibsute)."""

class FibaluseForceVisionVitesseIbsutiomialgieMixte(FibaluseForce, FibaluseVision, FibaluseVitesse, IbsutiomialgieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vision, sa vitesse et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class FibaluseForceVisionAffiniteIbsutiomialgie(FibaluseForce, FibaluseVision, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vision, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class FibaluseForceVisionAffiniteIbsutiomialgieMixte(FibaluseForce, FibaluseVision, FibaluseAffinite, IbsutiomialgieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vision, son affinité à un élément et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class FibaluseForcePvPmVitesse(FibaluseForce, FibalusePv, FibalusePm, FibaluseVitesse):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa régénération de PV, de PM et sa vitesse."""

class FibaluseForcePvPmVitesseMixte(FibaluseForce, FibalusePv, FibalusePm, FibaluseVitesse, MaladieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa régénération de PV, de PM et sa vitesse, et qui peut survivre sur une case."""

class FibaluseForcePvPmAffinite(FibaluseForce, FibalusePv, FibalusePm, FibaluseAffinite):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa régénération de PV, de PM et son affinité à un élément."""

class FibaluseForcePvPmAffiniteMixte(FibaluseForce, FibalusePv, FibalusePm, FibaluseAffinite, MaladieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa régénération de PV, de PM et son affinité à un élément, et qui peut survivre sur une case."""

class FibaluseForcePvPmIbsutiomialgie(FibaluseForce, FibalusePv, FibalusePm, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa régénération de PV, de PM et peut le tuer de façon subite (ibsute)."""

class FibaluseForcePvPmIbsutiomialgieMixte(FibaluseForce, FibalusePv, FibalusePm, IbsutiomialgieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa régénération de PV, de PM et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class FibaluseForcePvVitesseAffinite(FibaluseForce, FibalusePv, FibaluseVitesse, FibaluseAffinite):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa régénération de PV, sa vitesse et son affinité à un élément."""

class FibaluseForcePvVitesseAffiniteMixte(FibaluseForce, FibalusePv, FibaluseVitesse, FibaluseAffinite, MaladieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa régénération de PV, sa vitesse et son affinité à un élément, et qui peut survivre sur une case."""

class FibaluseForcePvVitesseIbsutiomialgie(FibaluseForce, FibalusePv, FibaluseVitesse, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa régénération de PV, sa vitesse et peut le tuer de façon subite (ibsute)."""

class FibaluseForcePvVitesseIbsutiomialgieMixte(FibaluseForce, FibalusePv, FibaluseVitesse, IbsutiomialgieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa régénération de PV, sa vitesse et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class FibaluseForcePvAffiniteIbsutiomialgie(FibaluseForce, FibalusePv, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa régénération de PV, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class FibaluseForcePvAffiniteIbsutiomialgieMixte(FibaluseForce, FibalusePv, FibaluseAffinite, IbsutiomialgieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa régénération de PV, son affinité à un élément et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class FibaluseForcePmVitesseAffinite(FibaluseForce, FibalusePm, FibaluseVitesse, FibaluseAffinite):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa régénération de PM, sa vitesse et son affinité à un élément."""

class FibaluseForcePmVitesseAffiniteMixte(FibaluseForce, FibalusePm, FibaluseVitesse, FibaluseAffinite, MaladieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa régénération de PM, sa vitesse et son affinité à un élément, et qui peut survivre sur une case."""

class FibaluseForcePmVitesseIbsutiomialgie(FibaluseForce, FibalusePm, FibaluseVitesse, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa régénération de PM, sa vitesse et peut le tuer de façon subite (ibsute)."""

class FibaluseForcePmVitesseIbsutiomialgieMixte(FibaluseForce, FibalusePm, FibaluseVitesse, IbsutiomialgieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa régénération de PM, sa vitesse et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class FibaluseForcePmAffiniteIbsutiomialgie(FibaluseForce, FibalusePm, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa régénération de PM, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class FibaluseForcePmAffiniteIbsutiomialgieMixte(FibaluseForce, FibalusePm, FibaluseAffinite, IbsutiomialgieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa régénération de PM, son affinité à un élément et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class FibaluseForceVitesseAffiniteIbsutiomialgie(FibaluseForce, FibaluseVitesse, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vitesse, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class FibaluseForceVitesseAffiniteIbsutiomialgieMixte(FibaluseForce, FibaluseVitesse, FibaluseAffinite, IbsutiomialgieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vitesse, son affinité à un élément et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class FibaluseVisionPvPmVitesse(FibaluseVision, FibalusePv, FibalusePm, FibaluseVitesse):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vision, sa régénération de PV, de PM et sa vitesse."""

class FibaluseVisionPvPmVitesseMixte(FibaluseVision, FibalusePv, FibalusePm, FibaluseVitesse, MaladieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vision, sa régénération de PV, de PM et sa vitesse, et qui peut survivre sur une case."""

class FibaluseVisionPvPmAffinite(FibaluseVision, FibalusePv, FibalusePm, FibaluseAffinite):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vision, sa régénération de PV, de PM et son affinité à un élément."""

class FibaluseVisionPvPmAffiniteMixte(FibaluseVision, FibalusePv, FibalusePm, FibaluseAffinite, MaladieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vision, sa régénération de PV, de PM et son affinité à un élément, et qui peut survivre sur une case."""

class FibaluseVisionPvPmIbsutiomialgie(FibaluseVision, FibalusePv, FibalusePm, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vision, sa régénération de PV, de PM et peut le tuer de façon subite (ibsute)."""

class FibaluseVisionPvPmIbsutiomialgieMixte(FibaluseVision, FibalusePv, FibalusePm, IbsutiomialgieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vision, sa régénération de PV, de PM et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class FibaluseVisionPvVitesseAffinite(FibaluseVision, FibalusePv, FibaluseVitesse, FibaluseAffinite):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vision, sa régénération de PV, sa vitesse et son affinité à un élément."""

class FibaluseVisionPvVitesseAffiniteMixte(FibaluseVision, FibalusePv, FibaluseVitesse, FibaluseAffinite, MaladieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vision, sa régénération de PV, sa vitesse et son affinité à un élément, et qui peut survivre sur une case."""

class FibaluseVisionPvVitesseIbsutiomialgie(FibaluseVision, FibalusePv, FibaluseVitesse, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vision, sa régénération de PV, sa vitesse et peut le tuer de façon subite (ibsute)."""

class FibaluseVisionPvVitesseIbsutiomialgieMixte(FibaluseVision, FibalusePv, FibaluseVitesse, IbsutiomialgieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vision, sa régénération de PV, sa vitesse et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class FibaluseVisionPvAffiniteIbsutiomialgie(FibaluseVision, FibalusePv, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vision, sa régénération de PV, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class FibaluseVisionPvAffiniteIbsutiomialgieMixte(FibaluseVision, FibalusePv, FibaluseAffinite, IbsutiomialgieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vision, sa régénération de PV, son affinité à un élément et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class FibaluseVisionPmVitesseAffinite(FibaluseVision, FibalusePm, FibaluseVitesse, FibaluseAffinite):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vision, sa régénération de PM, sa vitesse et son affinité à un élément."""

class FibaluseVisionPmVitesseAffiniteMixte(FibaluseVision, FibalusePm, FibaluseVitesse, FibaluseAffinite, MaladieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vision, sa régénération de PM, sa vitesse et son affinité à un élément, et qui peut survivre sur une case."""

class FibaluseVisionPmVitesseIbsutiomialgie(FibaluseVision, FibalusePm, FibaluseVitesse, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vision, sa régénération de PM, sa vitesse et peut le tuer de façon subite (ibsute)."""

class FibaluseVisionPmVitesseIbsutiomialgieMixte(FibaluseVision, FibalusePm, FibaluseVitesse, IbsutiomialgieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vision, sa régénération de PM, sa vitesse et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class FibaluseVisionPmAffiniteIbsutiomialgie(FibaluseVision, FibalusePm, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vision, sa régénération de PM, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class FibaluseVisionPmAffiniteIbsutiomialgieMixte(FibaluseVision, FibalusePm, FibaluseAffinite, IbsutiomialgieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vision, sa régénération de PM, son affinité à un élément et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class FibaluseVisionVitesseAffiniteIbsutiomialgie(FibaluseVision, FibaluseVitesse, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vision, sa vitesse, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class FibaluseVisionVitesseAffiniteIbsutiomialgieMixte(FibaluseVision, FibaluseVitesse, FibaluseAffinite, IbsutiomialgieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vision, sa vitesse, son affinité à un élément et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class FibalusePvPmVitesseAffinite(FibalusePv, FibalusePm, FibaluseVitesse, FibaluseAffinite):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa régénération de PV, de PM, sa vitesse et son affinité à un élément."""

class FibalusePvPmVitesseAffiniteMixte(FibalusePv, FibalusePm, FibaluseVitesse, FibaluseAffinite, MaladieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa régénération de PV, de PM, sa vitesse et son affinité à un élément, et qui peut survivre sur une case."""

class FibalusePvPmVitesseIbsutiomialgie(FibalusePv, FibalusePm, FibaluseVitesse, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa régénération de PV, de PM, sa vitesse et peut le tuer de façon subite (ibsute)."""

class FibalusePvPmVitesseIbsutiomialgieMixte(FibalusePv, FibalusePm, FibaluseVitesse, IbsutiomialgieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa régénération de PV, de PM, sa vitesse et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class FibalusePvPmAffiniteIbsutiomialgie(FibalusePv, FibalusePm, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa régénération de PV, de PM, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class FibalusePvPmAffiniteIbsutiomialgieMixte(FibalusePv, FibalusePm, FibaluseAffinite, IbsutiomialgieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa régénération de PV, de PM, son affinité à un élément et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class FibalusePvVitesseAffiniteIbsutiomialgie(FibalusePv, FibaluseVitesse, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa régénération de PV, sa vitesse, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class FibalusePvVitesseAffiniteIbsutiomialgieMixte(FibalusePv, FibaluseVitesse, FibaluseAffinite, IbsutiomialgieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa régénération de PV, sa vitesse, son affinité à un élément et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class FibalusePmVitesseAffiniteIbsutiomialgie(FibalusePm, FibaluseVitesse, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa régénération de PM, sa vitesse, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class FibalusePmVitesseAffiniteIbsutiomialgieMixte(FibalusePm, FibaluseVitesse, FibaluseAffinite, IbsutiomialgieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa régénération de PM, sa vitesse, son affinité à un élément et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class TirgnonoseFibaluseForceVisionPvPm(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePv, FibalusePm):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vision, sa régénération de PV et de PM."""

class TirgnonoseFibaluseForceVisionPvPmMixte(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePv, FibalusePm, MaladieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vision, sa régénération de PV et de PM, et qui peut survivre sur une case."""

class TirgnonoseFibaluseForceVisionPvVitesse(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePv, FibaluseVitesse):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vision, sa régénération de PV et sa vitesse."""

class TirgnonoseFibaluseForceVisionPvVitesseMixte(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePv, FibaluseVitesse, MaladieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vision, sa régénération de PV et sa vitesse, et qui peut survivre sur une case."""

class TirgnonoseFibaluseForceVisionPvAffinite(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePv, FibaluseAffinite):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vision, sa régénération de PV et son affinité à un élément."""

class TirgnonoseFibaluseForceVisionPvAffiniteMixte(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePv, FibaluseAffinite, MaladieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vision, sa régénération de PV et son affinité à un élément, et qui peut survivre sur une case."""

class TirgnonoseFibaluseForceVisionPvIbsutiomialgie(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePv, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vision, sa régénération de PV et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseForceVisionPvIbsutiomialgieMixte(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePv, IbsutiomialgieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vision, sa régénération de PV et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class TirgnonoseFibaluseForceVisionPmVitesse(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePm, FibaluseVitesse):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vision, sa régénération de PM et sa vitesse."""

class TirgnonoseFibaluseForceVisionPmVitesseMixte(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePm, FibaluseVitesse, MaladieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vision, sa régénération de PM et sa vitesse, et qui peut survivre sur une case."""

class TirgnonoseFibaluseForceVisionPmAffinite(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePm, FibaluseAffinite):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vision, sa régénération de PM et son affinité à un élément."""

class TirgnonoseFibaluseForceVisionPmAffiniteMixte(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePm, FibaluseAffinite, MaladieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vision, sa régénération de PM et son affinité à un élément, et qui peut survivre sur une case."""

class TirgnonoseFibaluseForceVisionPmIbsutiomialgie(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePm, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vision, sa régénération de PM et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseForceVisionPmIbsutiomialgieMixte(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePm, IbsutiomialgieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vision, sa régénération de PM et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class TirgnonoseFibaluseForceVisionVitesseAffinite(Tirgnonose, FibaluseForce, FibaluseVision, FibaluseVitesse, FibaluseAffinite):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vision, sa vitesse et son affinité à un élément."""

class TirgnonoseFibaluseForceVisionVitesseAffiniteMixte(Tirgnonose, FibaluseForce, FibaluseVision, FibaluseVitesse, FibaluseAffinite, MaladieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vision, sa vitesse et son affinité à un élément, et qui peut survivre sur une case."""

class TirgnonoseFibaluseForceVisionVitesseIbsutiomialgie(Tirgnonose, FibaluseForce, FibaluseVision, FibaluseVitesse, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vision, sa vitesse et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseForceVisionVitesseIbsutiomialgieMixte(Tirgnonose, FibaluseForce, FibaluseVision, FibaluseVitesse, IbsutiomialgieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vision, sa vitesse et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class TirgnonoseFibaluseForceVisionAffiniteIbsutiomialgie(Tirgnonose, FibaluseForce, FibaluseVision, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vision, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseForceVisionAffiniteIbsutiomialgieMixte(Tirgnonose, FibaluseForce, FibaluseVision, FibaluseAffinite, IbsutiomialgieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vision, son affinité à un élément et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class TirgnonoseFibaluseForcePvPmVitesse(Tirgnonose, FibaluseForce, FibalusePv, FibalusePm, FibaluseVitesse):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa régénération de PV, de PM et sa vitesse."""

class TirgnonoseFibaluseForcePvPmVitesseMixte(Tirgnonose, FibaluseForce, FibalusePv, FibalusePm, FibaluseVitesse, MaladieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa régénération de PV, de PM et sa vitesse, et qui peut survivre sur une case."""

class TirgnonoseFibaluseForcePvPmAffinite(Tirgnonose, FibaluseForce, FibalusePv, FibalusePm, FibaluseAffinite):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa régénération de PV, de PM et son affinité à un élément."""

class TirgnonoseFibaluseForcePvPmAffiniteMixte(Tirgnonose, FibaluseForce, FibalusePv, FibalusePm, FibaluseAffinite, MaladieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa régénération de PV, de PM et son affinité à un élément, et qui peut survivre sur une case."""

class TirgnonoseFibaluseForcePvPmIbsutiomialgie(Tirgnonose, FibaluseForce, FibalusePv, FibalusePm, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa régénération de PV, de PM et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseForcePvPmIbsutiomialgieMixte(Tirgnonose, FibaluseForce, FibalusePv, FibalusePm, IbsutiomialgieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa régénération de PV, de PM et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class TirgnonoseFibaluseForcePvVitesseAffinite(Tirgnonose, FibaluseForce, FibalusePv, FibaluseVitesse, FibaluseAffinite):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa régénération de PV, sa vitesse et son affinité à un élément."""

class TirgnonoseFibaluseForcePvVitesseAffiniteMixte(Tirgnonose, FibaluseForce, FibalusePv, FibaluseVitesse, FibaluseAffinite, MaladieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa régénération de PV, sa vitesse et son affinité à un élément, et qui peut survivre sur une case."""

class TirgnonoseFibaluseForcePvVitesseIbsutiomialgie(Tirgnonose, FibaluseForce, FibalusePv, FibaluseVitesse, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa régénération de PV, sa vitesse et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseForcePvVitesseIbsutiomialgieMixte(Tirgnonose, FibaluseForce, FibalusePv, FibaluseVitesse, IbsutiomialgieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa régénération de PV, sa vitesse et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class TirgnonoseFibaluseForcePvAffiniteIbsutiomialgie(Tirgnonose, FibaluseForce, FibalusePv, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa régénération de PV, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseForcePvAffiniteIbsutiomialgieMixte(Tirgnonose, FibaluseForce, FibalusePv, FibaluseAffinite, IbsutiomialgieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa régénération de PV, son affinité à un élément et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class TirgnonoseFibaluseForcePmVitesseAffinite(Tirgnonose, FibaluseForce, FibalusePm, FibaluseVitesse, FibaluseAffinite):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa régénération de PM, sa vitesse et son affinité à un élément."""

class TirgnonoseFibaluseForcePmVitesseAffiniteMixte(Tirgnonose, FibaluseForce, FibalusePm, FibaluseVitesse, FibaluseAffinite, MaladieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa régénération de PM, sa vitesse et son affinité à un élément, et qui peut survivre sur une case."""

class TirgnonoseFibaluseForcePmVitesseIbsutiomialgie(Tirgnonose, FibaluseForce, FibalusePm, FibaluseVitesse, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa régénération de PM, sa vitesse et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseForcePmVitesseIbsutiomialgieMixte(Tirgnonose, FibaluseForce, FibalusePm, FibaluseVitesse, IbsutiomialgieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa régénération de PM, sa vitesse et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class TirgnonoseFibaluseForcePmAffiniteIbsutiomialgie(Tirgnonose, FibaluseForce, FibalusePm, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa régénération de PM, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseForcePmAffiniteIbsutiomialgieMixte(Tirgnonose, FibaluseForce, FibalusePm, FibaluseAffinite, IbsutiomialgieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa régénération de PM, son affinité à un élément et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class TirgnonoseFibaluseForceVitesseAffiniteIbsutiomialgie(Tirgnonose, FibaluseForce, FibaluseVitesse, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vitesse, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseForceVitesseAffiniteIbsutiomialgieMixte(Tirgnonose, FibaluseForce, FibaluseVitesse, FibaluseAffinite, IbsutiomialgieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vitesse, son affinité à un élément et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class TirgnonoseFibaluseVisionPvPmVitesse(Tirgnonose, FibaluseVision, FibalusePv, FibalusePm, FibaluseVitesse):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vision, sa régénération de PV, de PM et sa vitesse."""

class TirgnonoseFibaluseVisionPvPmVitesseMixte(Tirgnonose, FibaluseVision, FibalusePv, FibalusePm, FibaluseVitesse, MaladieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vision, sa régénération de PV, de PM et sa vitesse, et qui peut survivre sur une case."""

class TirgnonoseFibaluseVisionPvPmAffinite(Tirgnonose, FibaluseVision, FibalusePv, FibalusePm, FibaluseAffinite):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vision, sa régénération de PV, de PM et son affinité à un élément."""

class TirgnonoseFibaluseVisionPvPmAffiniteMixte(Tirgnonose, FibaluseVision, FibalusePv, FibalusePm, FibaluseAffinite, MaladieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vision, sa régénération de PV, de PM et son affinité à un élément, et qui peut survivre sur une case."""

class TirgnonoseFibaluseVisionPvPmIbsutiomialgie(Tirgnonose, FibaluseVision, FibalusePv, FibalusePm, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vision, sa régénération de PV, de PM et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseVisionPvPmIbsutiomialgieMixte(Tirgnonose, FibaluseVision, FibalusePv, FibalusePm, IbsutiomialgieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vision, sa régénération de PV, de PM et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class TirgnonoseFibaluseVisionPvVitesseAffinite(Tirgnonose, FibaluseVision, FibalusePv, FibaluseVitesse, FibaluseAffinite):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vision, sa régénération de PV, sa vitesse et son affinité à un élément."""

class TirgnonoseFibaluseVisionPvVitesseAffiniteMixte(Tirgnonose, FibaluseVision, FibalusePv, FibaluseVitesse, FibaluseAffinite, MaladieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vision, sa régénération de PV, sa vitesse et son affinité à un élément, et qui peut survivre sur une case."""

class TirgnonoseFibaluseVisionPvVitesseIbsutiomialgie(Tirgnonose, FibaluseVision, FibalusePv, FibaluseVitesse, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vision, sa régénération de PV, sa vitesse et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseVisionPvVitesseIbsutiomialgieMixte(Tirgnonose, FibaluseVision, FibalusePv, FibaluseVitesse, IbsutiomialgieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vision, sa régénération de PV, sa vitesse et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class TirgnonoseFibaluseVisionPvAffiniteIbsutiomialgie(Tirgnonose, FibaluseVision, FibalusePv, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vision, sa régénération de PV, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseVisionPvAffiniteIbsutiomialgieMixte(Tirgnonose, FibaluseVision, FibalusePv, FibaluseAffinite, IbsutiomialgieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vision, sa régénération de PV, son affinité à un élément et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class TirgnonoseFibaluseVisionPmVitesseAffinite(Tirgnonose, FibaluseVision, FibalusePm, FibaluseVitesse, FibaluseAffinite):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vision, sa régénération de PM, sa vitesse et son affinité à un élément."""

class TirgnonoseFibaluseVisionPmVitesseAffiniteMixte(Tirgnonose, FibaluseVision, FibalusePm, FibaluseVitesse, FibaluseAffinite, MaladieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vision, sa régénération de PM, sa vitesse et son affinité à un élément, et qui peut survivre sur une case."""

class TirgnonoseFibaluseVisionPmVitesseIbsutiomialgie(Tirgnonose, FibaluseVision, FibalusePm, FibaluseVitesse, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vision, sa régénération de PM, sa vitesse et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseVisionPmVitesseIbsutiomialgieMixte(Tirgnonose, FibaluseVision, FibalusePm, FibaluseVitesse, IbsutiomialgieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vision, sa régénération de PM, sa vitesse et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class TirgnonoseFibaluseVisionPmAffiniteIbsutiomialgie(Tirgnonose, FibaluseVision, FibalusePm, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vision, sa régénération de PM, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseVisionPmAffiniteIbsutiomialgieMixte(Tirgnonose, FibaluseVision, FibalusePm, FibaluseAffinite, IbsutiomialgieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vision, sa régénération de PM, son affinité à un élément et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class TirgnonoseFibaluseVisionVitesseAffiniteIbsutiomialgie(Tirgnonose, FibaluseVision, FibaluseVitesse, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vision, sa vitesse, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseVisionVitesseAffiniteIbsutiomialgieMixte(Tirgnonose, FibaluseVision, FibaluseVitesse, FibaluseAffinite, IbsutiomialgieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vision, sa vitesse, son affinité à un élément et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class TirgnonoseFibalusePvPmVitesseAffinite(Tirgnonose, FibalusePv, FibalusePm, FibaluseVitesse, FibaluseAffinite):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa régénération de PV, de PM, sa vitesse et son affinité à un élément."""

class TirgnonoseFibalusePvPmVitesseAffiniteMixte(Tirgnonose, FibalusePv, FibalusePm, FibaluseVitesse, FibaluseAffinite, MaladieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa régénération de PV, de PM, sa vitesse et son affinité à un élément, et qui peut survivre sur une case."""

class TirgnonoseFibalusePvPmVitesseIbsutiomialgie(Tirgnonose, FibalusePv, FibalusePm, FibaluseVitesse, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa régénération de PV, de PM, sa vitesse et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibalusePvPmVitesseIbsutiomialgieMixte(Tirgnonose, FibalusePv, FibalusePm, FibaluseVitesse, IbsutiomialgieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa régénération de PV, de PM, sa vitesse et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class TirgnonoseFibalusePvPmAffiniteIbsutiomialgie(Tirgnonose, FibalusePv, FibalusePm, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa régénération de PV, de PM, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibalusePvPmAffiniteIbsutiomialgieMixte(Tirgnonose, FibalusePv, FibalusePm, FibaluseAffinite, IbsutiomialgieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa régénération de PV, de PM, son affinité à un élément et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class TirgnonoseFibalusePvVitesseAffiniteIbsutiomialgie(Tirgnonose, FibalusePv, FibaluseVitesse, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa régénération de PV, sa vitesse, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibalusePvVitesseAffiniteIbsutiomialgieMixte(Tirgnonose, FibalusePv, FibaluseVitesse, FibaluseAffinite, IbsutiomialgieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa régénération de PV, sa vitesse, son affinité à un élément et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class TirgnonoseFibalusePmVitesseAffiniteIbsutiomialgie(Tirgnonose, FibalusePm, FibaluseVitesse, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa régénération de PM, sa vitesse, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibalusePmVitesseAffiniteIbsutiomialgieMixte(Tirgnonose, FibalusePm, FibaluseVitesse, FibaluseAffinite, IbsutiomialgieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa régénération de PM, sa vitesse, son affinité à un élément et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class FibaluseForceVisionPvPmVitesse(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePv, FibalusePm, FibaluseVitesse):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vision, sa régénération de PV, de PM et sa vitesse."""

class FibaluseForceVisionPvPmVitesseMixte(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePv, FibalusePm, FibaluseVitesse, MaladieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vision, sa régénération de PV, de PM et sa vitesse, et qui peut survivre sur une case."""

class FibaluseForceVisionPvPmAffinite(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePv, FibalusePm, FibaluseAffinite):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vision, sa régénération de PV, de PM et son affinité à un élément."""

class FibaluseForceVisionPvPmAffiniteMixte(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePv, FibalusePm, FibaluseAffinite, MaladieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vision, sa régénération de PV, de PM et son affinité à un élément, et qui peut survivre sur une case."""

class FibaluseForceVisionPvPmIbsutiomialgie(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePv, FibalusePm, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vision, sa régénération de PV, de PM et peut le tuer de façon subite (ibsute)."""

class FibaluseForceVisionPvPmIbsutiomialgieMixte(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePv, FibalusePm, IbsutiomialgieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vision, sa régénération de PV, de PM et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class FibaluseForceVisionPvVitesseAffinite(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePv, FibaluseVitesse, FibaluseAffinite):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vision, sa régénération de PV, sa vitesse et son affinité à un élément."""

class FibaluseForceVisionPvVitesseAffiniteMixte(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePv, FibaluseVitesse, FibaluseAffinite, MaladieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vision, sa régénération de PV, sa vitesse et son affinité à un élément, et qui peut survivre sur une case."""

class FibaluseForceVisionPvVitesseIbsutiomialgie(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePv, FibaluseVitesse, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vision, sa régénération de PV, sa vitesse et peut le tuer de façon subite (ibsute)."""

class FibaluseForceVisionPvVitesseIbsutiomialgieMixte(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePv, FibaluseVitesse, IbsutiomialgieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vision, sa régénération de PV, sa vitesse et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class FibaluseForceVisionPvAffiniteIbsutiomialgie(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePv, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vision, sa régénération de PV, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class FibaluseForceVisionPvAffiniteIbsutiomialgieMixte(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePv, FibaluseAffinite, IbsutiomialgieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vision, sa régénération de PV, son affinité à un élément et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class FibaluseForceVisionPmVitesseAffinite(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePm, FibaluseVitesse, FibaluseAffinite):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vision, sa régénération de PM, sa vitesse et son affinité à un élément."""

class FibaluseForceVisionPmVitesseAffiniteMixte(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePm, FibaluseVitesse, FibaluseAffinite, MaladieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vision, sa régénération de PM, sa vitesse et son affinité à un élément, et qui peut survivre sur une case."""

class FibaluseForceVisionPmVitesseIbsutiomialgie(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePm, FibaluseVitesse, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vision, sa régénération de PM, sa vitesse et peut le tuer de façon subite (ibsute)."""

class FibaluseForceVisionPmVitesseIbsutiomialgieMixte(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePm, FibaluseVitesse, IbsutiomialgieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vision, sa régénération de PM, sa vitesse et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class FibaluseForceVisionPmAffiniteIbsutiomialgie(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePm, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vision, sa régénération de PM, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class FibaluseForceVisionPmAffiniteIbsutiomialgieMixte(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePm, FibaluseAffinite, IbsutiomialgieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vision, sa régénération de PM, son affinité à un élément et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class FibaluseForceVisionVitesseAffiniteIbsutiomialgie(Tirgnonose, FibaluseForce, FibaluseVision, FibaluseVitesse, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vision, sa vitesse, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class FibaluseForceVisionVitesseAffiniteIbsutiomialgieMixte(Tirgnonose, FibaluseForce, FibaluseVision, FibaluseVitesse, FibaluseAffinite, IbsutiomialgieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vision, sa vitesse, son affinité à un élément et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class FibaluseForcePvPmVitesseAffinite(Tirgnonose, FibaluseForce, FibalusePv, FibalusePm, FibaluseVitesse, FibaluseAffinite):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa régénération de PV, de PM, sa vitesse et son affinité à un élément."""

class FibaluseForcePvPmVitesseAffiniteMixte(Tirgnonose, FibaluseForce, FibalusePv, FibalusePm, FibaluseVitesse, FibaluseAffinite, MaladieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa régénération de PV, de PM, sa vitesse et son affinité à un élément, et qui peut survivre sur une case."""

class FibaluseForcePvPmVitesseIbsutiomialgie(Tirgnonose, FibaluseForce, FibalusePv, FibalusePm, FibaluseVitesse, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa régénération de PV, de PM, sa vitesse et peut le tuer de façon subite (ibsute)."""

class FibaluseForcePvPmVitesseIbsutiomialgieMixte(Tirgnonose, FibaluseForce, FibalusePv, FibalusePm, FibaluseVitesse, IbsutiomialgieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa régénération de PV, de PM, sa vitesse et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class FibaluseForcePvPmAffiniteIbsutiomialgie(Tirgnonose, FibaluseForce, FibalusePv, FibalusePm, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa régénération de PV, de PM, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class FibaluseForcePvPmAffiniteIbsutiomialgieMixte(Tirgnonose, FibaluseForce, FibalusePv, FibalusePm, FibaluseAffinite, IbsutiomialgieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa régénération de PV, de PM, son affinité à un élément et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class FibaluseForcePvVitesseAffiniteIbsutiomialgie(Tirgnonose, FibaluseForce, FibalusePv, FibaluseVitesse, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa régénération de PV, sa vitesse, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class FibaluseForcePvVitesseAffiniteIbsutiomialgieMixte(Tirgnonose, FibaluseForce, FibalusePv, FibaluseVitesse, FibaluseAffinite, IbsutiomialgieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa régénération de PV, sa vitesse, son affinité à un élément et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class FibaluseForcePmVitesseAffiniteIbsutiomialgie(Tirgnonose, FibaluseForce, FibalusePm, FibaluseVitesse, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa régénération de PM, sa vitesse, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class FibaluseForcePmVitesseAffiniteIbsutiomialgieMixte(Tirgnonose, FibaluseForce, FibalusePm, FibaluseVitesse, FibaluseAffinite, IbsutiomialgieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa régénération de PM, sa vitesse, son affinité à un élément et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class FibaluseVisionPvPmVitesseAffinite(Tirgnonose, FibaluseVision, FibalusePv, FibalusePm, FibaluseVitesse, FibaluseAffinite):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vision, sa régénération de PV, de PM, sa vitesse et son affinité à un élément."""

class FibaluseVisionPvPmVitesseAffiniteMixte(Tirgnonose, FibaluseVision, FibalusePv, FibalusePm, FibaluseVitesse, FibaluseAffinite, MaladieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vision, sa régénération de PV, de PM, sa vitesse et son affinité à un élément, et qui peut survivre sur une case."""

class FibaluseVisionPvPmVitesseIbsutiomialgie(Tirgnonose, FibaluseVision, FibalusePv, FibalusePm, FibaluseVitesse, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vision, sa régénération de PV, de PM, sa vitesse et peut le tuer de façon subite (ibsute)."""

class FibaluseVisionPvPmVitesseIbsutiomialgieMixte(Tirgnonose, FibaluseVision, FibalusePv, FibalusePm, FibaluseVitesse, IbsutiomialgieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vision, sa régénération de PV, de PM, sa vitesse et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class FibaluseVisionPvPmAffiniteIbsutiomialgie(Tirgnonose, FibaluseVision, FibalusePv, FibalusePm, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vision, sa régénération de PV, de PM, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class FibaluseVisionPvPmAffiniteIbsutiomialgieMixte(Tirgnonose, FibaluseVision, FibalusePv, FibalusePm, FibaluseAffinite, IbsutiomialgieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vision, sa régénération de PV, de PM, son affinité à un élément et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class FibaluseVisionPvVitesseAffiniteIbsutiomialgie(Tirgnonose, FibaluseVision, FibalusePv, FibaluseVitesse, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vision, sa régénération de PV, sa vitesse, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class FibaluseVisionPvVitesseAffiniteIbsutiomialgieMixte(Tirgnonose, FibaluseVision, FibalusePv, FibaluseVitesse, FibaluseAffinite, IbsutiomialgieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vision, sa régénération de PV, sa vitesse, son affinité à un élément et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class FibaluseVisionPmVitesseAffiniteIbsutiomialgie(Tirgnonose, FibaluseVision, FibalusePm, FibaluseVitesse, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vision, sa régénération de PM, sa vitesse, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class FibaluseVisionPmVitesseAffiniteIbsutiomialgieMixte(Tirgnonose, FibaluseVision, FibalusePm, FibaluseVitesse, FibaluseAffinite, IbsutiomialgieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vision, sa régénération de PM, sa vitesse, son affinité à un élément et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class FibalusePvPmVitesseAffiniteIbsutiomialgie(Tirgnonose, FibalusePv, FibalusePm, FibaluseVitesse, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa régénération de PV, de PM, sa vitesse, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class FibalusePvPmVitesseAffiniteIbsutiomialgieMixte(Tirgnonose, FibalusePv, FibalusePm, FibaluseVitesse, FibaluseAffinite, IbsutiomialgieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa régénération de PV, de PM, sa vitesse, son affinité à un élément et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class TirgnonoseFibaluseForceVisionPvPmVitesse(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePv, FibalusePm, FibaluseVitesse):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vision, sa régénération de PV, de PM et sa vitesse."""

class TirgnonoseFibaluseForceVisionPvPmVitesseMixte(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePv, FibalusePm, FibaluseVitesse, MaladieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vision, sa régénération de PV, de PM et sa vitesse, et qui peut survivre sur une case."""

class TirgnonoseFibaluseForceVisionPvPmAffinite(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePv, FibalusePm, FibaluseAffinite):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vision, sa régénération de PV, de PM et son affinité à un élément."""

class TirgnonoseFibaluseForceVisionPvPmAffiniteMixte(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePv, FibalusePm, FibaluseAffinite, MaladieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vision, sa régénération de PV, de PM et son affinité à un élément, et qui peut survivre sur une case."""

class TirgnonoseFibaluseForceVisionPvPmIbsutiomialgie(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePv, FibalusePm, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vision, sa régénération de PV, de PM et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseForceVisionPvPmIbsutiomialgieMixte(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePv, FibalusePm, IbsutiomialgieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vision, sa régénération de PV, de PM et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class TirgnonoseFibaluseForceVisionPvVitesseAffinite(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePv, FibaluseVitesse, FibaluseAffinite):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vision, sa régénération de PV, sa vitesse et son affinité à un élément."""

class TirgnonoseFibaluseForceVisionPvVitesseAffiniteMixte(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePv, FibaluseVitesse, FibaluseAffinite, MaladieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vision, sa régénération de PV, sa vitesse et son affinité à un élément, et qui peut survivre sur une case."""

class TirgnonoseFibaluseForceVisionPvVitesseIbsutiomialgie(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePv, FibaluseVitesse, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vision, sa régénération de PV, sa vitesse et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseForceVisionPvVitesseIbsutiomialgieMixte(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePv, FibaluseVitesse, IbsutiomialgieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vision, sa régénération de PV, sa vitesse et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class TirgnonoseFibaluseForceVisionPvAffiniteIbsutiomialgie(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePv, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vision, sa régénération de PV, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseForceVisionPvAffiniteIbsutiomialgieMixte(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePv, FibaluseAffinite, IbsutiomialgieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vision, sa régénération de PV, son affinité à un élément et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class TirgnonoseFibaluseForceVisionPmVitesseAffinite(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePm, FibaluseVitesse, FibaluseAffinite):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vision, sa régénération de PM, sa vitesse et son affinité à un élément."""

class TirgnonoseFibaluseForceVisionPmVitesseAffiniteMixte(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePm, FibaluseVitesse, FibaluseAffinite, MaladieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vision, sa régénération de PM, sa vitesse et son affinité à un élément, et qui peut survivre sur une case."""

class TirgnonoseFibaluseForceVisionPmVitesseIbsutiomialgie(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePm, FibaluseVitesse, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vision, sa régénération de PM, sa vitesse et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseForceVisionPmVitesseIbsutiomialgieMixte(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePm, FibaluseVitesse, IbsutiomialgieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vision, sa régénération de PM, sa vitesse et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class TirgnonoseFibaluseForceVisionPmAffiniteIbsutiomialgie(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePm, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vision, sa régénération de PM, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseForceVisionPmAffiniteIbsutiomialgieMixte(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePm, FibaluseAffinite, IbsutiomialgieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vision, sa régénération de PM, son affinité à un élément et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class TirgnonoseFibaluseForceVisionVitesseAffiniteIbsutiomialgie(Tirgnonose, FibaluseForce, FibaluseVision, FibaluseVitesse, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vision, sa vitesse, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseForceVisionVitesseAffiniteIbsutiomialgieMixte(Tirgnonose, FibaluseForce, FibaluseVision, FibaluseVitesse, FibaluseAffinite, IbsutiomialgieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vision, sa vitesse, son affinité à un élément et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class TirgnonoseFibaluseForcePvPmVitesseAffinite(Tirgnonose, FibaluseForce, FibalusePv, FibalusePm, FibaluseVitesse, FibaluseAffinite):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa régénération de PV, de PM, sa vitesse et son affinité à un élément."""

class TirgnonoseFibaluseForcePvPmVitesseAffiniteMixte(Tirgnonose, FibaluseForce, FibalusePv, FibalusePm, FibaluseVitesse, FibaluseAffinite, MaladieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa régénération de PV, de PM, sa vitesse et son affinité à un élément, et qui peut survivre sur une case."""

class TirgnonoseFibaluseForcePvPmVitesseIbsutiomialgie(Tirgnonose, FibaluseForce, FibalusePv, FibalusePm, FibaluseVitesse, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa régénération de PV, de PM, sa vitesse et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseForcePvPmVitesseIbsutiomialgieMixte(Tirgnonose, FibaluseForce, FibalusePv, FibalusePm, FibaluseVitesse, IbsutiomialgieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa régénération de PV, de PM, sa vitesse et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class TirgnonoseFibaluseForcePvPmAffiniteIbsutiomialgie(Tirgnonose, FibaluseForce, FibalusePv, FibalusePm, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa régénération de PV, de PM, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseForcePvPmAffiniteIbsutiomialgieMixte(Tirgnonose, FibaluseForce, FibalusePv, FibalusePm, FibaluseAffinite, IbsutiomialgieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa régénération de PV, de PM, son affinité à un élément et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class TirgnonoseFibaluseForcePvVitesseAffiniteIbsutiomialgie(Tirgnonose, FibaluseForce, FibalusePv, FibaluseVitesse, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa régénération de PV, sa vitesse, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseForcePvVitesseAffiniteIbsutiomialgieMixte(Tirgnonose, FibaluseForce, FibalusePv, FibaluseVitesse, FibaluseAffinite, IbsutiomialgieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa régénération de PV, sa vitesse, son affinité à un élément et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class TirgnonoseFibaluseForcePmVitesseAffiniteIbsutiomialgie(Tirgnonose, FibaluseForce, FibalusePm, FibaluseVitesse, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa régénération de PM, sa vitesse, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseForcePmVitesseAffiniteIbsutiomialgieMixte(Tirgnonose, FibaluseForce, FibalusePm, FibaluseVitesse, FibaluseAffinite, IbsutiomialgieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa régénération de PM, sa vitesse, son affinité à un élément et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class TirgnonoseFibaluseVisionPvPmVitesseAffinite(Tirgnonose, FibaluseVision, FibalusePv, FibalusePm, FibaluseVitesse, FibaluseAffinite):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vision, sa régénération de PV, de PM, sa vitesse et son affinité à un élément."""

class TirgnonoseFibaluseVisionPvPmVitesseAffiniteMixte(Tirgnonose, FibaluseVision, FibalusePv, FibalusePm, FibaluseVitesse, FibaluseAffinite, MaladieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vision, sa régénération de PV, de PM, sa vitesse et son affinité à un élément, et qui peut survivre sur une case."""

class TirgnonoseFibaluseVisionPvPmVitesseIbsutiomialgie(Tirgnonose, FibaluseVision, FibalusePv, FibalusePm, FibaluseVitesse, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vision, sa régénération de PV, de PM, sa vitesse et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseVisionPvPmVitesseIbsutiomialgieMixte(Tirgnonose, FibaluseVision, FibalusePv, FibalusePm, FibaluseVitesse, IbsutiomialgieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vision, sa régénération de PV, de PM, sa vitesse et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class TirgnonoseFibaluseVisionPvPmAffiniteIbsutiomialgie(Tirgnonose, FibaluseVision, FibalusePv, FibalusePm, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vision, sa régénération de PV, de PM, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseVisionPvPmAffiniteIbsutiomialgieMixte(Tirgnonose, FibaluseVision, FibalusePv, FibalusePm, FibaluseAffinite, IbsutiomialgieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vision, sa régénération de PV, de PM, son affinité à un élément et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class TirgnonoseFibaluseVisionPvVitesseAffiniteIbsutiomialgie(Tirgnonose, FibaluseVision, FibalusePv, FibaluseVitesse, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vision, sa régénération de PV, sa vitesse, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseVisionPvVitesseAffiniteIbsutiomialgieMixte(Tirgnonose, FibaluseVision, FibalusePv, FibaluseVitesse, FibaluseAffinite, IbsutiomialgieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vision, sa régénération de PV, sa vitesse, son affinité à un élément et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class TirgnonoseFibaluseVisionPmVitesseAffiniteIbsutiomialgie(Tirgnonose, FibaluseVision, FibalusePm, FibaluseVitesse, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vision, sa régénération de PM, sa vitesse, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseVisionPmVitesseAffiniteIbsutiomialgieMixte(Tirgnonose, FibaluseVision, FibalusePm, FibaluseVitesse, FibaluseAffinite, IbsutiomialgieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vision, sa régénération de PM, sa vitesse, son affinité à un élément et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class TirgnonoseFibalusePvPmVitesseAffiniteIbsutiomialgie(Tirgnonose, FibalusePv, FibalusePm, FibaluseVitesse, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa régénération de PV, de PM, sa vitesse, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibalusePvPmVitesseAffiniteIbsutiomialgieMixte(Tirgnonose, FibalusePv, FibalusePm, FibaluseVitesse, FibaluseAffinite, IbsutiomialgieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa régénération de PV, de PM, sa vitesse, son affinité à un élément et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class FibaluseForceVisionPvPmVitesseAffinite(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePv, FibalusePm, FibaluseVitesse, FibaluseAffinite):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vision, sa régénération de PV, de PM, sa vitesse et son affinité à un élément."""

class FibaluseForceVisionPvPmVitesseAffiniteMixte(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePv, FibalusePm, FibaluseVitesse, FibaluseAffinite, MaladieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vision, sa régénération de PV, de PM, sa vitesse et son affinité à un élément, et qui peut survivre sur une case."""

class FibaluseForceVisionPvPmVitesseIbsutiomialgie(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePv, FibalusePm, FibaluseVitesse, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vision, sa régénération de PV, de PM, sa vitesse et peut le tuer de façon subite (ibsute)."""

class FibaluseForceVisionPvPmVitesseIbsutiomialgieMixte(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePv, FibalusePm, FibaluseVitesse, IbsutiomialgieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vision, sa régénération de PV, de PM, sa vitesse et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class FibaluseForceVisionPvPmAffiniteIbsutiomialgie(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePv, FibalusePm, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vision, sa régénération de PV, de PM, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class FibaluseForceVisionPvPmAffiniteIbsutiomialgieMixte(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePv, FibalusePm, FibaluseAffinite, IbsutiomialgieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vision, sa régénération de PV, de PM, son affinité à un élément et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class FibaluseForceVisionPvVitesseAffiniteIbsutiomialgie(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePv, FibaluseVitesse, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vision, sa régénération de PV, sa vitesse, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class FibaluseForceVisionPvVitesseAffiniteIbsutiomialgieMixte(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePv, FibaluseVitesse, FibaluseAffinite, IbsutiomialgieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vision, sa régénération de PV, sa vitesse, son affinité à un élément et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class FibaluseForceVisionPmVitesseAffiniteIbsutiomialgie(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePm, FibaluseVitesse, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vision, sa régénération de PM, sa vitesse, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class FibaluseForceVisionPmVitesseAffiniteIbsutiomialgieMixte(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePm, FibaluseVitesse, FibaluseAffinite, IbsutiomialgieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vision, sa régénération de PM, sa vitesse, son affinité à un élément et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class FibaluseForcePvPmVitesseAffiniteIbsutiomialgie(Tirgnonose, FibaluseForce, FibalusePv, FibalusePm, FibaluseVitesse, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa régénération de PV, de PM, sa vitesse, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class FibaluseForcePvPmVitesseAffiniteIbsutiomialgieMixte(Tirgnonose, FibaluseForce, FibalusePv, FibalusePm, FibaluseVitesse, FibaluseAffinite, IbsutiomialgieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa régénération de PV, de PM, sa vitesse, son affinité à un élément et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class FibaluseVisionPvPmVitesseAffiniteIbsutiomialgie(Tirgnonose, FibaluseVision, FibalusePv, FibalusePm, FibaluseVitesse, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vision, sa régénération de PV, de PM, sa vitesse, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class FibaluseVisionPvPmVitesseAffiniteIbsutiomialgieMixte(Tirgnonose, FibaluseVision, FibalusePv, FibalusePm, FibaluseVitesse, FibaluseAffinite, IbsutiomialgieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa vision, sa régénération de PV, de PM, sa vitesse, son affinité à un élément et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class TirgnonoseFibaluseForceVisionPvPmVitesseAffinite(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePv, FibalusePm, FibaluseVitesse, FibaluseAffinite):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vision, sa régénération de PV, de PM, sa vitesse et son affinité à un élément."""

class TirgnonoseFibaluseForceVisionPvPmVitesseAffiniteMixte(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePv, FibalusePm, FibaluseVitesse, FibaluseAffinite, MaladieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vision, sa régénération de PV, de PM, sa vitesse et son affinité à un élément, et qui peut survivre sur une case."""

class TirgnonoseFibaluseForceVisionPvPmVitesseIbsutiomialgie(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePv, FibalusePm, FibaluseVitesse, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vision, sa régénération de PV, de PM, sa vitesse et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseForceVisionPvPmVitesseIbsutiomialgieMixte(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePv, FibalusePm, FibaluseVitesse, IbsutiomialgieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vision, sa régénération de PV, de PM, sa vitesse et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class TirgnonoseFibaluseForceVisionPvPmAffiniteIbsutiomialgie(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePv, FibalusePm, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vision, sa régénération de PV, de PM, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseForceVisionPvPmAffiniteIbsutiomialgieMixte(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePv, FibalusePm, FibaluseAffinite, IbsutiomialgieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vision, sa régénération de PV, de PM, son affinité à un élément et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class TirgnonoseFibaluseForceVisionPvVitesseAffiniteIbsutiomialgie(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePv, FibaluseVitesse, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vision, sa régénération de PV, sa vitesse, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseForceVisionPvVitesseAffiniteIbsutiomialgieMixte(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePv, FibaluseVitesse, FibaluseAffinite, IbsutiomialgieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vision, sa régénération de PV, sa vitesse, son affinité à un élément et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class TirgnonoseFibaluseForceVisionPmVitesseAffiniteIbsutiomialgie(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePm, FibaluseVitesse, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vision, sa régénération de PM, sa vitesse, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseForceVisionPmVitesseAffiniteIbsutiomialgieMixte(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePm, FibaluseVitesse, FibaluseAffinite, IbsutiomialgieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vision, sa régénération de PM, sa vitesse, son affinité à un élément et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class TirgnonoseFibaluseForcePvPmVitesseAffiniteIbsutiomialgie(Tirgnonose, FibaluseForce, FibalusePv, FibalusePm, FibaluseVitesse, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa régénération de PV, de PM, sa vitesse, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseForcePvPmVitesseAffiniteIbsutiomialgieMixte(Tirgnonose, FibaluseForce, FibalusePv, FibalusePm, FibaluseVitesse, FibaluseAffinite, IbsutiomialgieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa régénération de PV, de PM, sa vitesse, son affinité à un élément et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class TirgnonoseFibaluseVisionPvPmVitesseAffiniteIbsutiomialgie(Tirgnonose, FibaluseVision, FibalusePv, FibalusePm, FibaluseVitesse, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vision, sa régénération de PV, de PM, sa vitesse, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseVisionPvPmVitesseAffiniteIbsutiomialgieMixte(Tirgnonose, FibaluseVision, FibalusePv, FibalusePm, FibaluseVitesse, FibaluseAffinite, IbsutiomialgieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa vision, sa régénération de PV, de PM, sa vitesse, son affinité à un élément et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class FibaluseForceVisionPvPmVitesseAffiniteIbsutiomialgie(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePv, FibalusePm, FibaluseVitesse, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vision, sa régénération de PV, de PM, sa vitesse, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class FibaluseForceVisionPvPmVitesseAffiniteIbsutiomialgieMixte(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePv, FibalusePm, FibaluseVitesse, FibaluseAffinite, IbsutiomialgieMixte):
    """Une maladie qui rend faible (fibale) l'agissant en diminuant sa force, sa vision, sa régénération de PV, de PM, sa vitesse, son affinité à un élément et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

class TirgnonoseFibaluseForceVisionPvPmVitesseAffiniteIbsutiomialgie(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePv, FibalusePm, FibaluseVitesse, FibaluseAffinite, Ibsutiomialgie):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vision, sa régénération de PV, de PM, sa vitesse, son affinité à un élément et peut le tuer de façon subite (ibsute)."""

class TirgnonoseFibaluseForceVisionPvPmVitesseAffiniteIbsutiomialgieMixte(Tirgnonose, FibaluseForce, FibaluseVision, FibalusePv, FibalusePm, FibaluseVitesse, FibaluseAffinite, IbsutiomialgieMixte):
    """Une maladie qui grignote (tirgnone) les pvs de l'agissant et le rend faible (fibale) en diminuant sa force, sa vision, sa régénération de PV, de PM, sa vitesse, son affinité à un élément et peut le tuer de façon subite (ibsute), et qui peut survivre sur une case."""

maladies: dict[tuple[bool, bool, bool, bool, bool, bool, bool, bool, bool, bool], type[Maladie]] = {
    (False, False, False, False, False, False, False, False, False, False): Maladie,
    (False, False, False, False, False, False, False, False, False, True): MaladieMixte,
    (True, False, False, False, False, False, False, False, False, False): Tirgnonose,
    (True, False, False, False, False, False, False, False, False, True): TirgnonoseMixte,
    (False, True, False, False, False, False, False, False, False, False): Fibaluse,
    (False, True, False, False, False, False, False, False, False, True): FibaluseMixte,
    (True, True, False, False, False, False, False, False, False, False): TirgnonoseFibaluse,
    (True, True, False, False, False, False, False, False, False, True): TirgnonoseFibaluseMixte,
    (False, False, True, False, False, False, False, False, False, False): FibaluseForce,
    (False, False, True, False, False, False, False, False, False, True): FibaluseForceMixte,
    (True, False, True, False, False, False, False, False, False, False): TirgnonoseFibaluseForce,
    (True, False, True, False, False, False, False, False, False, True): TirgnonoseFibaluseForceMixte,
    (False, True, True, False, False, False, False, False, False, False): Maladie,
    (False, True, True, False, False, False, False, False, False, True): MaladieMixte,
    (True, True, True, False, False, False, False, False, False, False): Maladie,
    (True, True, True, False, False, False, False, False, False, True): MaladieMixte,
    (False, False, False, True, False, False, False, False, False, False): FibaluseVision,
    (False, False, False, True, False, False, False, False, False, True): FibaluseVisionMixte,
    (True, False, False, True, False, False, False, False, False, False): TirgnonoseFibaluseVision,
    (True, False, False, True, False, False, False, False, False, True): TirgnonoseFibaluseVisionMixte,
    (False, True, False, True, False, False, False, False, False, False): Maladie,
    (False, True, False, True, False, False, False, False, False, True): MaladieMixte,
    (True, True, False, True, False, False, False, False, False, False): Maladie,
    (True, True, False, True, False, False, False, False, False, True): MaladieMixte,
    (False, False, True, True, False, False, False, False, False, False): FibaluseForceVision,
    (False, False, True, True, False, False, False, False, False, True): FibaluseForceVisionMixte,
    (True, False, True, True, False, False, False, False, False, False): TirgnonoseFibaluseForceVision,
    (True, False, True, True, False, False, False, False, False, True): TirgnonoseFibaluseForceVisionMixte,
    (False, True, True, True, False, False, False, False, False, False): Maladie,
    (False, True, True, True, False, False, False, False, False, True): MaladieMixte,
    (True, True, True, True, False, False, False, False, False, False): Maladie,
    (True, True, True, True, False, False, False, False, False, True): MaladieMixte,
    (False, False, False, False, True, False, False, False, False, False): FibalusePv,
    (False, False, False, False, True, False, False, False, False, True): FibalusePvMixte,
    (True, False, False, False, True, False, False, False, False, False): TirgnonoseFibalusePv,
    (True, False, False, False, True, False, False, False, False, True): TirgnonoseFibalusePvMixte,
    (False, True, False, False, True, False, False, False, False, False): Maladie,
    (False, True, False, False, True, False, False, False, False, True): MaladieMixte,
    (True, True, False, False, True, False, False, False, False, False): Maladie,
    (True, True, False, False, True, False, False, False, False, True): MaladieMixte,
    (False, False, True, False, True, False, False, False, False, False): FibaluseForcePv,
    (False, False, True, False, True, False, False, False, False, True): FibaluseForcePvMixte,
    (True, False, True, False, True, False, False, False, False, False): TirgnonoseFibaluseForcePv,
    (True, False, True, False, True, False, False, False, False, True): TirgnonoseFibaluseForcePvMixte,
    (False, True, True, False, True, False, False, False, False, False): Maladie,
    (False, True, True, False, True, False, False, False, False, True): MaladieMixte,
    (True, True, True, False, True, False, False, False, False, False): Maladie,
    (True, True, True, False, True, False, False, False, False, True): MaladieMixte,
    (False, False, False, True, True, False, False, False, False, False): FibaluseVisionPv,
    (False, False, False, True, True, False, False, False, False, True): FibaluseVisionPvMixte,
    (True, False, False, True, True, False, False, False, False, False): TirgnonoseFibaluseVisionPv,
    (True, False, False, True, True, False, False, False, False, True): TirgnonoseFibaluseVisionPvMixte,
    (False, True, False, True, True, False, False, False, False, False): Maladie,
    (False, True, False, True, True, False, False, False, False, True): MaladieMixte,
    (True, True, False, True, True, False, False, False, False, False): Maladie,
    (True, True, False, True, True, False, False, False, False, True): MaladieMixte,
    (False, False, True, True, True, False, False, False, False, False): FibaluseForceVisionPv,
    (False, False, True, True, True, False, False, False, False, True): FibaluseForceVisionPvMixte,
    (True, False, True, True, True, False, False, False, False, False): TirgnonoseFibaluseForceVisionPv,
    (True, False, True, True, True, False, False, False, False, True): TirgnonoseFibaluseForceVisionPvMixte,
    (False, True, True, True, True, False, False, False, False, False): Maladie,
    (False, True, True, True, True, False, False, False, False, True): MaladieMixte,
    (True, True, True, True, True, False, False, False, False, False): Maladie,
    (True, True, True, True, True, False, False, False, False, True): MaladieMixte,
    (False, False, False, False, False, True, False, False, False, False): FibalusePm,
    (False, False, False, False, False, True, False, False, False, True): FibalusePmMixte,
    (True, False, False, False, False, True, False, False, False, False): TirgnonoseFibalusePm,
    (True, False, False, False, False, True, False, False, False, True): TirgnonoseFibalusePmMixte,
    (False, True, False, False, False, True, False, False, False, False): Maladie,
    (False, True, False, False, False, True, False, False, False, True): MaladieMixte,
    (True, True, False, False, False, True, False, False, False, False): Maladie,
    (True, True, False, False, False, True, False, False, False, True): MaladieMixte,
    (False, False, True, False, False, True, False, False, False, False): FibaluseForcePm,
    (False, False, True, False, False, True, False, False, False, True): FibaluseForcePmMixte,
    (True, False, True, False, False, True, False, False, False, False): TirgnonoseFibaluseForcePm,
    (True, False, True, False, False, True, False, False, False, True): TirgnonoseFibaluseForcePmMixte,
    (False, True, True, False, False, True, False, False, False, False): Maladie,
    (False, True, True, False, False, True, False, False, False, True): MaladieMixte,
    (True, True, True, False, False, True, False, False, False, False): Maladie,
    (True, True, True, False, False, True, False, False, False, True): MaladieMixte,
    (False, False, False, True, False, True, False, False, False, False): FibaluseVisionPm,
    (False, False, False, True, False, True, False, False, False, True): FibaluseVisionPmMixte,
    (True, False, False, True, False, True, False, False, False, False): TirgnonoseFibaluseVisionPm,
    (True, False, False, True, False, True, False, False, False, True): TirgnonoseFibaluseVisionPmMixte,
    (False, True, False, True, False, True, False, False, False, False): Maladie,
    (False, True, False, True, False, True, False, False, False, True): MaladieMixte,
    (True, True, False, True, False, True, False, False, False, False): Maladie,
    (True, True, False, True, False, True, False, False, False, True): MaladieMixte,
    (False, False, True, True, False, True, False, False, False, False): FibaluseForceVisionPm,
    (False, False, True, True, False, True, False, False, False, True): FibaluseForceVisionPmMixte,
    (True, False, True, True, False, True, False, False, False, False): TirgnonoseFibaluseForceVisionPm,
    (True, False, True, True, False, True, False, False, False, True): TirgnonoseFibaluseForceVisionPmMixte,
    (False, True, True, True, False, True, False, False, False, False): Maladie,
    (False, True, True, True, False, True, False, False, False, True): MaladieMixte,
    (True, True, True, True, False, True, False, False, False, False): Maladie,
    (True, True, True, True, False, True, False, False, False, True): MaladieMixte,
    (False, False, False, False, True, True, False, False, False, False): FibalusePvPm,
    (False, False, False, False, True, True, False, False, False, True): FibalusePvPmMixte,
    (True, False, False, False, True, True, False, False, False, False): TirgnonoseFibalusePvPm,
    (True, False, False, False, True, True, False, False, False, True): TirgnonoseFibalusePvPmMixte,
    (False, True, False, False, True, True, False, False, False, False): Maladie,
    (False, True, False, False, True, True, False, False, False, True): MaladieMixte,
    (True, True, False, False, True, True, False, False, False, False): Maladie,
    (True, True, False, False, True, True, False, False, False, True): MaladieMixte,
    (False, False, True, False, True, True, False, False, False, False): FibaluseForcePvPm,
    (False, False, True, False, True, True, False, False, False, True): FibaluseForcePvPmMixte,
    (True, False, True, False, True, True, False, False, False, False): TirgnonoseFibaluseForcePvPm,
    (True, False, True, False, True, True, False, False, False, True): TirgnonoseFibaluseForcePvPmMixte,
    (False, True, True, False, True, True, False, False, False, False): Maladie,
    (False, True, True, False, True, True, False, False, False, True): MaladieMixte,
    (True, True, True, False, True, True, False, False, False, False): Maladie,
    (True, True, True, False, True, True, False, False, False, True): MaladieMixte,
    (False, False, False, True, True, True, False, False, False, False): FibaluseVisionPvPm,
    (False, False, False, True, True, True, False, False, False, True): FibaluseVisionPvPmMixte,
    (True, False, False, True, True, True, False, False, False, False): TirgnonoseFibaluseVisionPvPm,
    (True, False, False, True, True, True, False, False, False, True): TirgnonoseFibaluseVisionPvPmMixte,
    (False, True, False, True, True, True, False, False, False, False): Maladie,
    (False, True, False, True, True, True, False, False, False, True): MaladieMixte,
    (True, True, False, True, True, True, False, False, False, False): Maladie,
    (True, True, False, True, True, True, False, False, False, True): MaladieMixte,
    (False, False, True, True, True, True, False, False, False, False): FibaluseForceVisionPvPm,
    (False, False, True, True, True, True, False, False, False, True): FibaluseForceVisionPvPmMixte,
    (True, False, True, True, True, True, False, False, False, False): TirgnonoseFibaluseForceVisionPvPm,
    (True, False, True, True, True, True, False, False, False, True): TirgnonoseFibaluseForceVisionPvPmMixte,
    (False, True, True, True, True, True, False, False, False, False): Maladie,
    (False, True, True, True, True, True, False, False, False, True): MaladieMixte,
    (True, True, True, True, True, True, False, False, False, False): Maladie,
    (True, True, True, True, True, True, False, False, False, True): MaladieMixte,
    (False, False, False, False, False, False, True, False, False, False): FibaluseVitesse,
    (False, False, False, False, False, False, True, False, False, True): FibaluseVitesseMixte,
    (True, False, False, False, False, False, True, False, False, False): TirgnonoseFibaluseVitesse,
    (True, False, False, False, False, False, True, False, False, True): TirgnonoseFibaluseVitesseMixte,
    (False, True, False, False, False, False, True, False, False, False): Maladie,
    (False, True, False, False, False, False, True, False, False, True): MaladieMixte,
    (True, True, False, False, False, False, True, False, False, False): Maladie,
    (True, True, False, False, False, False, True, False, False, True): MaladieMixte,
    (False, False, True, False, False, False, True, False, False, False): FibaluseForceVitesse,
    (False, False, True, False, False, False, True, False, False, True): FibaluseForceVitesseMixte,
    (True, False, True, False, False, False, True, False, False, False): TirgnonoseFibaluseForceVitesse,
    (True, False, True, False, False, False, True, False, False, True): TirgnonoseFibaluseForceVitesseMixte,
    (False, True, True, False, False, False, True, False, False, False): Maladie,
    (False, True, True, False, False, False, True, False, False, True): MaladieMixte,
    (True, True, True, False, False, False, True, False, False, False): Maladie,
    (True, True, True, False, False, False, True, False, False, True): MaladieMixte,
    (False, False, False, True, False, False, True, False, False, False): FibaluseVisionVitesse,
    (False, False, False, True, False, False, True, False, False, True): FibaluseVisionVitesseMixte,
    (True, False, False, True, False, False, True, False, False, False): TirgnonoseFibaluseVisionVitesse,
    (True, False, False, True, False, False, True, False, False, True): TirgnonoseFibaluseVisionVitesseMixte,
    (False, True, False, True, False, False, True, False, False, False): Maladie,
    (False, True, False, True, False, False, True, False, False, True): MaladieMixte,
    (True, True, False, True, False, False, True, False, False, False): Maladie,
    (True, True, False, True, False, False, True, False, False, True): MaladieMixte,
    (False, False, True, True, False, False, True, False, False, False): FibaluseForceVisionVitesse,
    (False, False, True, True, False, False, True, False, False, True): FibaluseForceVisionVitesseMixte,
    (True, False, True, True, False, False, True, False, False, False): TirgnonoseFibaluseForceVisionVitesse,
    (True, False, True, True, False, False, True, False, False, True): TirgnonoseFibaluseForceVisionVitesseMixte,
    (False, True, True, True, False, False, True, False, False, False): Maladie,
    (False, True, True, True, False, False, True, False, False, True): MaladieMixte,
    (True, True, True, True, False, False, True, False, False, False): Maladie,
    (True, True, True, True, False, False, True, False, False, True): MaladieMixte,
    (False, False, False, False, True, False, True, False, False, False): FibalusePvVitesse,
    (False, False, False, False, True, False, True, False, False, True): FibalusePvVitesseMixte,
    (True, False, False, False, True, False, True, False, False, False): TirgnonoseFibalusePvVitesse,
    (True, False, False, False, True, False, True, False, False, True): TirgnonoseFibalusePvVitesseMixte,
    (False, True, False, False, True, False, True, False, False, False): Maladie,
    (False, True, False, False, True, False, True, False, False, True): MaladieMixte,
    (True, True, False, False, True, False, True, False, False, False): Maladie,
    (True, True, False, False, True, False, True, False, False, True): MaladieMixte,
    (False, False, True, False, True, False, True, False, False, False): FibaluseForcePvVitesse,
    (False, False, True, False, True, False, True, False, False, True): FibaluseForcePvVitesseMixte,
    (True, False, True, False, True, False, True, False, False, False): TirgnonoseFibaluseForcePvVitesse,
    (True, False, True, False, True, False, True, False, False, True): TirgnonoseFibaluseForcePvVitesseMixte,
    (False, True, True, False, True, False, True, False, False, False): Maladie,
    (False, True, True, False, True, False, True, False, False, True): MaladieMixte,
    (True, True, True, False, True, False, True, False, False, False): Maladie,
    (True, True, True, False, True, False, True, False, False, True): MaladieMixte,
    (False, False, False, True, True, False, True, False, False, False): FibaluseVisionPvVitesse,
    (False, False, False, True, True, False, True, False, False, True): FibaluseVisionPvVitesseMixte,
    (True, False, False, True, True, False, True, False, False, False): TirgnonoseFibaluseVisionPvVitesse,
    (True, False, False, True, True, False, True, False, False, True): TirgnonoseFibaluseVisionPvVitesseMixte,
    (False, True, False, True, True, False, True, False, False, False): Maladie,
    (False, True, False, True, True, False, True, False, False, True): MaladieMixte,
    (True, True, False, True, True, False, True, False, False, False): Maladie,
    (True, True, False, True, True, False, True, False, False, True): MaladieMixte,
    (False, False, True, True, True, False, True, False, False, False): FibaluseForceVisionPvVitesse,
    (False, False, True, True, True, False, True, False, False, True): FibaluseForceVisionPvVitesseMixte,
    (True, False, True, True, True, False, True, False, False, False): TirgnonoseFibaluseForceVisionPvVitesse,
    (True, False, True, True, True, False, True, False, False, True): TirgnonoseFibaluseForceVisionPvVitesseMixte,
    (False, True, True, True, True, False, True, False, False, False): Maladie,
    (False, True, True, True, True, False, True, False, False, True): MaladieMixte,
    (True, True, True, True, True, False, True, False, False, False): Maladie,
    (True, True, True, True, True, False, True, False, False, True): MaladieMixte,
    (False, False, False, False, False, True, True, False, False, False): FibalusePmVitesse,
    (False, False, False, False, False, True, True, False, False, True): FibalusePmVitesseMixte,
    (True, False, False, False, False, True, True, False, False, False): TirgnonoseFibalusePmVitesse,
    (True, False, False, False, False, True, True, False, False, True): TirgnonoseFibalusePmVitesseMixte,
    (False, True, False, False, False, True, True, False, False, False): Maladie,
    (False, True, False, False, False, True, True, False, False, True): MaladieMixte,
    (True, True, False, False, False, True, True, False, False, False): Maladie,
    (True, True, False, False, False, True, True, False, False, True): MaladieMixte,
    (False, False, True, False, False, True, True, False, False, False): FibaluseForcePmVitesse,
    (False, False, True, False, False, True, True, False, False, True): FibaluseForcePmVitesseMixte,
    (True, False, True, False, False, True, True, False, False, False): TirgnonoseFibaluseForcePmVitesse,
    (True, False, True, False, False, True, True, False, False, True): TirgnonoseFibaluseForcePmVitesseMixte,
    (False, True, True, False, False, True, True, False, False, False): Maladie,
    (False, True, True, False, False, True, True, False, False, True): MaladieMixte,
    (True, True, True, False, False, True, True, False, False, False): Maladie,
    (True, True, True, False, False, True, True, False, False, True): MaladieMixte,
    (False, False, False, True, False, True, True, False, False, False): FibaluseVisionPmVitesse,
    (False, False, False, True, False, True, True, False, False, True): FibaluseVisionPmVitesseMixte,
    (True, False, False, True, False, True, True, False, False, False): TirgnonoseFibaluseVisionPmVitesse,
    (True, False, False, True, False, True, True, False, False, True): TirgnonoseFibaluseVisionPmVitesseMixte,
    (False, True, False, True, False, True, True, False, False, False): Maladie,
    (False, True, False, True, False, True, True, False, False, True): MaladieMixte,
    (True, True, False, True, False, True, True, False, False, False): Maladie,
    (True, True, False, True, False, True, True, False, False, True): MaladieMixte,
    (False, False, True, True, False, True, True, False, False, False): FibaluseForceVisionPmVitesse,
    (False, False, True, True, False, True, True, False, False, True): FibaluseForceVisionPmVitesseMixte,
    (True, False, True, True, False, True, True, False, False, False): TirgnonoseFibaluseForceVisionPmVitesse,
    (True, False, True, True, False, True, True, False, False, True): TirgnonoseFibaluseForceVisionPmVitesseMixte,
    (False, True, True, True, False, True, True, False, False, False): Maladie,
    (False, True, True, True, False, True, True, False, False, True): MaladieMixte,
    (True, True, True, True, False, True, True, False, False, False): Maladie,
    (True, True, True, True, False, True, True, False, False, True): MaladieMixte,
    (False, False, False, False, True, True, True, False, False, False): FibalusePvPmVitesse,
    (False, False, False, False, True, True, True, False, False, True): FibalusePvPmVitesseMixte,
    (True, False, False, False, True, True, True, False, False, False): TirgnonoseFibalusePvPmVitesse,
    (True, False, False, False, True, True, True, False, False, True): TirgnonoseFibalusePvPmVitesseMixte,
    (False, True, False, False, True, True, True, False, False, False): Maladie,
    (False, True, False, False, True, True, True, False, False, True): MaladieMixte,
    (True, True, False, False, True, True, True, False, False, False): Maladie,
    (True, True, False, False, True, True, True, False, False, True): MaladieMixte,
    (False, False, True, False, True, True, True, False, False, False): FibaluseForcePvPmVitesse,
    (False, False, True, False, True, True, True, False, False, True): FibaluseForcePvPmVitesseMixte,
    (True, False, True, False, True, True, True, False, False, False): TirgnonoseFibaluseForcePvPmVitesse,
    (True, False, True, False, True, True, True, False, False, True): TirgnonoseFibaluseForcePvPmVitesseMixte,
    (False, True, True, False, True, True, True, False, False, False): Maladie,
    (False, True, True, False, True, True, True, False, False, True): MaladieMixte,
    (True, True, True, False, True, True, True, False, False, False): Maladie,
    (True, True, True, False, True, True, True, False, False, True): MaladieMixte,
    (False, False, False, True, True, True, True, False, False, False): FibaluseVisionPvPmVitesse,
    (False, False, False, True, True, True, True, False, False, True): FibaluseVisionPvPmVitesseMixte,
    (True, False, False, True, True, True, True, False, False, False): TirgnonoseFibaluseVisionPvPmVitesse,
    (True, False, False, True, True, True, True, False, False, True): TirgnonoseFibaluseVisionPvPmVitesseMixte,
    (False, True, False, True, True, True, True, False, False, False): Maladie,
    (False, True, False, True, True, True, True, False, False, True): MaladieMixte,
    (True, True, False, True, True, True, True, False, False, False): Maladie,
    (True, True, False, True, True, True, True, False, False, True): MaladieMixte,
    (False, False, True, True, True, True, True, False, False, False): FibaluseForceVisionPvPmVitesse,
    (False, False, True, True, True, True, True, False, False, True): FibaluseForceVisionPvPmVitesseMixte,
    (True, False, True, True, True, True, True, False, False, False): TirgnonoseFibaluseForceVisionPvPmVitesse,
    (True, False, True, True, True, True, True, False, False, True): TirgnonoseFibaluseForceVisionPvPmVitesseMixte,
    (False, True, True, True, True, True, True, False, False, False): Maladie,
    (False, True, True, True, True, True, True, False, False, True): MaladieMixte,
    (True, True, True, True, True, True, True, False, False, False): Maladie,
    (True, True, True, True, True, True, True, False, False, True): MaladieMixte,
    (False, False, False, False, False, False, False, True, False, False): FibaluseAffinite,
    (False, False, False, False, False, False, False, True, False, True): FibaluseAffiniteMixte,
    (True, False, False, False, False, False, False, True, False, False): TirgnonoseFibaluseAffinite,
    (True, False, False, False, False, False, False, True, False, True): TirgnonoseFibaluseAffiniteMixte,
    (False, True, False, False, False, False, False, True, False, False): Maladie,
    (False, True, False, False, False, False, False, True, False, True): MaladieMixte,
    (True, True, False, False, False, False, False, True, False, False): Maladie,
    (True, True, False, False, False, False, False, True, False, True): MaladieMixte,
    (False, False, True, False, False, False, False, True, False, False): FibaluseForceAffinite,
    (False, False, True, False, False, False, False, True, False, True): FibaluseForceAffiniteMixte,
    (True, False, True, False, False, False, False, True, False, False): TirgnonoseFibaluseForceAffinite,
    (True, False, True, False, False, False, False, True, False, True): TirgnonoseFibaluseForceAffiniteMixte,
    (False, True, True, False, False, False, False, True, False, False): Maladie,
    (False, True, True, False, False, False, False, True, False, True): MaladieMixte,
    (True, True, True, False, False, False, False, True, False, False): Maladie,
    (True, True, True, False, False, False, False, True, False, True): MaladieMixte,
    (False, False, False, True, False, False, False, True, False, False): FibaluseVisionAffinite,
    (False, False, False, True, False, False, False, True, False, True): FibaluseVisionAffiniteMixte,
    (True, False, False, True, False, False, False, True, False, False): TirgnonoseFibaluseVisionAffinite,
    (True, False, False, True, False, False, False, True, False, True): TirgnonoseFibaluseVisionAffiniteMixte,
    (False, True, False, True, False, False, False, True, False, False): Maladie,
    (False, True, False, True, False, False, False, True, False, True): MaladieMixte,
    (True, True, False, True, False, False, False, True, False, False): Maladie,
    (True, True, False, True, False, False, False, True, False, True): MaladieMixte,
    (False, False, True, True, False, False, False, True, False, False): FibaluseForceVisionAffinite,
    (False, False, True, True, False, False, False, True, False, True): FibaluseForceVisionAffiniteMixte,
    (True, False, True, True, False, False, False, True, False, False): TirgnonoseFibaluseForceVisionAffinite,
    (True, False, True, True, False, False, False, True, False, True): TirgnonoseFibaluseForceVisionAffiniteMixte,
    (False, True, True, True, False, False, False, True, False, False): Maladie,
    (False, True, True, True, False, False, False, True, False, True): MaladieMixte,
    (True, True, True, True, False, False, False, True, False, False): Maladie,
    (True, True, True, True, False, False, False, True, False, True): MaladieMixte,
    (False, False, False, False, True, False, False, True, False, False): FibalusePvAffinite,
    (False, False, False, False, True, False, False, True, False, True): FibalusePvAffiniteMixte,
    (True, False, False, False, True, False, False, True, False, False): TirgnonoseFibalusePvAffinite,
    (True, False, False, False, True, False, False, True, False, True): TirgnonoseFibalusePvAffiniteMixte,
    (False, True, False, False, True, False, False, True, False, False): Maladie,
    (False, True, False, False, True, False, False, True, False, True): MaladieMixte,
    (True, True, False, False, True, False, False, True, False, False): Maladie,
    (True, True, False, False, True, False, False, True, False, True): MaladieMixte,
    (False, False, True, False, True, False, False, True, False, False): FibaluseForcePvAffinite,
    (False, False, True, False, True, False, False, True, False, True): FibaluseForcePvAffiniteMixte,
    (True, False, True, False, True, False, False, True, False, False): TirgnonoseFibaluseForcePvAffinite,
    (True, False, True, False, True, False, False, True, False, True): TirgnonoseFibaluseForcePvAffiniteMixte,
    (False, True, True, False, True, False, False, True, False, False): Maladie,
    (False, True, True, False, True, False, False, True, False, True): MaladieMixte,
    (True, True, True, False, True, False, False, True, False, False): Maladie,
    (True, True, True, False, True, False, False, True, False, True): MaladieMixte,
    (False, False, False, True, True, False, False, True, False, False): FibaluseVisionPvAffinite,
    (False, False, False, True, True, False, False, True, False, True): FibaluseVisionPvAffiniteMixte,
    (True, False, False, True, True, False, False, True, False, False): TirgnonoseFibaluseVisionPvAffinite,
    (True, False, False, True, True, False, False, True, False, True): TirgnonoseFibaluseVisionPvAffiniteMixte,
    (False, True, False, True, True, False, False, True, False, False): Maladie,
    (False, True, False, True, True, False, False, True, False, True): MaladieMixte,
    (True, True, False, True, True, False, False, True, False, False): Maladie,
    (True, True, False, True, True, False, False, True, False, True): MaladieMixte,
    (False, False, True, True, True, False, False, True, False, False): FibaluseForceVisionPvAffinite,
    (False, False, True, True, True, False, False, True, False, True): FibaluseForceVisionPvAffiniteMixte,
    (True, False, True, True, True, False, False, True, False, False): TirgnonoseFibaluseForceVisionPvAffinite,
    (True, False, True, True, True, False, False, True, False, True): TirgnonoseFibaluseForceVisionPvAffiniteMixte,
    (False, True, True, True, True, False, False, True, False, False): Maladie,
    (False, True, True, True, True, False, False, True, False, True): MaladieMixte,
    (True, True, True, True, True, False, False, True, False, False): Maladie,
    (True, True, True, True, True, False, False, True, False, True): MaladieMixte,
    (False, False, False, False, False, True, False, True, False, False): FibalusePmAffinite,
    (False, False, False, False, False, True, False, True, False, True): FibalusePmAffiniteMixte,
    (True, False, False, False, False, True, False, True, False, False): TirgnonoseFibalusePmAffinite,
    (True, False, False, False, False, True, False, True, False, True): TirgnonoseFibalusePmAffiniteMixte,
    (False, True, False, False, False, True, False, True, False, False): Maladie,
    (False, True, False, False, False, True, False, True, False, True): MaladieMixte,
    (True, True, False, False, False, True, False, True, False, False): Maladie,
    (True, True, False, False, False, True, False, True, False, True): MaladieMixte,
    (False, False, True, False, False, True, False, True, False, False): FibaluseForcePmAffinite,
    (False, False, True, False, False, True, False, True, False, True): FibaluseForcePmAffiniteMixte,
    (True, False, True, False, False, True, False, True, False, False): TirgnonoseFibaluseForcePmAffinite,
    (True, False, True, False, False, True, False, True, False, True): TirgnonoseFibaluseForcePmAffiniteMixte,
    (False, True, True, False, False, True, False, True, False, False): Maladie,
    (False, True, True, False, False, True, False, True, False, True): MaladieMixte,
    (True, True, True, False, False, True, False, True, False, False): Maladie,
    (True, True, True, False, False, True, False, True, False, True): MaladieMixte,
    (False, False, False, True, False, True, False, True, False, False): FibaluseVisionPmAffinite,
    (False, False, False, True, False, True, False, True, False, True): FibaluseVisionPmAffiniteMixte,
    (True, False, False, True, False, True, False, True, False, False): TirgnonoseFibaluseVisionPmAffinite,
    (True, False, False, True, False, True, False, True, False, True): TirgnonoseFibaluseVisionPmAffiniteMixte,
    (False, True, False, True, False, True, False, True, False, False): Maladie,
    (False, True, False, True, False, True, False, True, False, True): MaladieMixte,
    (True, True, False, True, False, True, False, True, False, False): Maladie,
    (True, True, False, True, False, True, False, True, False, True): MaladieMixte,
    (False, False, True, True, False, True, False, True, False, False): FibaluseForceVisionPmAffinite,
    (False, False, True, True, False, True, False, True, False, True): FibaluseForceVisionPmAffiniteMixte,
    (True, False, True, True, False, True, False, True, False, False): TirgnonoseFibaluseForceVisionPmAffinite,
    (True, False, True, True, False, True, False, True, False, True): TirgnonoseFibaluseForceVisionPmAffiniteMixte,
    (False, True, True, True, False, True, False, True, False, False): Maladie,
    (False, True, True, True, False, True, False, True, False, True): MaladieMixte,
    (True, True, True, True, False, True, False, True, False, False): Maladie,
    (True, True, True, True, False, True, False, True, False, True): MaladieMixte,
    (False, False, False, False, True, True, False, True, False, False): FibalusePvPmAffinite,
    (False, False, False, False, True, True, False, True, False, True): FibalusePvPmAffiniteMixte,
    (True, False, False, False, True, True, False, True, False, False): TirgnonoseFibalusePvPmAffinite,
    (True, False, False, False, True, True, False, True, False, True): TirgnonoseFibalusePvPmAffiniteMixte,
    (False, True, False, False, True, True, False, True, False, False): Maladie,
    (False, True, False, False, True, True, False, True, False, True): MaladieMixte,
    (True, True, False, False, True, True, False, True, False, False): Maladie,
    (True, True, False, False, True, True, False, True, False, True): MaladieMixte,
    (False, False, True, False, True, True, False, True, False, False): FibaluseForcePvPmAffinite,
    (False, False, True, False, True, True, False, True, False, True): FibaluseForcePvPmAffiniteMixte,
    (True, False, True, False, True, True, False, True, False, False): TirgnonoseFibaluseForcePvPmAffinite,
    (True, False, True, False, True, True, False, True, False, True): TirgnonoseFibaluseForcePvPmAffiniteMixte,
    (False, True, True, False, True, True, False, True, False, False): Maladie,
    (False, True, True, False, True, True, False, True, False, True): MaladieMixte,
    (True, True, True, False, True, True, False, True, False, False): Maladie,
    (True, True, True, False, True, True, False, True, False, True): MaladieMixte,
    (False, False, False, True, True, True, False, True, False, False): FibaluseVisionPvPmAffinite,
    (False, False, False, True, True, True, False, True, False, True): FibaluseVisionPvPmAffiniteMixte,
    (True, False, False, True, True, True, False, True, False, False): TirgnonoseFibaluseVisionPvPmAffinite,
    (True, False, False, True, True, True, False, True, False, True): TirgnonoseFibaluseVisionPvPmAffiniteMixte,
    (False, True, False, True, True, True, False, True, False, False): Maladie,
    (False, True, False, True, True, True, False, True, False, True): MaladieMixte,
    (True, True, False, True, True, True, False, True, False, False): Maladie,
    (True, True, False, True, True, True, False, True, False, True): MaladieMixte,
    (False, False, True, True, True, True, False, True, False, False): FibaluseForceVisionPvPmAffinite,
    (False, False, True, True, True, True, False, True, False, True): FibaluseForceVisionPvPmAffiniteMixte,
    (True, False, True, True, True, True, False, True, False, False): TirgnonoseFibaluseForceVisionPvPmAffinite,
    (True, False, True, True, True, True, False, True, False, True): TirgnonoseFibaluseForceVisionPvPmAffiniteMixte,
    (False, True, True, True, True, True, False, True, False, False): Maladie,
    (False, True, True, True, True, True, False, True, False, True): MaladieMixte,
    (True, True, True, True, True, True, False, True, False, False): Maladie,
    (True, True, True, True, True, True, False, True, False, True): MaladieMixte,
    (False, False, False, False, False, False, True, True, False, False): FibaluseVitesseAffinite,
    (False, False, False, False, False, False, True, True, False, True): FibaluseVitesseAffiniteMixte,
    (True, False, False, False, False, False, True, True, False, False): TirgnonoseFibaluseVitesseAffinite,
    (True, False, False, False, False, False, True, True, False, True): TirgnonoseFibaluseVitesseAffiniteMixte,
    (False, True, False, False, False, False, True, True, False, False): Maladie,
    (False, True, False, False, False, False, True, True, False, True): MaladieMixte,
    (True, True, False, False, False, False, True, True, False, False): Maladie,
    (True, True, False, False, False, False, True, True, False, True): MaladieMixte,
    (False, False, True, False, False, False, True, True, False, False): FibaluseForceVitesseAffinite,
    (False, False, True, False, False, False, True, True, False, True): FibaluseForceVitesseAffiniteMixte,
    (True, False, True, False, False, False, True, True, False, False): TirgnonoseFibaluseForceVitesseAffinite,
    (True, False, True, False, False, False, True, True, False, True): TirgnonoseFibaluseForceVitesseAffiniteMixte,
    (False, True, True, False, False, False, True, True, False, False): Maladie,
    (False, True, True, False, False, False, True, True, False, True): MaladieMixte,
    (True, True, True, False, False, False, True, True, False, False): Maladie,
    (True, True, True, False, False, False, True, True, False, True): MaladieMixte,
    (False, False, False, True, False, False, True, True, False, False): FibaluseVisionVitesseAffinite,
    (False, False, False, True, False, False, True, True, False, True): FibaluseVisionVitesseAffiniteMixte,
    (True, False, False, True, False, False, True, True, False, False): TirgnonoseFibaluseVisionVitesseAffinite,
    (True, False, False, True, False, False, True, True, False, True): TirgnonoseFibaluseVisionVitesseAffiniteMixte,
    (False, True, False, True, False, False, True, True, False, False): Maladie,
    (False, True, False, True, False, False, True, True, False, True): MaladieMixte,
    (True, True, False, True, False, False, True, True, False, False): Maladie,
    (True, True, False, True, False, False, True, True, False, True): MaladieMixte,
    (False, False, True, True, False, False, True, True, False, False): FibaluseForceVisionVitesseAffinite,
    (False, False, True, True, False, False, True, True, False, True): FibaluseForceVisionVitesseAffiniteMixte,
    (True, False, True, True, False, False, True, True, False, False): TirgnonoseFibaluseForceVisionVitesseAffinite,
    (True, False, True, True, False, False, True, True, False, True): TirgnonoseFibaluseForceVisionVitesseAffiniteMixte,
    (False, True, True, True, False, False, True, True, False, False): Maladie,
    (False, True, True, True, False, False, True, True, False, True): MaladieMixte,
    (True, True, True, True, False, False, True, True, False, False): Maladie,
    (True, True, True, True, False, False, True, True, False, True): MaladieMixte,
    (False, False, False, False, True, False, True, True, False, False): FibalusePvVitesseAffinite,
    (False, False, False, False, True, False, True, True, False, True): FibalusePvVitesseAffiniteMixte,
    (True, False, False, False, True, False, True, True, False, False): TirgnonoseFibalusePvVitesseAffinite,
    (True, False, False, False, True, False, True, True, False, True): TirgnonoseFibalusePvVitesseAffiniteMixte,
    (False, True, False, False, True, False, True, True, False, False): Maladie,
    (False, True, False, False, True, False, True, True, False, True): MaladieMixte,
    (True, True, False, False, True, False, True, True, False, False): Maladie,
    (True, True, False, False, True, False, True, True, False, True): MaladieMixte,
    (False, False, True, False, True, False, True, True, False, False): FibaluseForcePvVitesseAffinite,
    (False, False, True, False, True, False, True, True, False, True): FibaluseForcePvVitesseAffiniteMixte,
    (True, False, True, False, True, False, True, True, False, False): TirgnonoseFibaluseForcePvVitesseAffinite,
    (True, False, True, False, True, False, True, True, False, True): TirgnonoseFibaluseForcePvVitesseAffiniteMixte,
    (False, True, True, False, True, False, True, True, False, False): Maladie,
    (False, True, True, False, True, False, True, True, False, True): MaladieMixte,
    (True, True, True, False, True, False, True, True, False, False): Maladie,
    (True, True, True, False, True, False, True, True, False, True): MaladieMixte,
    (False, False, False, True, True, False, True, True, False, False): FibaluseVisionPvVitesseAffinite,
    (False, False, False, True, True, False, True, True, False, True): FibaluseVisionPvVitesseAffiniteMixte,
    (True, False, False, True, True, False, True, True, False, False): TirgnonoseFibaluseVisionPvVitesseAffinite,
    (True, False, False, True, True, False, True, True, False, True): TirgnonoseFibaluseVisionPvVitesseAffiniteMixte,
    (False, True, False, True, True, False, True, True, False, False): Maladie,
    (False, True, False, True, True, False, True, True, False, True): MaladieMixte,
    (True, True, False, True, True, False, True, True, False, False): Maladie,
    (True, True, False, True, True, False, True, True, False, True): MaladieMixte,
    (False, False, True, True, True, False, True, True, False, False): FibaluseForceVisionPvVitesseAffinite,
    (False, False, True, True, True, False, True, True, False, True): FibaluseForceVisionPvVitesseAffiniteMixte,
    (True, False, True, True, True, False, True, True, False, False): TirgnonoseFibaluseForceVisionPvVitesseAffinite,
    (True, False, True, True, True, False, True, True, False, True): TirgnonoseFibaluseForceVisionPvVitesseAffiniteMixte,
    (False, True, True, True, True, False, True, True, False, False): Maladie,
    (False, True, True, True, True, False, True, True, False, True): MaladieMixte,
    (True, True, True, True, True, False, True, True, False, False): Maladie,
    (True, True, True, True, True, False, True, True, False, True): MaladieMixte,
    (False, False, False, False, False, True, True, True, False, False): FibalusePmVitesseAffinite,
    (False, False, False, False, False, True, True, True, False, True): FibalusePmVitesseAffiniteMixte,
    (True, False, False, False, False, True, True, True, False, False): TirgnonoseFibalusePmVitesseAffinite,
    (True, False, False, False, False, True, True, True, False, True): TirgnonoseFibalusePmVitesseAffiniteMixte,
    (False, True, False, False, False, True, True, True, False, False): Maladie,
    (False, True, False, False, False, True, True, True, False, True): MaladieMixte,
    (True, True, False, False, False, True, True, True, False, False): Maladie,
    (True, True, False, False, False, True, True, True, False, True): MaladieMixte,
    (False, False, True, False, False, True, True, True, False, False): FibaluseForcePmVitesseAffinite,
    (False, False, True, False, False, True, True, True, False, True): FibaluseForcePmVitesseAffiniteMixte,
    (True, False, True, False, False, True, True, True, False, False): TirgnonoseFibaluseForcePmVitesseAffinite,
    (True, False, True, False, False, True, True, True, False, True): TirgnonoseFibaluseForcePmVitesseAffiniteMixte,
    (False, True, True, False, False, True, True, True, False, False): Maladie,
    (False, True, True, False, False, True, True, True, False, True): MaladieMixte,
    (True, True, True, False, False, True, True, True, False, False): Maladie,
    (True, True, True, False, False, True, True, True, False, True): MaladieMixte,
    (False, False, False, True, False, True, True, True, False, False): FibaluseVisionPmVitesseAffinite,
    (False, False, False, True, False, True, True, True, False, True): FibaluseVisionPmVitesseAffiniteMixte,
    (True, False, False, True, False, True, True, True, False, False): TirgnonoseFibaluseVisionPmVitesseAffinite,
    (True, False, False, True, False, True, True, True, False, True): TirgnonoseFibaluseVisionPmVitesseAffiniteMixte,
    (False, True, False, True, False, True, True, True, False, False): Maladie,
    (False, True, False, True, False, True, True, True, False, True): MaladieMixte,
    (True, True, False, True, False, True, True, True, False, False): Maladie,
    (True, True, False, True, False, True, True, True, False, True): MaladieMixte,
    (False, False, True, True, False, True, True, True, False, False): FibaluseForceVisionPmVitesseAffinite,
    (False, False, True, True, False, True, True, True, False, True): FibaluseForceVisionPmVitesseAffiniteMixte,
    (True, False, True, True, False, True, True, True, False, False): TirgnonoseFibaluseForceVisionPmVitesseAffinite,
    (True, False, True, True, False, True, True, True, False, True): TirgnonoseFibaluseForceVisionPmVitesseAffiniteMixte,
    (False, True, True, True, False, True, True, True, False, False): Maladie,
    (False, True, True, True, False, True, True, True, False, True): MaladieMixte,
    (True, True, True, True, False, True, True, True, False, False): Maladie,
    (True, True, True, True, False, True, True, True, False, True): MaladieMixte,
    (False, False, False, False, True, True, True, True, False, False): FibalusePvPmVitesseAffinite,
    (False, False, False, False, True, True, True, True, False, True): FibalusePvPmVitesseAffiniteMixte,
    (True, False, False, False, True, True, True, True, False, False): TirgnonoseFibalusePvPmVitesseAffinite,
    (True, False, False, False, True, True, True, True, False, True): TirgnonoseFibalusePvPmVitesseAffiniteMixte,
    (False, True, False, False, True, True, True, True, False, False): Maladie,
    (False, True, False, False, True, True, True, True, False, True): MaladieMixte,
    (True, True, False, False, True, True, True, True, False, False): Maladie,
    (True, True, False, False, True, True, True, True, False, True): MaladieMixte,
    (False, False, True, False, True, True, True, True, False, False): FibaluseForcePvPmVitesseAffinite,
    (False, False, True, False, True, True, True, True, False, True): FibaluseForcePvPmVitesseAffiniteMixte,
    (True, False, True, False, True, True, True, True, False, False): TirgnonoseFibaluseForcePvPmVitesseAffinite,
    (True, False, True, False, True, True, True, True, False, True): TirgnonoseFibaluseForcePvPmVitesseAffiniteMixte,
    (False, True, True, False, True, True, True, True, False, False): Maladie,
    (False, True, True, False, True, True, True, True, False, True): MaladieMixte,
    (True, True, True, False, True, True, True, True, False, False): Maladie,
    (True, True, True, False, True, True, True, True, False, True): MaladieMixte,
    (False, False, False, True, True, True, True, True, False, False): FibaluseVisionPvPmVitesseAffinite,
    (False, False, False, True, True, True, True, True, False, True): FibaluseVisionPvPmVitesseAffiniteMixte,
    (True, False, False, True, True, True, True, True, False, False): TirgnonoseFibaluseVisionPvPmVitesseAffinite,
    (True, False, False, True, True, True, True, True, False, True): TirgnonoseFibaluseVisionPvPmVitesseAffiniteMixte,
    (False, True, False, True, True, True, True, True, False, False): Maladie,
    (False, True, False, True, True, True, True, True, False, True): MaladieMixte,
    (True, True, False, True, True, True, True, True, False, False): Maladie,
    (True, True, False, True, True, True, True, True, False, True): MaladieMixte,
    (False, False, True, True, True, True, True, True, False, False): FibaluseForceVisionPvPmVitesseAffinite,
    (False, False, True, True, True, True, True, True, False, True): FibaluseForceVisionPvPmVitesseAffiniteMixte,
    (True, False, True, True, True, True, True, True, False, False): TirgnonoseFibaluseForceVisionPvPmVitesseAffinite,
    (True, False, True, True, True, True, True, True, False, True): TirgnonoseFibaluseForceVisionPvPmVitesseAffiniteMixte,
    (False, True, True, True, True, True, True, True, False, False): Maladie,
    (False, True, True, True, True, True, True, True, False, True): MaladieMixte,
    (True, True, True, True, True, True, True, True, False, False): Maladie,
    (True, True, True, True, True, True, True, True, False, True): MaladieMixte,
    (False, False, False, False, False, False, False, False, True, False): Ibsutiomialgie,
    (False, False, False, False, False, False, False, False, True, True): IbsutiomialgieMixte,
    (True, False, False, False, False, False, False, False, True, False): TirgnonoseIbsutiomialgie,
    (True, False, False, False, False, False, False, False, True, True): TirgnonoseIbsutiomialgieMixte,
    (False, True, False, False, False, False, False, False, True, False): FibaluseIbsutiomialgie,
    (False, True, False, False, False, False, False, False, True, True): FibaluseIbsutiomialgieMixte,
    (True, True, False, False, False, False, False, False, True, False): TirgnonoseFibaluseIbsutiomialgie,
    (True, True, False, False, False, False, False, False, True, True): TirgnonoseFibaluseIbsutiomialgieMixte,
    (False, False, True, False, False, False, False, False, True, False): FibaluseForceIbsutiomialgie,
    (False, False, True, False, False, False, False, False, True, True): FibaluseForceIbsutiomialgieMixte,
    (True, False, True, False, False, False, False, False, True, False): TirgnonoseFibaluseForceIbsutiomialgie,
    (True, False, True, False, False, False, False, False, True, True): TirgnonoseFibaluseForceIbsutiomialgieMixte,
    (False, True, True, False, False, False, False, False, True, False): Maladie,
    (False, True, True, False, False, False, False, False, True, True): MaladieMixte,
    (True, True, True, False, False, False, False, False, True, False): Maladie,
    (True, True, True, False, False, False, False, False, True, True): MaladieMixte,
    (False, False, False, True, False, False, False, False, True, False): FibaluseVisionIbsutiomialgie,
    (False, False, False, True, False, False, False, False, True, True): FibaluseVisionIbsutiomialgieMixte,
    (True, False, False, True, False, False, False, False, True, False): TirgnonoseFibaluseVisionIbsutiomialgie,
    (True, False, False, True, False, False, False, False, True, True): TirgnonoseFibaluseVisionIbsutiomialgieMixte,
    (False, True, False, True, False, False, False, False, True, False): Maladie,
    (False, True, False, True, False, False, False, False, True, True): MaladieMixte,
    (True, True, False, True, False, False, False, False, True, False): Maladie,
    (True, True, False, True, False, False, False, False, True, True): MaladieMixte,
    (False, False, True, True, False, False, False, False, True, False): FibaluseForceVisionIbsutiomialgie,
    (False, False, True, True, False, False, False, False, True, True): FibaluseForceVisionIbsutiomialgieMixte,
    (True, False, True, True, False, False, False, False, True, False): TirgnonoseFibaluseForceVisionIbsutiomialgie,
    (True, False, True, True, False, False, False, False, True, True): TirgnonoseFibaluseForceVisionIbsutiomialgieMixte,
    (False, True, True, True, False, False, False, False, True, False): Maladie,
    (False, True, True, True, False, False, False, False, True, True): MaladieMixte,
    (True, True, True, True, False, False, False, False, True, False): Maladie,
    (True, True, True, True, False, False, False, False, True, True): MaladieMixte,
    (False, False, False, False, True, False, False, False, True, False): FibalusePvIbsutiomialgie,
    (False, False, False, False, True, False, False, False, True, True): FibalusePvIbsutiomialgieMixte,
    (True, False, False, False, True, False, False, False, True, False): TirgnonoseFibalusePvIbsutiomialgie,
    (True, False, False, False, True, False, False, False, True, True): TirgnonoseFibalusePvIbsutiomialgieMixte,
    (False, True, False, False, True, False, False, False, True, False): Maladie,
    (False, True, False, False, True, False, False, False, True, True): MaladieMixte,
    (True, True, False, False, True, False, False, False, True, False): Maladie,
    (True, True, False, False, True, False, False, False, True, True): MaladieMixte,
    (False, False, True, False, True, False, False, False, True, False): FibaluseForcePvIbsutiomialgie,
    (False, False, True, False, True, False, False, False, True, True): FibaluseForcePvIbsutiomialgieMixte,
    (True, False, True, False, True, False, False, False, True, False): TirgnonoseFibaluseForcePvIbsutiomialgie,
    (True, False, True, False, True, False, False, False, True, True): TirgnonoseFibaluseForcePvIbsutiomialgieMixte,
    (False, True, True, False, True, False, False, False, True, False): Maladie,
    (False, True, True, False, True, False, False, False, True, True): MaladieMixte,
    (True, True, True, False, True, False, False, False, True, False): Maladie,
    (True, True, True, False, True, False, False, False, True, True): MaladieMixte,
    (False, False, False, True, True, False, False, False, True, False): FibaluseVisionPvIbsutiomialgie,
    (False, False, False, True, True, False, False, False, True, True): FibaluseVisionPvIbsutiomialgieMixte,
    (True, False, False, True, True, False, False, False, True, False): TirgnonoseFibaluseVisionPvIbsutiomialgie,
    (True, False, False, True, True, False, False, False, True, True): TirgnonoseFibaluseVisionPvIbsutiomialgieMixte,
    (False, True, False, True, True, False, False, False, True, False): Maladie,
    (False, True, False, True, True, False, False, False, True, True): MaladieMixte,
    (True, True, False, True, True, False, False, False, True, False): Maladie,
    (True, True, False, True, True, False, False, False, True, True): MaladieMixte,
    (False, False, True, True, True, False, False, False, True, False): FibaluseForceVisionPvIbsutiomialgie,
    (False, False, True, True, True, False, False, False, True, True): FibaluseForceVisionPvIbsutiomialgieMixte,
    (True, False, True, True, True, False, False, False, True, False): TirgnonoseFibaluseForceVisionPvIbsutiomialgie,
    (True, False, True, True, True, False, False, False, True, True): TirgnonoseFibaluseForceVisionPvIbsutiomialgieMixte,
    (False, True, True, True, True, False, False, False, True, False): Maladie,
    (False, True, True, True, True, False, False, False, True, True): MaladieMixte,
    (True, True, True, True, True, False, False, False, True, False): Maladie,
    (True, True, True, True, True, False, False, False, True, True): MaladieMixte,
    (False, False, False, False, False, True, False, False, True, False): FibalusePmIbsutiomialgie,
    (False, False, False, False, False, True, False, False, True, True): FibalusePmIbsutiomialgieMixte,
    (True, False, False, False, False, True, False, False, True, False): TirgnonoseFibalusePmIbsutiomialgie,
    (True, False, False, False, False, True, False, False, True, True): TirgnonoseFibalusePmIbsutiomialgieMixte,
    (False, True, False, False, False, True, False, False, True, False): Maladie,
    (False, True, False, False, False, True, False, False, True, True): MaladieMixte,
    (True, True, False, False, False, True, False, False, True, False): Maladie,
    (True, True, False, False, False, True, False, False, True, True): MaladieMixte,
    (False, False, True, False, False, True, False, False, True, False): FibaluseForcePmIbsutiomialgie,
    (False, False, True, False, False, True, False, False, True, True): FibaluseForcePmIbsutiomialgieMixte,
    (True, False, True, False, False, True, False, False, True, False): TirgnonoseFibaluseForcePmIbsutiomialgie,
    (True, False, True, False, False, True, False, False, True, True): TirgnonoseFibaluseForcePmIbsutiomialgieMixte,
    (False, True, True, False, False, True, False, False, True, False): Maladie,
    (False, True, True, False, False, True, False, False, True, True): MaladieMixte,
    (True, True, True, False, False, True, False, False, True, False): Maladie,
    (True, True, True, False, False, True, False, False, True, True): MaladieMixte,
    (False, False, False, True, False, True, False, False, True, False): FibaluseVisionPmIbsutiomialgie,
    (False, False, False, True, False, True, False, False, True, True): FibaluseVisionPmIbsutiomialgieMixte,
    (True, False, False, True, False, True, False, False, True, False): TirgnonoseFibaluseVisionPmIbsutiomialgie,
    (True, False, False, True, False, True, False, False, True, True): TirgnonoseFibaluseVisionPmIbsutiomialgieMixte,
    (False, True, False, True, False, True, False, False, True, False): Maladie,
    (False, True, False, True, False, True, False, False, True, True): MaladieMixte,
    (True, True, False, True, False, True, False, False, True, False): Maladie,
    (True, True, False, True, False, True, False, False, True, True): MaladieMixte,
    (False, False, True, True, False, True, False, False, True, False): FibaluseForceVisionPmIbsutiomialgie,
    (False, False, True, True, False, True, False, False, True, True): FibaluseForceVisionPmIbsutiomialgieMixte,
    (True, False, True, True, False, True, False, False, True, False): TirgnonoseFibaluseForceVisionPmIbsutiomialgie,
    (True, False, True, True, False, True, False, False, True, True): TirgnonoseFibaluseForceVisionPmIbsutiomialgieMixte,
    (False, True, True, True, False, True, False, False, True, False): Maladie,
    (False, True, True, True, False, True, False, False, True, True): MaladieMixte,
    (True, True, True, True, False, True, False, False, True, False): Maladie,
    (True, True, True, True, False, True, False, False, True, True): MaladieMixte,
    (False, False, False, False, True, True, False, False, True, False): FibalusePvPmIbsutiomialgie,
    (False, False, False, False, True, True, False, False, True, True): FibalusePvPmIbsutiomialgieMixte,
    (True, False, False, False, True, True, False, False, True, False): TirgnonoseFibalusePvPmIbsutiomialgie,
    (True, False, False, False, True, True, False, False, True, True): TirgnonoseFibalusePvPmIbsutiomialgieMixte,
    (False, True, False, False, True, True, False, False, True, False): Maladie,
    (False, True, False, False, True, True, False, False, True, True): MaladieMixte,
    (True, True, False, False, True, True, False, False, True, False): Maladie,
    (True, True, False, False, True, True, False, False, True, True): MaladieMixte,
    (False, False, True, False, True, True, False, False, True, False): FibaluseForcePvPmIbsutiomialgie,
    (False, False, True, False, True, True, False, False, True, True): FibaluseForcePvPmIbsutiomialgieMixte,
    (True, False, True, False, True, True, False, False, True, False): TirgnonoseFibaluseForcePvPmIbsutiomialgie,
    (True, False, True, False, True, True, False, False, True, True): TirgnonoseFibaluseForcePvPmIbsutiomialgieMixte,
    (False, True, True, False, True, True, False, False, True, False): Maladie,
    (False, True, True, False, True, True, False, False, True, True): MaladieMixte,
    (True, True, True, False, True, True, False, False, True, False): Maladie,
    (True, True, True, False, True, True, False, False, True, True): MaladieMixte,
    (False, False, False, True, True, True, False, False, True, False): FibaluseVisionPvPmIbsutiomialgie,
    (False, False, False, True, True, True, False, False, True, True): FibaluseVisionPvPmIbsutiomialgieMixte,
    (True, False, False, True, True, True, False, False, True, False): TirgnonoseFibaluseVisionPvPmIbsutiomialgie,
    (True, False, False, True, True, True, False, False, True, True): TirgnonoseFibaluseVisionPvPmIbsutiomialgieMixte,
    (False, True, False, True, True, True, False, False, True, False): Maladie,
    (False, True, False, True, True, True, False, False, True, True): MaladieMixte,
    (True, True, False, True, True, True, False, False, True, False): Maladie,
    (True, True, False, True, True, True, False, False, True, True): MaladieMixte,
    (False, False, True, True, True, True, False, False, True, False): FibaluseForceVisionPvPmIbsutiomialgie,
    (False, False, True, True, True, True, False, False, True, True): FibaluseForceVisionPvPmIbsutiomialgieMixte,
    (True, False, True, True, True, True, False, False, True, False): TirgnonoseFibaluseForceVisionPvPmIbsutiomialgie,
    (True, False, True, True, True, True, False, False, True, True): TirgnonoseFibaluseForceVisionPvPmIbsutiomialgieMixte,
    (False, True, True, True, True, True, False, False, True, False): Maladie,
    (False, True, True, True, True, True, False, False, True, True): MaladieMixte,
    (True, True, True, True, True, True, False, False, True, False): Maladie,
    (True, True, True, True, True, True, False, False, True, True): MaladieMixte,
    (False, False, False, False, False, False, True, False, True, False): FibaluseVitesseIbsutiomialgie,
    (False, False, False, False, False, False, True, False, True, True): FibaluseVitesseIbsutiomialgieMixte,
    (True, False, False, False, False, False, True, False, True, False): TirgnonoseFibaluseVitesseIbsutiomialgie,
    (True, False, False, False, False, False, True, False, True, True): TirgnonoseFibaluseVitesseIbsutiomialgieMixte,
    (False, True, False, False, False, False, True, False, True, False): Maladie,
    (False, True, False, False, False, False, True, False, True, True): MaladieMixte,
    (True, True, False, False, False, False, True, False, True, False): Maladie,
    (True, True, False, False, False, False, True, False, True, True): MaladieMixte,
    (False, False, True, False, False, False, True, False, True, False): FibaluseForceVitesseIbsutiomialgie,
    (False, False, True, False, False, False, True, False, True, True): FibaluseForceVitesseIbsutiomialgieMixte,
    (True, False, True, False, False, False, True, False, True, False): TirgnonoseFibaluseForceVitesseIbsutiomialgie,
    (True, False, True, False, False, False, True, False, True, True): TirgnonoseFibaluseForceVitesseIbsutiomialgieMixte,
    (False, True, True, False, False, False, True, False, True, False): Maladie,
    (False, True, True, False, False, False, True, False, True, True): MaladieMixte,
    (True, True, True, False, False, False, True, False, True, False): Maladie,
    (True, True, True, False, False, False, True, False, True, True): MaladieMixte,
    (False, False, False, True, False, False, True, False, True, False): FibaluseVisionVitesseIbsutiomialgie,
    (False, False, False, True, False, False, True, False, True, True): FibaluseVisionVitesseIbsutiomialgieMixte,
    (True, False, False, True, False, False, True, False, True, False): TirgnonoseFibaluseVisionVitesseIbsutiomialgie,
    (True, False, False, True, False, False, True, False, True, True): TirgnonoseFibaluseVisionVitesseIbsutiomialgieMixte,
    (False, True, False, True, False, False, True, False, True, False): Maladie,
    (False, True, False, True, False, False, True, False, True, True): MaladieMixte,
    (True, True, False, True, False, False, True, False, True, False): Maladie,
    (True, True, False, True, False, False, True, False, True, True): MaladieMixte,
    (False, False, True, True, False, False, True, False, True, False): FibaluseForceVisionVitesseIbsutiomialgie,
    (False, False, True, True, False, False, True, False, True, True): FibaluseForceVisionVitesseIbsutiomialgieMixte,
    (True, False, True, True, False, False, True, False, True, False): TirgnonoseFibaluseForceVisionVitesseIbsutiomialgie,
    (True, False, True, True, False, False, True, False, True, True): TirgnonoseFibaluseForceVisionVitesseIbsutiomialgieMixte,
    (False, True, True, True, False, False, True, False, True, False): Maladie,
    (False, True, True, True, False, False, True, False, True, True): MaladieMixte,
    (True, True, True, True, False, False, True, False, True, False): Maladie,
    (True, True, True, True, False, False, True, False, True, True): MaladieMixte,
    (False, False, False, False, True, False, True, False, True, False): FibalusePvVitesseIbsutiomialgie,
    (False, False, False, False, True, False, True, False, True, True): FibalusePvVitesseIbsutiomialgieMixte,
    (True, False, False, False, True, False, True, False, True, False): TirgnonoseFibalusePvVitesseIbsutiomialgie,
    (True, False, False, False, True, False, True, False, True, True): TirgnonoseFibalusePvVitesseIbsutiomialgieMixte,
    (False, True, False, False, True, False, True, False, True, False): Maladie,
    (False, True, False, False, True, False, True, False, True, True): MaladieMixte,
    (True, True, False, False, True, False, True, False, True, False): Maladie,
    (True, True, False, False, True, False, True, False, True, True): MaladieMixte,
    (False, False, True, False, True, False, True, False, True, False): FibaluseForcePvVitesseIbsutiomialgie,
    (False, False, True, False, True, False, True, False, True, True): FibaluseForcePvVitesseIbsutiomialgieMixte,
    (True, False, True, False, True, False, True, False, True, False): TirgnonoseFibaluseForcePvVitesseIbsutiomialgie,
    (True, False, True, False, True, False, True, False, True, True): TirgnonoseFibaluseForcePvVitesseIbsutiomialgieMixte,
    (False, True, True, False, True, False, True, False, True, False): Maladie,
    (False, True, True, False, True, False, True, False, True, True): MaladieMixte,
    (True, True, True, False, True, False, True, False, True, False): Maladie,
    (True, True, True, False, True, False, True, False, True, True): MaladieMixte,
    (False, False, False, True, True, False, True, False, True, False): FibaluseVisionPvVitesseIbsutiomialgie,
    (False, False, False, True, True, False, True, False, True, True): FibaluseVisionPvVitesseIbsutiomialgieMixte,
    (True, False, False, True, True, False, True, False, True, False): TirgnonoseFibaluseVisionPvVitesseIbsutiomialgie,
    (True, False, False, True, True, False, True, False, True, True): TirgnonoseFibaluseVisionPvVitesseIbsutiomialgieMixte,
    (False, True, False, True, True, False, True, False, True, False): Maladie,
    (False, True, False, True, True, False, True, False, True, True): MaladieMixte,
    (True, True, False, True, True, False, True, False, True, False): Maladie,
    (True, True, False, True, True, False, True, False, True, True): MaladieMixte,
    (False, False, True, True, True, False, True, False, True, False): FibaluseForceVisionPvVitesseIbsutiomialgie,
    (False, False, True, True, True, False, True, False, True, True): FibaluseForceVisionPvVitesseIbsutiomialgieMixte,
    (True, False, True, True, True, False, True, False, True, False): TirgnonoseFibaluseForceVisionPvVitesseIbsutiomialgie,
    (True, False, True, True, True, False, True, False, True, True): TirgnonoseFibaluseForceVisionPvVitesseIbsutiomialgieMixte,
    (False, True, True, True, True, False, True, False, True, False): Maladie,
    (False, True, True, True, True, False, True, False, True, True): MaladieMixte,
    (True, True, True, True, True, False, True, False, True, False): Maladie,
    (True, True, True, True, True, False, True, False, True, True): MaladieMixte,
    (False, False, False, False, False, True, True, False, True, False): FibalusePmVitesseIbsutiomialgie,
    (False, False, False, False, False, True, True, False, True, True): FibalusePmVitesseIbsutiomialgieMixte,
    (True, False, False, False, False, True, True, False, True, False): TirgnonoseFibalusePmVitesseIbsutiomialgie,
    (True, False, False, False, False, True, True, False, True, True): TirgnonoseFibalusePmVitesseIbsutiomialgieMixte,
    (False, True, False, False, False, True, True, False, True, False): Maladie,
    (False, True, False, False, False, True, True, False, True, True): MaladieMixte,
    (True, True, False, False, False, True, True, False, True, False): Maladie,
    (True, True, False, False, False, True, True, False, True, True): MaladieMixte,
    (False, False, True, False, False, True, True, False, True, False): FibaluseForcePmVitesseIbsutiomialgie,
    (False, False, True, False, False, True, True, False, True, True): FibaluseForcePmVitesseIbsutiomialgieMixte,
    (True, False, True, False, False, True, True, False, True, False): TirgnonoseFibaluseForcePmVitesseIbsutiomialgie,
    (True, False, True, False, False, True, True, False, True, True): TirgnonoseFibaluseForcePmVitesseIbsutiomialgieMixte,
    (False, True, True, False, False, True, True, False, True, False): Maladie,
    (False, True, True, False, False, True, True, False, True, True): MaladieMixte,
    (True, True, True, False, False, True, True, False, True, False): Maladie,
    (True, True, True, False, False, True, True, False, True, True): MaladieMixte,
    (False, False, False, True, False, True, True, False, True, False): FibaluseVisionPmVitesseIbsutiomialgie,
    (False, False, False, True, False, True, True, False, True, True): FibaluseVisionPmVitesseIbsutiomialgieMixte,
    (True, False, False, True, False, True, True, False, True, False): TirgnonoseFibaluseVisionPmVitesseIbsutiomialgie,
    (True, False, False, True, False, True, True, False, True, True): TirgnonoseFibaluseVisionPmVitesseIbsutiomialgieMixte,
    (False, True, False, True, False, True, True, False, True, False): Maladie,
    (False, True, False, True, False, True, True, False, True, True): MaladieMixte,
    (True, True, False, True, False, True, True, False, True, False): Maladie,
    (True, True, False, True, False, True, True, False, True, True): MaladieMixte,
    (False, False, True, True, False, True, True, False, True, False): FibaluseForceVisionPmVitesseIbsutiomialgie,
    (False, False, True, True, False, True, True, False, True, True): FibaluseForceVisionPmVitesseIbsutiomialgieMixte,
    (True, False, True, True, False, True, True, False, True, False): TirgnonoseFibaluseForceVisionPmVitesseIbsutiomialgie,
    (True, False, True, True, False, True, True, False, True, True): TirgnonoseFibaluseForceVisionPmVitesseIbsutiomialgieMixte,
    (False, True, True, True, False, True, True, False, True, False): Maladie,
    (False, True, True, True, False, True, True, False, True, True): MaladieMixte,
    (True, True, True, True, False, True, True, False, True, False): Maladie,
    (True, True, True, True, False, True, True, False, True, True): MaladieMixte,
    (False, False, False, False, True, True, True, False, True, False): FibalusePvPmVitesseIbsutiomialgie,
    (False, False, False, False, True, True, True, False, True, True): FibalusePvPmVitesseIbsutiomialgieMixte,
    (True, False, False, False, True, True, True, False, True, False): TirgnonoseFibalusePvPmVitesseIbsutiomialgie,
    (True, False, False, False, True, True, True, False, True, True): TirgnonoseFibalusePvPmVitesseIbsutiomialgieMixte,
    (False, True, False, False, True, True, True, False, True, False): Maladie,
    (False, True, False, False, True, True, True, False, True, True): MaladieMixte,
    (True, True, False, False, True, True, True, False, True, False): Maladie,
    (True, True, False, False, True, True, True, False, True, True): MaladieMixte,
    (False, False, True, False, True, True, True, False, True, False): FibaluseForcePvPmVitesseIbsutiomialgie,
    (False, False, True, False, True, True, True, False, True, True): FibaluseForcePvPmVitesseIbsutiomialgieMixte,
    (True, False, True, False, True, True, True, False, True, False): TirgnonoseFibaluseForcePvPmVitesseIbsutiomialgie,
    (True, False, True, False, True, True, True, False, True, True): TirgnonoseFibaluseForcePvPmVitesseIbsutiomialgieMixte,
    (False, True, True, False, True, True, True, False, True, False): Maladie,
    (False, True, True, False, True, True, True, False, True, True): MaladieMixte,
    (True, True, True, False, True, True, True, False, True, False): Maladie,
    (True, True, True, False, True, True, True, False, True, True): MaladieMixte,
    (False, False, False, True, True, True, True, False, True, False): FibaluseVisionPvPmVitesseIbsutiomialgie,
    (False, False, False, True, True, True, True, False, True, True): FibaluseVisionPvPmVitesseIbsutiomialgieMixte,
    (True, False, False, True, True, True, True, False, True, False): TirgnonoseFibaluseVisionPvPmVitesseIbsutiomialgie,
    (True, False, False, True, True, True, True, False, True, True): TirgnonoseFibaluseVisionPvPmVitesseIbsutiomialgieMixte,
    (False, True, False, True, True, True, True, False, True, False): Maladie,
    (False, True, False, True, True, True, True, False, True, True): MaladieMixte,
    (True, True, False, True, True, True, True, False, True, False): Maladie,
    (True, True, False, True, True, True, True, False, True, True): MaladieMixte,
    (False, False, True, True, True, True, True, False, True, False): FibaluseForceVisionPvPmVitesseIbsutiomialgie,
    (False, False, True, True, True, True, True, False, True, True): FibaluseForceVisionPvPmVitesseIbsutiomialgieMixte,
    (True, False, True, True, True, True, True, False, True, False): TirgnonoseFibaluseForceVisionPvPmVitesseIbsutiomialgie,
    (True, False, True, True, True, True, True, False, True, True): TirgnonoseFibaluseForceVisionPvPmVitesseIbsutiomialgieMixte,
    (False, True, True, True, True, True, True, False, True, False): Maladie,
    (False, True, True, True, True, True, True, False, True, True): MaladieMixte,
    (True, True, True, True, True, True, True, False, True, False): Maladie,
    (True, True, True, True, True, True, True, False, True, True): MaladieMixte,
    (False, False, False, False, False, False, False, True, True, False): FibaluseAffiniteIbsutiomialgie,
    (False, False, False, False, False, False, False, True, True, True): FibaluseAffiniteIbsutiomialgieMixte,
    (True, False, False, False, False, False, False, True, True, False): TirgnonoseFibaluseAffiniteIbsutiomialgie,
    (True, False, False, False, False, False, False, True, True, True): TirgnonoseFibaluseAffiniteIbsutiomialgieMixte,
    (False, True, False, False, False, False, False, True, True, False): Maladie,
    (False, True, False, False, False, False, False, True, True, True): MaladieMixte,
    (True, True, False, False, False, False, False, True, True, False): Maladie,
    (True, True, False, False, False, False, False, True, True, True): MaladieMixte,
    (False, False, True, False, False, False, False, True, True, False): FibaluseForceAffiniteIbsutiomialgie,
    (False, False, True, False, False, False, False, True, True, True): FibaluseForceAffiniteIbsutiomialgieMixte,
    (True, False, True, False, False, False, False, True, True, False): TirgnonoseFibaluseForceAffiniteIbsutiomialgie,
    (True, False, True, False, False, False, False, True, True, True): TirgnonoseFibaluseForceAffiniteIbsutiomialgieMixte,
    (False, True, True, False, False, False, False, True, True, False): Maladie,
    (False, True, True, False, False, False, False, True, True, True): MaladieMixte,
    (True, True, True, False, False, False, False, True, True, False): Maladie,
    (True, True, True, False, False, False, False, True, True, True): MaladieMixte,
    (False, False, False, True, False, False, False, True, True, False): FibaluseVisionAffiniteIbsutiomialgie,
    (False, False, False, True, False, False, False, True, True, True): FibaluseVisionAffiniteIbsutiomialgieMixte,
    (True, False, False, True, False, False, False, True, True, False): TirgnonoseFibaluseVisionAffiniteIbsutiomialgie,
    (True, False, False, True, False, False, False, True, True, True): TirgnonoseFibaluseVisionAffiniteIbsutiomialgieMixte,
    (False, True, False, True, False, False, False, True, True, False): Maladie,
    (False, True, False, True, False, False, False, True, True, True): MaladieMixte,
    (True, True, False, True, False, False, False, True, True, False): Maladie,
    (True, True, False, True, False, False, False, True, True, True): MaladieMixte,
    (False, False, True, True, False, False, False, True, True, False): FibaluseForceVisionAffiniteIbsutiomialgie,
    (False, False, True, True, False, False, False, True, True, True): FibaluseForceVisionAffiniteIbsutiomialgieMixte,
    (True, False, True, True, False, False, False, True, True, False): TirgnonoseFibaluseForceVisionAffiniteIbsutiomialgie,
    (True, False, True, True, False, False, False, True, True, True): TirgnonoseFibaluseForceVisionAffiniteIbsutiomialgieMixte,
    (False, True, True, True, False, False, False, True, True, False): Maladie,
    (False, True, True, True, False, False, False, True, True, True): MaladieMixte,
    (True, True, True, True, False, False, False, True, True, False): Maladie,
    (True, True, True, True, False, False, False, True, True, True): MaladieMixte,
    (False, False, False, False, True, False, False, True, True, False): FibalusePvAffiniteIbsutiomialgie,
    (False, False, False, False, True, False, False, True, True, True): FibalusePvAffiniteIbsutiomialgieMixte,
    (True, False, False, False, True, False, False, True, True, False): TirgnonoseFibalusePvAffiniteIbsutiomialgie,
    (True, False, False, False, True, False, False, True, True, True): TirgnonoseFibalusePvAffiniteIbsutiomialgieMixte,
    (False, True, False, False, True, False, False, True, True, False): Maladie,
    (False, True, False, False, True, False, False, True, True, True): MaladieMixte,
    (True, True, False, False, True, False, False, True, True, False): Maladie,
    (True, True, False, False, True, False, False, True, True, True): MaladieMixte,
    (False, False, True, False, True, False, False, True, True, False): FibaluseForcePvAffiniteIbsutiomialgie,
    (False, False, True, False, True, False, False, True, True, True): FibaluseForcePvAffiniteIbsutiomialgieMixte,
    (True, False, True, False, True, False, False, True, True, False): TirgnonoseFibaluseForcePvAffiniteIbsutiomialgie,
    (True, False, True, False, True, False, False, True, True, True): TirgnonoseFibaluseForcePvAffiniteIbsutiomialgieMixte,
    (False, True, True, False, True, False, False, True, True, False): Maladie,
    (False, True, True, False, True, False, False, True, True, True): MaladieMixte,
    (True, True, True, False, True, False, False, True, True, False): Maladie,
    (True, True, True, False, True, False, False, True, True, True): MaladieMixte,
    (False, False, False, True, True, False, False, True, True, False): FibaluseVisionPvAffiniteIbsutiomialgie,
    (False, False, False, True, True, False, False, True, True, True): FibaluseVisionPvAffiniteIbsutiomialgieMixte,
    (True, False, False, True, True, False, False, True, True, False): TirgnonoseFibaluseVisionPvAffiniteIbsutiomialgie,
    (True, False, False, True, True, False, False, True, True, True): TirgnonoseFibaluseVisionPvAffiniteIbsutiomialgieMixte,
    (False, True, False, True, True, False, False, True, True, False): Maladie,
    (False, True, False, True, True, False, False, True, True, True): MaladieMixte,
    (True, True, False, True, True, False, False, True, True, False): Maladie,
    (True, True, False, True, True, False, False, True, True, True): MaladieMixte,
    (False, False, True, True, True, False, False, True, True, False): FibaluseForceVisionPvAffiniteIbsutiomialgie,
    (False, False, True, True, True, False, False, True, True, True): FibaluseForceVisionPvAffiniteIbsutiomialgieMixte,
    (True, False, True, True, True, False, False, True, True, False): TirgnonoseFibaluseForceVisionPvAffiniteIbsutiomialgie,
    (True, False, True, True, True, False, False, True, True, True): TirgnonoseFibaluseForceVisionPvAffiniteIbsutiomialgieMixte,
    (False, True, True, True, True, False, False, True, True, False): Maladie,
    (False, True, True, True, True, False, False, True, True, True): MaladieMixte,
    (True, True, True, True, True, False, False, True, True, False): Maladie,
    (True, True, True, True, True, False, False, True, True, True): MaladieMixte,
    (False, False, False, False, False, True, False, True, True, False): FibalusePmAffiniteIbsutiomialgie,
    (False, False, False, False, False, True, False, True, True, True): FibalusePmAffiniteIbsutiomialgieMixte,
    (True, False, False, False, False, True, False, True, True, False): TirgnonoseFibalusePmAffiniteIbsutiomialgie,
    (True, False, False, False, False, True, False, True, True, True): TirgnonoseFibalusePmAffiniteIbsutiomialgieMixte,
    (False, True, False, False, False, True, False, True, True, False): Maladie,
    (False, True, False, False, False, True, False, True, True, True): MaladieMixte,
    (True, True, False, False, False, True, False, True, True, False): Maladie,
    (True, True, False, False, False, True, False, True, True, True): MaladieMixte,
    (False, False, True, False, False, True, False, True, True, False): FibaluseForcePmAffiniteIbsutiomialgie,
    (False, False, True, False, False, True, False, True, True, True): FibaluseForcePmAffiniteIbsutiomialgieMixte,
    (True, False, True, False, False, True, False, True, True, False): TirgnonoseFibaluseForcePmAffiniteIbsutiomialgie,
    (True, False, True, False, False, True, False, True, True, True): TirgnonoseFibaluseForcePmAffiniteIbsutiomialgieMixte,
    (False, True, True, False, False, True, False, True, True, False): Maladie,
    (False, True, True, False, False, True, False, True, True, True): MaladieMixte,
    (True, True, True, False, False, True, False, True, True, False): Maladie,
    (True, True, True, False, False, True, False, True, True, True): MaladieMixte,
    (False, False, False, True, False, True, False, True, True, False): FibaluseVisionPmAffiniteIbsutiomialgie,
    (False, False, False, True, False, True, False, True, True, True): FibaluseVisionPmAffiniteIbsutiomialgieMixte,
    (True, False, False, True, False, True, False, True, True, False): TirgnonoseFibaluseVisionPmAffiniteIbsutiomialgie,
    (True, False, False, True, False, True, False, True, True, True): TirgnonoseFibaluseVisionPmAffiniteIbsutiomialgieMixte,
    (False, True, False, True, False, True, False, True, True, False): Maladie,
    (False, True, False, True, False, True, False, True, True, True): MaladieMixte,
    (True, True, False, True, False, True, False, True, True, False): Maladie,
    (True, True, False, True, False, True, False, True, True, True): MaladieMixte,
    (False, False, True, True, False, True, False, True, True, False): FibaluseForceVisionPmAffiniteIbsutiomialgie,
    (False, False, True, True, False, True, False, True, True, True): FibaluseForceVisionPmAffiniteIbsutiomialgieMixte,
    (True, False, True, True, False, True, False, True, True, False): TirgnonoseFibaluseForceVisionPmAffiniteIbsutiomialgie,
    (True, False, True, True, False, True, False, True, True, True): TirgnonoseFibaluseForceVisionPmAffiniteIbsutiomialgieMixte,
    (False, True, True, True, False, True, False, True, True, False): Maladie,
    (False, True, True, True, False, True, False, True, True, True): MaladieMixte,
    (True, True, True, True, False, True, False, True, True, False): Maladie,
    (True, True, True, True, False, True, False, True, True, True): MaladieMixte,
    (False, False, False, False, True, True, False, True, True, False): FibalusePvPmAffiniteIbsutiomialgie,
    (False, False, False, False, True, True, False, True, True, True): FibalusePvPmAffiniteIbsutiomialgieMixte,
    (True, False, False, False, True, True, False, True, True, False): TirgnonoseFibalusePvPmAffiniteIbsutiomialgie,
    (True, False, False, False, True, True, False, True, True, True): TirgnonoseFibalusePvPmAffiniteIbsutiomialgieMixte,
    (False, True, False, False, True, True, False, True, True, False): Maladie,
    (False, True, False, False, True, True, False, True, True, True): MaladieMixte,
    (True, True, False, False, True, True, False, True, True, False): Maladie,
    (True, True, False, False, True, True, False, True, True, True): MaladieMixte,
    (False, False, True, False, True, True, False, True, True, False): FibaluseForcePvPmAffiniteIbsutiomialgie,
    (False, False, True, False, True, True, False, True, True, True): FibaluseForcePvPmAffiniteIbsutiomialgieMixte,
    (True, False, True, False, True, True, False, True, True, False): TirgnonoseFibaluseForcePvPmAffiniteIbsutiomialgie,
    (True, False, True, False, True, True, False, True, True, True): TirgnonoseFibaluseForcePvPmAffiniteIbsutiomialgieMixte,
    (False, True, True, False, True, True, False, True, True, False): Maladie,
    (False, True, True, False, True, True, False, True, True, True): MaladieMixte,
    (True, True, True, False, True, True, False, True, True, False): Maladie,
    (True, True, True, False, True, True, False, True, True, True): MaladieMixte,
    (False, False, False, True, True, True, False, True, True, False): FibaluseVisionPvPmAffiniteIbsutiomialgie,
    (False, False, False, True, True, True, False, True, True, True): FibaluseVisionPvPmAffiniteIbsutiomialgieMixte,
    (True, False, False, True, True, True, False, True, True, False): TirgnonoseFibaluseVisionPvPmAffiniteIbsutiomialgie,
    (True, False, False, True, True, True, False, True, True, True): TirgnonoseFibaluseVisionPvPmAffiniteIbsutiomialgieMixte,
    (False, True, False, True, True, True, False, True, True, False): Maladie,
    (False, True, False, True, True, True, False, True, True, True): MaladieMixte,
    (True, True, False, True, True, True, False, True, True, False): Maladie,
    (True, True, False, True, True, True, False, True, True, True): MaladieMixte,
    (False, False, True, True, True, True, False, True, True, False): FibaluseForceVisionPvPmAffiniteIbsutiomialgie,
    (False, False, True, True, True, True, False, True, True, True): FibaluseForceVisionPvPmAffiniteIbsutiomialgieMixte,
    (True, False, True, True, True, True, False, True, True, False): TirgnonoseFibaluseForceVisionPvPmAffiniteIbsutiomialgie,
    (True, False, True, True, True, True, False, True, True, True): TirgnonoseFibaluseForceVisionPvPmAffiniteIbsutiomialgieMixte,
    (False, True, True, True, True, True, False, True, True, False): Maladie,
    (False, True, True, True, True, True, False, True, True, True): MaladieMixte,
    (True, True, True, True, True, True, False, True, True, False): Maladie,
    (True, True, True, True, True, True, False, True, True, True): MaladieMixte,
    (False, False, False, False, False, False, True, True, True, False): FibaluseVitesseAffiniteIbsutiomialgie,
    (False, False, False, False, False, False, True, True, True, True): FibaluseVitesseAffiniteIbsutiomialgieMixte,
    (True, False, False, False, False, False, True, True, True, False): TirgnonoseFibaluseVitesseAffiniteIbsutiomialgie,
    (True, False, False, False, False, False, True, True, True, True): TirgnonoseFibaluseVitesseAffiniteIbsutiomialgieMixte,
    (False, True, False, False, False, False, True, True, True, False): Maladie,
    (False, True, False, False, False, False, True, True, True, True): MaladieMixte,
    (True, True, False, False, False, False, True, True, True, False): Maladie,
    (True, True, False, False, False, False, True, True, True, True): MaladieMixte,
    (False, False, True, False, False, False, True, True, True, False): FibaluseForceVitesseAffiniteIbsutiomialgie,
    (False, False, True, False, False, False, True, True, True, True): FibaluseForceVitesseAffiniteIbsutiomialgieMixte,
    (True, False, True, False, False, False, True, True, True, False): TirgnonoseFibaluseForceVitesseAffiniteIbsutiomialgie,
    (True, False, True, False, False, False, True, True, True, True): TirgnonoseFibaluseForceVitesseAffiniteIbsutiomialgieMixte,
    (False, True, True, False, False, False, True, True, True, False): Maladie,
    (False, True, True, False, False, False, True, True, True, True): MaladieMixte,
    (True, True, True, False, False, False, True, True, True, False): Maladie,
    (True, True, True, False, False, False, True, True, True, True): MaladieMixte,
    (False, False, False, True, False, False, True, True, True, False): FibaluseVisionVitesseAffiniteIbsutiomialgie,
    (False, False, False, True, False, False, True, True, True, True): FibaluseVisionVitesseAffiniteIbsutiomialgieMixte,
    (True, False, False, True, False, False, True, True, True, False): TirgnonoseFibaluseVisionVitesseAffiniteIbsutiomialgie,
    (True, False, False, True, False, False, True, True, True, True): TirgnonoseFibaluseVisionVitesseAffiniteIbsutiomialgieMixte,
    (False, True, False, True, False, False, True, True, True, False): Maladie,
    (False, True, False, True, False, False, True, True, True, True): MaladieMixte,
    (True, True, False, True, False, False, True, True, True, False): Maladie,
    (True, True, False, True, False, False, True, True, True, True): MaladieMixte,
    (False, False, True, True, False, False, True, True, True, False): FibaluseForceVisionVitesseAffiniteIbsutiomialgie,
    (False, False, True, True, False, False, True, True, True, True): FibaluseForceVisionVitesseAffiniteIbsutiomialgieMixte,
    (True, False, True, True, False, False, True, True, True, False): TirgnonoseFibaluseForceVisionVitesseAffiniteIbsutiomialgie,
    (True, False, True, True, False, False, True, True, True, True): TirgnonoseFibaluseForceVisionVitesseAffiniteIbsutiomialgieMixte,
    (False, True, True, True, False, False, True, True, True, False): Maladie,
    (False, True, True, True, False, False, True, True, True, True): MaladieMixte,
    (True, True, True, True, False, False, True, True, True, False): Maladie,
    (True, True, True, True, False, False, True, True, True, True): MaladieMixte,
    (False, False, False, False, True, False, True, True, True, False): FibalusePvVitesseAffiniteIbsutiomialgie,
    (False, False, False, False, True, False, True, True, True, True): FibalusePvVitesseAffiniteIbsutiomialgieMixte,
    (True, False, False, False, True, False, True, True, True, False): TirgnonoseFibalusePvVitesseAffiniteIbsutiomialgie,
    (True, False, False, False, True, False, True, True, True, True): TirgnonoseFibalusePvVitesseAffiniteIbsutiomialgieMixte,
    (False, True, False, False, True, False, True, True, True, False): Maladie,
    (False, True, False, False, True, False, True, True, True, True): MaladieMixte,
    (True, True, False, False, True, False, True, True, True, False): Maladie,
    (True, True, False, False, True, False, True, True, True, True): MaladieMixte,
    (False, False, True, False, True, False, True, True, True, False): FibaluseForcePvVitesseAffiniteIbsutiomialgie,
    (False, False, True, False, True, False, True, True, True, True): FibaluseForcePvVitesseAffiniteIbsutiomialgieMixte,
    (True, False, True, False, True, False, True, True, True, False): TirgnonoseFibaluseForcePvVitesseAffiniteIbsutiomialgie,
    (True, False, True, False, True, False, True, True, True, True): TirgnonoseFibaluseForcePvVitesseAffiniteIbsutiomialgieMixte,
    (False, True, True, False, True, False, True, True, True, False): Maladie,
    (False, True, True, False, True, False, True, True, True, True): MaladieMixte,
    (True, True, True, False, True, False, True, True, True, False): Maladie,
    (True, True, True, False, True, False, True, True, True, True): MaladieMixte,
    (False, False, False, True, True, False, True, True, True, False): FibaluseVisionPvVitesseAffiniteIbsutiomialgie,
    (False, False, False, True, True, False, True, True, True, True): FibaluseVisionPvVitesseAffiniteIbsutiomialgieMixte,
    (True, False, False, True, True, False, True, True, True, False): TirgnonoseFibaluseVisionPvVitesseAffiniteIbsutiomialgie,
    (True, False, False, True, True, False, True, True, True, True): TirgnonoseFibaluseVisionPvVitesseAffiniteIbsutiomialgieMixte,
    (False, True, False, True, True, False, True, True, True, False): Maladie,
    (False, True, False, True, True, False, True, True, True, True): MaladieMixte,
    (True, True, False, True, True, False, True, True, True, False): Maladie,
    (True, True, False, True, True, False, True, True, True, True): MaladieMixte,
    (False, False, True, True, True, False, True, True, True, False): FibaluseForceVisionPvVitesseAffiniteIbsutiomialgie,
    (False, False, True, True, True, False, True, True, True, True): FibaluseForceVisionPvVitesseAffiniteIbsutiomialgieMixte,
    (True, False, True, True, True, False, True, True, True, False): TirgnonoseFibaluseForceVisionPvVitesseAffiniteIbsutiomialgie,
    (True, False, True, True, True, False, True, True, True, True): TirgnonoseFibaluseForceVisionPvVitesseAffiniteIbsutiomialgieMixte,
    (False, True, True, True, True, False, True, True, True, False): Maladie,
    (False, True, True, True, True, False, True, True, True, True): MaladieMixte,
    (True, True, True, True, True, False, True, True, True, False): Maladie,
    (True, True, True, True, True, False, True, True, True, True): MaladieMixte,
    (False, False, False, False, False, True, True, True, True, False): FibalusePmVitesseAffiniteIbsutiomialgie,
    (False, False, False, False, False, True, True, True, True, True): FibalusePmVitesseAffiniteIbsutiomialgieMixte,
    (True, False, False, False, False, True, True, True, True, False): TirgnonoseFibalusePmVitesseAffiniteIbsutiomialgie,
    (True, False, False, False, False, True, True, True, True, True): TirgnonoseFibalusePmVitesseAffiniteIbsutiomialgieMixte,
    (False, True, False, False, False, True, True, True, True, False): Maladie,
    (False, True, False, False, False, True, True, True, True, True): MaladieMixte,
    (True, True, False, False, False, True, True, True, True, False): Maladie,
    (True, True, False, False, False, True, True, True, True, True): MaladieMixte,
    (False, False, True, False, False, True, True, True, True, False): FibaluseForcePmVitesseAffiniteIbsutiomialgie,
    (False, False, True, False, False, True, True, True, True, True): FibaluseForcePmVitesseAffiniteIbsutiomialgieMixte,
    (True, False, True, False, False, True, True, True, True, False): TirgnonoseFibaluseForcePmVitesseAffiniteIbsutiomialgie,
    (True, False, True, False, False, True, True, True, True, True): TirgnonoseFibaluseForcePmVitesseAffiniteIbsutiomialgieMixte,
    (False, True, True, False, False, True, True, True, True, False): Maladie,
    (False, True, True, False, False, True, True, True, True, True): MaladieMixte,
    (True, True, True, False, False, True, True, True, True, False): Maladie,
    (True, True, True, False, False, True, True, True, True, True): MaladieMixte,
    (False, False, False, True, False, True, True, True, True, False): FibaluseVisionPmVitesseAffiniteIbsutiomialgie,
    (False, False, False, True, False, True, True, True, True, True): FibaluseVisionPmVitesseAffiniteIbsutiomialgieMixte,
    (True, False, False, True, False, True, True, True, True, False): TirgnonoseFibaluseVisionPmVitesseAffiniteIbsutiomialgie,
    (True, False, False, True, False, True, True, True, True, True): TirgnonoseFibaluseVisionPmVitesseAffiniteIbsutiomialgieMixte,
    (False, True, False, True, False, True, True, True, True, False): Maladie,
    (False, True, False, True, False, True, True, True, True, True): MaladieMixte,
    (True, True, False, True, False, True, True, True, True, False): Maladie,
    (True, True, False, True, False, True, True, True, True, True): MaladieMixte,
    (False, False, True, True, False, True, True, True, True, False): FibaluseForceVisionPmVitesseAffiniteIbsutiomialgie,
    (False, False, True, True, False, True, True, True, True, True): FibaluseForceVisionPmVitesseAffiniteIbsutiomialgieMixte,
    (True, False, True, True, False, True, True, True, True, False): TirgnonoseFibaluseForceVisionPmVitesseAffiniteIbsutiomialgie,
    (True, False, True, True, False, True, True, True, True, True): TirgnonoseFibaluseForceVisionPmVitesseAffiniteIbsutiomialgieMixte,
    (False, True, True, True, False, True, True, True, True, False): Maladie,
    (False, True, True, True, False, True, True, True, True, True): MaladieMixte,
    (True, True, True, True, False, True, True, True, True, False): Maladie,
    (True, True, True, True, False, True, True, True, True, True): MaladieMixte,
    (False, False, False, False, True, True, True, True, True, False): FibalusePvPmVitesseAffiniteIbsutiomialgie,
    (False, False, False, False, True, True, True, True, True, True): FibalusePvPmVitesseAffiniteIbsutiomialgieMixte,
    (True, False, False, False, True, True, True, True, True, False): TirgnonoseFibalusePvPmVitesseAffiniteIbsutiomialgie,
    (True, False, False, False, True, True, True, True, True, True): TirgnonoseFibalusePvPmVitesseAffiniteIbsutiomialgieMixte,
    (False, True, False, False, True, True, True, True, True, False): Maladie,
    (False, True, False, False, True, True, True, True, True, True): MaladieMixte,
    (True, True, False, False, True, True, True, True, True, False): Maladie,
    (True, True, False, False, True, True, True, True, True, True): MaladieMixte,
    (False, False, True, False, True, True, True, True, True, False): FibaluseForcePvPmVitesseAffiniteIbsutiomialgie,
    (False, False, True, False, True, True, True, True, True, True): FibaluseForcePvPmVitesseAffiniteIbsutiomialgieMixte,
    (True, False, True, False, True, True, True, True, True, False): TirgnonoseFibaluseForcePvPmVitesseAffiniteIbsutiomialgie,
    (True, False, True, False, True, True, True, True, True, True): TirgnonoseFibaluseForcePvPmVitesseAffiniteIbsutiomialgieMixte,
    (False, True, True, False, True, True, True, True, True, False): Maladie,
    (False, True, True, False, True, True, True, True, True, True): MaladieMixte,
    (True, True, True, False, True, True, True, True, True, False): Maladie,
    (True, True, True, False, True, True, True, True, True, True): MaladieMixte,
    (False, False, False, True, True, True, True, True, True, False): FibaluseVisionPvPmVitesseAffiniteIbsutiomialgie,
    (False, False, False, True, True, True, True, True, True, True): FibaluseVisionPvPmVitesseAffiniteIbsutiomialgieMixte,
    (True, False, False, True, True, True, True, True, True, False): TirgnonoseFibaluseVisionPvPmVitesseAffiniteIbsutiomialgie,
    (True, False, False, True, True, True, True, True, True, True): TirgnonoseFibaluseVisionPvPmVitesseAffiniteIbsutiomialgieMixte,
    (False, True, False, True, True, True, True, True, True, False): Maladie,
    (False, True, False, True, True, True, True, True, True, True): MaladieMixte,
    (True, True, False, True, True, True, True, True, True, False): Maladie,
    (True, True, False, True, True, True, True, True, True, True): MaladieMixte,
    (False, False, True, True, True, True, True, True, True, False): FibaluseForceVisionPvPmVitesseAffiniteIbsutiomialgie,
    (False, False, True, True, True, True, True, True, True, True): FibaluseForceVisionPvPmVitesseAffiniteIbsutiomialgieMixte,
    (True, False, True, True, True, True, True, True, True, False): TirgnonoseFibaluseForceVisionPvPmVitesseAffiniteIbsutiomialgie,
    (True, False, True, True, True, True, True, True, True, True): TirgnonoseFibaluseForceVisionPvPmVitesseAffiniteIbsutiomialgieMixte,
    (False, True, True, True, True, True, True, True, True, False): Maladie,
    (False, True, True, True, True, True, True, True, True, True): MaladieMixte,
    (True, True, True, True, True, True, True, True, True, False): Maladie,
    (True, True, True, True, True, True, True, True, True, True): MaladieMixte,
}
"""
(tirgnonose, fibaluse, force, vision, pv, pm, vitesse, affinite, ibsutiomialgie) -> maladie correspondante
"""
