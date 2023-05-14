from __future__ import annotations
from typing import TYPE_CHECKING, List

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from Jeu.Controleur import Controleur
    from Jeu.Labyrinthe.Structure_spatiale.Position import Position
    from Jeu.Effet.Effet import Effet

# Imports des classes parentes
from Jeu.Entitee.Item.Item import Item

# Valeurs par défaut des paramètres
from Jeu.Labyrinthe.Structure_spatiale.Position import ABSENT

class Projectile(Item):
    """La classe des items destinés à être lancés. Possèdent naturellement une vitesse non nulle."""
    def __init__(self,controleur:Controleur,position:Position=ABSENT,vitesse:float=0,effets:List[Effet]=[]):
        Item.__init__(self,controleur,position)
        self.vitesse = vitesse
        self.effets = effets #Les effets déclenché lors du choc avec un agissant.

    def get_classe(self):
        return Projectile

    def get_titre(self,observation=0):
        return "Projectile"

    @staticmethod
    def get_image():
        return SKIN_PROJECTILE

# Imports utilisés dans le code
from Affichage.Skins.Skins import SKIN_PROJECTILE