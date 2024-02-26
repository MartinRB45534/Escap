from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import carte as crt

# Imports des classes parentes
from ..agissant import EffetAgissant

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ...entitee import Agissant
    from ...commons import Element

class AttaqueParticulier(EffetAgissant):
    """L'effet d'attaque dans sa version particulière. Créée par une attaque (version intermèdiaire), chargé d'infligé les dégats, en passant d'abord les défenses de l'agissant. Attachée à la victime."""
    def __init__(self,responsable:Agissant,degats:float,element:Element,direction:Optional[crt.Direction] = None,taux_perce:float = 0,inverse:bool=False):
        EffetAgissant.__init__(self)
        self.responsable = responsable
        self.degats = degats*(1-taux_perce)
        self.degats_imbloquables = degats*taux_perce #Ces dégats ne seront pas affectés par les bloquages.
        self.element = element
        self.direction = direction
        self.inverse = inverse #Si True, l'affinité à l'élément est pénalisante et l'immunité est ignorée.

    def attaque(self, agissant:Agissant):
        """L'attaque est lancée sur l'agissant."""
        self.degats += self.degats_imbloquables
        agissant.subit(self.degats,self.element,self.inverse)
