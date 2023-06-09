from __future__ import annotations
from typing import List, Optional, Tuple, TYPE_CHECKING
from warnings import warn
import pygame

if TYPE_CHECKING:
    from Placeholder import Placeheldholder

from .Affichable import Affichable
from .Conteneur import Conteneur

class Wrapper(Conteneur):
    """Un conteneur avec un unique élément"""
    def __init__(self):
        self.objets:List[Affichable] = [] #Il peut quand même avoir des objets 'normaux'
        self.contenu:Optional[Affichable] = None #L'objet qu'il 'contient'
        self.fond = (0,0,0,0)
        self.tailles = (0,0) #La largeur et la hauteur (ou l'inverse ?)
        self.position = (0,0)
    
    def set_contenu(self,contenu:Optional[Affichable]):
        self.contenu = contenu

    def set_fond(self,fond:Tuple[int,int,int,int]|Tuple[int,int,int]):
        self.fond = fond

    def decale(self,decalage:Tuple[int,int]):
        self.position = [self.position[0] + decalage[0],self.position[1] + decalage[1]]
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
        surf = pygame.Surface(self.tailles,pygame.SRCALPHA)
        surf.fill(self.fond)
        self.contenu.affiche(surf,frame,frame_par_tour)
        screen.blit(surf,self.position)
        for objet in self.objets:
            objet.affiche(screen,frame,frame_par_tour)

    def clique(self,position:List[int],droit:bool=False):
        assert self.contenu is not None
        #Trouve l'élément survolé par la souris et le renvoie
        res = False
        if self.touche(position):
            res = self #La plupart des trucs qu'on veut pouvoir cliquer sont les Wrapper, pas les listes et pavages intermédiaires
            pos_rel = [position[0]-self.position[0],position[1]-self.position[1]]
            res_contenu = self.contenu.clique(pos_rel,droit)
            if res_contenu:
                res = res_contenu
        for objet in self.objets:
            res_objet = objet.clique(position,droit)
            if res_objet:
                res = res_objet
        return res
    
    def clique_placeholder(self,placeheldholder:Placeheldholder,droit:bool=False):
        assert self.contenu is not None
        res = False
        res_contenu = self.contenu.clique_placeholder(placeheldholder,droit)
        if res_contenu:
            res = res_contenu
        for objet in self.objets:
            res_objet = objet.clique_placeholder(placeheldholder,droit)
            if res_objet:
                res = res_objet
        return res

    def survol(self,position):
        assert self.contenu is not None
        #Trouve l'élément survolé par la souris et le renvoie
        res = False
        if self.touche(position):
            res = self
            pos_rel = [position[0]-self.position[0],position[1]-self.position[1]]
            res_contenu = self.contenu.survol(pos_rel)
            if res_contenu:
                res = res_contenu
        for objet in self.objets:
            res_objet = objet.survol(position)
            if res_objet:
                res = res_objet
        return res

    def scroll(self,position,x,y):
        assert self.contenu is not None
        res = False
        if self.touche(position):
            pos_rel = [position[0]-self.position[0],position[1]-self.position[1]]
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
