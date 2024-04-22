"""
Contient la classes des maladies mixtes (qui affectent aussi les cases).
"""

from __future__ import annotations
from typing import TYPE_CHECKING

import random

# Imports des classes parentes
from ..agissant import Maladie
from ..case import OnPostActionCase

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ...labyrinthe import Case
    from ...entitee import Agissant

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
            self.transmet(malade_potentiel)
        self.duree -= 1

    def transmet(self, agissant: Agissant):
        """Se transmet un agissant."""
        if random.random() < self.transmissible(agissant):
            for effet in [*agissant.effets]:
                if isinstance(effet, Maladie) and effet.nom == self.nom:
                    if effet.niveau < self.niveau:
                        agissant.effets.remove(effet)
                        agissant.effets.add(self.__class__()) #Nid à problèmes très potentiel !

    def transmissible(self, agissant:Agissant):
        """Retourne l'infectabilité de la maladie pour l'agissant donné."""
        non_infectable = agissant.statistiques.get_non_infectable(self.__class__)
        non_infectable -= self.transmissibilite
        return min(1, max(0, 10 - non_infectable)/10)

    def termine(self) -> bool:
        return self.duree <= 0
