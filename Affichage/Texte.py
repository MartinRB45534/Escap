from __future__ import annotations
from typing import List, Optional
import pygame

from .Cliquable import Cliquable
from .Affichable import Taille_variable
from .Wrapper_noeud import Wrapper_noeud, Wrapper_noeud_bloque
from .Pavage import Pavage_horizontal, Pavage_vertical
from .Marge import Marge_horizontale, Marge_verticale

from .Polices import *

class Texte(Cliquable):
    """Un élément qui est juste un bout de texte."""
    def __init__(self,texte:str, texte_marque_survol:Optional[str]=None, texte_marque_actif:Optional[str]=None, texte_marque_courant:Optional[str]=None, texte_est_courant:Optional[str]=None, texte_actif:Optional[str]=None):
        Cliquable.__init__(self)
        # Élément le plus important : le texte "normal"
        self.texte=texte
        # Second élément le plus important : le texte survolé (pour montrer au joueur qu'il peut cliquer dessus et que c'est interactif, que le jeu a pas planté, etc.)
        self.texte_marque_survol=texte_marque_survol if texte_marque_survol else self.texte
        # Troisième élément le plus important : le texte actif (pour montrer au joueur que c'est le texte qui est actuellement sélectionné)
        self.texte_marque_actif=texte_marque_actif if texte_marque_actif else self.texte_marque_survol
        # Élément aussi non-négligeable : le texte courant (pour montrer au joueur que c'est le texte qui est actuellement presque sélectionné, mais pas encore)
        self.texte_marque_courant=texte_marque_courant if texte_marque_courant else self.texte_marque_actif
        # Élément moins important : le texte courant (pour montrer au joueur que s'il revient dans le dialogue, c'est le texte qui sera sélectionné)
        self.texte_est_courant=texte_est_courant if texte_est_courant else self.texte
        # Élément pas très important non plus : le texte actif (pour montrer au joueur que s'il revient dans le dialogue, le texte sera actif)
        self.texte_actif=texte_actif if texte_actif else self.texte_est_courant
    
    def get_texte(self,reset=False) -> str:
        if self.marque_survol:
            if reset:
                self.marque_survol = False
            return self.texte_marque_survol
        elif self.marque_actif:
            if reset:
                self.marque_actif = False
            return self.texte_marque_actif
        elif self.marque_courant:
            if reset:
                self.marque_courant = False
            return self.texte_marque_courant
        elif self.est_courant:
            if reset:
                self.est_courant = False
            return self.texte_est_courant
        elif self.actif:
            return self.texte_actif
        else:
            return self.texte

    def affiche(self,screen:pygame.Surface,frame:int=1,frame_par_tour:int=1):
        texte=POLICE20.render(self.get_texte(True),True,(0,0,0))
        screen.blit(texte,self.position)

    def get_tailles(self,tailles):
        return [POLICE20.size(self.get_texte())[0],20]

class Pave(Taille_variable,Texte):
    """Un élément avec beaucoup de texte. S'adapte sur plusieurs lignes si besoin"""

    def get_tailles(self,tailles):
        mots = self.get_texte().split() # Peut-être voir à couper mieux un jour (espaces insécables, etc.)
        i = 0
        hauteur = 0
        while i < len(mots):
            ligne = mots[i]
            i+=1
            while i < len(mots) and POLICE20.size(ligne+" "+mots[i])[0] <= tailles[0]:
                ligne = ligne + " " + mots[i]
                i+=1
            hauteur += 1
        return [tailles[0],20*hauteur]

    def set_tailles(self,tailles):
        mots = self.get_texte().split()
        i = 0
        hauteur = 0
        while i < len(mots):
            ligne = mots[i]
            i+=1
            hauteur += 1
            while i < len(mots) and POLICE20.size(ligne+" "+mots[i])[0] <= tailles[0]:
                ligne = ligne + " " + mots[i]
                i+=1
        self.tailles = [tailles[0],20*hauteur]

    def affiche(self,screen:pygame.Surface,frame:int,frame_par_tour:int):
        """Fonction qui prend en entrée une chaine de caractère et renvoie les surfaces des lignes successives du texte."""
        hauteur = 0
        mots = self.get_texte(True).split()
        i = 0
        while i < len(mots):
            ligne = mots[i]
            i+=1
            while i < len(mots) and POLICE20.size(ligne+" "+mots[i])[0] <= self.tailles[0]:
                ligne = ligne + " " + mots[i]
                i+=1
            screen.blit(POLICE20.render(ligne,True,(0,0,0)),[self.position[0],self.position[1]+hauteur*20])
            hauteur += 1

class Paves(Pave):
    """Un pavé avec plusieurs lignes"""
    def __init__(self, textes:List[str], textes_marques_survol:Optional[List[str]]=None, textes_marques_actifs:Optional[List[str]]=None, textes_marque_courant:Optional[List[str]]=None, textes_est_courant:Optional[List[str]]=None, textes_actifs:Optional[List[str]]=None):
        Cliquable.__init__(self)
        self.textes=textes
        self.textes_marques_survol=textes_marques_survol if textes_marques_survol else self.textes
        self.textes_marques_actifs=textes_marques_actifs if textes_marques_actifs else self.textes_marques_survol
        self.textes_marque_courant=textes_marque_courant if textes_marque_courant else self.textes_marques_actifs
        self.textes_est_courant=textes_est_courant if textes_est_courant else self.textes
        self.textes_actifs=textes_actifs if textes_actifs else self.textes_est_courant

    def get_textes(self,reset=False) -> List[str]:
        if self.marque_survol:
            if reset:
                self.marque_survol = False
            return self.textes_marques_survol
        elif self.marque_actif:
            if reset:
                self.marque_actif = False
            return self.textes_marques_actifs
        elif self.marque_courant:
            if reset:
                self.marque_courant = False
            return self.textes_marque_courant
        elif self.est_courant:
            if reset:
                self.est_courant = False
            return self.textes_est_courant
        elif self.actif:
            return self.textes_actifs
        else:
            return self.textes

    def get_tailles(self,tailles):
        hauteur = 0
        textes = self.get_textes()
        for texte in textes:
            mots = texte.split() #On explose sur les espaces
            i = 0
            while i < len(mots):
                ligne = mots[i]
                i+=1
                while i < len(mots) and POLICE20.size(ligne+" "+mots[i])[0] <= tailles[0]:
                    ligne = ligne + " " + mots[i]
                    i+=1
                hauteur += 1
        return [tailles[0],20*hauteur]

    def set_tailles(self,tailles):
        hauteur = 0
        textes = self.get_textes()
        for texte in textes:
            mots = texte.split() #On explose sur les espaces
            i = 0
            hauteur = 0
            while i < len(mots):
                ligne = mots[i]
                i+=1
                while i < len(mots) and POLICE20.size(ligne+" "+mots[i])[0] <= tailles[0]:
                    ligne = ligne + " " + mots[i]
                    i+=1
                hauteur += 1
        self.tailles = [tailles[0],20*hauteur]

    def affiche(self,screen:pygame.Surface,frame:int,frame_par_tour:int):
        hauteur = 0
        textes = self.get_textes()
        for texte in textes:
            mots = texte.split() #On explose sur les espaces
            i = 0
            while i < len(mots):
                ligne = mots[i]
                i+=1
                while i < len(mots) and POLICE20.size(ligne+" "+mots[i])[0] <= self.tailles[0]:
                    ligne = ligne + " " + mots[i]
                    i+=1
                screen.blit(POLICE20.render(ligne,True,(0,0,0)),[self.position[0],self.position[1]+hauteur*20])
                hauteur += 1

class Center_texte(Wrapper_noeud_bloque):
    def __init__(self, texte:str):

        Wrapper_noeud.__init__(self)
        self.texte = Texte(texte)
        self.set_courant(self.texte)
        self.init()

    def init(self):
        contenu = Pavage_vertical()
        monotique = Pavage_horizontal()
        monotique.set_contenu([Marge_verticale(), self.texte, Marge_verticale()], [-1, 0, -1])
        contenu.set_contenu([Marge_horizontale(), monotique, Marge_horizontale()], [-1, 0, -1])
        self.set_contenu(contenu)

class Margin_texte(Wrapper_noeud_bloque):
    def __init__(self, texte:str):
        Wrapper_noeud.__init__(self)

        self.texte = Texte(texte)
        self.set_courant(self.texte)
        self.init()

    def init(self):
        contenu = Pavage_vertical()
        monotique = Pavage_horizontal()
        monotique.set_contenu([Marge_verticale(), self.texte, Marge_verticale()], [5, 0, 5])
        contenu.set_contenu([Marge_horizontale(), monotique, Marge_horizontale()], [5, 0, 5])
        self.set_contenu(contenu)

class Center_horizontal_texte(Center_texte, Margin_texte):
    def init(self):
        contenu = Pavage_vertical()
        monotique = Pavage_horizontal()
        monotique.set_contenu([Marge_verticale(), self.texte, Marge_verticale()], [-1, 0, -1])
        contenu.set_contenu([Marge_horizontale(), monotique, Marge_horizontale()], [5, 0, 5])
        self.set_contenu(contenu)

class Center_vertical_texte(Center_texte, Margin_texte):
    def init(self):
        contenu = Pavage_vertical()
        monotique = Pavage_horizontal()
        monotique.set_contenu([Marge_verticale(), self.texte, Marge_verticale()], [5, 0, 5])
        contenu.set_contenu([Marge_horizontale(), monotique, Marge_horizontale()], [-1, 0, -1])
        self.set_contenu(contenu)
