"""
Contient la classe maladie.
"""

from __future__ import annotations
from typing import TYPE_CHECKING
import random

# Imports des classes parentes
from ...timings import OnFinTourAgissant

# Imports utilisés dans le code
from .....commons import Deplacement, Forme, Passage

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from .....entitee.agissant.agissant import Agissant

class FamilleMaladie:
    """Une famille qui regroupe plusieurs maladies."""
    maladies:set[type[Maladie]]
    def __init__(self, maladies:set[type[Maladie]]):
        self.maladies = maladies

class Maladie(OnFinTourAgissant):
    """L'effet de maladie. Applique un déboost à l'agissant. Peut se transmettre aux voisins. Il existe différentes maladies."""
    contagiosite:float
    distance:float
    infectabilite:float
    persistence:float
    virulence:float
    famille:FamilleMaladie
    def __init__(self):
        self.immunite = 0

    def fin_tour(self,agissant:Agissant):
        self.contamine(agissant)

    def contamine(self,agissant:Agissant):
        """Contamine les voisins de l'agissant."""
        non_contagieux = agissant.statistiques.get_non_contagieux(self.__class__)
        non_contagieux -= self.contagiosite
        contagieux = min(1, max(0, 10 - non_contagieux)/10)
        zone = agissant.labyrinthe.a_portee(
            agissant.position,self.distance*contagieux,Deplacement.SPATIAL,Forme.CERCLE,Passage(False,False,False,True,False))
        for position in zone :
            voisin = agissant.labyrinthe.get_case(position).agissant
            if voisin:
                self.infecte(voisin)

    def infecte(self,voisin:Agissant):
        """Infecte un agissant."""
        non_infectable = voisin.statistiques.get_non_infectable(self.__class__)
        non_infectable -= self.infectabilite
        infectable = min(1, max(0, 10 - non_infectable)/10)
        if random.random() < infectable:
            for effet in [*voisin.effets]:
                if isinstance(effet, self.__class__):
                    voisin.effets.remove(effet)
            voisin.effets.add(self.__class__()) #Nid à problèmes très potentiel !

    def termine(self) -> bool:
        return self.immunite > self.persistence
