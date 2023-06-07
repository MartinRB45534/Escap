from __future__ import annotations
from typing import List, Tuple, TYPE_CHECKING
import Affichage as af

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ..Structure_spatiale.Position import Position
    from ..Structure_spatiale.Direction import Direction
    from ..Extrait import Extrait
    from ..Labyrinthe import Labyrinthe

class Vignette_case(af.Vignette_composee):
    def __init__(self,position:Tuple[int,int],vue:Extrait|Labyrinthe,pos:Position,taille:Tuple[int,int]):
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
                if not(vue.get_mur(pos,direction).ferme):
                    vignettes.append(af.Vignette(position,taille,SKIN_MUR_BROUILLARD,direction))
        else:
            vignettes.append(af.Vignette(position,taille,SKIN_BROUILLARD))

        af.Vignette_composee.__init__(self,vignettes,taille)

from .Skins import *