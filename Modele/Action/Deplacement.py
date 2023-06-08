from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import Carte as crt

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ..Entitee.Agissant.Agissant import Agissant
    from ..Entitee.Item.Item import Item
    from ..Systeme.Skill.Actif import Actif

# Imports des classes parentes
from .Action import Action, Action_final
from .Action_skill import Action_skill

class Deplace(Action):
    """
    L'action de déplacement (item ou agissant).
    """
    def __init__(self,agissant:Agissant,latence:float,direction:crt.Direction):
        super().__init__(agissant,latence)
        self.direction = direction

    def action(self):
        self.agissant.labyrinthe.veut_passer(self.agissant,self.direction)

class Vole(Deplace,Action_final):
    """
    L'action des items qui volent.
    """
    def __init__(self,item:Item,latence:float,direction:crt.Direction):
        self.item = item
        self.latence = 0
        self.latence_max = latence
        self.taux_vitesse = {}
        self.direction = direction
        self.repete = True

    def action(self):
        self.item.labyrinthe.veut_passer(self.item,self.direction)

    def execute(self):
        """L'action est appelée à chaque tour."""
        self.latence += self.get_vitesse()
        if self.latence >= self.latence_max:
            return self.termine()

    def termine(self):
        """Le vol ne se finit pas, il est interrompu."""
        self.action()
        self.latence = 0
        return super().termine()
        
    def get_skin(self):
        pass
        # TODO: Ajouter le get_skin

class Marche(Deplace,Action_skill,Action_final):
    """
    L'action des agissants qui se déplacent.
    """
    def __init__(self,agissant:Agissant,latence:float,skill:Actif,xp:float,direction:crt.Direction):
        Action_skill.__init__(self,agissant,latence,skill,xp)
        self.direction = direction
