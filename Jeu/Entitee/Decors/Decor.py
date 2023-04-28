from Jeu.Constantes import *
from Affichage.Skins.Skins import *
from Jeu.Entitee.Entitee import *
from Jeu.Systeme.Constantes_decors.Decors import *


class Decors(Non_superposable):
    """La classe des éléments de décors qu'on ne peut pas traverser. On peut interagir avec certains ?"""
    def __init__(self,position:Position):
        Entitee.__init__(self,position)
        self.etat  = "intact"

    def get_classe(self):
        return Decors

class Decors_interactif(Decors,Interactif):
    """La classe des éléments de décors avec lesquels on peut interagir."""
    pass

class Ustensile(Decors_interactif):
    """Permet de créer un Item à partir d'ingrédients"""
    def __init__(self,position:Position,recettes:List[dict]):
        Decors.__init__(self,position)
        self.recettes = recettes #Les recettes de création d'Item

    def get_recettes(self):
        return self.recettes

    def cuisine(self,recette:dict):
        return eval(recette["produit"])(None)

    def get_classe(self):
        return Ustensile