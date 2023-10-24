"""
Ce module contient la classe Illustration, qui permet de charger une image.
"""

from typing import Tuple
from warnings import warn
import pygame

class Illustration:
    """Une image qui peut être affichée."""
    path = "Affichage/assets/"
    default = 'Affichage/assets/vide.png'
    def __init__(self,nom_fichier:str):
        try:
            self.image = pygame.image.load(self.path+nom_fichier).convert_alpha()
        except FileNotFoundError:
            self.image = pygame.image.load(self.default).convert_alpha()
            warn(f"N'a pas pu charger {nom_fichier}, remplacé par vide.png")
        except pygame.error as message:
            warn("N'oubliez pas d'initialiser pygame avant d'importer l'affichage !")
            raise message

    def dessine_toi(self,screen:pygame.Surface,position:Tuple[int,int],_frame:int=1,_frame_par_tour:int=1):
        """Dessine l'illustration sur l'écran."""
        screen.blit(self.image,position)

class Image(Illustration):
    """Une image avec une direction, qui peut être tournée."""
    def dessine_toi(self,screen:pygame.Surface,position:Tuple[int,int],tailles:Tuple[int,int]=(40,40),_frame:int=1,_frame_par_tour:int=1,direction:int=0):
        screen.blit(pygame.transform.scale(pygame.transform.rotate(self.image,int(direction)*-90),tailles),position)

class Skin(Illustration):
    """Un skin, qui peut être tourné et redimensionné."""
    def dessine_toi(self,screen:pygame.Surface,position:Tuple[int,int],taille:int=40,_frame:int=1,_frame_par_tour:int=1,direction:int=0):
        screen.blit(pygame.transform.scale(pygame.transform.rotate(self.image,int(direction)*-90),(taille,taille)),position)
