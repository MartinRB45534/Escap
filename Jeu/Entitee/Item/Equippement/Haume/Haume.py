from __future__ import annotations
from typing import TYPE_CHECKING

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from Jeu.Controleur import Controleur
    from Jeu.Labyrinthe.Structure_spatiale.Position import Position

# Imports des classes parentes
from Jeu.Entitee.Item.Equippement.Equippement import Equipement

# Valeurs par défaut des paramètres
from Jeu.Labyrinthe.Structure_spatiale.Position import ABSENT

class Haume(Equipement):
    """La classe des équipements de type haume. On ne peut en porter qu'un à la fois."""
    def __init__(self,controleur:Controleur,position:Position=ABSENT):
        Equipement.__init__(self,controleur,position)
        self.poids = 3 #C'est plutôt léger.
        self.frottements = 6

    def get_classe(self):
        return Haume

    def get_titre(self,observation=0):
        return "Haume"

    def get_description(self,observation=0):
        return ["Un haume","..."]

    @staticmethod
    def get_image():
        return SKIN_CASQUE

    def get_skin(self):
        return SKIN_CASQUE_BASIQUE

# Imports utilisés dans le code
from Affichage.Skins.Skins import SKIN_CASQUE,SKIN_CASQUE_BASIQUE