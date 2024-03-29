"""
Contient la classe WrapperCliquable
"""

from __future__ import annotations
from typing import Literal, TYPE_CHECKING
import pygame

from .cliquable import Cliquable
from .wrapper import Wrapper

from ._ensure_pygame import transparency_flag

if TYPE_CHECKING:
    from .survolable import Survolable

class WrapperCliquable(Wrapper,Cliquable):
    """Un wrapper qui peut être cliqué"""
    def __init__(self):
        Cliquable.__init__(self)
        Wrapper.__init__(self)

    def affiche(self,screen:pygame.Surface,frame:int=1,frame_par_tour:int=1):
        assert self.contenu is not None
        surf = pygame.Surface(self.tailles,transparency_flag)
        # On ajoute un contour
        if self.marque_survol:
            self.marque_survol = False
            surf.fill((228,35,19,255)) #Rouge
            surf.fill(self.fond,pygame.Rect(2,2,self.tailles[0]-4,self.tailles[1]-4))
        elif self.marque_actif:
            self.marque_actif = False
            surf.fill((51,153,0,255)) #Vert
            surf.fill(self.fond,pygame.Rect(2,2,self.tailles[0]-4,self.tailles[1]-4))
        elif self.marque_courant:
            self.marque_courant = False
            surf.fill((255,192,0,255)) #Jaune
            surf.fill(self.fond,pygame.Rect(2,2,self.tailles[0]-4,self.tailles[1]-4))
        elif self.est_courant:
            self.est_courant = False
            surf.fill((238,238,238,255)) #Gris
            surf.fill(self.fond,pygame.Rect(2,2,self.tailles[0]-4,self.tailles[1]-4))
        elif self.actif:
            surf.fill((238,238,238,255)) #Gris
            surf.fill(self.fond,pygame.Rect(2,2,self.tailles[0]-4,self.tailles[1]-4))
        else:
            surf.fill(self.fond)
        self.contenu.affiche(surf,frame,frame_par_tour)
        screen.blit(surf,self.position)
        for objet in self.objets:
            objet.affiche(screen,frame,frame_par_tour)

    def clique(self,position:tuple[int,int],droit:bool=False) -> Cliquable|Literal[False]:
        clique = Wrapper.clique(self,position,droit)
        if clique is self:
            self.set_actif()
        else:
            self.unset_actif()
        if clique:
            return self
        return False

    def survol(self,position:tuple[int,int]) -> Survolable|Literal[False]:
        survol = Wrapper.survol(self,position)
        if survol is self:
            self.marque_survol = True
        else:
            self.marque_survol = False
        if survol:
            return self
        return False
