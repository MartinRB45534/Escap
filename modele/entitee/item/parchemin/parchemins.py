"""Les deux classes de parchemins."""

from __future__ import annotations
from typing import TYPE_CHECKING

import carte as crt

# Imports des classes parentes
from .parchemin import Parchemin
from ....action import Impregne
from ...agissant import NOONE

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ....action.magie.magie import Magie

class ParcheminImpregne(Parchemin):
    """Un parchemin imprégné d'une magie."""
    magie: type[Magie]


class ParcheminVierge(ParcheminImpregne):
    """Un parchemin qui peut être imprégné d'une magie."""
    latence_impregne: float
    taux_cout_caste: float
    taux_cout_impregne: float
    taux_latence_caste: float
    taux_latence_impregne: float

    def __init__(self, position: crt.Position):
        ParcheminImpregne.__init__(self, position)
        self.action_portee = Impregne(NOONE, self.latence_impregne, self,
                             self.taux_cout_impregne, self.taux_cout_caste,
                             self.taux_latence_impregne, self.taux_latence_caste)
