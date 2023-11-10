"""Contient la classe MenuDeroulant, qui est un menu déroulant"""

from __future__ import annotations
from typing import List, Tuple

import pygame

# Imports des classes parentes
from .liste import ListeMargeVerticale
from .placeholder import Placeheldholder, Placeholder
from .texte import Texte

class MenuDeroulant(Placeheldholder):
    """Un menu déroulant"""
    def __init__(self):
        Placeheldholder.__init__(self)
        self.liste = ListeMargeVerticale(2)
        self.objets.append(self.liste)

    def get_tailles(self, tailles: Tuple[int, int]):
        assert self.contenu is not None
        tailles_contenu = self.contenu.get_tailles(tailles)
        tailles_liste = self.liste.get_tailles(tailles)
        return (max(tailles_contenu[0], tailles_liste[0]), tailles_contenu[1])

    def set_tailles(self, tailles: Tuple[int, int]):
        assert self.contenu is not None
        self.contenu.set_tailles(tailles)
        self.liste.set_tailles((tailles[0], self.liste.get_tailles(tailles)[1]))
        Placeheldholder.set_tailles(self, tailles)

    def set_contenu_liste(self,contenu:List[TexteMenuDeroulant]):
        """Change le contenu du menu déroulant."""
        self.liste.set_contenu(contenu)

    def affiche(self, screen: pygame.Surface, frame: int = 1, frame_par_tour: int = 1):
        """Place le menu déroulant et l'affiche."""
        self.liste.set_position((self.position[0], self.position[1] + self.tailles[1]))
        self.liste.set_tailles((self.tailles[0], screen.get_height() - self.position[1] - self.tailles[1] - 2))
        super().affiche(screen, frame, frame_par_tour)

class TexteMenuDeroulant(Placeholder, Texte):
    """Un item d'un menu déroulant"""
    def __init__(self, menu_deroulant: MenuDeroulant, texte: str):
        Placeholder.__init__(self, menu_deroulant, Texte(texte))
        Texte.__init__(self, texte)
