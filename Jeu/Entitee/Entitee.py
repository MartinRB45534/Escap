from Jeu.Constantes import *
from Jeu.Skins.Skins import *

class Entitee:
    """La classe des entitées"""
    def __init__(self,position,ID=None):
        self.position = position
        self.latence = 0
        self.effets = []
        self.controleur = None
        if ID==None:
            self.ID = ID_MAX.incremente()
        else:
            self.ID = ID

    def set_position(self,position):
        self.position = position

    def ajoute_effet(self,effet):
        self.effets.append(effet)

    def get_position(self):
        return self.position

    def get_direction(self):
        return DIRECTIONS[0]

    def get_description(self,observation):
        return ["Une entitee","N'aurait pas dû être instanciée.","Probablement une erreur..."]

    def get_skin(self):
        return SKIN_MYSTERE

    def active(self,controleur):
        self.controleur = controleur

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

    def add_latence(self,latence):
        self.latence += latence

    def set_latence(self,latence):
        self.latence = latence