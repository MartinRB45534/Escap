from __future__ import annotations
from typing import TYPE_CHECKING, Optional, List
import Carte as crt

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from .....Entitee.Agissant.Agissant import Agissant
    from .....Systeme.Skill.Actif import Actif
    from ....Attaque.Attaque import Attaque_case_delayee
    from .....Systeme.Elements import Element

# Imports des classes parentes
from ...Magie.Magie import Magie,Cible_case,Magies_offensives

class Magie_attaque_distance(Cible_case,Magies_offensives):
    """Les magies qui créent une attaque à distance."""
    def __init__(self,skill:Actif,agissant:Agissant,cible:Optional[crt.Position],gain_xp:float,cout_pm:float,portee:float,degats:float,element:Element,latence:float,niveau:int):
        Magie.__init__(self,skill,agissant,gain_xp,cout_pm,latence,niveau)
        self.cible = cible
        self.effets:List[Attaque_case_delayee] = []
        self.portee = portee
        self.degats = degats
        self.element = element

    def action(self):
        if self.cible is None:
            self.interrompt()
        elif self.effets == []:
            for position in self.agissant.labyrinthe.a_portee(self.cible,self.portee,Deplacement.MAGIQUE,Forme.CERCLE,Passage(True,True,True,False,True)):
                effet = Attaque_case_delayee(self.agissant,self.degats,self.element,"distance")
                self.agissant.labyrinthe.get_case(position).effets.add(effet)
                self.effets.append(effet)
        else:
            for effet in self.effets:
                effet.phase = "en cours"

from .....Labyrinthe.Deplacement import Deplacement
from .....Labyrinthe.Forme import Forme
from .....Labyrinthe.Passage import Passage