from __future__ import annotations
from typing import List
import pygame

from Affichable import Affichable

class Parent(Affichable):
    """Un élément de l'affichage. Peut contenir des sous-éléments."""
    def __init__(self):
        self.tailles = (0,0) #La largeur et la hauteur (ou l'inverse ?)
        self.position = (0,0)
        self.objets:List[Affichable] = [] #La liste des objets à afficher

    def set_objets(self,objets:List[Affichable]):
        self.objets = objets

    def set_position(self,position):
        self.decale([position[0]-self.position[0],position[1]-self.position[1]])

    def decale(self,decalage):
        self.position = [self.position[0] + decalage[0],self.position[1] + decalage[1]]
        for objet in self.objets:
            objet.decale(decalage)

    def affiche(self,screen:pygame.Surface,frame:int=1,frame_par_tour:int=1):
        #Fait afficher ses objets
        for objet in self.objets:
            objet.affiche(screen,frame,frame_par_tour)

    def clique(self,position: List[int], droit: bool = False):
        #Trouve l'élément survolé par la souris et le renvoie
        res = False
        if self.touche(position):
            res = self
        for objet in self.objets:
            res_objet = objet.clique(position,droit)
            if res_objet:
                res = res_objet
        return res
    
    def clique_placeholder(self,placeheldholder,droit: bool = False):
        res = False
        for objet in self.objets:
            if objet.clique_placeholder(placeheldholder,droit):
                res = objet
        return res

    def survol(self,position):
        #Trouve l'élément survolé par la souris et le renvoie
        res = False
        if self.touche(position):
            res = self
        for objet in self.objets:
            res_objet = objet.survol(position)
            if res_objet:
                res = res_objet
        return res

    def scroll(self,position,x,y):
        res = False
        for objet in self.objets:
            if objet.scroll(position,x,y):
                res = True
        return res

    def update(self):
        for objet in self.objets:
            objet.update()
