from __future__ import annotations
from typing import List, TYPE_CHECKING
import pygame
if TYPE_CHECKING:
    from Placeholder import Placeheldholder

class Affichable:
    """Un élément qui s'affiche. Apparaît à l'écran."""
    def __init__(self):
        self.tailles = (0,0) #La largeur et la hauteur (ou l'inverse ?)
        self.position = (0,0)

    def set_tailles(self,tailles):
        self.tailles = tailles

    def get_tailles(self,tailles): #Certains utilisent les tailles en entrée ici
        return self.tailles

    def set_position(self,position):
        self.position = position

    def decale(self,decalage):
        self.position = [self.position[0] + decalage[0],self.position[1] + decalage[1]]

    def affiche(self,screen:pygame.Surface,frame:int=1,frame_par_tour:int=1):
        pass

    def touche(self,position):
        return position[0]>=self.position[0] and position[1]>=self.position[1] and position[0]<self.position[0]+self.tailles[0] and position[1]<self.position[1]+self.tailles[1]

    def clique(self,position: List[int], droit: bool = False):
        #Trouve l'élément survolé par la souris et le renvoie
        res = False
        if self.touche(position):
            res = self
        return res
    
    def clique_placeholder(self,placeheldholder:Placeheldholder,droit: bool = False):
        return False

    def survol(self,position):
        #Trouve l'élément survolé par la souris et le renvoie
        res = False
        if self.touche(position):
            res = self
        return res

    def scroll(self,position,x,y):
        return False

    def update(self):
        pass

class Taille_variable(Affichable):
    """Les éléments dont la taille réelle dépend de la taille qu'on leur attribut, de façon compliquée."""

class Proportionnel(Affichable):
    def __init__(self,proportions):
        self.tailles = (0,0)
        self.position = (0,0)
        self.proportions = proportions

    def get_tailles(self,tailles):
        return [min(tailles[0]//self.proportions[0],tailles[1]//self.proportions[1])*self.proportions[0],min(tailles[0]//self.proportions[0],tailles[1]//self.proportions[1])*self.proportions[1]]

    def set_tailles(self,tailles):
        self.tailles = [min(tailles[0]//self.proportions[0],tailles[1]//self.proportions[1])*self.proportions[0],min(tailles[0]//self.proportions[0],tailles[1]//self.proportions[1])*self.proportions[1]]
