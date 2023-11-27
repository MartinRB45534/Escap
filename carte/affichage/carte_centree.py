"""
Affiche la carte centrée sur une case.
"""

from __future__ import annotations
from typing import TYPE_CHECKING
import affichage as af

from .carte_extrait import CarteExtrait
from ..structure_spatiale.position import Position
from .vignette_case import VignetteCase

if TYPE_CHECKING:
    from ..extrait import Extrait
    from ..labyrinthe import Labyrinthe

class CarteCentree(CarteExtrait):
    """Un affichage de la carte centrée sur une case."""
    def __init__(self, extrait:Extrait|Labyrinthe, centre:Position):
        CarteExtrait.__init__(self, extrait)
        self.centre = centre

    def update(self):
        assert isinstance(self.courant,VignetteCase|None)
        courant = None
        self.objets:list[af.Affichable] = []
        if len(self.labyrinthe.nodes) > 1: # On a au moins une case plus l'absente
            # On a le même étage pour toutes les cases du labyrinthe (sauf l'absente)
            assert len({position.etage for position in self.labyrinthe.nodes if position is not POSITION_ABSENTE}) == 1
            etage = [position.etage for position in self.labyrinthe.nodes if position is not POSITION_ABSENTE][0]
            visible = [min(position.x for position in self.labyrinthe.nodes)-1, max(position.x for position in self.labyrinthe.nodes)+1, min(position.y for position in self.labyrinthe.nodes)-1, max(position.y for position in self.labyrinthe.nodes)+1]
            visible = [min(visible[0], self.centre.x-1), max(visible[1], self.centre.x+1), min(visible[2], self.centre.y-1), max(visible[3], self.centre.y+1)]
            visible = [min(visible[0], 2*self.centre.x-visible[1]), max(visible[1], 2*self.centre.x-visible[0]), min(visible[2], 2*self.centre.y-visible[3]), max(visible[3], 2*self.centre.y-visible[2])]
            nb_cases = max(visible[1]-visible[0], visible[3]-visible[2])+3
            taille_case = int(min(self.tailles) // (nb_cases-1))
            hauteur_exploitee = taille_case * nb_cases
            marge = (min(self.tailles) - hauteur_exploitee) // 2
            self.nb_cases = nb_cases
            marge_haut = self.position[1]+marge#+taille_case//2
            for j in range(self.nb_cases):
                marge_gauche = self.position[0]+marge#+taille_case//2
                for i in range(self.nb_cases):
                    pos = Position(etage, visible[0]+i, visible[2]+j)
                    vignette = self.make_vignette((marge_gauche, marge_haut), pos, taille_case)
                    if self.courant and vignette.pos == self.courant.pos:
                        courant = vignette
                        if self.courant.actif:
                            vignette.set_actif()
                    self.objets.append(vignette)
                    marge_gauche += taille_case
                marge_haut += taille_case
        self.set_courant(courant)

from ..structure_spatiale.absent import POSITION_ABSENTE