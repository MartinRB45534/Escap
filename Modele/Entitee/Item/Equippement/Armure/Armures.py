from __future__ import annotations
from typing import TYPE_CHECKING

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ..Controleur import Controleur
    from ..Labyrinthe.Structure_spatiale.Position import Position

# Imports des classes parentes
from ..Entitee.Item.Equippement.Armure.Armure import Armure
from ..Entitee.Item.Equippement.Role.Defensif.Defensifs import Defensif_proportion

# Valeurs par défaut des paramètres
from ..Labyrinthe.Structure_spatiale.Position import ABSENT
from ..Constantes import TERRE

class Armure_type(Armure,Defensif_proportion):
    """Une armure type : défend contre les attaques."""
    def __init__(self,taux_degats:float,position:crt.Position=crt.POSITION_ABSENTE):
        Armure.__init__(self,controleur,position)
        Defensif_proportion.__init__(self,taux_degats)
