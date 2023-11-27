"""
Les entitées (tout ce qui occupe le labyrinthe).
"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import carte as crt

# Pas de classe parente

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ..effet.effet import Effet
    from ..labyrinthe.mur import Mur

class Entitee:
    """La classe des entitées"""
    ID_max = 10 # Les 10 premières ID sont réservées
    def __init__(self, position: crt.Position=crt.POSITION_ABSENTE, id_: Optional[int]=None):
        self.position:crt.Position = position
        self._priorite:float = 0
        self.effets:list[Effet] = []
        if id_ is None:
            # Dans les cas d'héritage multiple, on peut déjà avoir exécuté cet __init__
            # On vérifie donc si on a déjà un ID
            if not hasattr(self, "id"):
                self.id = Entitee.ID_max
                Entitee.ID_max += 1
        else:
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

    @property
    def priorite(self) -> float:
        """Retourne la priorité de l'entitée."""
        return self._priorite

    def get_direction(self) -> crt.Direction:
        """Retourne la direction de l'entitée."""
        return crt.Direction.HAUT # Direction par défaut

class EntiteeSuperieure(Entitee):
    """La classe des entitées qui font bouger le labyrinthe autour d'eux."""

class Interactif(Entitee):
    """La classe des entitées avec lesquelles on peut interagir. Les humains, principalement, et quelques éléments de décors."""

class NonSuperposable(Entitee):
    """La classe des entitées qui 'occupent' une place, donc qu'on ne peut pas superposer (aux fantômes près)."""

class Mobile(Entitee):
    """La classe des entitées qui peuvent se déplacer (par elles-mêmes pour les agissants, en étant lancées pour les items)."""
    def __init__(self,position: crt.Position=crt.POSITION_ABSENTE, id_: Optional[int]=None, fantome:bool=False):
        Entitee.__init__(self,position,id_)
        self.fantome = fantome
    
    def passe(self,_mur:Mur) -> bool:
        """Renvoie True si l'entitée peut passer à travers le mur (fermé)."""
        return self.fantome
