from __future__ import annotations
from typing import List, TYPE_CHECKING
import pygame
if TYPE_CHECKING:
    from Placeholder import Placeheldholder

from .Affichable import Affichable

class Conteneur(Affichable):
    """Un élément qui peut en 'contenir' d'autres, c'est-à-dire qu'il va les afficher 'à l'interieur' et ils ne pourront pas déborder."""
    def __init__(self):
        self.objets:List[Affichable] = [] #Il peut quand même avoir des objets 'normaux'
        self.contenu:List[Affichable] = [] #Les objets qu'il 'contient'
        self.fond = (0,0,0,0)
        self.tailles = (0,0) #La largeur et la hauteur (ou l'inverse ?)
        self.position = (0,0)
    
    def set_contenu(self,contenu):
        self.contenu = contenu

    def set_fond(self,fond):
        self.fond = fond

    def decale(self,decalage):
        self.position = [self.position[0] + decalage[0],self.position[1] + decalage[1]]
        for objet in self.objets:
            objet.decale(decalage)
    
    def affiche(self,screen:pygame.Surface,frame:int=1,frame_par_tour:int=1):
        surf = pygame.Surface(self.tailles,pygame.SRCALPHA)
        surf.fill(self.fond)
        for contenu in self.contenu:
            contenu.affiche(surf,frame,frame_par_tour)
        screen.blit(surf,self.position)
        for objet in self.objets:
            objet.affiche(screen,frame,frame_par_tour)

    def clique(self,position:List[int],droit:bool=False):
        #Trouve l'élément survolé par la souris et le renvoie
        res = False
        if self.touche(position):
            pos_rel = [position[0]-self.position[0],position[1]-self.position[1]]
            for contenu in self.contenu:
                res_contenu = contenu.clique(pos_rel,droit)
                if res_contenu:
                    res = res_contenu
        for objet in self.objets:
            res_objet = objet.clique(position,droit)
            if res_objet:
                res = res_objet
        return res

    def clique_placeholder(self,placeheldholder:Placeheldholder,droit:bool=False):
        res = False
        for contenu in self.contenu:
            res_contenu = contenu.clique_placeholder(placeheldholder,droit)
            if res_contenu:
                res = res_contenu
        for objet in self.objets:
            res_objet = objet.clique_placeholder(placeheldholder,droit)
            if res_objet:
                res = res_objet
        return res

    def survol(self,position):
        #Trouve l'élément survolé par la souris et le renvoie
        res = False
        if self.touche(position):
            pos_rel = [position[0]-self.position[0],position[1]-self.position[1]]
            for contenu in self.contenu:
                res_contenu = contenu.survol(pos_rel)
                if res_contenu:
                    res = res_contenu
        for objet in self.objets:
            res_objet = objet.survol(position)
            if res_objet:
                res = res_objet
        return res

    def scroll(self,position,x,y):
        res = False
        if self.touche(position):
            pos_rel = [position[0]-self.position[0],position[1]-self.position[1]]
            for contenu in self.contenu:
                if contenu.scroll(pos_rel,x,y):
                    res = True
        for objet in self.objets:
            if objet.scroll(position,x,y):
                res = True
        return res

    def update(self):
        for contenu in self.contenu:
            contenu.update()
        for objet in self.objets:
            objet.update()
