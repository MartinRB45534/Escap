from __future__ import annotations
from typing import TYPE_CHECKING

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ..Controleur import Controleur
    from ..Labyrinthe.Structure_spatiale.Position import Position

# Imports des classes parentes
from ..Entitee.Item.Equippement.Equippement import Equipement

# Valeurs par défaut des paramètres
from ..Labyrinthe.Structure_spatiale.Position import ABSENT

class Anneau(Equipement):
    """La classe des équipements de type anneau. Le nombre d'anneaux qu'on peut porter dépend de l'espèce. Les anneaux peuvent avoir des effets très différends (magiques pour la plupart)."""
    def __init__(self,controleur:Controleur,position:Position=ABSENT):
        Equipement.__init__(self,controleur,position)
        self.poids = 1 #C'est très léger !
        self.frottement = 2 #Il y a mieux.

    def get_titre(self,observation=0):
        return "Anneau"

    def get_description(self,observation=0):
        return ["Un anneau","Tu peux en porter plusieurs."]

    def get_classe(self):
        return Anneau

    def get_skin(self):
        return SKIN_ANNEAU

    @staticmethod
    def get_image():
        return SKIN_ANNEAU

# Imports utilisés dans le code
from Old_Affichage.Skins.Skins import SKIN_ANNEAU