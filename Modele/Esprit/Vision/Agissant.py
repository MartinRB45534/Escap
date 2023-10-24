from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import carte as crt

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ...entitee.agissant.vue.agissant import AgissantVu
    from .Position import VisionPosition
    from .Vision import Vision

class VisionAgissant:
    def __init__(self, agissant:Optional[AgissantVu],tour:int,labyrinthe:Vision):
        self.agissants = {tour:agissant} if agissant is not None else {} # Les agissants sont stockés par tour
        # Résumé des infos (à mettre à jour à chaque nouvelle vision)
        self.labyrinthe = labyrinthe
        self.position:crt.Position|VisionPosition = POSITION_INCONNUE
        # Autres infos
        self.DPS_contact:Optional[float] = None # Dégâts par seconde en contact
        self.DPS_distance:Optional[float] = None # Dégâts par seconde à distance
        self.portee:Optional[int] = None # Distance à laquelle il peut attaquer à distance
        self.resilience:Optional[float] = None # Résilience aux dégâts (comment la calculer ?)
        self.mobilite:Optional[float] = None # Mobilité (comment la calculer ?)
        self.degats:Optional[float] = None # Dégâts en propre (en distinguant le boosteur du boosté par exemple)
        self.defense:Optional[float] = None # Capacite à défendre les autres (comment la calculer ?)
        self.interference:Optional[float] = None # Capacité à gêner (comment la calculer ?)
        self.appreciabilite:Optional[float] = None # Critères arbitraires

    def voit(self, agissant:AgissantVu, tour: int):
        for tour_vu in self.agissants:
            if tour_vu <= tour:
                # On retire les visions obsolètes
                self.agissants.pop(tour_vu)
        self.agissants[tour] = agissant

# Imports utilisés dans le code
from .Position import POSITION_INCONNUE