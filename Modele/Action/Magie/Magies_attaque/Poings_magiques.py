from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import Carte as crt

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ....Entitee.Agissant.Agissant import Agissant
    from ....Systeme.Skill.Actif import Actif
    from ....Systeme.Elements import Element

# Imports des classes parentes
from ...Magie.Magie import Magie, Magie_dirigee, Magies_offensives

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
                self.agissant.labyrinthe.get_case(position).effets.add(Attaque_case(self.agissant,self.degats,self.element,"contact",self.direction))

# Imports utilisés dans le code
from ....Effet.Attaque.Attaque import Attaque_case
from ....Labyrinthe.Deplacement import Deplacement
from ....Labyrinthe.Forme import Forme
from ....Labyrinthe.Passage import Passage