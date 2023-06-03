from __future__ import annotations
from typing import TYPE_CHECKING

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from Old_Jeu.Entitee.Agissant.Agissant import Agissant

# Imports des classes parentes
from Old_Jeu.Effet.Effet import On_debut_tour,On_tick

class Poison(On_debut_tour,On_tick):
    """La classe des effets d'empoisonnement."""
    def __init__(self,responsable:Agissant,degats_max:float,progression:float):
        self.affiche = False
        self.phase = "démarrage"
        self.responsable = responsable
        self.degats = 0
        self.progression = progression
        self.degats_max = degats_max

    def action(self,victime:Agissant):
        if self.phase == "en cours" :
            victime.pv -= self.degats
            if self.degats < self.degats_max:
                self.degats += self.progression

    def execute(self,victime:Agissant):
        if self.phase == "démarrage" :
            self.phase = "en cours"
        elif victime.etat == "mort" :
            self.termine()
        else :
            self.action(victime)
