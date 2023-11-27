"""
Ce module contient la classe Conteneur, qui est un élément qui peut en contenir d'autres.
"""

from __future__ import annotations
from typing import Literal, TYPE_CHECKING
import pygame

from .affichable import Affichable

from ._ensure_pygame import transparency_flag

if TYPE_CHECKING:
    from .placeholder import Placeheldholder
    from .cliquable import Cliquable
    from .survolable import Survolable

class Conteneur(Affichable):
    """Un élément qui peut en 'contenir' d'autres, c'est-à-dire qu'il va les afficher 'à l'interieur' et ils ne pourront pas déborder."""
    def __init__(self):
        self.objets:list[Affichable] = [] #Il peut quand même avoir des objets 'normaux'
        self.contenu:list[Affichable] = [] #Les objets qu'il 'contient'
        self.fond:tuple[int,int,int]|tuple[int,int,int,int] = (0,0,0,0)
        super().__init__()

    def set_contenu(self,contenu:list[Affichable]):
        """Change le contenu du conteneur."""
        self.contenu = contenu

    def set_fond(self,fond:tuple[int,int,int,int]):
        """Change le fond du conteneur."""
        self.fond = fond

    def decale(self,decalage:tuple[int,int]):
        """Décale l'élément et ses objets."""
        super().decale(decalage)
        for objet in self.objets:
            objet.decale(decalage)

    def affiche(self,screen:pygame.Surface,frame:int=1,frame_par_tour:int=1):
        surf = pygame.Surface(self.tailles, transparency_flag)
        surf.fill(self.fond)
        for contenu in self.contenu:
            contenu.affiche(surf,frame,frame_par_tour)
        screen.blit(surf,self.position)
        for objet in self.objets:
            objet.affiche(screen,frame,frame_par_tour)

    def clique(self,position:tuple[int,int],droit:bool=False) -> Cliquable|Literal[False]:
        #Trouve l'élément survolé par la souris et le renvoie
        res = False
        if self.touche(position):
            pos_rel = (position[0]-self.position[0],position[1]-self.position[1])
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

    def survol(self,position:tuple[int,int]) -> Survolable|Literal[False]:
        #Trouve l'élément survolé par la souris et le renvoie
        res = False
        if self.touche(position):
            pos_rel = (position[0]-self.position[0],position[1]-self.position[1])
            for contenu in self.contenu:
                res_contenu = contenu.survol(pos_rel)
                if res_contenu:
                    res = res_contenu
        for objet in self.objets:
            res_objet = objet.survol(position)
            if res_objet:
                res = res_objet
        return res

    def scroll(self,position:tuple[int,int],x:int,y:int):
        res = False
        if self.touche(position):
            pos_rel = (position[0]-self.position[0],position[1]-self.position[1])
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
