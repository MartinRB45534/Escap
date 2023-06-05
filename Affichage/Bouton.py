from __future__ import annotations
from typing import List
import pygame

from .Wrapper_cliquable import Wrapper_cliquable
from .Pavage import Pavage_vertical, Pavage_horizontal
from .Marge import Marge_verticale, Marge_horizontale
from .Texte import Texte
from .Vignette import Vignette

class Bouton(Wrapper_cliquable):
    def __init__(self, skin, texte, fond=(255,255,255), fond_marque_survol=(200,200,200), fond_marque_actif=None, fond_marque_courant=None, fond_est_courant=None, fond_actif=None):
        Wrapper_cliquable.__init__(self)

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
        contenu = Pavage_vertical()
        triptique = Pavage_horizontal()
        triptique.set_contenu([Marge_verticale(),Vignette((0,0),20,self.skin),Marge_verticale(),Texte(self.texte),Marge_verticale()],[5,0,5,0,5])
        contenu.set_contenu([Marge_horizontale(),triptique,Marge_horizontale()],[5,0,5])
        self.set_contenu(contenu)

    def get_fond(self):
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
        surf = pygame.Surface(self.tailles,pygame.SRCALPHA)
        surf.fill(self.get_fond())
        self.contenu.affiche(surf,frame,frame_par_tour)
        screen.blit(surf,self.position)
        for objet in self.objets:
            objet.affiche(screen,frame,frame_par_tour)
