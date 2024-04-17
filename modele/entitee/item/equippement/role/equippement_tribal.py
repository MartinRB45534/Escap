"""Les équipements tribaux."""

from __future__ import annotations
from typing import TYPE_CHECKING

# Imports des classes parentes
from ..equippement import Equippement

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ....agissant.agissant import Agissant
    from ....agissant.espece import Espece

class EquippementTribal(Equippement):
    """La classe des équipements tribaux. Ils sont destinés à une espèce en particulier."""
    espece:Espece
    taux:float

    def equippe(self,agissant:Agissant):
        if not self.espece in agissant.espece :
            self.taux_stats["incompatibilité porteur"] = self.taux
