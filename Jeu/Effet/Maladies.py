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

class Tirnogose(Maladie):
    """Maladie qui cause une perte progressive de PV. Peut se transmettre aux voisins."""
    def __init__(self,contagiosite,distance,persistence,virulence):
        self.affiche = False
        self.phase = "démarrage"
        self.contagiosite = contagiosite
        self.distance = distance
        self.persistence = persistence
        self.immunite = 0
        self.virulence = virulence

    def action(self,malade):
        if self.phase == "en cours" :
            malade.pv -= self.virulence
            self.immunite += 1

class Fibaluse(Maladie):
    """Maladie qui réduit les statistiques. Peut se transmettre aux voisins."""
    def __init__(self,contagiosite,distance,persistence,virulence):
        self.affiche = False
        self.phase = "démarrage"
        self.contagiosite = contagiosite
        self.distance = distance
        self.persistence = persistence
        self.immunite = 0
        self.virulence = virulence

    def action(self,malade):
        if self.phase == "démarrage" and "maladf" not in malade.taux_stats :
            malade.taux_stats["maladf"] = self.virulence
        elif self.phase == "en cours" :
            self.immunite += 1
        elif self.phase == "terminé" :
            malade.taux_stats.pop("maladf")

    def execute(self,malade):
        if self.phase == "démarrage" :
            self.action(malade)
            self.phase = "en cours"
        elif self.persistence <= self.immunite :
            self.termine()
            self.action(malade)
        else :
            self.action(malade)

class Ibsutiomialgie(Maladie):
    """Maladie qui peut causer une mort subite. Peut se transmettre aux voisins."""
    def __init__(self,contagiosite,distance,persistence,virulence):
        self.affiche = False
        self.phase = "démarrage"
        self.contagiosite = contagiosite
        self.distance = distance
        self.persistence = persistence
        self.immunite = 0
        self.virulence = virulence

    def action(self,malade):
        if self.phase == "démarrage" and random.random() < self.virulence :
            malade.meurt()
        elif self.phase == "en cours" :
            self.immunite += 1

class Poison(On_debut_tour,On_tick):
    """La classe des effets d'empoisonnement."""
    def __init__(self,responsable,degats_max,progression):
        self.affiche = False
        self.phase = "démarrage"
        self.responsable = responsable
        self.degats = 0
        self.progression = progression
        self.degats_max = degats_max

    def action(self,victime):
        if self.phase == "en cours" :
            victime.pv -= self.degats
            if self.degats < self.degats_max:
                self.degats += self.progression

    def execute(self,victime):
        if self.phase == "démarrage" :
            self.phase = "en cours"
        elif victime.etat == "mort" :
            self.termine()
        else :
            self.action(victime)

class Antidote(One_shot,On_fin_tour):
    """Effet qui supprime les effets de poison du joueur."""
    def __init__(self):
        self.affiche = False
        self.phase = "démarrage"

    def action(self,porteur):
        for effet in porteur.effets:
            if isinstance(effet,Poison):
                effet.phase = "terminé" # Rajouter une condition de priorite

class Medicament(One_shot,On_fin_tour):
    """Effet qui supprime les effets de maladie du joueur."""
    def __init__(self):
        self.affiche = False
        self.phase = "démarrage"

    def action(self,porteur):
        for effet in porteur.effets:
            if isinstance(effet,Maladie): # Créer des médicaments différents selon les maladies ?
                effet.phase = "terminé" # Rajouter une condition de priorite

class Purification(One_shot,On_fin_tour):
    """Effet qui supprime les effets de poison ou maladie du joueur."""
    def __init__(self):
        self.affiche = False
        self.phase = "démarrage"

    def action(self,porteur):
        for effet in porteur.effets:
            if isinstance(effet,(Maladie,Poison)):
                effet.phase = "terminé" # Rajouter une condition de priorite
