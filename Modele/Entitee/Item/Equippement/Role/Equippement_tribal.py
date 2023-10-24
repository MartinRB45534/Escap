from __future__ import annotations
from typing import TYPE_CHECKING

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ....agissant.agissant import Agissant
    from ....agissant.espece import Espece

# Imports des classes parentes
from ..equippement import Equippement

class Equippement_tribal(Equippement):
    def __init__(self,espece:Espece,taux:float):
        self.espece = espece
        self.taux = taux

    def equippe(self,agissant:Agissant):
        if not self.espece in agissant.espece :
            self.taux_stats["incompatibilité porteur"] = self.taux
