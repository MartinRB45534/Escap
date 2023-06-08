from __future__ import annotations
from typing import TYPE_CHECKING

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ....Agissant.Agissant import Agissant

# Imports des classes parentes
from ..Equippement import Equipement

class Equipement_tribal(Equipement):
    def __init__(self,espece:str,taux:float):
        self.espece = espece
        self.taux = taux

    def equippe(self,agissant:Agissant):
        if not self.espece in agissant.especes :
            self.taux_stats["incompatibilité porteur"] = self.taux
