from __future__ import annotations
from typing import List, Tuple, TYPE_CHECKING
from operator import itemgetter

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ..Structure_spatiale.Position import Position
    from ..Structure_spatiale.Direction import Direction
    from ..Structure_spatiale.Decalage import Decalage
    from ..Extrait import Extrait
    from ..Labyrinthe import Labyrinthe
    from .Vignette_case import Vignette_case

# Import des classes parentes
from Affichage import Affichable, Parent_noeud, Proportionnel, Cliquable

class Carte_extrait(Parent_noeud, Proportionnel):
    def __init__(self, extrait:Extrait|Labyrinthe):
        Parent_noeud.__init__(self)

        self.labyrinthe = extrait
        self.taille_case = 0
        self.nb_cases = 0
        self.proportions = [1, 1]

    def set_tailles(self, tailles):
        Proportionnel.set_tailles(self, tailles)
        self.update()

    def update(self):
        assert isinstance(self.courant,Vignette_case|None)
        courant = None
        self.objets:List[Affichable] = []
        if len(self.labyrinthe.position_case) > 1: # On a au moins une case plus l'absente
            # On a le même étage pour toutes les cases du labyrinthe (sauf l'absente)
            assert len({position.etage for position in self.labyrinthe.position_case if position is not POSITION_ABSENTE}) == 1
            etage = [position.etage for position in self.labyrinthe.position_case if position is not POSITION_ABSENTE][0]
            visible = [min(position.x for position in self.labyrinthe.position_case), max(position.x for position in self.labyrinthe.position_case), min(position.y for position in self.labyrinthe.position_case), max(position.y for position in self.labyrinthe.position_case)]
            debut = Position(etage, visible[0], visible[2])
            nb_cases = max(visible[1]-visible[0], visible[3]-visible[2])+1
            taille_case = int(min(self.tailles) // (nb_cases-1))
            hauteur_exploitee = taille_case * nb_cases
            marge = (min(self.tailles) - hauteur_exploitee) // 2
            self.nb_cases = nb_cases
            marge_haut = self.position[1]+marge#+taille_case//2
            for j in range(self.nb_cases):
                marge_gauche = self.position[0]+marge#+taille_case//2
                for i in range(self.nb_cases):
                    pos = debut + Decalage(i, j)
                    vignette = self.make_vignette((marge_gauche, marge_haut), pos, (taille_case, taille_case))
                    if self.courant and vignette.pos == self.courant.pos:
                        courant = vignette
                        if self.courant.actif:
                            vignette.set_actif()
                    self.objets.append(vignette)
                    marge_gauche += taille_case
                marge_haut += taille_case
        self.set_courant(courant)

    def make_vignette(self, position:Tuple[int,int], position_vue:Position, tailles:Tuple[int,int]):
        return Vignette_case(position, self.labyrinthe, position_vue, tailles)
    
    def select(self, selection:Cliquable, droit:bool=False):
        if not droit:
            if isinstance(selection, Vignette_case):
                self.set_courant(selection)

    def set_default_courant(self):
        vignettes = [vignette for vignette in self.objets if isinstance(vignette, Vignette_case) and vignette.pos != POSITION_ABSENTE]
        if vignettes:
            self.set_courant(vignettes[0])
        else:
            self.set_courant(None)

    def in_up(self):
        if isinstance(self.courant, Vignette_case):
            up = self.courant.pos + Direction.HAUT
            vignettes = [vignette for vignette in self.objets if isinstance(vignette, Vignette_case) and vignette.pos == up]
            if vignettes:
                self.set_courant(vignettes[0])
            else:
                self.set_courant(None)
        return self
    
    def in_down(self):
        if isinstance(self.courant, Vignette_case):
            down = self.courant.pos + Direction.BAS
            vignettes = [vignette for vignette in self.objets if isinstance(vignette, Vignette_case) and vignette.pos == down]
            if vignettes:
                self.set_courant(vignettes[0])
            else:
                self.set_courant(None)
        return self
    
    def in_left(self):
        if isinstance(self.courant, Vignette_case):
            left = self.courant.pos + Direction.GAUCHE
            vignettes = [vignette for vignette in self.objets if isinstance(vignette, Vignette_case) and vignette.pos == left]
            if vignettes:
                self.set_courant(vignettes[0])
            else:
                self.set_courant(None)
        return self
    
    def in_right(self):
        if isinstance(self.courant, Vignette_case):
            right = self.courant.pos + Direction.DROITE
            vignettes = [vignette for vignette in self.objets if isinstance(vignette, Vignette_case) and vignette.pos == right]
            if vignettes:
                self.set_courant(vignettes[0])
            else:
                self.set_courant(None)
        return self

from ..Structure_spatiale.Absent import POSITION_ABSENTE