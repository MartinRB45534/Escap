from __future__ import annotations
from typing import TYPE_CHECKING, List
import Carte as crt

# Imports des classes parentes
from ..Entitee import Non_superposable, Interactif

class Decors(Non_superposable):
    """La classe des éléments de décors qu'on ne peut pas traverser. On peut interagir avec certains ?"""
    def __init__(self,position:crt.Position=crt.POSITION_ABSENTE):
        Entitee.__init__(self,position)
        self.etat  = "intact"

class Decors_interactif(Decors,Interactif):
    """La classe des éléments de décors avec lesquels on peut interagir."""
    pass

class Ustensile(Decors_interactif):
    """Permet de créer un Item à partir d'ingrédients"""
    def __init__(self,recettes:List[dict],position:crt.Position=crt.POSITION_ABSENTE):
        Decors.__init__(self,position)
        self.recettes = recettes #Les recettes de création d'Item

    def get_recettes(self):
        return self.recettes

    def cuisine(self,recette:dict):
        return eval(recette["produit"])(crt.POSITION_ABSENTE) # TODO : purger le code des eval !!!
    
# Imports utilisés dans le code
from ..Entitee import Entitee