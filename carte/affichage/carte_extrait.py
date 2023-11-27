"""
Affiche un extrait de labyrinthe.
"""

from __future__ import annotations
from typing import TYPE_CHECKING
import affichage as af

from ..structure_spatiale.absent import POSITION_ABSENTE

from ..structure_spatiale.direction import Direction
from ..structure_spatiale.position import Position
from .vignette_case import VignetteCase

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ..extrait import Extrait
    from ..labyrinthe import Labyrinthe

class CarteExtrait(af.ParentNoeud, af.Proportionnel):
    """Affiche une carte centrée sur une case."""
    def __init__(self, extrait:Extrait|Labyrinthe):
        super().__init__()

        self.labyrinthe = extrait
        self.taille_case = 0
        self.nb_cases = 0
        self.proportions = [1, 1]

    def set_tailles(self, tailles:tuple[int,int]):
        af.Proportionnel.set_tailles(self, tailles)
        self.update()

    def update(self):
        assert isinstance(self.courant,VignetteCase|None)
        courant = None
        self.objets:list[af.Affichable] = []
        if len(self.labyrinthe.nodes) > 1: # On a au moins une case plus l'absente
            # On a le même étage pour toutes les cases du labyrinthe (sauf l'absente)
            assert len({position.etage for position in self.labyrinthe.nodes if position is not POSITION_ABSENTE}) == 1
            etage = [position.etage for position in self.labyrinthe.nodes if position is not POSITION_ABSENTE][0]
            visible = [min(position.x for position in self.labyrinthe.nodes)-1, max(position.x for position in self.labyrinthe.nodes)+1, min(position.y for position in self.labyrinthe.nodes)-1, max(position.y for position in self.labyrinthe.nodes)+1]
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

    def make_vignette(self, position:tuple[int,int], position_vue:Position, taille:int):
        """Crée une vignette à partir d'une position et d'une taille."""
        return VignetteCase(position, self.labyrinthe, position_vue, taille)

    def select(self, selection:af.Cliquable, droit:bool=False):
        if not droit:
            if isinstance(selection, VignetteCase):
                self.set_courant(selection)

    def set_default_courant(self):
        vignettes = [vignette for vignette in self.objets if isinstance(vignette, VignetteCase) and vignette.pos != POSITION_ABSENTE]
        if vignettes:
            self.set_courant(vignettes[0])
        else:
            self.set_courant(None)

    def in_up(self):
        if isinstance(self.courant, VignetteCase):
            up = self.courant.pos + Direction.HAUT
            vignettes = [vignette for vignette in self.objets if isinstance(vignette, VignetteCase) and vignette.pos == up]
            if vignettes:
                self.set_courant(vignettes[0])
            else:
                self.set_courant(None)
        return self

    def in_down(self):
        if isinstance(self.courant, VignetteCase):
            down = self.courant.pos + Direction.BAS
            vignettes = [vignette for vignette in self.objets if isinstance(vignette, VignetteCase) and vignette.pos == down]
            if vignettes:
                self.set_courant(vignettes[0])
            else:
                self.set_courant(None)
        return self

    def in_left(self):
        if isinstance(self.courant, VignetteCase):
            left = self.courant.pos + Direction.GAUCHE
            vignettes = [vignette for vignette in self.objets if isinstance(vignette, VignetteCase) and vignette.pos == left]
            if vignettes:
                self.set_courant(vignettes[0])
            else:
                self.set_courant(None)
        return self

    def in_right(self):
        if isinstance(self.courant, VignetteCase):
            right = self.courant.pos + Direction.DROITE
            vignettes = [vignette for vignette in self.objets if isinstance(vignette, VignetteCase) and vignette.pos == right]
            if vignettes:
                self.set_courant(vignettes[0])
            else:
                self.set_courant(None)
        return self
