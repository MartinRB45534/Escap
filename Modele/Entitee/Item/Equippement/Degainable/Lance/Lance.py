from __future__ import annotations
from typing import TYPE_CHECKING
import carte as crt

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ......labyrinthe.labyrinthe import Labyrinthe
    from ......commons.elements import Element

# Imports des classes parentes
from ..degainable import Arme

class Lance(Arme):
    """La classe des armes de type lance. Permettent de porter des coups rectilignes devant l'agissant."""
    def __init__(self,labyrinthe:Labyrinthe,poids:float,frottements:float,element:Element,tranchant:float,portee:int,position:crt.Position=crt.POSITION_ABSENTE):
        Arme.__init__(self,labyrinthe,poids,frottements,element,tranchant,portee,position)
