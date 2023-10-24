"""Contient la classe Bouton, qui est un bouton cliquable avec un texte et une vignette"""

from __future__ import annotations
from typing import Tuple, Optional
import pygame

from .wrapper_cliquable import WrapperCliquable
from .pavage import PavageVertical, PavageHorizontal
from .marge import MargeVerticale, MargeHorizontale
from .texte import Texte
from .vignette import Vignette
from .skins import Skin

from ._ensure_pygame import transparency_flag

class Bouton(WrapperCliquable):
    def __init__(self, skin:Skin, texte:str, fond:Tuple[int,int,int]=(255,255,255), fond_marque_survol:Tuple[int,int,int]=(200,200,200), fond_marque_actif:Optional[Tuple[int,int,int]]=None, fond_marque_courant:Optional[Tuple[int,int,int]]=None, fond_est_courant:Optional[Tuple[int,int,int]]=None, fond_actif:Optional[Tuple[int,int,int]]=None):
        WrapperCliquable.__init__(self)

        self.fond = fond
        self.fond_marque_survol = fond_marque_survol if fond_marque_survol else self.fond
        self.fond_marque_actif = fond_marque_actif if fond_marque_actif else self.fond_marque_survol
        self.fond_marque_courant = fond_marque_courant if fond_marque_courant else self.fond_marque_actif
        self.fond_est_courant = fond_est_courant if fond_est_courant else self.fond
        self.fond_actif = fond_actif if fond_actif else self.fond_marque_courant

        self.skin = skin
        self.texte = texte
        self.init()

    def init(self):
        """Initialise le bouton"""
        contenu = PavageVertical()
        triptique = PavageHorizontal()
        triptique.set_contenu([MargeVerticale(),Vignette((0,0),20,self.skin),MargeVerticale(),Texte(self.texte),MargeVerticale()],[5,0,5,0,5])
        contenu.set_contenu([MargeHorizontale(),triptique,MargeHorizontale()],[5,0,5])
        self.set_contenu(contenu)

    def get_fond(self):
        """Renvoie le fond du bouton en fonction de son état"""
        if self.marque_survol:
            return self.fond_marque_survol
        elif self.marque_actif:
            return self.fond_marque_actif
        elif self.marque_courant:
            return self.fond_marque_courant
        elif self.est_courant:
            return self.fond_est_courant
        elif self.actif:
            return self.fond_actif
        else:
            return self.fond

    def affiche(self,screen:pygame.Surface,frame:int=1,frame_par_tour:int=1):
        assert self.contenu is not None
        surf = pygame.Surface(self.tailles,transparency_flag)
        surf.fill(self.get_fond())
        self.contenu.affiche(surf,frame,frame_par_tour)
        screen.blit(surf,self.position)
        for objet in self.objets:
            objet.affiche(screen,frame,frame_par_tour)
