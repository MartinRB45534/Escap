from __future__ import annotations

# Pas d'import pour les annotations

# Imports des classes parentes
from ..Equippement import Equippement

# Imports pour les variables de classe
from .....Systeme.Elements import Element

class Elementaire(Equippement):
    """La classe des équipements qui augmentent l'affinité à un élément."""
    element:Element
    def __init__(self,taux_aff:float):
        self.taux_aff = taux_aff

    def augmente_affinite(self, affinite:float) -> float:
        """Augmente l'affinité à l'élément."""
        return affinite*self.taux_aff
