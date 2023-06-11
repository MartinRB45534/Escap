from __future__ import annotations
from typing import TYPE_CHECKING

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ...Entitee.Agissant.Vue.Mur import Mur_vu

class Vision_mur:
    def __init__(self, murs:dict[int,Mur_vu]):
        self.murs = murs

    def voit(self, mur:Mur_vu, tour: int):
        for tour_vu in self.murs:
            if tour_vu <= tour:
                # On retire les visions obsolètes
                self.murs.pop(tour_vu)
        self.murs[tour] = mur