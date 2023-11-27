"""Contient la classe Armure."""

from __future__ import annotations
from typing import TYPE_CHECKING
import carte as crt

# Imports des classes parentes
from ..equippement import Equippement

# Imports utilisés dans le code
from .....affichage import SKIN_ARMURE

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from .....labyrinthe.labyrinthe import Labyrinthe

class Armure(Equippement):
    """La classe des équipements de type armure. On ne peut en porter qu'une à la fois."""
    def __init__(self,labyrinthe:Labyrinthe,position:crt.Position=crt.POSITION_ABSENTE):
        Equippement.__init__(self,labyrinthe,position)
        self.poids = 10 #C'est lourd !
        self.frottements = 8 #Il y a pire.

    @staticmethod
    def get_image():
        return SKIN_ARMURE
