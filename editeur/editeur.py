"""L'éditeur du jeu."""

from __future__ import annotations
from typing import Optional

import pygame

import affichage as af
import commons as cm

from .affichage import AffichageEditeur

class Editeur:
    """L'éditeur du jeu."""
    def __init__(self):
        self.loop=False
        self.affichage = AffichageEditeur()

    def run(self,screen:pygame.Surface):
        """Fait tourner l'éditeur."""
        self.loop=True
        self.affichage.set_tailles(screen.get_size())
        self.affichage.set_actif()
        while self.loop:
            self.input()
            self.affichage.trouve_actif()
            self.affichage.update()
            self.affichage.affiche(screen)
            pygame.display.flip()
            self.patiente()

    def input(self):
        """Traite les inputs."""
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.quitte()
            elif event.type == pygame.VIDEORESIZE:
                self.affichage.set_tailles(event.size)
            elif event.type in [pygame.MOUSEBUTTONDOWN,pygame.MOUSEBUTTONUP,
                                pygame.MOUSEWHEEL,pygame.MOUSEMOTION]:
                self.affichage.bouge_souris(event)
            elif event.type in [pygame.KEYDOWN,pygame.KEYUP]:
                self.controle_clavier(event,cm.get_modifiers(event.mod))
        if af.TexteInput.current_input is not None:
            af.TexteInput.event(events) # type: ignore # Type partially unknown
        # On resurvole pour conserver le survol des boutons
        if pygame.mouse.get_focused():
            self.affichage.survol(pygame.mouse.get_pos())

    def quitte(self):
        """Quitte l'éditeur."""
        self.loop=False

    def patiente(self):
        """Fait patienter l'éditeur."""
        pygame.time.wait(50)

    def get_direction(self, event:pygame.event.Event) -> Optional[af.DirectionAff]:
        """Renvoie la direction correspondant à une touche du clavier."""
        match event.scancode: # Le scancode est le code de la touche,
                              # indépendant de la disposition du clavier
            case pygame.KSCAN_UP:
                return af.DirectionAff.UP
            case pygame.KSCAN_W:
                if not af.TexteInput.current_input:
                    return af.DirectionAff.UP
            case pygame.KSCAN_DOWN:
                return af.DirectionAff.DOWN
            case pygame.KSCAN_S:
                if not af.TexteInput.current_input:
                    return af.DirectionAff.DOWN
            case pygame.KSCAN_LEFT:
                return af.DirectionAff.LEFT
            case pygame.KSCAN_A:
                if not af.TexteInput.current_input:
                    return af.DirectionAff.LEFT
            case pygame.KSCAN_RIGHT:
                return af.DirectionAff.RIGHT
            case pygame.KSCAN_D:
                if not af.TexteInput.current_input:
                    return af.DirectionAff.RIGHT
            case pygame.KSCAN_RETURN:
                return af.DirectionAff.IN
            case pygame.KSCAN_BACKSPACE:
                return af.DirectionAff.OUT
            case pygame.KSCAN_TAB:
                return af.DirectionAff.NEXT
            case _:
                pass

    def controle_clavier(self,event:pygame.event.Event,modifiers:set[int]):
        """Contrôle l'affichage à partir d'un évènement clavier."""
        direction = self.get_direction(event)
        if direction is None:
            return
        if pygame.KMOD_LSHIFT in modifiers or pygame.KMOD_RSHIFT in modifiers:
            direction = direction.oppose
        if af.TexteInput.current_input is not None:
            if direction is af.DirectionAff.IN: # Return is used to validate the input
                direction = af.DirectionAff.VALIDATE
            elif direction in [af.DirectionAff.UP,af.DirectionAff.DOWN,
                               af.DirectionAff.NEXT,af.DirectionAff.PREVIOUS]:
                pass # Let those keys navigate as usual
            else:
                return
        if event.type == pygame.KEYDOWN:
            self.affichage.navigue(direction)
