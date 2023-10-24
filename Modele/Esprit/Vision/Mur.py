from __future__ import annotations
from typing import TYPE_CHECKING

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ...entitee.agissant.vue.mur import MurVu

class VisionMur:
    def __init__(self, murs:dict[int,MurVu]):
        self.murs = murs

    def voit(self, mur:MurVu, tour: int):
        for tour_vu in self.murs:
            if tour_vu <= tour:
                # On retire les visions obsolètes
                self.murs.pop(tour_vu)
        self.murs[tour] = mur