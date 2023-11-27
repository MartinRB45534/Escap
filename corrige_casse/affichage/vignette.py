"""Contient la classe Vignette, qui est un élément qui est juste une image."""

from __future__ import annotations
from typing import Tuple, TYPE_CHECKING
import pygame

from .affichable import Affichable

from .erreur import DisplayError

if TYPE_CHECKING:
    from skin import Skin, Image

class Vignette(Affichable):
    """Un élément qui est juste une image."""
    def __init__(self,position:Tuple[int,int],taille:int,skin:Skin,direction:int=0):
        super().__init__()
        self.tailles = (taille,taille)
        self.position = position
        self.skin = skin
        self.direction = direction

    def set_tailles(self,tailles:Tuple[int,int]):
        if tailles != self.tailles:
            raise DisplayError(f"Tu ne peux pas modifier la taille d'une vignette ! Vérifie où tu as rangé {self}.")

    def affiche(self,screen:pygame.Surface,frame:int=1,frame_par_tour:int=1):
        self.skin.dessine_toi(screen,self.position,frame,frame_par_tour,self.tailles[0],self.direction)

class VignetteImage(Affichable):
    """Un élément qui est juste une image."""
    def __init__(self,position:Tuple[int,int],tailles:Tuple[int,int],skin:Image,direction:int=0):
        super().__init__()
        self.tailles = tailles
        self.position = position
        self.skin = skin
        self.direction = direction

    def set_tailles(self,tailles:Tuple[int,int]):
        if tailles != self.tailles:
            raise DisplayError(f"Tu ne peux pas modifier la taille d'une vignette ! Vérifie où tu as rangé {self}.")

    def affiche(self,screen:pygame.Surface,frame:int=1,frame_par_tour:int=1):
        self.skin.dessine_toi(screen,self.position,frame,frame_par_tour,self.tailles,0)
