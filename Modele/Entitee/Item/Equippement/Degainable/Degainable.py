from __future__ import annotations
from typing import TYPE_CHECKING, Dict
import carte as crt

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from .....labyrinthe.labyrinthe import Labyrinthe
    from .....commons.elements import Element

# Imports des classes parentes
from ..equippement import Equippement

class Degainable(Equippement):
    """La classe des items qui doivent être dégainés. Sont utilisés en complément d'un skill, n'ont pas d'effet le reste du temps."""
    pass

class Arme(Degainable):
    """La classe des équipements qui augmentent la force d'attaque."""
    def __init__(self,labyrinthe:Labyrinthe,poids:float,frottements:float,element:Element,tranchant:float,portee:int,position:crt.Position=crt.POSITION_ABSENTE):
        Equippement.__init__(self,labyrinthe,position)
        self.element = element
        self.tranchant = tranchant
        self.taux_tranchant:Dict[str, float] = {}
        self.portee = portee
        self.taux_portee:Dict[str, float] = {}
        self.taux_stats:Dict[str, float] = {}

    def get_stats_attaque(self):
        tranchant = self.tranchant
        for taux in self.taux_tranchant.values():
            tranchant *= taux
        portee = self.portee
        for taux in self.taux_portee.values():
            portee *= taux
        for taux in self.taux_stats.values():
            tranchant *= taux
            portee *= taux
        return self.element,tranchant,portee

    @staticmethod
    def get_image():
        return SKIN_ARME
    
# Imports utilisés dans le code
from .....affichage.skins import SKIN_ARME