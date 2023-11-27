"""Contient la classe Heaume."""

from __future__ import annotations
from typing import TYPE_CHECKING
import carte as crt

# Imports des classes parentes
from ..equippement import Equippement

# Imports utilisés dans le code
from .....affichage import SKIN_HEAUME

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from .....labyrinthe.labyrinthe import Labyrinthe

class Heaume(Equippement):
    """La classe des équipements de type heaume. On ne peut en porter qu'un à la fois."""
    def __init__(self,labyrinthe:Labyrinthe,poids:float,frottements:float,position:crt.Position=crt.POSITION_ABSENTE):
        Equippement.__init__(self,labyrinthe,position)
        self.poids = poids
        self.frottements = frottements

    @staticmethod
    def get_image():
        return SKIN_HEAUME
