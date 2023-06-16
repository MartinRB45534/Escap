from __future__ import annotations
from typing import TYPE_CHECKING
import Carte as crt

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from .....Labyrinthe.Labyrinthe import Labyrinthe

# Imports des classes parentes
from ..Equippement import Equippement

class Anneau(Equippement):
    """La classe des équipements de type anneau. Le nombre d'anneaux qu'on peut porter dépend de l'espèce. Les anneaux peuvent avoir des effets très différends (magiques pour la plupart)."""
    def __init__(self,labyrinthe:Labyrinthe,poids:float,frottements:float,position:crt.Position=crt.POSITION_ABSENTE):
        Equippement.__init__(self,labyrinthe,position)
        self.poids = poids
        self.frottement = frottements

    @staticmethod
    def get_image():
        return SKIN_ANNEAU

# Imports utilisés dans le code
from Old_Affichage.Skins.Skins import SKIN_ANNEAU