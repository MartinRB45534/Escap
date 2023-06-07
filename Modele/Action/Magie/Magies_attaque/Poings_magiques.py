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
            for case in self.agissant.controleur.get_pos_touches(self.agissant.position,self.portee,"Sd_T___",self.direction,responsable=self.agissant):
                self.agissant.controleur.case_from_position(case).effets.append(Attaque_case(self.agissant,self.degats,self.element,"contact",self.direction))

# Imports utilisés dans le code
from ....Effet.Attaque.Attaque import Attaque_case