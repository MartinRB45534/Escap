from __future__ import annotations
from typing import TYPE_CHECKING

import carte as crt

# Imports des classes parentes
from .mage import Mage
from ..agissant import Agissant

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ....action import MagieAttaqueDirigee

class Attaquant_magique_poing(Mage):
    """Les mages qui ont des attaques magiques de corps à corps si nécessaire."""

    def peut_frapper(self):
        return False
    
    def frappe(self):
        return ""

    def attaque(self, direction: crt.Direction):
        if self.peut_frapper():
            skill = self.get_skill_magique()
            action = skill.fait(self,self.frappe())
            if TYPE_CHECKING:
                assert isinstance(action,MagieAttaqueDirigee)
            action.direction = direction
            self.fait(action)
        else:
            Agissant.attaque(self,direction)
