from __future__ import annotations
from typing import List, TYPE_CHECKING, Optional

from Jeu.Constantes import *
from Affichage.Skins.Skins import *
from Jeu.Labyrinthe.Structure_spatiale.Bord import *

if TYPE_CHECKING:
    from Jeu.Effet.Effets import Effet
    from Jeu.Controleur import Controleur

class Entitee:
    """La classe des entitées"""
    def __init__(self,position: Optional[Position]=None,ID: Optional[int]=None):
        self.position = position
        self.priorite = 0
        self.latence = 0
        self.effets:List[Effet] = []
        self.controleur = None
        if ID is None:
            self.ID = ID_MAX.incremente()
        else:
            self.ID = ID

    def set_position(self,position: Position):
        self.position = position

    def ajoute_effet(self,effet: Effet):
        self.effets.append(effet)

    def get_position(self):
        return self.position
    
    def get_priorite(self):
        return self.priorite

    def get_direction(self):
        return DIRECTIONS[0]

    def get_description(self,observation=0):
        return ["Une entitee","N'aurait pas dû être instanciée.","Probablement une erreur..."]

    def get_skin(self):
        return SKIN_MYSTERE

    def active(self,controleur:Controleur):
        self.controleur = controleur

    def get_classe(self):
        return Entitee

    def desactive(self):
        self.controleur = None

class Entitee_superieure(Entitee):
    """La classe des entitées qui font bouger le labyrinthe autour d'eux."""
    pass

class Fantome(Entitee):
    """La classe des entitées qui traversent les murs."""
    pass

class Interactif(Entitee):
    """La classe des entitées avec lesquelles on peut interagir. Les humains, principalement, et quelques éléments de décors."""
    pass

class Non_superposable(Entitee):
    """La classe des entitées qui 'occupent' une place, donc qu'on ne peut pas superposer (aux fantômes près)."""
    pass

class Mobile(Entitee):
    """La classe des entitées qui peuvent se déplacer (par elles-mêmes pour les agissants, en étant lancées pour les items)."""

    def add_latence(self,latence: float):
        self.latence += latence

    def set_latence(self,latence: float):
        self.latence = latence