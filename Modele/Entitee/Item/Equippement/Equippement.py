from __future__ import annotations
from typing import TYPE_CHECKING, Dict

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ..Controleur import Controleur
    from ..Labyrinthe.Structure_spatiale.Position import Position
    from ..Entitee.Agissant.Agissant import Agissant

# Imports des classes parentes
from ..Entitee.Item.Item import Item

# Valeurs par défaut des paramètres
from ..Labyrinthe.Structure_spatiale.Position import ABSENT

class Equipement(Item):
    """La classe des items qui peuvent être portés. Sont toujours actifs tant qu'ils sont portés."""
    def __init__(self,controleur:Controleur,position:Position=ABSENT):
        Item.__init__(self,controleur,position)
        self.taux_stats:Dict[str,float] = {}

    def equippe(self,agissant:Agissant):
        pass

    def desequippe(self):
        for cause in self.taux_stats:
            if cause == "incompatibilité porteur":
                self.taux_stats.pop(cause)
