from __future__ import annotations
from typing import TYPE_CHECKING
import Carte as crt

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ......Labyrinthe.Labyrinthe import Labyrinthe
    from ......Systeme.Elements import Element

# Imports des classes parentes
from ..Degainable import Arme

class Epee(Arme):
    """La classe des armes de type épée. Permettent de porter des coups semi-circulaires devant l'agissant."""
    def __init__(self,labyrinthe:Labyrinthe,poids:float,frottements:float,element:Element,tranchant:float,portee:int,position:crt.Position=crt.POSITION_ABSENTE):
        Arme.__init__(self,labyrinthe,poids,frottements,element,tranchant,portee,position)
