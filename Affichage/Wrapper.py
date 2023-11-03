"""
Conteneur avec un unique élément
"""

from __future__ import annotations
from typing import Optional, Tuple, List, Literal, TYPE_CHECKING
from warnings import warn
import pygame

from .affichable import Affichable
from .survolable import Survolable
from .cliquable import Cliquable

from ._ensure_pygame import transparency_flag

if TYPE_CHECKING:
    from .placeholder import Placeheldholder

class Wrapper(Affichable):
    """Un conteneur avec un unique élément"""
    def __init__(self):
        super().__init__()
        self.objets:List[Affichable] = []
        self.contenu:Optional[Affichable] = None #L'objet qu'il 'contient'
        self.fond:Tuple[int,int,int,int]|Tuple[int,int,int] = (0,0,0,0)

    def set_contenu(self,contenu:Optional[Affichable]):
        """Change le contenu du conteneur."""
        self.contenu = contenu

    def set_fond(self,fond:Tuple[int,int,int,int]|Tuple[int,int,int]):
        """Change le fond du conteneur."""
        self.fond = fond

    def decale(self,decalage:Tuple[int,int]):
        self.position = (self.position[0] + decalage[0],self.position[1] + decalage[1])
        for objet in self.objets:
            objet.decale(decalage)

    def set_tailles(self,tailles:Tuple[int,int]):
        assert self.contenu is not None
        self.tailles = tailles
        self.contenu.set_tailles(tailles)

    def get_tailles(self,tailles:Tuple[int,int]):
        if self.contenu is None:
            warn(f"{self} n'a pas de contenu !")
            return (0,0)
        return self.contenu.get_tailles(tailles)

    def affiche(self,screen:pygame.Surface,frame:int=1,frame_par_tour:int=1):
        assert self.contenu is not None
        surf = pygame.Surface(self.tailles,transparency_flag)
        surf.fill(self.fond)
        self.contenu.affiche(surf,frame,frame_par_tour)
        screen.blit(surf,self.position)
        for objet in self.objets:
            objet.affiche(screen,frame,frame_par_tour)

    def clique(self,position:Tuple[int,int],droit:bool=False) -> Cliquable|Literal[False]:
        res = False
        if self.touche(position):
            if isinstance(self,Cliquable):
                res = self
            if self.contenu:
                pos_rel = (position[0]-self.position[0],position[1]-self.position[1])
                res_contenu = self.contenu.clique(pos_rel,droit)
                if res_contenu:
                    res = res_contenu
        for objet in self.objets:
            res_objet = objet.clique(position,droit)
            if res_objet:
                res = res_objet
        return res

    def clique_placeholder(self,placeheldholder:Placeheldholder,_droit:bool=False):
        res = False
        if self.contenu:
            res_contenu = self.contenu.clique_placeholder(placeheldholder,_droit)
            if res_contenu:
                res = res_contenu
        for objet in self.objets:
            res_objet = objet.clique_placeholder(placeheldholder,_droit)
            if res_objet:
                res = res_objet
        return res

    def survol(self,position:Tuple[int,int]) -> Survolable|Literal[False]:
        res = False
        if self.touche(position):
            if isinstance(self,Survolable):
                res = self
            if self.contenu:
                pos_rel = (position[0]-self.position[0],position[1]-self.position[1])
                res_contenu = self.contenu.survol(pos_rel)
                if res_contenu:
                    res = res_contenu
        for objet in self.objets:
            res_objet = objet.survol(position)
            if res_objet:
                res = res_objet
        return res

    def scroll(self,position:Tuple[int,int],x:int,y:int):
        assert self.contenu is not None
        res = False
        if self.touche(position):
            pos_rel = (position[0]-self.position[0],position[1]-self.position[1])
            if self.contenu.scroll(pos_rel,x,y):
                res = True
        for objet in self.objets:
            if objet.scroll(position,x,y):
                res = True
        return res

    def update(self):
        assert self.contenu is not None
        self.contenu.update()
        for objet in self.objets:
            objet.update()
