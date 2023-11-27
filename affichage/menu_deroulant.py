"""Contient la classe MenuDeroulant, qui est un menu déroulant"""

from __future__ import annotations

import pygame

from affichage.affichable import Affichable

# Imports des classes parentes
from .cliquable import Cliquable
from .liste import ListeMargeVerticale
from .placeholder import Placeheldholder, Placeholder
from .texte import Texte
from .wrapper import Wrapper
from .wrapper_noeud import WrapperNoeud

class MenuDeroulant(Placeheldholder):
    """Un menu déroulant"""
    def __init__(self, contenu: Texte):
        Placeheldholder.__init__(self)
        self.liste = ListeMargeVerticale(2, True)
        self.liste.fond = (200, 200, 200)
        self.contenu = contenu
        self.courant = contenu

    def get_tailles(self, tailles: tuple[int, int]):
        assert self.contenu is not None
        tailles_contenu = self.contenu.get_tailles(tailles)
        tailles_liste = self.liste.get_tailles(tailles)
        return (max(tailles_contenu[0], tailles_liste[0]), tailles_contenu[1])

    def set_tailles(self, tailles: tuple[int, int]):
        assert self.contenu is not None
        self.tailles = tailles
        self.contenu.set_tailles(tailles)
        self.liste.set_tailles((tailles[0], self.liste.get_tailles(tailles)[1]))

    def set_contenu(self, contenu: Affichable):
        if isinstance(contenu, Texte):
            self.contenu = contenu
            self.courant = contenu
        else:
            raise TypeError("Le contenu d'un menu déroulant doit être un Texte")

    def set_contenu_liste(self,contenu:list[TexteMenuDeroulant]):
        """Change le contenu du menu déroulant."""
        self.liste.set_contenu(contenu)

    def clique(self, position: tuple[int, int], droit: bool = False):
        self.objets.append(self.liste)
        clique = Wrapper.clique(self, position, droit)
        self.objets.pop() # Ce serait bien de faire ça plus proprement
        if clique is self or clique is self.contenu:
            self.set_actif()
            return self
        return False

    def trouve_actif(self):
        Cliquable.trouve_actif(self)

    def set_actif(self):
        Cliquable.set_actif(self) # On n'utilise pas le set_actif de Placeheldholder

    def unset_actif(self):
        Cliquable.unset_actif(self) # Idem

    def in_in(self):
        return False

    def in_up(self):
        # On circule dans le menu déroulant
        courant = self.liste.contenu[self.liste.courant]
        assert isinstance(courant, TexteMenuDeroulant), """La liste du menu déroulant
ne devrait avoir que des TexteMenuDeroulant en courant"""
        if self.liste.courant > 1:
            self.liste.courant -= 2 # On saute la marge
        else:
            self.liste.courant = 0
        courant = self.liste.contenu[self.liste.courant]
        assert isinstance(courant, TexteMenuDeroulant), """La liste du menu déroulant
ne devrait avoir que des TexteMenuDeroulant en courant"""
        courant.set_actif()
        return self

    def in_down(self):
        # On circule dans le menu déroulant
        courant = self.liste.contenu[self.liste.courant]
        assert isinstance(courant, TexteMenuDeroulant), """La liste du menu déroulant
ne devrait avoir que des TexteMenuDeroulant en courant"""
        if self.liste.courant < len(self.liste.contenu) - 2:
            self.liste.courant += 2
        else:
            self.liste.courant = len(self.liste.contenu) - 1
        courant = self.liste.contenu[self.liste.courant]
        assert isinstance(courant, TexteMenuDeroulant), """La liste du menu déroulant
ne devrait avoir que des TexteMenuDeroulant en courant"""
        courant.set_actif()
        return self

    def affiche(self, screen: pygame.Surface, frame: int = 1, frame_par_tour: int = 1):
        """Place le menu déroulant et l'affiche."""
        self.liste.set_position((self.position[0], self.position[1] + self.tailles[1] + 2))
        tailles_liste = self.liste.get_tailles((self.tailles[0],
            screen.get_height()- self.position[1] - self.tailles[1] - 2))
        self.liste.set_tailles(tailles_liste)
        WrapperNoeud.affiche(self, screen, frame, frame_par_tour)

    def affiche_liste(self, screen: pygame.Surface, marge: tuple[int, int],
                      frame: int = 1, frame_par_tour: int = 1):
        """Affiche la liste du menu déroulant."""
        self.liste.position = (self.liste.position[0] + marge[0], self.liste.position[1] + marge[1])
        self.liste.affiche(screen, frame, frame_par_tour)

class TexteMenuDeroulant(Placeholder, Texte):
    """Un item d'un menu déroulant"""
    def __init__(self, menu_deroulant: MenuDeroulant, texte: str):
        Placeholder.__init__(self, menu_deroulant, Texte(texte))
        Texte.__init__(self, texte)
