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

class Maladie(OnFinTourAgissant):
    """L'effet de maladie. Applique un déboost à l'agissant. Peut se transmettre aux voisins. Il existe différentes maladies."""
    contagiosite:float
    distance:float
    persistence:float
    virulence:float
    def __init__(self):
        self.immunite = 0

    def fin_tour(self,agissant:Agissant):
        zone = agissant.labyrinthe.a_portee(
            agissant.position,self.distance,Deplacement.SPATIAL,Forme.CERCLE,Passage(False,False,False,True,False))
        for position in zone :
            voisin = agissant.labyrinthe.get_case(position).agissant
            if voisin:
                if random.random() < self.contagiosite and (not isinstance(effet, self.__class__) for effet in voisin.effets): #On ne tombe pas deux fois malade de la même maladie simultanément
                    voisin.effets.add(self.__class__()) #Nid à problèmes très potentiel !
        self.immunite += 1

    def termine(self) -> bool:
        return self.immunite > self.persistence
