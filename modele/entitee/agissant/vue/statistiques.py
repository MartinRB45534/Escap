"""La vue des statistiques."""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional

# Valeurs par défaut des paramètres
from ....commons.elements import Element

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ..statistiques import Statistiques

class StatistiquesVues:
    """La vision des statistiques."""
    def __init__(self, priorite:Optional[float]=None, vitesse:Optional[float]=None, force:Optional[float]=None, proportion_pv:Optional[float]=None, pv_max:Optional[float]=None, pv:Optional[float]=None, regen_pv_max:Optional[float]=None, regen_pv_min:Optional[float]=None, regen_pv:Optional[float]=None, restauration_regen_pv:Optional[float]=None, proportion_pm:Optional[float]=None, pm_max:Optional[float]=None, pm:Optional[float]=None, regen_pm:Optional[float]=None, affinites:dict[Element,Optional[float]]={element: None for element in Element}, immunites:set[Element]=set(),):
        self.priorite = priorite
        self.vitesse = vitesse
        self.force = force
        self.proportion_pv = proportion_pv
        self.pv_max = pv_max
        self.pv = pv
        self.regen_pv_max = regen_pv_max
        self.regen_pv_min = regen_pv_min
        self.regen_pv = regen_pv
        self.restauration_regen_pv = restauration_regen_pv
        self.proportion_pm = proportion_pm
        self.pm_max = pm_max
        self.pm = pm
        self.regen_pm = regen_pm
        self.affinites = affinites
        self.immunites = immunites

def voit_statistiques(statistiques:Statistiques) -> StatistiquesVues:
    """Transforme des statistiques en statistiques vues."""
    return StatistiquesVues(
        proportion_pv=statistiques.pv / statistiques.pv_max,
    ) # Par défaut, on ne voit que la proportion de pv
