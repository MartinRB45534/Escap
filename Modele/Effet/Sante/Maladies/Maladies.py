from __future__ import annotations
from typing import TYPE_CHECKING

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ....Entitee.Agissant.Agissant import Agissant

# Imports des classes parentes
from .Maladie import Maladie

class Tirnogose(Maladie):
    """Maladie qui cause une perte progressive de PV. Peut se transmettre aux voisins."""
    def __init__(self,contagiosite:float,distance:float,persistence:float,virulence:float):
        self.affiche = False
        self.phase = "démarrage"
        self.contagiosite = contagiosite
        self.distance = distance
        self.persistence = persistence
        self.immunite = 0
        self.virulence = virulence

    def action(self,malade:Agissant):
        if self.phase == "en cours" :
            malade.statistiques.pv -= self.virulence
            self.immunite += 1

class Fibaluse(Maladie):
    """Maladie qui réduit les statistiques. Peut se transmettre aux voisins."""
    def __init__(self,contagiosite:float,distance:float,persistence:float,virulence:float):
        self.affiche = False
        self.phase = "démarrage"
        self.contagiosite = contagiosite
        self.distance = distance
        self.persistence = persistence
        self.immunite = 0
        self.virulence = virulence

    def action(self,malade:Agissant):
        if self.phase == "en cours" :
            self.immunite += 1

    def execute(self,malade:Agissant):
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
    def __init__(self,contagiosite:float,distance:float,persistence:float,virulence:float):
        self.affiche = False
        self.phase = "démarrage"
        self.contagiosite = contagiosite
        self.distance = distance
        self.persistence = persistence
        self.immunite = 0
        self.virulence = virulence

    def action(self,malade:Agissant):
        if self.phase == "démarrage" and random.random() < self.virulence :
            malade.meurt()
        elif self.phase == "en cours" :
            self.immunite += 1

# Imports utilisés dans le code
import random