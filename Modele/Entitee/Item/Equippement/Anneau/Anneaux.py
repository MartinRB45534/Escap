from __future__ import annotations
from typing import TYPE_CHECKING

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ..Controleur import Controleur
    from ..Labyrinthe.Structure_spatiale.Position import Position

# Imports des classes parentes
from ..Entitee.Item.Equippement.Anneau.Anneau import Anneau
from ..Entitee.Item.Equippement.Role.Reparateur.Reparateurs import Renforce_regen_pv
from ..Entitee.Item.Equippement.Role.Reparateur_magique.Reparateurs_magiques import Renforce_regen_pm

# Valeurs par défaut des paramètres
from ..Labyrinthe.Structure_spatiale.Position import ABSENT
from ..Constantes import TERRE

class Anneau_magique(Anneau,Renforce_regen_pm):
    """Un anneau magique : augmente la régénération des pm."""
    def __init__(self,controleur:Controleur,taux_regen:float,position:Position=ABSENT):
        Equipement.__init__(self,controleur,position)
        Renforce_regen_pm.__init__(self,taux_regen)

class Anneau_de_vitalite(Anneau,Renforce_regen_pv):
    """Un anneau un peu moins magique : augmente la régénération des pv."""
    def __init__(self,controleur:Controleur,taux_regen:float,position:Position=ABSENT):
        Equipement.__init__(self,controleur,position)
        Renforce_regen_pv.__init__(self,taux_regen)

# Imports utilisés dans le code
from ..Entitee.Item.Equippement.Equippement import Equipement