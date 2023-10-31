"""L'affichage principal de l'éditeur."""

from __future__ import annotations
import pygame

import affichage as af
from affichage.cliquable import Cliquable

from .onglet import Onglet

class AffichageEditeur(af.WrapperNoeud,af.NoeudHorizontalProfondeurAgnostique,af.NoeudVerticalProfondeurAgnostique):
    """L'affichage principal de l'éditeur."""
    def __init__(self):
        af.WrapperNoeud.__init__(self)
        af.NoeudHorizontalProfondeurAgnostique.__init__(self)
        af.NoeudVerticalProfondeurAgnostique.__init__(self)
        self.contenu = af.PavageVertical()
        diptique = af.PavageHorizontal()
        liste_onglets = af.ListeVerticale()
        self.onglet = af.Wrapper()
        self.onglet1 = Onglet(af.NumberInput())
        self.onglet2 = Onglet(af.IntInput())
        self.onglet3 = Onglet(af.TexteInput())
        self.bouton1 = af.Bouton(af.SKIN_SHADE,"Number Input")
        self.bouton2 = af.Bouton(af.SKIN_SHADE,"Int Input")
        self.bouton3 = af.Bouton(af.SKIN_SHADE,"Text Input")

        self.onglet.set_contenu(af.CenterTexte("L'onglet s'affichera ici"))
        liste_onglets.set_contenu([af.MargeHorizontale(),self.bouton1,af.MargeHorizontale(),self.bouton2,af.MargeHorizontale(),self.bouton3,af.MargeHorizontale()],[5,0,5,0,5,0,5])
        diptique.set_contenu([af.MargeVerticale(),liste_onglets,af.MargeVerticale(),self.onglet,af.MargeVerticale()],[5,0,5,-1,5])
        self.contenu.set_contenu([af.MargeHorizontale(),diptique,af.MargeHorizontale()],[5,-1,5])

        self.fond = (255,255,255)
        self.actif = True
        self.set_courant(self.bouton1)

    def select(self, selection: Cliquable, droit: bool = False):
        """Sélectionne l'élément (fait plus de choses dans certaines classes filles)."""
        if not droit:
            if selection == self.bouton1:
                self.onglet.set_contenu(self.onglet1)
                self.courant = self.onglet1
            elif selection == self.bouton2:
                self.onglet.set_contenu(self.onglet2)
                self.courant = self.onglet2
            elif selection == self.bouton3:
                self.onglet.set_contenu(self.onglet3)
                self.courant = self.onglet3
        self.onglet.set_tailles(self.onglet.tailles)

    def in_up(self):
        match self.courant:
            case self.bouton2:
                self.set_courant(self.bouton1)
            case self.bouton3:
                self.set_courant(self.bouton2)
            case _:
                pass

    def in_down(self):
        match self.courant:
            case self.bouton1:
                self.set_courant(self.bouton2)
            case self.bouton2:
                self.set_courant(self.bouton3)
            case _:
                pass

    def in_left(self):
        match self.courant:
            case self.onglet1:
                self.set_courant(self.bouton1)
            case self.onglet2:
                self.set_courant(self.bouton2)
            case self.onglet3:
                self.set_courant(self.bouton3)
            case _:
                pass

    def in_right(self):
        match self.courant:
            case self.bouton1:
                self.select(self.bouton1)
            case self.bouton2:
                self.select(self.bouton2)
            case self.bouton3:
                self.select(self.bouton3)
            case _:
                pass

    def bouge_souris(self, event:pygame.event.Event):
        """Traite les évènements liés à la souris."""
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: #On a cliqué sur quelque chose. Vérifions quoi :
            af.TexteInput.current_input = None # On a cliqué, on n'est plus en train de saisir du texte
            pygame.key.set_repeat() # On n'est plus en train de saisir du texte
            if not self.clique(event.pos):
                # Now that's weird...
                print("Clic sur rien")
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3: #On a cliqué droit
            af.TexteInput.current_input = None
            pygame.key.set_repeat()
            if not self.clique(event.pos, True):
                # Now that's weird...
                print("Clic droit sur rien")
        elif event.type == pygame.MOUSEWHEEL: #On a scrollé
            self.scroll(pygame.mouse.get_pos(), 10*event.x, 10*event.y)
        elif event.type == pygame.MOUSEMOTION: #On a bougé la souris
            # On vérifie que la souris est dans la fenêtre
            if event.pos[0] >= 0 and event.pos[0] <= self.tailles[0] and event.pos[1] >= 0 and event.pos[1] <= self.tailles[1]:
                # print("survol")
                self.survol(event.pos)
