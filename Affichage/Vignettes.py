from __future__ import annotations
from typing import List, Optional
import pygame

from .Affichable import Affichable
from .Parent import Parent
from .Cliquable import Cliquable
from .Noeud import Noeud
from .Placeholder import Placeholder, Placeheldholder
from .Texte import Texte
from .Vignette import Vignette

class Vignette_composee(Cliquable,Parent):
    def __init__(self,vignettes:List[Affichable],taille,shade=False,invalide=False):
        Cliquable.__init__(self)
        self.tailles = [taille,taille]
        self.objets = vignettes
        if shade or invalide:
            self.objets.append(Vignette((0,0),taille,SKIN_SHADE))
        if invalide:
            self.objets.append(Vignette((0,0),taille,SKIN_SHADE))

class Vignette_placeholder(Vignette_composee, Placeholder):
    def __init__(self,placeheldholder:Placeheldholder,placeheld:Optional[Cliquable],placeheldholder_ajuster:Optional[Affichable],vignettes:List[Affichable],taille,shade=False,invalide=False):
        Placeholder.__init__(self,placeheldholder,placeheld,placeheldholder_ajuster)
        self.tailles = [taille,taille]
        self.objets = vignettes
        if shade or invalide:
            self.objets.append(Vignette((0,0),taille,SKIN_SHADE))
        if invalide:
            self.objets.append(Vignette((0,0),taille,SKIN_SHADE))

    def affiche(self, screen: pygame.Surface, frame: int = 1, frame_par_tour: int = 1):
        if self.marque_actif or self.marque_courant or self.marque_survol:
            self.decale((2,2)) # /!\ Trouver un meilleur moyen de marquer l'activité
        super().affiche(screen, frame, frame_par_tour)
        if self.marque_actif or self.marque_courant or self.marque_survol:
            self.decale((-2,-2))
            self.marque_actif = False
            self.marque_courant = False
            self.marque_survol = False

class Vignette_composee_texte(Vignette_composee):
    def __init__(self,vignettes:List[Affichable],texte,taille,shade=False,invalide=False):
        Vignette_composee.__init__(self,vignettes,taille,shade,invalide)
        texte = Texte(texte)
        self.objets.append(texte)
        tailles_texte = texte.get_tailles(self.tailles)
        texte.set_position([self.tailles[0]-tailles_texte[0],self.tailles[1]-tailles_texte[1]])

    def set_tailles(self, tailles):
        Vignette_composee.set_tailles(self,tailles)
        for objet in self.objets:
            if isinstance(objet,Texte):
                tailles_texte = objet.get_tailles(self.tailles)
                objet.set_position([self.tailles[0]-tailles_texte[0],self.tailles[1]-tailles_texte[1]])

class Vignette_placeholder_texte(Vignette_composee_texte,Vignette_placeholder):
    def __init__(self,placeheldholder:Placeheldholder,placeheld:Optional[Cliquable],placeheldholder_ajuster:Optional[Parent],vignettes:List[Affichable],texte,taille,shade=False,invalide=False):
        Vignette_placeholder.__init__(self,placeheldholder,placeheld,placeheldholder_ajuster,vignettes,taille,shade,invalide)
        texte = Texte(texte)
        self.objets.append(texte)
        tailles_texte = texte.get_tailles(self.tailles)
        texte.set_position([self.tailles[0]-tailles_texte[0],self.tailles[1]-tailles_texte[1]])

class Vignette_placeholder_updatable(Vignette_placeholder):
    def __init__(self,placeheldholder:Placeheldholder,placeheld:Noeud,placeheldholder_ajuster:Affichable,vignettes:List[Affichable],taille,shade=False,invalide=False):
        Vignette_placeholder.__init__(self,placeheldholder,placeheld,placeheldholder_ajuster,vignettes,taille,shade,invalide)

        self.shades:List[Affichable] = []
        if shade or invalide:
            self.objets.append(Vignette((0,0),taille,SKIN_SHADE))
            self.shades.append(Vignette((0,0),taille,SKIN_SHADE))
        if invalide:
            self.objets.append(Vignette((0,0),taille,SKIN_SHADE))
            self.shades.append(Vignette((0,0),taille,SKIN_SHADE))

from .Skins import SKIN_SHADE