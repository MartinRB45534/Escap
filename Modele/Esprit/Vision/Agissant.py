from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import Carte as crt

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ...Entitee.Agissant.Vue.Agissant import Agissant_vu
    from .Position import Vision_position
    from .Vision import Vision

class Vision_agissant:
    def __init__(self, agissant:Optional[Agissant_vu],tour:int,labyrinthe:Vision):
        self.agissants = {tour:agissant} if agissant is not None else {} # Les agissants sont stockés par tour
        # Résumé des infos (à mettre à jour à chaque nouvelle vision)
        self.labyrinthe = labyrinthe
        self.position:crt.Position|Vision_position = POSITION_INCONNUE
        # Autres infos
        self.dangerosite:float = 0 # Le risque qu'on prend à s'approcher de cet agissant
        self.importance:float = 0 # L'importance d'attaquer cet agissant
        # Une importance élevée malgré une dangerosité faible indique que l'agissant est plutôt un support
        # Une dangerosité élevée malgré une importance faible indique que l'agissant reçoit beaucoup de soutien (buff etc.)

    def antagonise(self, dangerosite:float, importance:float):
        self.dangerosite += dangerosite
        self.importance += importance

    def voit(self, agissant:Agissant_vu, tour: int):
        for tour_vu in self.agissants:
            if tour_vu <= tour:
                # On retire les visions obsolètes
                self.agissants.pop(tour_vu)
        self.agissants[tour] = agissant

# Imports utilisés dans le code
from .Position import POSITION_INCONNUE