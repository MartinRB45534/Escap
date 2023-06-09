from __future__ import annotations
from typing import TYPE_CHECKING
import pygame
from warnings import warn

if TYPE_CHECKING:
    from Skin import Skin, Image

from .Affichable import Affichable

class Vignette(Affichable):
    """Un élément qui est juste une image."""
    def __init__(self,position,taille,skin:Skin,direction:int=0):
        self.tailles = [taille,taille]
        self.position = position
        self.skin = skin
        self.direction = direction

    def set_tailles(self,tailles):
        if tailles != self.tailles:
            warn(f"Tu ne peux pas modifier la taille d'une vignette ! Vérifie où tu as rangé {self}.")

    def affiche(self,screen:pygame.Surface,frame:int=1,frame_par_tour:int=1):
        self.skin.dessine_toi(screen,self.position,self.tailles[0],frame,frame_par_tour,self.direction)

class Vignette_image(Vignette):
    def __init__(self,position,tailles,skin:Image,direction:int=0):
        self.tailles = tailles
        self.position = position
        self.skin = skin
        self.direction = direction

    def affiche(self,screen:pygame.Surface,frame:int=1,frame_par_tour:int=1):
        self.skin.dessine_toi(screen,self.position,self.tailles,frame,frame_par_tour,0)
