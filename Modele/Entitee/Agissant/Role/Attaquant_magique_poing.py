from __future__ import annotations
import carte as crt

# Imports des classes parentes
from .mage import Mage

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
            assert isinstance(action,Magie_attaque_contact)
            action.direction = direction
            self.fait(action)
        else:
            Agissant.attaque(self,direction)

# Imports utilisés dans le code
from ..agissant import Agissant
from ....effet.action.magie.magies_attaque.Poings_magiques import Magie_attaque_contact
