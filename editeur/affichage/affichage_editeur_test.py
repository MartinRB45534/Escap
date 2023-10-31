"""
L'affichage principal de l'éditeur,
réalisé avec des boutons et des placeholders.

N'est plus censé être utilisé.
"""

raise ImportError("Ce fichier n'est plus utilisé. Voir affichage_editeur_test.py")

# Ignore pylint errors in this file
# pylint: disable=misplaced-future,unreachable

from __future__ import annotations
import pygame

import affichage as af

class AffichageEditeur(af.WrapperNoeud):
    """L'affichage principal de l'éditeur."""
    def __init__(self):
        af.WrapperNoeud.__init__(self)
        self.contenu = af.PavageHorizontal()
        liste_onglets = af.ListeVerticale()
        ongletint = af.Placeheldholder()
        ongletext = af.PavageVertical()
        ongletext.set_contenu([af.MargeHorizontale(),
                                ongletint,
                                af.MargeHorizontale()],[5,-1,5])

        bouton1ext = af.PavageVertical()
        bouton1int = af.PavageHorizontal()
        bouton1int.set_contenu([af.MargeVerticale(),
                                af.BoutonPlaceholder(ongletint,
                                    af.CenterTexte("Ceci sera l'onglet 1"),
                                    af.SKIN_VIDE,"Onglet 1"
                                ),
                                af.MargeVerticale()],
                                [5,0,5])
        bouton1ext.set_contenu([af.MargeHorizontale(),
                                bouton1int,
                                af.MargeHorizontale()],
                                [5,0,5])

        bouton2ext = af.PavageVertical()
        bouton2int = af.PavageHorizontal()
        bouton2int.set_contenu([af.MargeVerticale(),
                                af.BoutonPlaceholder(ongletint,
                                    af.CenterTexte("Ceci sera l'onglet 2"),
                                    af.SKIN_VIDE,"Onglet 2"
                                ),
                                af.MargeVerticale()],
                                [5,0,5])
        bouton2ext.set_contenu([af.MargeHorizontale(),
                                bouton2int,
                                af.MargeHorizontale()],
                                [5,0,5])

        liste_onglets.set_contenu([
            af.MargeHorizontale(),
            bouton1ext,
            af.MargeHorizontale(),
            bouton2ext,
            af.MargeHorizontale()],
        [5,0,5,0,5])
        self.contenu.set_contenu([
            af.MargeVerticale(),
            liste_onglets,
            af.MargeVerticale(),
            ongletext,
            af.MargeVerticale()],
            [5,0,5,-1,5])
        
        self.fond = (255,255,255)
        self.actif = True
        self.courant = ongletint

    def bouge_souris(self, event:pygame.event.Event):
        """Traite les évènements liés à la souris."""
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: #On a cliqué sur quelque chose. Vérifions quoi :
            if not self.clique(event.pos):
                # Now that's weird...
                print("Clic sur rien")
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3: #On a cliqué droit
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
