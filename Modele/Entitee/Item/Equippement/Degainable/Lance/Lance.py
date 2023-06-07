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

class Lance(Arme):
    """La classe des armes de type lance. Permettent de porter des coups rectilignes devant l'agissant."""
    def __init__(self,controleur:Controleur,element:Element,tranchant:float,portee:int,position:Position=ABSENT):
        Arme.__init__(self,controleur,element,tranchant,portee,position)
        self.poids = 3
        self.frottements = 3

    def get_titre(self,observation=0):
        return "Lance"

    def get_description(self,observation=0):
        return ["Une lance","Pour faire des trous dans les gens."]

    def get_skin(self):
        return SKIN_LANCE

# Imports utilisés dans le code
from Old_Affichage.Skins.Skins import SKIN_LANCE