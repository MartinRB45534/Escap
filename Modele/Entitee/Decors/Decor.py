from __future__ import annotations
from typing import TYPE_CHECKING, List

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from Old_Jeu.Controleur import Controleur
    from Old_Jeu.Labyrinthe.Structure_spatiale.Position import Position

# Imports des classes parentes
from Old_Jeu.Entitee.Entitee import Non_superposable, Interactif

# Valeurs par défaut des paramètres
from Old_Jeu.Labyrinthe.Structure_spatiale.Position import ABSENT

class Decors(Non_superposable):
    """La classe des éléments de décors qu'on ne peut pas traverser. On peut interagir avec certains ?"""
    def __init__(self,controleur:Controleur,position:Position=ABSENT):
        Entitee.__init__(self,controleur,position)
        self.etat  = "intact"

    def get_classe(self):
        return Decors

class Decors_interactif(Decors,Interactif):
    """La classe des éléments de décors avec lesquels on peut interagir."""
    pass

class Ustensile(Decors_interactif):
    """Permet de créer un Item à partir d'ingrédients"""
    def __init__(self,controleur:Controleur,recettes:List[dict],position:Position=ABSENT):
        Decors.__init__(self,controleur,position)
        self.recettes = recettes #Les recettes de création d'Item

    def get_recettes(self):
        return self.recettes

    def cuisine(self,recette:dict):
        return eval(recette["produit"])(self.controleur,ABSENT)

    def get_classe(self):
        return Ustensile
    
# Imports utilisés dans le code
from Old_Jeu.Entitee.Entitee import Entitee