"""Contient la classe Bouclier."""

from __future__ import annotations
from typing import TYPE_CHECKING
import carte as crt

# Imports des classes parentes
from ..degainable import Degainable

# Imports utilisés dans le code
from ......affichage import SKIN_BOUCLIER
from ......effet import AttaqueCase

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ......labyrinthe.labyrinthe import Labyrinthe

class Bouclier(Degainable):
    """La classe des boucliers. Permettent de se protéger des attaques lorsqu'ils sont utilisés."""
    def __init__(self,labyrinthe:Labyrinthe,poids:float,frottements:float,degats_bloques:float,taux_degats:float,position:crt.Position=crt.POSITION_ABSENTE):
        Degainable.__init__(self,labyrinthe,position)
        self.degats_bloques = degats_bloques
        self.taux_degats = taux_degats
        self.taux_stats = {}
        self.poids = poids
        self.frottements = frottements

    def intercepte(self,attaque:AttaqueCase):
        """Intercepte une attaque."""
        attaque.degats -= self.degats_bloques
        if attaque.degats < 0:
            attaque.degats = 0
        else :
            for taux in self.taux_stats.values():
                attaque.degats *=  taux
            attaque.degats *= self.taux_degats

    @staticmethod
    def get_image():
        return SKIN_BOUCLIER
