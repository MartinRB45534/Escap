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

class Degainable(Equipement):
    """La classe des items qui doivent être dégainés. Sont utilisés en complément d'un skill, n'ont pas d'effet le reste du temps."""
    pass

class Arme(Degainable):
    """La classe des équipements qui augmentent la force d'attaque."""
    def __init__(self,controleur:Controleur,element:Element,tranchant:float,portee:int,position:Position=ABSENT):
        Equipement.__init__(self,controleur,position)
        self.element = element
        self.tranchant = tranchant
        self.taux_tranchant = {}
        self.portee = portee
        self.taux_portee = {}
        self.taux_stats = {}

    def get_stats_attaque(self):
        tranchant = self.tranchant
        for taux in self.taux_tranchant.values():
            tranchant *= taux
        portee = self.portee
        for taux in self.taux_portee.values():
            portee *= taux
        for taux in self.taux_stats.values():
            tranchant *= taux
            portee *= taux
        return self.element,tranchant,portee

    def get_classe(self):
        return Arme

    @staticmethod
    def get_image():
        return SKIN_ARME
    
# Imports utilisés dans le code
from Old_Affichage.Skins.Skins import SKIN_ARME