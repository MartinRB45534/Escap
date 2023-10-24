from __future__ import annotations
from typing import TYPE_CHECKING
import random
import carte as crt

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ...entitee.agissant.agissant import Agissant


# Imports des classes parentes
from .agissant import Effet_agissant
from ..effet import OnTick

class Confusion(OnTick, Effet_agissant):
    """Les enchantements qui provoque des erreurs de direction."""
    def __init__(self,agissant:Agissant,taux_erreur:float):
        self.agissant = agissant
        self.taux_erreur = taux_erreur

    def action(self):
        if isinstance(self.agissant.action, Deplace) :
            dir_voulue = self.agissant.action.direction
            if random.random() < self.taux_erreur:
                dir_possibles = [dir for dir in crt.Direction if dir is not dir_voulue]
                self.agissant.action.direction = random.choice(dir_possibles)

class EnchantementPochesTrouees(OnTick, Effet_agissant):
    """Les enchantements qui fait droper des items involontairement."""
    def __init__(self,agissant:Agissant,taux_drop:float):
        self.agissant = agissant
        self.taux_drop = taux_drop

    def action(self):
        if random.random() < self.taux_drop :
            self.agissant.inventaire.drop_random(self.agissant.labyrinthe.position_case[self.agissant.position])

from ..action.deplacement import Deplace