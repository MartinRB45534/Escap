from __future__ import annotations
from typing import List

from Affichage import Affichable, Vignette, Vignette_composee

class Vignette_case(Vignette_composee):
    def __init__(self,position,joueur:PJ,vue:Representation_vue,pos,taille):
        assert joueur.controleur is not None
        vignettes:List[Affichable] = []
        if pos in vue:
            vue_case = vue.case_from_position(pos)
            if not(vue_case.clarte):
                vignettes.append(Vignette(position,taille,SKIN_BROUILLARD))
            elif vue_case.clarte==-1: #On a affaire à une case accessible mais pas vue
                vignettes.append(Vignette(position,taille,SKIN_BROUILLARD))
                for i in DIRECTIONS:
                    if vue_case.cibles[i][BASIQUE]:
                        pos_voisin = vue_case.case.position+i
                        if pos_voisin in vue and vue.case_from_position(pos_voisin).clarte>0:
                            vignettes.append(Vignette(position,taille,SKIN_MUR_BROUILLARD,i))
            else:
                vignettes.append(Vignette(position,taille,SKINS_CASES[vue_case.code])) #La case en premier, donc en bas
                case:Case = joueur.controleur.case_from_position(vue_case.case.position)
                for i in DIRECTIONS:
                    mur:Mur = case[i]
                    for effet in mur.effets:
                        if effet.affiche:
                            if isinstance(effet,Porte) :
                                vignettes.append(Vignette(position,taille,effet.get_skin(joueur.get_clees()),i))
                            elif isinstance(effet,Mur_plein|Mur_impassable) :
                                vignettes.append(Vignette(position,taille,effet.get_skin(vue_case.code),i))
                            else :
                                vignettes.append(Vignette(position,taille,effet.get_skin(),i))
                for effet in case.effets:
                    if effet.affiche:
                        vignettes.append(Vignette(position,taille,effet.get_skin()))
        else:
            vignettes.append(Vignette(position,taille,SKIN_BROUILLARD))

        Vignette_composee.__init__(self,vignettes,taille)
