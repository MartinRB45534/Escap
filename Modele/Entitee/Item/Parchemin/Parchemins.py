"""Les deux classes de parchemins."""

from __future__ import annotations
from typing import TYPE_CHECKING
import carte as crt

# Imports des classes parentes
from .parchemin import Parchemin

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ....action.non_skill import Impregne
    from ....action.magie.magie import Magie
    from ....labyrinthe.labyrinthe import Labyrinthe
    from ....effet.agissant.agissant import EffetAgissant

class ParcheminPreEcrit(Parchemin):
    """La classe des consommables qui s'activent avec du mana."""
    def __init__(self,labyrinthe:Labyrinthe,effet:EffetAgissant,cout:float,duree:float,position:crt.Position=crt.POSITION_ABSENTE):
        Parchemin.__init__(self,labyrinthe,position)
        self.effet = effet
        self.duree = duree
        self.cout = cout

class ParcheminVierge(Parchemin):
    """Un parchemin qui peut être imprégné d'une magie."""
    def __init__(self,labyrinthe:Labyrinthe,impregne:Impregne|Magie,position:crt.Position=crt.POSITION_ABSENTE):
        Parchemin.__init__(self,labyrinthe,position)
        self.action_portee:Impregne|Magie = impregne
