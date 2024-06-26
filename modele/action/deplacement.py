"""
Contient les classes d'action de déplacement.
"""

from __future__ import annotations
from typing import TYPE_CHECKING
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
    def __init__(self,agissant:Agissant,direction:crt.Direction):
        Action.__init__(self,agissant)
        self.direction = direction

    def action(self):
        self.agissant.labyrinthe.agissant_veut_passer(self.agissant,self.direction)

class Marche(Deplace,ActionSkill,ActionFinal):
    """
    L'action des agissants qui se déplacent.
    """
    def __init__(self,agissant:Agissant,skill:Actif,direction:crt.Direction):
        Deplace.__init__(self,agissant,direction)
        ActionSkill.__init__(self,agissant,skill)
        ActionFinal.__init__(self,agissant)

class Plane:
    """
    L'action des items qui volent. (Ce n'est pas techniquement une action, mais ça se comporte comme un déplacement.)
    """
    latence_max:float
    def __init__(self,item:Item,lanceur:Agissant,direction:crt.Direction):
        self.item = item
        self.lanceur = lanceur
        self.latence:float = 0
        self.taux_vitesse:dict[str,float] = {}
        self.direction = direction

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
