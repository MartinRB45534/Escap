"""Contient la classe Accelerateur."""

from __future__ import annotations
from typing import TYPE_CHECKING
import carte as crt

# Imports des classes parentes
from ..equippement import Equippement

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from .....labyrinthe.labyrinthe import Labyrinthe

class Accelerateur(Equippement):
    """La classe des équipements qui augmentent la vitesse."""
    def __init__(self,labyrinthe:Labyrinthe,position:crt.Position,taux_vitesse:float):
        Equippement.__init__(self,labyrinthe,position)
        self.taux_vitesse = taux_vitesse

    def augmente_vitesse(self,vitesse:float):
        """Augmente la vitesse."""
        taux_vitesse = self.taux_vitesse
        for taux in self.taux_stats.values():
            taux_vitesse *= taux
        return vitesse * taux_vitesse
