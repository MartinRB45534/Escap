"""Contient la classe HeaumeType."""

from __future__ import annotations
from typing import TYPE_CHECKING
import carte as crt

# Imports des classes parentes
from .heaume import Heaume
from ..role.defensif.defensifs import DefensifProportion

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from .....labyrinthe.labyrinthe import Labyrinthe

class HeaumeType(Heaume,DefensifProportion): # TODO : Est-ce que ça a vraiment à être là ?
    """Un heaume type : défend contre les attaques."""
    def __init__(self,labyrinthe:Labyrinthe,poids:float,frottements:float,taux_degats:float,position:crt.Position=crt.POSITION_ABSENTE):
        Heaume.__init__(self,labyrinthe,poids,frottements,position)
        DefensifProportion.__init__(self,labyrinthe,position,taux_degats)
