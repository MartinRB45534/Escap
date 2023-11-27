"""Les équipements tribaux."""

from __future__ import annotations
from typing import TYPE_CHECKING
import carte as crt

# Imports des classes parentes
from ..equippement import Equippement

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from .....labyrinthe.labyrinthe import Labyrinthe
    from ....agissant.agissant import Agissant
    from ....agissant.espece import Espece

class EquippementTribal(Equippement):
    """La classe des équipements tribaux. Ils sont destinés à une espèce en particulier."""
    def __init__(self,labyrinthe:Labyrinthe,position:crt.Position,espece:Espece,taux:float):
        Equippement.__init__(self,labyrinthe,position)
        self.espece = espece
        self.taux = taux

    def equippe(self,agissant:Agissant):
        if not self.espece in agissant.espece :
            self.taux_stats["incompatibilité porteur"] = self.taux
