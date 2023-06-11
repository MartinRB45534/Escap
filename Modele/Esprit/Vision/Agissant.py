from __future__ import annotations
from typing import TYPE_CHECKING
import Carte as crt

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ...Entitee.Agissant.Vue.Agissant import Agissant_vu
    from .Position import Vision_position

class Vision_agissant:
    def __init__(self, agissants:dict[int,Agissant_vu],labyrinthe):
        self.agissants = agissants
        # Résumé des infos (à mettre à jour à chaque nouvelle vision)
        self.labyrinthe = labyrinthe
        self.position:crt.Position|Vision_position = POSITION_INCONNUE

    def voit(self, agissant:Agissant_vu, tour: int):
        for tour_vu in self.agissants:
            if tour_vu <= tour:
                # On retire les visions obsolètes
                self.agissants.pop(tour_vu)
        self.agissants[tour] = agissant

# Imports utilisés dans le code
from .Position import POSITION_INCONNUE