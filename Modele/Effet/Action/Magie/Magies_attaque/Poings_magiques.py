from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import carte as crt

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from .....entitee.agissant.agissant import Agissant
    from .....systeme.skill.actif import Actif
    from .....systeme.elements import Element

# Imports des classes parentes
from ...magie.magie import Magie, Magie_dirigee, Magies_offensives

class Magie_attaque_contact(Magie_dirigee,Magies_offensives):
    """Les magies qui créent une attaque au contact."""
    def __init__(self,skill:Actif,agissant:Agissant,direction:Optional[crt.Direction],gain_xp:float,cout_pm:float,portee:float,degats:float,element:Element,latence:float,niveau:int):
        Magie.__init__(self,skill,agissant,gain_xp,cout_pm,latence,niveau)
        self.portee = portee
        self.degats = degats
        self.element = element
        self.direction = direction

    def action(self):
        if self.direction is None:
            self.interrompt()
        else:
            for position in self.agissant.labyrinthe.a_portee(self.agissant.position,self.portee,Deplacement.SPATIAL,Forme.DEMI_CERCLE,Passage(False,False,False,False,False)):
                self.agissant.labyrinthe.get_case(position).effets.add(AttaqueCase(self.agissant,self.degats,self.element,"contact",self.direction))

# Imports utilisés dans le code
from ....attaque.attaque import AttaqueCase
from .....labyrinthe.deplacement import Deplacement
from .....labyrinthe.forme import Forme
from .....labyrinthe.passage import Passage