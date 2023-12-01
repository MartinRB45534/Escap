"""Contient la classe Degainable, parente de tous les items qui doivent être dégainés."""

from __future__ import annotations
from typing import TYPE_CHECKING
import carte as crt

# Imports des classes parentes
from ..equippement import Equippement
    
# Imports utilisés dans le code
from .....affichage import SKIN_ARME

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from .....labyrinthe.labyrinthe import Labyrinthe
    from .....commons.elements import Element

class Degainable(Equippement):
    """La classe des items qui doivent être dégainés. Sont utilisés en complément d'un skill, n'ont pas d'effet le reste du temps."""

class Arme(Degainable):
    """La classe des équipements qui augmentent la force d'attaque."""
    def __init__(self,labyrinthe:Labyrinthe,poids:float,frottements:float,element:Element,tranchant:float,portee:float,position:crt.Position=crt.POSITION_ABSENTE):
        Degainable.__init__(self,labyrinthe,position)
        self.poids = poids
        self.frottements = frottements
        self.element = element
        self.tranchant = tranchant
        self.taux_tranchant:dict[str, float] = {}
        self.portee = portee
        self.taux_portee:dict[str, float] = {}
        self.taux_stats:dict[str, float] = {}

    def get_stats_attaque(self):
        """Renvoie les stats de l'arme."""
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
