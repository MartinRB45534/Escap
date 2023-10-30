"""Les cases vues par les agissants."""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Set
import carte as crt

from .agissant import voit_agissant
from .item import voit_item

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ....effet.effet import Effet
    from ....effet.case.aura.aura import Aura
    from .agissant import AgissantVu
    from .item import ItemVu
    from ...decors.decors import Decors
    from ....labyrinthe import Case

class CaseVue(crt.Case):
    """Une case vue par un agissant."""
    def __init__(self,position:crt.Position, opacite:float, niveau:int, repoussante:bool, agissant:Optional[AgissantVu], decors:Optional[Decors], items:Set[ItemVu], effets:Set[Effet], auras:Set[Aura]):
        crt.Case.__init__(self,position)
        self.opacite = opacite
        self.niveau = niveau
        self.repoussante = repoussante
        self.agissant = agissant
        self.decors = decors
        self.items = items
        self.effets = effets
        self.auras = auras

class CasePasVue(crt.Case):
    """Une case en dehors du champ de vision d'un agissant."""

def voit_case(case:Case) -> CaseVue:
    """Transforme une case en case vue."""
    return CaseVue(
        case.position,
        case.get_opacite(),
        case.niveau,
        case.repoussante,
        voit_agissant(case.agissant) if case.agissant else None,
        case.decors,
        {voit_item(item) for item in case.items},
        case.effets,
        case.auras
        )
