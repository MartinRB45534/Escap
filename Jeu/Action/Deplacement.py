from __future__ import annotations
from typing import TYPE_CHECKING, Optional

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from Jeu.Entitee.Agissant.Agissant import Agissant
    from Jeu.Entitee.Item.Item import Item
    from Jeu.Labyrinthe.Structure_spatiale.Direction import Direction

# Imports des classes parentes
from Jeu.Action.Action import Action

class Deplace(Action):
    """
    L'action de déplacement (item ou agissant).
    """
    def __init__(self,agissant:Agissant,latence:float,direction:Direction):
        super().__init__(agissant,latence)
        self.direction = direction

    def action(self):
        lab = self.agissant.controleur.labs[self.agissant.position.lab]
        lab.veut_passer(self.agissant,self.direction)

    def get_skin(self):
        pass
        # TODO: Ajouter le get_skin

class Vole(Action):
    """
    L'action des items qui volent.
    """
    def __init__(self,item:Item,latence:float,direction:Direction):
        self.item = item
        self.latence = 0
        self.latence_max = latence
        self.taux_vitesse = {}
        self.direction = direction

    def action(self):
        lab = self.item.controleur.labs[self.item.position.lab]
        lab.veut_passer(self.item,self.direction)

    def termine(self):
        self.item.action
        
    def get_skin(self):
        pass
        # TODO: Ajouter le get_skin