
"""Contient les classes des effets des items."""
from __future__ import annotations
from typing import TYPE_CHECKING

# Imports des classes parentes
from .item import EffetItem, EffetArme
from .timings import OnFinTourItem

# Imports utilisés dans le code
from ..case.attaque import AttaqueCase
from ...commons import Deplacement, Passage, Forme, Element

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ...entitee.item.item import Item

class Sursis(OnFinTourItem):
    """L'effet de sursis d'un projectile perçant qui a jusqu'à la fin du tour pour tuer l'agissant sur sa case."""
    def fin_tour(self, item: Item) -> None:
        if item.labyrinthe.position_case[item.position].agissant is not None:
            item.heurte()

class OnHit(EffetItem):
    """La classe des effets qui se déclenchent quand un projectile heurte un agissant ou un mur."""
    def __init__(self,portee:float,degats:float,element:Element=Element.TERRE):
        EffetItem.__init__(self)
        self.affiche = False
        self.portee = portee
        self.degats = degats
        self.element = element

    def hit(self,item:Item):
        """L'effet est déclenché quand l'item heurte un agissant ou un mur."""
        if item.action is None:
            raise ValueError("L'item frappe sans être en vol !")
        zone = item.labyrinthe.a_portee(item.position,self.portee,Deplacement.SPATIAL,Forme.CERCLE,Passage(False,False,False,True,False))
        for position in zone:
            item.labyrinthe.get_case(position).effets.add(AttaqueCase(item.action.lanceur,self.degats,self.element))

class EffetTranchant(EffetArme):
    """Effet qui modifie le tranchant d'une arme (en positif ou négatif)."""
    def modifie_tranchant(self, tranchant:float) -> float:
        """Modifie la stat tranchant de l'arme."""
        raise NotImplementedError

class EffetPortee(EffetArme):
    """Effet qui modifie la portée d'une arme (en positif ou négatif)."""
    def modifie_portee(self, portee:float) -> float:
        """Modifie la stat portée de l'arme."""
        raise NotImplementedError

class EffetBombe(OnHit):
    """Enchantement qui confère des propriétés explosives à un item."""
    def __init__(self,portee:float,degats:float,element:Element=Element.TERRE):
        OnHit.__init__(self,portee,degats,element)
