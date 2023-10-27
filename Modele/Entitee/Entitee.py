from __future__ import annotations
from typing import TYPE_CHECKING, Optional, List
import carte as crt

# Pas de classe parente

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ..action.action import Action
    from ..effet.effet import Effet

class Entitee:
    """La classe des entitées"""
    ID_max = 10 # Les 10 premières ID sont réservées
    def __init__(self, position: crt.Position=crt.POSITION_ABSENTE, id_: Optional[int]=None):
        self.position:crt.Position = position
        self.priorite:float = 0
        self.effets:List[Effet] = []
        if id_ is None:
            id_ = Entitee.ID_max
            Entitee.ID_max += 1
        self.id = id_

    def set_position(self,position: crt.Position):
        """Change la position de l'entitée."""
        self.position = position

    def ajoute_effet(self,effet: Effet):
        """Ajoute un effet à l'entitée."""
        self.effets.append(effet)

    def get_position(self):
        """Retourne la position de l'entitée."""
        return self.position

    def get_priorite(self):
        """Retourne la priorité de l'entitée."""
        return self.priorite

    def get_direction(self) -> crt.Direction:
        """Retourne la direction de l'entitée."""
        return crt.Direction.HAUT # Direction par défaut

class EntiteeSuperieure(Entitee):
    """La classe des entitées qui font bouger le labyrinthe autour d'eux."""

class Fantome(Entitee):
    """La classe des entitées qui traversent les murs."""

class Interactif(Entitee):
    """La classe des entitées avec lesquelles on peut interagir. Les humains, principalement, et quelques éléments de décors."""

class NonSuperposable(Entitee):
    """La classe des entitées qui 'occupent' une place, donc qu'on ne peut pas superposer (aux fantômes près)."""

class Mobile(Entitee):
    """La classe des entitées qui peuvent se déplacer (par elles-mêmes pour les agissants, en étant lancées pour les items)."""
    def __init__(self, position: crt.Position=crt.POSITION_ABSENTE, id_: Optional[int]=None):
        super().__init__(position,id_)
        self.action:Optional[Action] = None

    def add_latence(self,latence: float):
        """Ajoute de la latence à l'action de l'entitée."""
        if self.action is not None:
            self.action.latence += latence

    def set_latence(self,latence: float):
        """Modifie la latence de l'action de l'entitée."""
        if self.action is not None:
            self.action.latence = latence
