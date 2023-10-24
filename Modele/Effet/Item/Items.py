from __future__ import annotations
from typing import TYPE_CHECKING

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ...entitee.item.item import Item
    from ...entitee.item.equippement.degainable import Arme
    from .item import OnHit

# Imports des classes parentes
from ...effet import OnTick
from .item import EffetItem

class Effet_arme(EffetItem):
    """Effet qui est placé sur une arme."""
    def __init__(self, item:Arme):
        self.item = item

class Effet_tranchant(OnTick, Effet_arme):
    """Effet qui modifie le tranchant d'une arme (en positif ou négatif)."""
    def modifie_tranchant(self, tranchant:float) -> float:
        raise NotImplementedError

class Effet_portee(OnTick, Effet_arme):
    """Effet qui modifie la portée d'une arme (en positif ou négatif)."""
    def modifie_portee(self, portee:float) -> float:
        raise NotImplementedError

class Effet_bombe(OnTick, EffetItem):
    """Enchantement qui confère des propriétés explosives à un item."""
    def __init__(self,item:Item,effet:OnHit):
        self.item = item
        self.effet = effet
        self.item.effets.append(self.effet)

    def execute(self) -> None:
        pass
