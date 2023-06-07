from __future__ import annotations
from typing import TYPE_CHECKING, Optional, List

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ..Controleur import Controleur
    from ..Action.Action import Action
    from ..Labyrinthe.Structure_spatiale.Position import Position
    from ..Effet.Effet import Effet

# Pas de classe parente

# Valeurs par défaut des paramètres
from ..Labyrinthe.Structure_spatiale.Position import ABSENT

class Entitee:
    """La classe des entitées"""
    def __init__(self,controleur:Controleur, position: Position=ABSENT, ID: Optional[int]=None):
        self.position:Position = position
        self.priorite:float = 0
        self.effets:List[Effet] = []
        self.controleur = controleur
        if ID is None:
            self.ID = ID_MAX.incremente()
        else:
            self.ID = ID

    def set_position(self,position: Position):
        self.position = position

    def ajoute_effet(self,effet: Effet):
        self.effets.append(effet)

    def get_position(self):
        return self.position
    
    def get_priorite(self):
        return self.priorite

    def get_direction(self):
        return DIRECTIONS[0]

    def get_description(self,observation=0):
        return ["Une entitee","N'aurait pas dû être instanciée.","Probablement une erreur..."]

    def get_skin(self):
        return SKIN_MYSTERE

class Entitee_superieure(Entitee):
    """La classe des entitées qui font bouger le labyrinthe autour d'eux."""
    pass

class Fantome(Entitee):
    """La classe des entitées qui traversent les murs."""
    pass

class Interactif(Entitee):
    """La classe des entitées avec lesquelles on peut interagir. Les humains, principalement, et quelques éléments de décors."""
    pass

class Non_superposable(Entitee):
    """La classe des entitées qui 'occupent' une place, donc qu'on ne peut pas superposer (aux fantômes près)."""
    pass

class Mobile(Entitee):
    """La classe des entitées qui peuvent se déplacer (par elles-mêmes pour les agissants, en étant lancées pour les items)."""
    def __init__(self):
        self.action:Optional[Action] = None

    def add_latence(self,latence: float):
        if self.action is not None:
            self.action.latence += latence

    def set_latence(self,latence: float):
        if self.action is not None:
            self.action.latence = latence

# Imports utilisés dans le code
from ..Labyrinthe.Structure_spatiale.Direction import DIRECTIONS
from ..Constantes import ID_MAX
from Old_Affichage.Skins.Skins import SKIN_MYSTERE