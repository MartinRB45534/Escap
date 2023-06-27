from __future__ import annotations
from typing import TYPE_CHECKING

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from .....Entitee.Agissant.Agissant import Agissant

# Imports des classes parentes
from ....Effet import On_tick
from ...Agissant import Effet_agissant

class Maladie(On_tick, Effet_agissant):
    """L'effet de maladie. Applique un déboost à l'agissant. Peut se transmettre aux voisins. Il existe différentes maladies."""
    def __init__(self,agissant:Agissant,contagiosite:float,distance:float,persistence:float,virulence:float):
        self.agissant = agissant
        self.contagiosite = contagiosite
        self.distance = distance
        self.persistence = persistence
        self.virulence = virulence
        self.immunite = 0

    def action(self) -> None:
        raise NotImplementedError

    def contagion(self): #Méthode propre aux maladies
        zone = self.agissant.labyrinthe.a_portee(self.agissant.position,self.distance,Deplacement.SPATIAL,Forme.CERCLE,Passage(False,False,False,True,False))
        for position in zone :
            agissant = self.agissant.labyrinthe.get_case(position).agissant
            if agissant != None:
                if random.random() < self.contagiosite and (type(self) != type(effet) for effet in agissant.effets): #On ne tombe pas deux fois malade de la même maladie
                    agissant.effets.append(type(self)(agissant,self.contagiosite,self.distance,self.persistence,self.virulence)) #Nid à problèmes très potentiel !

    def execute(self):
        self.action()

    def termine(self) -> bool:
        return self.immunite > self.persistence

# Imports utilisés dans le code
import random
from .....Labyrinthe.Deplacement import Deplacement
from .....Labyrinthe.Forme import Forme
from .....Labyrinthe.Passage import Passage