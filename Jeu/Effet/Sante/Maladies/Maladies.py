from Jeu.Effet.Effet import *
from Jeu.Effet.Sante.Maladies.Maladie import *
from Jeu.Constantes import *
import random

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
