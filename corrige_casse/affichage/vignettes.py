"""Contient les classes de vignettes."""

from __future__ import annotations
from typing import List, Tuple, Optional
import pygame

from .affichable import Affichable
from .cliquable import Cliquable
from .noeud import Noeud
from .placeholder import Placeholder, Placeheldholder
from .texte import Texte
from .vignette import Vignette

from .skins import SKIN_SHADE

class VignetteComposee(Cliquable):
    """Une vignette qui est composée de plusieurs vignettes."""
    def __init__(self,vignettes:List[Affichable],taille:int,shade:bool=False,invalide:bool=False):
        super().__init__()
        self.tailles = (taille,taille)
        self.objets = vignettes
        if shade or invalide:
            self.objets.append(Vignette((0,0),taille,SKIN_SHADE))
        if invalide:
            self.objets.append(Vignette((0,0),taille,SKIN_SHADE))

class VignettePlaceholder(VignetteComposee, Placeholder):
    """Une vignette qui est composée de plusieurs vignettes et d'un placeholder."""
    def __init__(self,placeheldholder:Placeheldholder,placeheld:Optional[Cliquable],placeheldholder_ajuster:Optional[Affichable],vignettes:List[Affichable],taille:int,shade:bool=False,invalide:bool=False):
        Placeholder.__init__(self,placeheldholder,placeheld,placeheldholder_ajuster)
        VignetteComposee.__init__(self,vignettes,taille,shade,invalide)

    def affiche(self, screen: pygame.Surface, frame: int = 1, frame_par_tour: int = 1):
        if self.marque_actif or self.marque_courant or self.marque_survol:
            self.decale((2,2)) # /!\ Trouver un meilleur moyen de marquer l'activité
        super().affiche(screen, frame, frame_par_tour)
        if self.marque_actif or self.marque_courant or self.marque_survol:
            self.decale((-2,-2))
            self.marque_actif = False
            self.marque_courant = False
            self.marque_survol = False

class VignetteComposeeTexte(VignetteComposee):
    """Une vignette qui est composée de plusieurs vignettes et d'un texte."""
    def __init__(self,vignettes:List[Affichable],blabla:str,taille:int,shade:bool=False,invalide:bool=False):
        VignetteComposee.__init__(self,vignettes,taille,shade,invalide)
        texte = Texte(blabla)
        self.objets.append(texte)
        tailles_texte = texte.get_tailles(self.tailles)
        texte.set_position((self.tailles[0]-tailles_texte[0],self.tailles[1]-tailles_texte[1]))

    def set_tailles(self, tailles: Tuple[int, int]):
        VignetteComposee.set_tailles(self,tailles)
        for objet in self.objets:
            if isinstance(objet,Texte):
                tailles_texte = objet.get_tailles(self.tailles)
                objet.set_position((self.tailles[0]-tailles_texte[0],self.tailles[1]-tailles_texte[1]))

class VignettePlaceholderTexte(VignetteComposeeTexte,VignettePlaceholder):
    """Une vignette qui est composée de plusieurs vignettes, d'un texte et d'un placeholder."""
    def __init__(self,placeheldholder:Placeheldholder,placeheld:Optional[Cliquable],placeheldholder_ajuster:Optional[Affichable],vignettes:List[Affichable],blabla:str,taille:int,shade:bool=False,invalide:bool=False):
        VignettePlaceholder.__init__(self,placeheldholder,placeheld,placeheldholder_ajuster,vignettes,taille,shade,invalide)
        VignetteComposeeTexte.__init__(self,vignettes,blabla,taille,shade,invalide)

class VignettePlaceholderUpdatable(VignettePlaceholder):
    """Une vignette qui est composée de plusieurs vignettes, d'un texte et d'un placeholder, et qui peut être mise à jour."""
    def __init__(self,placeheldholder:Placeheldholder,placeheld:Noeud,placeheldholder_ajuster:Affichable,vignettes:List[Affichable],taille:int,shade:bool=False,invalide:bool=False):
        VignettePlaceholder.__init__(self,placeheldholder,placeheld,placeheldholder_ajuster,vignettes,taille,shade,invalide)

        self.shades:List[Affichable] = []
        if shade or invalide:
            self.objets.append(Vignette((0,0),taille,SKIN_SHADE))
            self.shades.append(Vignette((0,0),taille,SKIN_SHADE))
        if invalide:
            self.objets.append(Vignette((0,0),taille,SKIN_SHADE))
            self.shades.append(Vignette((0,0),taille,SKIN_SHADE))
