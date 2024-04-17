"""Contient les classes des différents types de défensifs."""

from __future__ import annotations
from typing import TYPE_CHECKING

# Imports des classes parentes
from .defensif import Defensif

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ......effet.agissant.attaque import AttaqueParticulier

class DefensifProportion(Defensif):
    """Bloque une proportion des dégats (le plus courant)."""
    taux_degats:float

    def intercepte(self,attaque:AttaqueParticulier):
        degats_bloques = self.taux_degats
        for taux in self.taux_stats.values():
            degats_bloques *= taux
        attaque.degats *= (1-degats_bloques)

class DefensifSeuil(Defensif):
    """Bloque les dégats s'ils sont en dessous d'un seuil (utile contre les stratégies d'attaques nombreuses et rapides mais faibles)."""
    degats:float

    def intercepte(self,attaque:AttaqueParticulier):
        degats = self.degats
        for taux in self.taux_stats.values():
            degats *= taux
        if attaque.degats <= degats: #On bloque les attaques trop faibles
            attaque.degats = 0

class DefensifPlafond(Defensif):
    """Limite les dégats à un plafond (utile contre les stratégies d'attaques peu nombreuses mais puissantes)."""
    degats:float

    def intercepte(self,attaque:AttaqueParticulier):
        degats = self.degats
        for taux in self.taux_stats.values():
            degats *= 1/taux
        if attaque.degats > degats: #On limite la force des attaques
            attaque.degats = degats

class DefensifValeur(Defensif):
    """Bloque une valeur fixe de dégats (utile contre les stratégies d'attaques nombreuses et rapides mais faibles, et moins inutile que le DefensifSeuil contre les attaques puissantes)."""
    degats:float

    def intercepte(self,attaque:AttaqueParticulier):
        degats = self.degats
        for taux in self.taux_stats.values():
            degats *= taux
        if attaque.degats > degats: #On limite la force des attaques
            attaque.degats -= degats
        else:
            attaque.degats = 0
