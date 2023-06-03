from __future__ import annotations
from typing import TYPE_CHECKING

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from Old_Jeu.Controleur import Controleur
    from Old_Jeu.Labyrinthe.Structure_spatiale.Position import Position
    from Old_Jeu.Entitee.Agissant.Agissant import Agissant

# Imports des classes parentes
from Old_Jeu.Entitee.Item.Item import Item

# Valeurs par défaut des paramètres
from Old_Jeu.Labyrinthe.Structure_spatiale.Position import ABSENT

class Cadavre(Item):
    def __init__(self,controleur:Controleur,agissant:Agissant,position:Position=ABSENT):
        """Les restes d'un agissant. Peut être ressuscité ou réanimé. Certains monstres se vendent aussi à bon prix."""
        Item.__init__(self,controleur,position)
        self.poids = 1
        self.agissant = agissant

    def get_titre(self,observation=0):
        return "Cadavre"

    def get_description(self,observation=0):
        return ["Un cadavre","Où as-tu trouvé ça ?"]

    @staticmethod
    def get_image():
        return SKIN_CADAVRE

# Imports utilisés dans le code
from Old_Affichage.Skins.Skins import SKIN_CADAVRE