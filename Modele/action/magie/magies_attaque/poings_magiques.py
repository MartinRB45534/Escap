"""
Contient les magies d'attaque au contact
"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import carte as crt

# Imports des classes parentes
from ..magie import MagieDirigee, MagiesOffensives

# Imports utilisés dans le code
from ....effet import AttaqueCase
from ....commons import Deplacement, Forme, Passage

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ....entitee.agissant.agissant import Agissant
    from ....systeme.skill.actif import Actif
    from ....commons.elements import Element

class MagieAttaqueContact(MagieDirigee,MagiesOffensives):
    """Les magies qui créent une attaque au contact."""
    def __init__(self,skill:Actif,agissant:Agissant,direction:Optional[crt.Direction],gain_xp:float,cout_pm:float,portee:float,degats:float,element:Element,latence:float,niveau:int):
        MagieDirigee.__init__(self,skill,agissant,gain_xp,cout_pm,latence,direction,niveau)
        MagiesOffensives.__init__(self,skill,agissant,gain_xp,cout_pm,latence,niveau)
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
