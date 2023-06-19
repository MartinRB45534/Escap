from __future__ import annotations
from typing import TYPE_CHECKING
import Carte as crt

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ....Action.Non_skill import Impregne
    from ....Action.Magie.Magie import Magie
    from ....Labyrinthe.Labyrinthe import Labyrinthe

# Imports des classes parentes
from .Parchemin import Parchemin

class Parchemin_vierge(Parchemin):
    """Un parchemin qui peut être imprégné d'une magie."""
    def __init__(self,labyrinthe:Labyrinthe,impregne:Impregne|Magie,position:crt.Position=crt.POSITION_ABSENTE):
        Item.__init__(self,labyrinthe,position)
        self.action_portee:Impregne|Magie = impregne

# Imports utilisés dans le code
from ....Entitee.Item.Item import Item