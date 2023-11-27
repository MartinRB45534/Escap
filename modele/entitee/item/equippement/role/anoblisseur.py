"""Contient la classe Anoblisseur."""

from __future__ import annotations
from typing import TYPE_CHECKING
import carte as crt

# Imports des classes parentes
from ..equippement import Equippement

if TYPE_CHECKING:
    from .....labyrinthe.labyrinthe import Labyrinthe

class Anoblisseur(Equippement):
    """La classe des équipements qui augmentent la priorité."""
    def __init__(self,labyrinthe:Labyrinthe,position:crt.Position,taux_priorite:float):
        Equippement.__init__(self,labyrinthe,position)
        self.taux_priorite = taux_priorite

    def augmente_priorite(self,priorite:float):
        """Augmente la priorité."""
        taux_priorite = self.taux_priorite
        for taux in self.taux_stats.values():
            taux_priorite *= taux
        return priorite * taux_priorite
