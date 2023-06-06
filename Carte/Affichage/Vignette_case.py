from __future__ import annotations
from typing import List, Tuple, TYPE_CHECKING

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ..Structure_spatiale.Position import Position
    from ..Structure_spatiale.Direction import Direction
    from ..Extrait import Extrait
    from ..Labyrinthe import Labyrinthe

from Affichage import Affichable, Vignette, Vignette_composee

class Vignette_case(Vignette_composee):
    def __init__(self,position:Tuple[int,int],vue:Extrait|Labyrinthe,pos:Position,taille:Tuple[int,int]):
        self.pos = pos
        vignettes:List[Affichable] = []
        if pos in vue:
            vignettes.append(Vignette(position,taille,SKIN_CASE)) #La case en premier, donc en bas
            for direction in Direction:
                if vue.get_mur(pos,direction).ferme:
                    vignettes.append(Vignette(position,taille,SKIN_MUR,direction))
        elif isinstance(vue,Extrait) and pos in vue.exterieur:
            vignettes.append(Vignette(position,taille,SKIN_BROUILLARD))
            for direction in Direction:
                if not(vue.get_mur(pos,direction).ferme):
                    vignettes.append(Vignette(position,taille,SKIN_MUR_BROUILLARD,direction))
        else:
            vignettes.append(Vignette(position,taille,SKIN_BROUILLARD))

        Vignette_composee.__init__(self,vignettes,taille)

from .Skins import *