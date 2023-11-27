"""
This module contains the base class for all GUI elements, Affichable,
and its subclasses Taille_variable and Proportionnel.
"""

from __future__ import annotations
from typing import TYPE_CHECKING, Literal
import pygame
if TYPE_CHECKING:
    from .placeholder import Placeheldholder
    from .cliquable import Cliquable
    from .survolable import Survolable

class Affichable:
    """Un élément qui s'affiche. Apparaît à l'écran."""
    def __init__(self):
        self.tailles:tuple[int,int] = (0,0) #La largeur et la hauteur (ou l'inverse ?)
        self.position:tuple[int,int] = (0,0)

    def set_tailles(self,tailles:tuple[int,int]):
        """Change les tailles de l'élément."""
        self.tailles = tailles

    def get_tailles(self,_tailles:tuple[int,int]): #Certains utilisent les tailles en entrée ici
        """Renvoie les tailles de l'élément."""
        return self.tailles

    def set_position(self,position:tuple[int,int]):
        """Change la position de l'élément."""
        self.position = position

    def decale(self,decalage:tuple[int,int]):
        """Décale l'élément (différent de set_position pour certaines classes filles)."""
        self.position = (self.position[0] + decalage[0],self.position[1] + decalage[1])

    def affiche(self,screen:pygame.Surface,frame:int=1,frame_par_tour:int=1):
        """Affiche l'élément à l'écran."""

    def touche(self,position:tuple[int,int]):
        """Renvoie True si la position est dans l'élément, False sinon."""
        return position[0]>=self.position[0] and position[1]>=self.position[1] and position[0]<self.position[0]+self.tailles[0] and position[1]<self.position[1]+self.tailles[1]

    def survol(self,_position:tuple[int,int]) -> Survolable|Literal[False]:
        """Renvoie l'élément survolé, ou False sinon."""
        return False

    def clique(self,_position:tuple[int,int],_droit:bool=False) -> Cliquable|Literal[False]:
        """Renvoie l'élément cliqué, ou False sinon."""
        return False

    def clique_placeholder(self,_placeheldholder:Placeheldholder,_droit: bool = False) -> Cliquable|Literal[False] :
        """Renvoie le placeholder, ou False sinon."""
        return False

    def scroll(self,_position:tuple[int,int],_x:int,_y:int) -> bool:
        """Renvoie l'élément scrollé, ou False sinon."""
        return False

    def update(self):
        """Met à jour l'affichage de l'élément."""

class TailleVariable(Affichable):
    """Les éléments dont la taille réelle dépend de la taille qu'on leur attribut, de façon compliquée."""

class Proportionnel(Affichable):
    """Les éléments dont les tailles sont proportionnelles."""
    def __init__(self,proportions:tuple[int,int]):
        super().__init__()
        self.proportions = proportions

    def get_tailles(self,tailles:tuple[int,int]):
        return (min(tailles[0]//self.proportions[0],
                    tailles[1]//self.proportions[1])
                *self.proportions[0],
                min(tailles[0]//self.proportions[0],
                    tailles[1]//self.proportions[1])
                *self.proportions[1])

    def set_tailles(self,tailles:tuple[int,int]):
        self.tailles = (min(tailles[0]//self.proportions[0],
                            tailles[1]//self.proportions[1])
                        *self.proportions[0],
                        min(tailles[0]//self.proportions[0],
                            tailles[1]//self.proportions[1])
                        *self.proportions[1])
