from __future__ import annotations
from typing import TYPE_CHECKING
import carte as crt

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from .....labyrinthe.labyrinthe import Labyrinthe

# Imports des classes parentes
from .Heaume import Heaume
from ..role.Defensif.Defensifs import Defensif_proportion

class Heaume_type(Heaume,Defensif_proportion):
    """Un heaume type : défend contre les attaques."""
    def __init__(self,labyrinthe:Labyrinthe,poids:float,frottements:float,taux_degats:float,position:crt.Position=crt.POSITION_ABSENTE):
        Heaume.__init__(self,labyrinthe,poids,frottements,position)
        Defensif_proportion.__init__(self,taux_degats)
