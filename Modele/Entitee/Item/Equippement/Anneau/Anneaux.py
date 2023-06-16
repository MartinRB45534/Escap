from __future__ import annotations
from typing import TYPE_CHECKING
import Carte as crt

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from .....Labyrinthe.Labyrinthe import Labyrinthe

# Imports des classes parentes
from .Anneau import Anneau
from ..Role.Reparateur.Reparateurs import Renforce_regen_pv
from ..Role.Reparateur_magique.Reparateurs_magiques import Renforce_regen_pm

class Anneau_magique(Anneau,Renforce_regen_pm):
    """Un anneau magique : augmente la régénération des pm."""
    def __init__(self,labyrinthe:Labyrinthe,poids:float,frottements:float,taux_regen:float,position:crt.Position=crt.POSITION_ABSENTE):
        Equippement.__init__(self,labyrinthe,position)
        Renforce_regen_pm.__init__(self,taux_regen)
        self.poids = poids
        self.frottements = frottements

class Anneau_de_vitalite(Anneau,Renforce_regen_pv):
    """Un anneau un peu moins magique : augmente la régénération des pv."""
    def __init__(self,labyrinthe:Labyrinthe,poids:float,frottements:float,taux_regen:float,position:crt.Position=crt.POSITION_ABSENTE):
        Equippement.__init__(self,labyrinthe,position)
        Renforce_regen_pv.__init__(self,taux_regen)
        self.poids = poids
        self.frottements = frottements

# Imports utilisés dans le code
from ...Equippement.Equippement import Equippement