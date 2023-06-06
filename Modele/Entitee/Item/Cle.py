from __future__ import annotations
from typing import TYPE_CHECKING, List

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from Old_Jeu.Controleur import Controleur
    from Old_Jeu.Labyrinthe.Structure_spatiale.Position import Position
    from Old_Jeu.Entitee.Agissant.Agissant import Agissant

# Imports des classes parentes
from Old_Jeu.Entitee.Item.Item import Item

# Valeurs par défaut des paramètres
from Old_Jeu.Labyrinthe.Structure_spatiale.Position import ABSENT

class Cle(Item):
    """La classe des items qui ouvrent les portes (et les coffres ?)."""
    def __init__(self,controleur:Controleur,codes:List[str],position:Position=ABSENT):
        Item.__init__(self,controleur,position)
        self.codes = codes

    def get_codes(self):
        return self.codes

    def get_classe(self):
        return Cle

    def get_titre(self,observation=0):
        return "Clé"

    def get_description(self,observation=0):
        return ["Une clé","Je suppose qu'elle ouvre une porte."]

    def get_skin(self):
        return SKIN_CLE

    @staticmethod
    def get_image():
        return SKIN_CLE

# Imports utilisés dans le code
from Old_Affichage.Skins.Skins import SKIN_CLE