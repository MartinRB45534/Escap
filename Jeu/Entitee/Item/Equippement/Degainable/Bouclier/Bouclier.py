from __future__ import annotations
from typing import TYPE_CHECKING

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from Jeu.Controleur import Controleur
    from Jeu.Labyrinthe.Structure_spatiale.Position import Position

# Imports des classes parentes
from Jeu.Entitee.Item.Equippement.Degainable.Degainable import Degainable

# Valeurs par défaut des paramètres
from Jeu.Labyrinthe.Structure_spatiale.Position import ABSENT

class Bouclier(Degainable):
    """La classe des boucliers. Permettent de se protéger des attaques lorsqu'ils sont utilisés."""
    def __init__(self,controleur:Controleur,degats_bloques:float,taux_degats:float,position:Position=ABSENT):
        Equipement.__init__(self,controleur,position)
        self.degats_bloques = degats_bloques
        self.taux_degats = taux_degats
        self.taux_stats = {}
        self.poids = 5
        self.frottements = 1 #En mode frisbee ça volle très bien !

    def intercepte(self,attaque:Attaque_case):
        attaque.degats -= self.degats_bloques
        if attaque.degats < 0:
            attaque.degats = 0
        else :
            for taux in self.taux_stats.values():
                attaque.degats *=  taux
            attaque.degats *= self.taux_degats

    def get_classe(self):
        return Bouclier

    def get_titre(self,observation=0):
        return "Bouclier"

    def get_description(self,observation=0):
        return ["Un frisbee","Ah non, c'est un bouclier !"]

    @staticmethod
    def get_image():
        return SKIN_BOUCLIER

# Imports utilisés dans le code
from Affichage.Skins.Skins import SKIN_BOUCLIER
from Jeu.Effet.Attaque.Attaque import Attaque_case
from Jeu.Entitee.Item.Equippement.Equippement import Equipement