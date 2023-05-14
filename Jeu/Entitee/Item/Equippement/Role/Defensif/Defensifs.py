from __future__ import annotations
from typing import TYPE_CHECKING

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from Jeu.Effet.Attaque.Attaque import Attaque_particulier

# Imports des classes parentes
from Jeu.Entitee.Item.Equippement.Role.Defensif.Defensif import Defensif

class Defensif_proportion(Defensif):
    def __init__(self,taux_degats:float):
        self.taux_degats = taux_degats

    def intercepte(self,attaque:Attaque_particulier):
        degats_bloques = self.taux_degats
        for taux in self.taux_stats.values():
            degats_bloques *= taux
        attaque.degats *= (1-degats_bloques)

class Defensif_seuil(Defensif):
    def __init__(self,degats:float):
        self.degats = degats

    def intercepte(self,attaque:Attaque_particulier):
        degats = self.degats
        for taux in self.taux_stats.values():
            degats *= taux
        if attaque.degats <= degats: #On bloque les attaques trop faibles
            attaque.degats = 0

class Defensif_plafond(Defensif):
    def __init__(self,degats:float):
        self.degats = degats

    def intercepte(self,attaque:Attaque_particulier):
        degats = self.degats
        for taux in self.taux_stats.values():
            degats *= 1/taux
        if attaque.degats > degats: #On limite la force des attaques
            attaque.degats = degats

class Defensif_valeur(Defensif):
    def __init__(self,degats:float):
        self.degats = degats

    def intercepte(self,attaque:Attaque_particulier):
        degats = self.degats
        for taux in self.taux_stats.values():
            degats *= taux
        if attaque.degats > degats: #On limite la force des attaques
            attaque.degats -= degats
        else:
            attaque.degats = 0
#On suppose pour l'instant qu'un item défensif n'appartient qu'à une seule de ces catégories
