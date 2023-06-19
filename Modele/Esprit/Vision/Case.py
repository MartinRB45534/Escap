from __future__ import annotations
from typing import TYPE_CHECKING, Dict

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ...Entitee.Agissant.Vue.Case import Case_vue

class Vision_case:
    def __init__(self, case:Case_vue, tour:int):
        self.cases:Dict[int, Case_vue] = {}
        self.voit(case, tour)

    def voit(self, case:Case_vue, tour: int):
        for tour_vu in self.cases:
            if tour_vu <= tour:
                # On retire les visions obsolètes
                self.cases.pop(tour_vu)
        self.cases[tour] = case