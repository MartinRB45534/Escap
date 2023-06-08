from __future__ import annotations
from typing import TYPE_CHECKING, Optional, List
import Carte as crt

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ..Action.Action import Action
    from ..Effet.Effet import Effet

# Pas de classe parente

class Entitee:
    """La classe des entitées"""
    ID_MAX = 10 # Les 10 premières ID sont réservées
    def __init__(self, position: crt.Position=crt.POSITION_ABSENTE, ID: Optional[int]=None):
        self.position:crt.Position = position
        self.priorite:float = 0
        self.effets:List[Effet] = []
        if ID is None:
            self.ID = Entitee.ID_MAX
            Entitee.ID_MAX += 1
        else:
            self.ID = ID

    def set_position(self,position: crt.Position):
        self.position = position

    def ajoute_effet(self,effet: Effet):
        self.effets.append(effet)

    def get_position(self):
        return self.position
    
    def get_priorite(self):
        return self.priorite

    def get_direction(self):
        return crt.Direction.HAUT # Direction par défaut

class Entitee_superieure(Entitee):
    """La classe des entitées qui font bouger le labyrinthe autour d'eux."""
    pass

class Fantome(Entitee):
    """La classe des entitées qui traversent les murs."""
    pass

class Interactif(Entitee):
    """La classe des entitées avec lesquelles on peut interagir. Les humains, principalement, et quelques éléments de décors."""
    pass

class Non_superposable(Entitee):
    """La classe des entitées qui 'occupent' une place, donc qu'on ne peut pas superposer (aux fantômes près)."""
    pass

class Mobile(Entitee):
    """La classe des entitées qui peuvent se déplacer (par elles-mêmes pour les agissants, en étant lancées pour les items)."""
    def __init__(self):
        self.action:Optional[Action] = None

    def add_latence(self,latence: float):
        if self.action is not None:
            self.action.latence += latence

    def set_latence(self,latence: float):
        if self.action is not None:
            self.action.latence = latence