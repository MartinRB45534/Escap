"""
Contient les classes d'action de déplacement.
"""

from __future__ import annotations
from typing import TYPE_CHECKING, Dict
import carte as crt

# Imports des classes parentes
from .action import Action, ActionFinal
from .action_skill import ActionSkill

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ..entitee.agissant.agissant import Agissant
    from ..entitee.item.item import Item
    from ..systeme.skill.actif import Actif

class Deplace(Action):
    """
    L'action de déplacement (item ou agissant).
    """
    def __init__(self,agissant:Agissant,latence:float,direction:crt.Direction):
        super().__init__(agissant,latence)
        self.direction = direction

    def action(self):
        self.agissant.labyrinthe.agissant_veut_passer(self.agissant,self.direction)

class Marche(Deplace,ActionSkill,ActionFinal):
    """
    L'action des agissants qui se déplacent.
    """
    def __init__(self,agissant:Agissant,latence:float,skill:Actif,xp:float,direction:crt.Direction):
        Deplace.__init__(self,agissant,latence,direction)
        ActionSkill.__init__(self,agissant,latence,skill,xp)
        ActionFinal.__init__(self,agissant,latence)

class Plane:
    """
    L'action des items qui volent. (Ce n'est pas techniquement une action, mais ça se comporte comme un déplacement.)
    """
    def __init__(self,item:Item,lanceur:Agissant,latence:float,direction:crt.Direction):
        self.item = item
        self.lanceur = lanceur
        self.latence:float = 0
        self.latence_max = latence
        self.taux_vitesse:Dict[str,float] = {}
        self.direction = direction
        self.repete = True

    def action(self):
        """L'action est appelée à certains moments."""
        self.item.labyrinthe.item_veut_passer(self.item,self.direction)

    def execute(self):
        """L'action est appelée à chaque tour."""
        self.latence += self.get_vitesse()
        if self.latence >= self.latence_max:
            self.termine()

    def termine(self):
        """Le vol ne se finit pas, il est interrompu."""
        self.action()
        self.latence = 0

    def get_vitesse(self):
        """Retourne la vitesse de l'item."""
        vitesse = 1
        for taux in self.taux_vitesse.values():
            vitesse *= taux
        return vitesse
