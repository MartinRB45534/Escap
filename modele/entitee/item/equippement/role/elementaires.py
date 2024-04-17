"""Contient la classe des équipements élémentaires"""

from __future__ import annotations
from typing import TYPE_CHECKING

# Imports des classes parentes
from ..equippement import Equippement

# Imports pour les variables de classe

if TYPE_CHECKING:
    from .....commons.elements import Element

class Elementaire(Equippement):
    """La classe des équipements qui augmentent l'affinité à un élément."""
    element:Element
    taux_aff:float

    def augmente_affinite(self, affinite:float) -> float:
        """Augmente l'affinité à l'élément."""
        return affinite*self.taux_aff
