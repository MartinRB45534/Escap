import pygame

from .Affichable import Affichable

class Marge(Affichable):
    """Un espace vide."""
    def __init__(self):
        self.tailles = (0,0) #La largeur et la hauteur (ou l'inverse ?)
        self.position = (0,0)

    def set_tailles(self,tailles):
        self.tailles = tailles

    def get_tailles(self,tailles):
        return tailles

    def set_position(self,position):
        self.position = position

    def touche(self,position):
        return False

    def affiche(self,screen:pygame.Surface,frame:int=1,frame_par_tour:int=1):
        pass

class Marge_verticale(Marge):
    """Un espace vide, placé verticalement."""

    def get_tailles(self,tailles):
        return [tailles[0],0]

class Marge_horizontale(Marge):
    """Un espace vide, placé verticalement."""

    def get_tailles(self,tailles):
        return [0,tailles[1]]
