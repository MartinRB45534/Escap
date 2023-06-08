from __future__ import annotations
from typing import TYPE_CHECKING
import Carte as crt

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ......Labyrinthe.Labyrinthe import Labyrinthe

# Imports des classes parentes
from ..Degainable import Degainable

class Bouclier(Degainable):
    """La classe des boucliers. Permettent de se protéger des attaques lorsqu'ils sont utilisés."""
    def __init__(self,labyrinthe:Labyrinthe,poids:float,frottements:float,degats_bloques:float,taux_degats:float,position:crt.Position=crt.POSITION_ABSENTE):
        Equipement.__init__(self,labyrinthe,position)
        self.degats_bloques = degats_bloques
        self.taux_degats = taux_degats
        self.taux_stats = {}
        self.poids = poids
        self.frottements = frottements

    def intercepte(self,attaque:Attaque_case):
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

# Imports utilisés dans le code
from Old_Affichage.Skins.Skins import SKIN_BOUCLIER
from ......Effet.Attaque.Attaque import Attaque_case
from ...Equippement import Equipement