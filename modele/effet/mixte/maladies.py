"""
Contient les classes des maladies mixtes (qui affectent aussi les cases).
"""

from __future__ import annotations
from typing import TYPE_CHECKING

import random

from modele.labyrinthe.case import Case

# Imports des classes parentes
from ..agissant import Maladie, Tirgnogose, Fibaluse, Ibsutiomialgie, TypesMaladies
from ..case import OnPostActionCase

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ...labyrinthe import Case

class MaladieMixte(OnPostActionCase, Maladie):
    """Maladie qui peut survivre sur une case. Peut se transmettre à un agissant qui passe dessus."""
    transmissibilite:float
    portee:float
    duree_max:int
    def __init__(self):
        Maladie.__init__(self)
        self.duree = self.duree_max

    def post_action(self, case: Case):
        malade_potentiel = case.agissant
        if malade_potentiel:
            if random.random() < self.transmissibilite and (not isinstance(effet, self.__class__) for effet in malade_potentiel.effets):
                malade_potentiel.effets.add(self.__class__())
        self.duree -= 1

    def termine(self) -> bool:
        return self.duree <= 0
    
class TirgnogoseMixte(MaladieMixte, Tirgnogose):
    """Maladie qui cause une perte progressive de PV. Peut se transmettre aux voisins. Peut survivre sur une case."""

class FibaluseMixte(MaladieMixte, Fibaluse):
    """Maladie qui réduit les statistiques. Peut se transmettre aux voisins. Peut survivre sur une case."""

class IbsutiomialgieMixte(MaladieMixte, Ibsutiomialgie):
    """Maladie qui peut causer une mort subite. Peut se transmettre aux voisins. Peut survivre sur une case."""

maladies: dict[tuple[TypesMaladies, bool], type[Maladie]] = {
    (TypesMaladies.TIRGNOGOSE, False): Tirgnogose,
    (TypesMaladies.FIBALUSE, False): Fibaluse,
    (TypesMaladies.IBSUTIOMIALGIE, False): Ibsutiomialgie,
    (TypesMaladies.TIRGNOGOSE, True): TirgnogoseMixte,
    (TypesMaladies.FIBALUSE, True): FibaluseMixte,
    (TypesMaladies.IBSUTIOMIALGIE, True): IbsutiomialgieMixte
}
"""
(TypesMaladies, bool) -> type[Maladie]
"""
