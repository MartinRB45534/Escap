from __future__ import annotations
from typing import TYPE_CHECKING

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ....Entitee.Agissant.Agissant import Agissant

# Imports des classes parentes
from ...Effet import On_post_decision,On_tick

class Maladie(On_post_decision,On_tick):
    """L'effet de maladie. Applique un déboost à l'agissant. Peut se transmettre aux voisins. Il existe différentes maladies."""
    def __init__(self,contagiosite,distance,persistence,virulence):
        self.affiche = False
        self.phase = "démarrage"
        self.contagiosite = contagiosite
        self.distance = distance
        self.persistence = persistence
        self.virulence = virulence
        self.immunite = 0

    def action(self,malade:Agissant):
        raise NotImplementedError

    def contagion(self,malade:Agissant): #Méthode propre aux maladies
        zone = malade.labyrinthe.a_portee(malade.position,self.distance,Deplacement.SPATIAL,Forme.CERCLE,Passage(False,False,False,True,False))
        for position in zone :
            agissant = malade.labyrinthe.get_case(position).agissant
            if agissant != None:
                if random.random() < self.contagiosite and (type(self) != type(effet) for effet in agissant.effets): #On ne tombe pas deux fois malade de la même maladie
                    agissant.effets.append(type(self)(self.contagiosite,self.distance,self.persistence,self.virulence)) #Nid à problèmes très potentiel !

    def execute(self,malade:Agissant):
        if self.phase == "démarrage" :
            self.phase = "en cours"
        elif self.immunite <= self.persistence :
            self.termine()
        else :
            self.action(malade)

# Imports utilisés dans le code
import random
from ....Entitee.Agissant.Agissant import NoOne
from ....Labyrinthe.Deplacement import Deplacement
from ....Labyrinthe.Forme import Forme
from ....Labyrinthe.Passage import Passage