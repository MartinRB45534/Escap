from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import carte as crt
from modele.labyrinthe.case import Case

# Imports des classes parentes
from ..case.case import EffetCase
from ..agissant.agissant import EffetAgissant

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ...entitee.agissant.agissant import Agissant
    from ...labyrinthe.case import Case
    from ...commons.elements import Element

# Un attaque se déroule en trois temps : l'action (sur l'attaquant), l'attaque (sur les cases), et l'attaque particulière (sur les agissants).

class AttaqueCase(EffetCase):
    """L'effet d'attaque dans sa version intermédiaire. Créée par une attaque (version générale), chargé d'attacher une attaque particulière aux agissants de la case, en passant d'abord les défenses de la case. Attaché à la case."""
    def __init__(self,responsable:Agissant,degats:float,element:Element,distance:str="contact",direction:Optional[crt.Direction] = None,taux_perce:float=0,inverse:bool=False):
        EffetCase.__init__(self)
        self.responsable = responsable
        self.degats = degats
        self.element = element
        self.direction = direction
        self.taux_perce = taux_perce
        self.inverse = inverse
        self.distance = distance

    def attaque(self,case:Case):
        """L'attaque est lancée sur la case."""
        victime_potentielle = case.agissant
        if victime_potentielle is not None and victime_potentielle not in self.responsable.esprit.corps:
            victime_potentielle.effets.append(AttaqueParticulier(self.responsable,self.degats,self.element,self.distance,self.direction,self.taux_perce,self.inverse))

class AttaqueCaseDelayee(AttaqueCase):
    """L'attaque est délayée, c'est à dire qu'elle ne s'effectue pas tout de suite. Elle sera déclenchée par un autre effet."""
    def __init__(self,responsable:Agissant,degats:float,element:Element,distance:str="distance",direction:Optional[crt.Direction] = None,taux_perce:float=0,inverse:bool=False):
        AttaqueCase.__init__(self,responsable,degats,element,distance,direction,taux_perce,inverse)
        self.attente = True

    def attaque(self, case: Case):
        if not self.attente:
            super().attaque(case)

    def termine(self) -> bool:
        return not self.attente

class AttaqueParticulier(EffetAgissant):
    """L'effet d'attaque dans sa version particulière. Créée par une attaque (version intermèdiaire), chargé d'infligé les dégats, en passant d'abord les défenses de l'agissant. Attachée à la victime."""
    def __init__(self,responsable:Agissant,degats:float,element:Element,distance:str="contact",direction:Optional[crt.Direction] = None,taux_perce:float = 0,inverse:bool=False):
        EffetAgissant.__init__(self)
        self.responsable = responsable
        self.degats = degats*(1-taux_perce)
        self.degats_imbloquables = degats*taux_perce #Ces dégats ne seront pas affectés par les bloquages.
        self.element = element
        self.direction = direction
        self.distance = distance
        self.inverse = inverse #Si True, l'affinité à l'élément est pénalisante et l'immunité est ignorée.

    def attaque(self, agissant:Agissant):
        """L'attaque est lancée sur l'agissant."""
        self.degats += self.degats_imbloquables
        agissant.subit(self.degats,self.element,self.inverse)
