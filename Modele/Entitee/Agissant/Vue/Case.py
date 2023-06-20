from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Set
import Carte as crt

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ....Effet.Effet import Effet
    from ....Effet.Auras import Aura
    from .Agissant import Agissant_vu
    from .Item import Item_vu
    from ...Decors.Decors import Decors

# Import de la classe parente
from ....Labyrinthe.Case import Case

class Case_vue(crt.Case):
    def __init__(self,position:crt.Position, opacite:float, niveau:int, repoussante:bool, agissant:Optional[Agissant_vu], decors:Optional[Decors], items:Set[Item_vu], effets:Set[Effet], auras:Set[Aura]):
        self.position = position
        self.opacite = opacite
        self.niveau = niveau
        self.repoussante = repoussante
        self.agissant = agissant
        self.decors = decors
        self.items = items
        self.effets = effets
        self.auras = auras

class Case_pas_vue(crt.Case):
    pass

def voit_case(case:Case) -> Case_vue:
    return Case_vue(
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

from .Agissant import voit_agissant
from .Item import voit_item