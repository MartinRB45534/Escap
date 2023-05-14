from __future__ import annotations
from typing import TYPE_CHECKING

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from Jeu.Controleur import Controleur
    from Jeu.Labyrinthe.Structure_spatiale.Position import Position
    from Jeu.Entitee.Agissant.Agissant import Agissant

# Imports des classes parentes
from Jeu.Entitee.Item.Item import Item

# Valeurs par défaut des paramètres
from Jeu.Labyrinthe.Structure_spatiale.Position import ABSENT

class Oeuf(Item):
    def __init__(self,controleur:Controleur,agissant:Agissant,position:Position=ABSENT):
        """Un item qui transporte un agissant. Va éclore avec le temps."""
        Item.__init__(self,controleur,position)
        self.poids = 1
        self.agissant = agissant

    def get_titre(self,observation=0):
        return "Oeuf"

    def get_description(self,observation=0):
        return ["Un oeuf","Je n'ai rien pour le cuire..."]

    @staticmethod
    def get_image():
        return SKIN_OEUF
    
# Imports utilisés dans le code
from Affichage.Skins.Skins import SKIN_OEUF