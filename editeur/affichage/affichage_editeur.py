"""L'affichage principal de l'éditeur."""

from __future__ import annotations
from typing import Literal
import pygame

import affichage as af
from affichage.cliquable import Cliquable
import stockage as stck

# Imports utilisés dans le code
from .onglet_sur_categorie import OngletSurCategorie

class AffichageEditeur(af.Onglets):
    """L'affichage principal de l'éditeur."""
    def __init__(self):
        af.Onglets.__init__(self,af.DirectionAff.LEFT)
        stck.StockageGlobal()
        self.set_onglets([
            OngletSurCategorie(stck.Stockage.global_),
        ])
        assert isinstance(self.contenu, af.WrapperMarge)
        self.contenu.marges = (5, 5, 5, 5)

    def bouge_souris(self, event:pygame.event.Event):
        """Traite les évènements liés à la souris."""
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            #On a cliqué sur quelque chose. Vérifions quoi :
            af.TexteInput.current_input = None
            # On a cliqué, on n'est plus en train de saisir du texte
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
            if (event.pos[0] >= 0 and
                event.pos[0] <= self.tailles[0] and
                event.pos[1] >= 0 and
                event.pos[1] <= self.tailles[1]):
                self.survol(event.pos)

    def update(self):
        af.Onglets.update(self)
        self.set_tailles(self.tailles)

    def in_out(self) -> Cliquable | Literal[False]:
        return False # Ceci devrait être l'élément parent de toute la hiérarchie
