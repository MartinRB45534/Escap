from __future__ import annotations
from typing import List, Tuple, TYPE_CHECKING
import affichage as af

from ..structure_spatiale.direction import Direction

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ..structure_spatiale.position import Position
    from ..extrait import Extrait
    from ..labyrinthe import Labyrinthe

class VignetteCase(af.VignetteComposee):
    """Vignette représentant une case."""
    def __init__(self,position:Tuple[int,int],vue:Extrait|Labyrinthe,pos:Position,taille:int):
        self.pos = pos
        vignettes:List[af.Affichable] = []
        if pos in vue:
            vignettes.append(af.Vignette(position,taille,SKIN_CASE)) #La case en premier, donc en bas
            for direction in Direction:
                if vue.get_mur(pos,direction).ferme:
                    vignettes.append(af.Vignette(position,taille,SKIN_MUR,direction))
        elif isinstance(vue,Extrait) and pos in vue.exterieur:
            vignettes.append(af.Vignette(position,taille,SKIN_BROUILLARD))
            for direction in Direction:
                if not vue.get_mur(pos,direction).ferme :
                    vignettes.append(af.Vignette(position,taille,SKIN_MUR_BROUILLARD,direction))
        else:
            vignettes.append(af.Vignette(position,taille,SKIN_BROUILLARD))

        af.VignetteComposee.__init__(self,vignettes,taille)

from .skins import SKIN_CASE, SKIN_MUR, SKIN_BROUILLARD, SKIN_MUR_BROUILLARD
