"""Contient la classe des équipements élémentaires"""

from __future__ import annotations
from typing import TYPE_CHECKING
import carte as crt

# Imports des classes parentes
from ..equippement import Equippement

# Imports pour les variables de classe

if TYPE_CHECKING:
    from .....labyrinthe.labyrinthe import Labyrinthe
    from .....commons.elements import Element

class Elementaire(Equippement):
    """La classe des équipements qui augmentent l'affinité à un élément."""
    def __init__(self,labyrinthe:Labyrinthe,position:crt.Position,element:Element,taux_aff:float):
        Equippement.__init__(self,labyrinthe,position)
        self.element = element
        self.taux_aff = taux_aff

    def augmente_affinite(self, affinite:float) -> float:
        """Augmente l'affinité à l'élément."""
        return affinite*self.taux_aff
