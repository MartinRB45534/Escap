from __future__ import annotations
from typing import TYPE_CHECKING

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ...entitee.agissant.vue.case import CaseVue

class VisionCase:
    def __init__(self, case:CaseVue, tour:int):
        self.cases:dict[int, CaseVue] = {}
        self.voit(case, tour)

    def voit(self, case:CaseVue, tour: int):
        for tour_vu in self.cases:
            if tour_vu <= tour:
                # On retire les visions obsolètes
                self.cases.pop(tour_vu)
        self.cases[tour] = case