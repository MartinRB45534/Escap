from __future__ import annotations
from typing import TYPE_CHECKING
import carte as crt

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ....effet.action.non_skill import Impregne
    from ....effet.action.magie.magie import Magie
    from ....labyrinthe.labyrinthe import Labyrinthe

# Imports des classes parentes
from .Parchemin import Parchemin

class Parchemin_vierge(Parchemin):
    """Un parchemin qui peut être imprégné d'une magie."""
    def __init__(self,labyrinthe:Labyrinthe,impregne:Impregne|Magie,position:crt.Position=crt.POSITION_ABSENTE):
        Item.__init__(self,labyrinthe,position)
        self.action_portee:Impregne|Magie = impregne

# Imports utilisés dans le code
from ....entitee.item.item import Item