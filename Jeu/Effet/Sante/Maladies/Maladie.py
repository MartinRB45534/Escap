from Jeu.Effet.Effet import *
from Jeu.Constantes import *
import random

class Maladie(On_post_decision,On_tick):
    """L'effet de maladie. Applique un déboost à l'agissant. Peut se transmettre aux voisins. Il existe différentes maladies."""
    def __init__(self,contagiosite,distance,persistence,virulence):
        self.affiche = False
        self.phase = "démarrage"
        self.contagiosite = contagiosite
        self.distance = distance
        self.persistence = persistence
        self.immunite = 0

    def action(self,malade):
        print("À surdéfinir !")

    def contagion(self,malade): #Méthode propre aux maladies
        voisins = malade.controleur.trouve_agissants(malade,self.distance)
        for voisin in voisins :
            if random.random() < self.contagiosite and (type(self) != type(effet) for effet in voisin.effets): #On ne tombe pas deux fois malade de la même maladie
                voisin.effets.append(type(self)(self.contagiosite,self.distance,self.persistence,self.virulence)) #Nid à problèmes très potentiel !

    def execute(self,malade):
        if self.phase == "démarrage" :
            self.phase = "en cours"
        elif self.immunite <= self.persistence :
            self.termine()
        else :
            self.action(malade)
