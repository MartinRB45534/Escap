from __future__ import annotations
from typing import TYPE_CHECKING

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ...Entitee.Item.Item import Item
    from ...Entitee.Item.Equippement.Degainable import Arme
    from .Item import On_hit

# Imports des classes parentes
from ...Effet import On_tick
from .Item import Effet_item

class Effet_arme(Effet_item):
    """Effet qui est placé sur une arme."""
    def __init__(self, item:Arme):
        self.item = item

class Effet_tranchant(On_tick, Effet_arme):
    """Effet qui modifie le tranchant d'une arme (en positif ou négatif)."""
    def modifie_tranchant(self, tranchant:float) -> float:
        raise NotImplementedError

class Effet_portee(On_tick, Effet_arme):
    """Effet qui modifie la portée d'une arme (en positif ou négatif)."""
    def modifie_portee(self, portee:float) -> float:
        raise NotImplementedError

class Effet_bombe(On_tick, Effet_item):
    """Enchantement qui confère des propriétés explosives à un item."""
    def __init__(self,item:Item,effet:On_hit):
        self.item = item
        self.effet = effet
        self.item.effets.append(self.effet)

    def execute(self) -> None:
        pass
