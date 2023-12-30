"""Contient la classe Bouton, qui est un bouton cliquable avec un texte et une vignette"""

from __future__ import annotations
from typing import Literal, Optional, Callable, TYPE_CHECKING
import pygame

from affichage.survolable import Survolable

from .wrapper import Wrapper
from .wrapper_cliquable import WrapperCliquable
from .wrapper_marge import WrapperMarge
from .pavage import PavageHorizontalMarge
from .placeholder import Placeholder
from .texte import Texte
from .vignette import Vignette
from .skins import Skin

from ._ensure_pygame import transparency_flag

if TYPE_CHECKING:
    from .cliquable import Cliquable
    from .placeholder import Placeheldholder

class Bouton(WrapperCliquable):
    """Un bouton cliquable avec un texte et une vignette"""
    def __init__(self, skin:Skin, texte:str, fond:tuple[int,int,int]=(255,255,255), fond_marque_survol:Optional[tuple[int,int,int]]=(228,35,19), fond_marque_actif:Optional[tuple[int,int,int]]=(51,153,0), fond_marque_courant:Optional[tuple[int,int,int]]=(255,192,0), fond_est_courant:Optional[tuple[int,int,int]]=(238,238,238), fond_actif:Optional[tuple[int,int,int]]=(238,238,238)):
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
        contenu = WrapperMarge()
        liste = PavageHorizontalMarge()
        liste.set_contenu([Vignette((0,0),20,self.skin),Texte(self.texte)])
        contenu.set_contenu(liste)
        self.set_contenu(contenu)

    def get_fond(self):
        """Renvoie le fond du bouton en fonction de son état"""
        if self.marque_survol:
            self.marque_survol = False
            return self.fond_marque_survol
        elif self.marque_actif:
            self.marque_actif = False
            return self.fond_marque_actif
        elif self.marque_courant:
            self.marque_courant = False
            return self.fond_marque_courant
        elif self.est_courant:
            self.est_courant = False
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
    
    def survol(self, position: tuple[int, int]) -> Survolable | Literal[False]:
        survol = WrapperCliquable.survol(self, position)
        if survol:
            self.marque_survol = True
        return survol

    def clique(self,position:tuple[int,int],droit:bool=False) -> Cliquable|Literal[False]:
        clique = Wrapper.clique(self,position,droit)
        if clique:
            self.set_actif()
            assert self.actif
            return self
        return False

class BoutonFonction(Bouton):
    """Un bouton qui appelle lui-même une fonction"""
    def __init__(self, skin:Skin, texte:str, fonction:Callable[[],None], fond:tuple[int,int,int]=(255,255,255), fond_marque_survol:tuple[int,int,int]=(200,200,200), fond_marque_actif:Optional[tuple[int,int,int]]=None, fond_marque_courant:Optional[tuple[int,int,int]]=None, fond_est_courant:Optional[tuple[int,int,int]]=None, fond_actif:Optional[tuple[int,int,int]]=None):
        Bouton.__init__(self, skin, texte, fond, fond_marque_survol, fond_marque_actif, fond_marque_courant, fond_est_courant, fond_actif)
        self.fonction = fonction

    def set_actif(self):
        if self.actif:
            self.fonction()
        else:
            Bouton.set_actif(self)

class BoutonPlaceholder(Placeholder, Bouton):
    """Un placeholder qui se présente comme un bouton"""
    def __init__(self, placeheldholder:Placeheldholder, placeheld:Optional[Cliquable], skin:Skin, texte:str, fond:tuple[int,int,int]=(255,255,255), fond_marque_survol:tuple[int,int,int]=(200,200,200), fond_marque_actif:Optional[tuple[int,int,int]]=None, fond_marque_courant:Optional[tuple[int,int,int]]=None, fond_est_courant:Optional[tuple[int,int,int]]=None, fond_actif:Optional[tuple[int,int,int]]=None):
        Placeholder.__init__(self, placeheldholder, placeheld)
        Bouton.__init__(self, skin, texte, fond, fond_marque_survol, fond_marque_actif, fond_marque_courant, fond_est_courant, fond_actif)

class BoutonOnOff(Bouton):
    """Un bouton qui a deux états, et qui change d'état à chaque clic"""
    def __init__(self, skin_on:Skin, skin_off:Skin, texte_on:str, texte_off:str, fond:tuple[int,int,int]=(255,255,255), fond_marque_survol:tuple[int,int,int]=(200,200,200), fond_marque_actif:Optional[tuple[int,int,int]]=None, fond_marque_courant:Optional[tuple[int,int,int]]=None, fond_est_courant:Optional[tuple[int,int,int]]=None, fond_actif:Optional[tuple[int,int,int]]=None):
        self.skin_on = skin_on
        self.skin_off = skin_off
        self.texte_on = texte_on
        self.texte_off = texte_off
        self.on = False
        self.accepte = True # Pour coller avec les inputs
        Bouton.__init__(self, skin_off, texte_off, fond, fond_marque_survol, fond_marque_actif, fond_marque_courant, fond_est_courant, fond_actif)

    def set_actif(self):
        if self.actif:
            self.on = not self.on
            if self.on:
                self.skin = self.skin_on
                self.texte = self.texte_on
            else:
                self.skin = self.skin_off
                self.texte = self.texte_off
            self.init()
        else:
            Bouton.set_actif(self)

    @property
    def valeur(self):
        """Renvoie la valeur du bouton, comme pour les inputs"""
        return str(self.on)

    @valeur.setter
    def valeur(self, valeur:str):
        """Change la valeur du bouton, comme pour les inputs"""
        self.on = valeur == "True"
        if self.on:
            self.skin = self.skin_on
            self.texte = self.texte_on
        else:
            self.skin = self.skin_off
            self.texte = self.texte_off
        self.init()

    def accepte_autre(self, valeur: str):
        """Renvoie si la valeur saisie est acceptée."""
        return valeur in ("True","False")
