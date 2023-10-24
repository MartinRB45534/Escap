"""
Ce module contient les classes Marge, qui sont les espaces vides dans les pavages.
"""

from __future__ import annotations
from typing import Tuple
import pygame

from .affichable import Affichable

class Marge(Affichable):
    """Un espace vide."""
    def touche(self,position:Tuple[int,int]):
        return False

    def affiche(self,screen:pygame.Surface,frame:int=1,frame_par_tour:int=1):
        pass

class MargeVerticale(Marge):
    """Un espace vide, placé verticalement."""

    def get_tailles(self,tailles:Tuple[int,int]):
        return (tailles[0],0)

class MargeHorizontale(Marge):
    """Un espace vide, placé verticalement."""

    def get_tailles(self,tailles:Tuple[int,int]):
        return (0,tailles[1])
