"""L'affichage principal de l'éditeur."""

from __future__ import annotations
import pygame

import affichage as af
import stockage as stck

# Imports utilisés dans le code
from .especes import OngletEspeces
from .items import OngletItems

class AffichageEditeur(af.Onglets):
    """L'affichage principal de l'éditeur."""
    def __init__(self):
        af.Onglets.__init__(self,af.DirectionAff.LEFT)
        self.set_jeu(stck.StockageGlobal.global_)

    def set_jeu(self, stockage:stck.StockageGlobal):
        """Définit le jeu à afficher."""
        self.stockage = stockage
        self.set_onglets([
            OngletEspeces(self.stockage),
            # OngletEffets(self.jeu),
            OngletItems(self.stockage),
        ])

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
