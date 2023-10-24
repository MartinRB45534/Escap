from __future__ import annotations
from typing import TYPE_CHECKING

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ...entitee.agissant.agissant import Agissant

# Imports des classes parentes
from .agissant import Effet_agissant
from ..effet import Evenement

class Investissement_mana(Evenement,Effet_agissant):
    """Le joueur met du mana de côté, et en a plus après !"""
    def __init__(self,agissant:Agissant,temps_restant:float,mana:float):
        self.agissant = agissant
        self.temps_restant = temps_restant
        self.mana = mana

    def action(self):
        if self.termine():
            self.agissant.statistiques.pm += self.mana

class Reserve_mana(Effet_agissant):
    """Effet qui correspond à une réserve de mana pour le joueur qui peut piocher dedans lorsqu'il en a besoin, mais ce mana n'est pas compté dans le calcul de son mana max."""
    def __init__(self,agissant:Agissant,mana:float):
        self.agissant = agissant
        self.mana = mana

    def action(self,mana:float):
        self.mana -= mana

    def execute(self,mana:float):
        self.action(mana)

    def termine(self):
        return self.mana <= 0
