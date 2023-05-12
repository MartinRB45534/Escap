from Affichage.Skins.Skins import SKIN_CADAVRE
from Jeu.Labyrinthe.Structure_spatiale.Position import ABSENT, Position
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Jeu.Controleur import Controleur
    from Jeu.Entitee.Agissant.Agissant import Agissant
from Jeu.Entitee.Item.Item import Item

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