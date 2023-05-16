from __future__ import annotations
from typing import TYPE_CHECKING

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from Jeu.Controleur import Controleur
    from Jeu.Entitee.Agissant.Agissant import Agissant
    from Jeu.Labyrinthe.Structure_spatiale.Position import Position
    from Jeu.Effet.Effet import Effet

# Imports des classes parentes
from Jeu.Entitee.Item.Item import Consommable

# Valeurs par défaut des paramètres
from Jeu.Labyrinthe.Structure_spatiale.Position import ABSENT

class Potion(Consommable):
    """La classe des consommables qui peuvent se boire (ne requièrent pas de magie pour être activés)."""
    def __init__(self,controleur:Controleur,effet:Effet,position:Position=ABSENT):
        Item.__init__(self,controleur,position)
        self.effet = effet

    def utilise(self,agissant:Agissant):
        agissant.ajoute_effet(self.effet)
        self.etat = "brisé"

    def get_description(self,observation=0):
        return ["Une potion","Tu veux la boire ?"]

    def get_classe(self):
        return Potion

    def get_skin(self):
        return SKIN_POTION

    @staticmethod
    def get_image():
        return SKIN_POTION

# Imports utilisés dans le code
from Affichage.Skins.Skins import SKIN_POTION
from Jeu.Entitee.Item.Item import Item