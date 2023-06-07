from __future__ import annotations
from typing import TYPE_CHECKING

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ..Controleur import Controleur
    from ..Labyrinthe.Structure_spatiale.Position import Position

# Imports des classes parentes
from ..Entitee.Item.Equippement.Degainable.Degainable import Arme

# Valeurs par défaut des paramètres
from ..Labyrinthe.Structure_spatiale.Position import ABSENT

class Epee(Arme):
    """La classe des armes de type épée. Permettent de porter des coups semi-circulaires devant l'agissant."""
    def __init__(self,controleur:Controleur,element:Element,tranchant:float,portee:int,position:Position=ABSENT):
        Arme.__init__(self,controleur,element,tranchant,portee,position)
        self.poids = 5
        self.frottements = 4

    def get_titre(self,observation=0):
        return "Épée"

    def get_description(self,observation=0):
        return ["Une épée","Pour couper le saucisson."]

    def get_skin(self):
        return SKIN_EPEE

# Imports utilisés dans le code
from Old_Affichage.Skins.Skins import SKIN_EPEE