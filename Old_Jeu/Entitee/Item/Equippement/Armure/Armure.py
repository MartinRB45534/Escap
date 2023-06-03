from __future__ import annotations
from typing import TYPE_CHECKING

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from Old_Jeu.Controleur import Controleur
    from Old_Jeu.Labyrinthe.Structure_spatiale.Position import Position

# Imports des classes parentes
from Old_Jeu.Entitee.Item.Equippement.Equippement import Equipement

# Valeurs par défaut des paramètres
from Old_Jeu.Labyrinthe.Structure_spatiale.Position import ABSENT

class Armure(Equipement):
    """La classe des équipements de type armure. On ne peut en porter qu'une à la fois."""
    def __init__(self,controleur:Controleur,position:Position=ABSENT):
        Equipement.__init__(self,controleur,position)
        self.poids = 10 #C'est lourd !
        self.frottements = 8 #Il y a pire.

    def get_classe(self):
        return Armure

    def get_titre(self,observation=0):
        return "Armure"

    def get_description(self,observation=0):
        return ["Une armure","Essaye de l'enfiler !"]

    @staticmethod
    def get_image():
        return SKIN_ARMURE

    def get_skin(self):
        return SKIN_ARMURE_BASIQUE

# Imports utilisés dans le code
from Old_Affichage.Skins.Skins import SKIN_ARMURE, SKIN_ARMURE_BASIQUE