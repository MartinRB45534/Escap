from __future__ import annotations
from Jeu.Effet.Effets import Direction
from Jeu.Entitee.Agissant.Agissants import Direction

# Pas d'imports pour les annotations

# Imports des classes parentes
from Jeu.Entitee.Agissant.Role.Mage import Mage
from Jeu.Entitee.Item.Items import Direction
from Jeu.Labyrinthe.Structure_spatiale.Direction import Direction

class Attaquant_magique_poing(Mage):
    """Les mages qui ont des attaques magiques de corps à corps si nécessaire."""

    def peut_frapper(self):
        return False
    
    def frappe(self):
        return ""

    def attaque(self, direction: Direction):
        if self.peut_frapper():
            skill = self.get_skill_magique()
            action = skill.fait(self.frappe(),self)
            assert isinstance(action,Magie_attaque_contact)
            action.direction = direction
            self.fait(action)
        else:
            Agissant.attaque(self,direction)
        self.set_statut("attaque")

# Imports utilisés dans le code
from Jeu.Entitee.Agissant.Agissant import Agissant
from Jeu.Action.Magie.Magies_attaque.Poings_magiques import Magie_attaque_contact
