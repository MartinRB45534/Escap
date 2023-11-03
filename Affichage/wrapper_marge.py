"""
Contient les classes Wrapper_noeud et Wrapper_noeud_bloque
"""

from __future__ import annotations
from typing import Tuple, Literal, TYPE_CHECKING
from warnings import warn
import pygame

from affichage.cliquable import Cliquable

from .wrapper import Wrapper

from ._ensure_pygame import transparency_flag

if TYPE_CHECKING:
    from .survolable import Survolable
    from .cliquable import Cliquable

class WrapperMarge(Wrapper):
    """Un wrapper qui a une petite marge"""
    def __init__(self, marges: Tuple[int, int, int, int] = (5, 5, 5, 5)):
        Wrapper.__init__(self)
        self.marges = marges

    def set_tailles(self, tailles: Tuple[int, int]):
        Wrapper.set_tailles(self, (tailles[0]-self.marges[0]-self.marges[2],tailles[1]-self.marges[1]-self.marges[3]))

    def get_tailles(self, tailles: Tuple[int, int]):
        tailles = Wrapper.get_tailles(self, tailles)
        return (tailles[0]+self.marges[0]+self.marges[2],tailles[1]+self.marges[1]+self.marges[3])

    def affiche(self, screen: pygame.Surface, frame: int = 1, frame_par_tour: int = 1):
        surf = pygame.Surface((self.tailles[0]-self.marges[0]-self.marges[2],self.tailles[1]-self.marges[1]-self.marges[3]), transparency_flag)
        Wrapper.affiche(self, surf, frame, frame_par_tour)
        screen.blit(surf, (self.position[0]+self.marges[0],self.position[1]+self.marges[1]))

    def clique(self, position: Tuple[int, int], droit: bool = False) -> Cliquable | Literal[False]:
        return Wrapper.clique(self, (position[0]-self.marges[0],position[1]-self.marges[1]), droit)

    def survol(self, position: Tuple[int, int]) -> Survolable | Literal[False]:
        return Wrapper.survol(self, (position[0]-self.marges[0],position[1]-self.marges[1]))

    def scroll(self, position: Tuple[int, int], x: int, y: int):
        return Wrapper.scroll(self, (position[0]-self.marges[0],position[1]-self.marges[1]), x, y)

class WrapperCentre(WrapperMarge):
    """Un wrapper qui centre son contenu"""
    def __init__(self):
        WrapperMarge.__init__(self, (0, 0, 0, 0))

    def set_tailles(self, tailles: Tuple[int, int]):
        self.get_tailles(tailles) # Pour calculer les marges
        WrapperMarge.set_tailles(self, tailles)

    def get_tailles(self, tailles: Tuple[int, int]):
        if self.contenu is None:
            warn(f"{self} n'a pas de contenu !")
            return (0,0)
        tailles_contenu = self.contenu.get_tailles(tailles)
        if tailles_contenu[0] > tailles[0]:
            tailles_contenu = (tailles[0],tailles_contenu[1])
        if tailles_contenu[1] > tailles[1]:
            tailles_contenu = (tailles_contenu[0],tailles[1])
        self.marges = ((tailles[0]-tailles_contenu[0])//2,(tailles[1]-tailles_contenu[1])//2,(tailles[0]-tailles_contenu[0])//2,(tailles[1]-tailles_contenu[1])//2)
        return WrapperMarge.get_tailles(self, tailles)

class WrapperCentreHorizontal(WrapperMarge):
    """Un wrapper qui centre son contenu horizontalement (avec une marge verticale)"""
    def __init__(self):
        WrapperMarge.__init__(self, (0, 5, 0, 5))

    def set_tailles(self, tailles: Tuple[int, int]):
        self.get_tailles(tailles)
        WrapperMarge.set_tailles(self, tailles)

    def get_tailles(self, tailles: Tuple[int, int]):
        if self.contenu is None:
            warn(f"{self} n'a pas de contenu !")
            return (0,0)
        tailles_contenu = self.contenu.get_tailles(tailles)
        if tailles_contenu[0] > tailles[0]:
            tailles_contenu = (tailles[0],tailles_contenu[1])
        self.marges = ((tailles[0]-tailles_contenu[0])//2,self.marges[1],(tailles[0]-tailles_contenu[0])//2,self.marges[3])
        return WrapperMarge.get_tailles(self, tailles)

class WrapperCentreVertical(WrapperMarge):
    """Un wrapper qui centre son contenu verticalement (avec une marge horizontale)"""
    def __init__(self):
        WrapperMarge.__init__(self, (5, 0, 5, 0))

    def set_tailles(self, tailles: Tuple[int, int]):
        self.get_tailles(tailles)
        WrapperMarge.set_tailles(self, tailles)

    def get_tailles(self, tailles: Tuple[int, int]):
        if self.contenu is None:
            warn(f"{self} n'a pas de contenu !")
            return (0,0)
        tailles_contenu = self.contenu.get_tailles(tailles)
        if tailles_contenu[1] > tailles[1]:
            tailles_contenu = (tailles_contenu[0],tailles[1])
        self.marges = (self.marges[0],(tailles[1]-tailles_contenu[1])//2,self.marges[2],(tailles[1]-tailles_contenu[1])//2)
        return WrapperMarge.get_tailles(self, tailles)
