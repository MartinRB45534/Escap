from __future__ import annotations
from typing import TYPE_CHECKING
import Carte as crt

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from .....Labyrinthe.Labyrinthe import Labyrinthe

# Imports des classes parentes
from ..Equippement import Equippement

class Heaume(Equippement):
    """La classe des équipements de type heaume. On ne peut en porter qu'un à la fois."""
    def __init__(self,labyrinthe:Labyrinthe,poids:float,frottements:float,position:crt.Position=crt.POSITION_ABSENTE):
        Equippement.__init__(self,labyrinthe,position)

    @staticmethod
    def get_image():
        return SKIN_HEAUME

# Imports utilisés dans le code
from .....Affichage.Skins import SKIN_HEAUME