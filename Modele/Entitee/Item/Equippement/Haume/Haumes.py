from __future__ import annotations
from typing import TYPE_CHECKING
import Carte as crt

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from .....Labyrinthe.Labyrinthe import Labyrinthe

# Imports des classes parentes
from .Haume import Haume
from ..Role.Defensif.Defensifs import Defensif_proportion

class Haume_type(Haume,Defensif_proportion):
    """Un haume type : défend contre les attaques."""
    def __init__(self,labyrinthe:Labyrinthe,poids:float,frottements:float,taux_degats:float,position:crt.Position=crt.POSITION_ABSENTE):
        Haume.__init__(self,labyrinthe,poids,frottements,position)
        Defensif_proportion.__init__(self,taux_degats)
