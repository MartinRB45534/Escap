from __future__ import annotations
from typing import TYPE_CHECKING

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from Old_Jeu.Controleur import Controleur
    from Old_Jeu.Labyrinthe.Structure_spatiale.Position import Position

# Imports des classes parentes
from Old_Jeu.Entitee.Item.Equippement.Haume.Haume import Haume
from Old_Jeu.Entitee.Item.Equippement.Role.Defensif.Defensifs import Defensif_proportion

# Valeurs par défaut des paramètres
from Old_Jeu.Labyrinthe.Structure_spatiale.Position import ABSENT

class Haume_type(Haume,Defensif_proportion):
    """Un haume type : défend contre les attaques."""
    def __init__(self,controleur:Controleur,taux_degats:float,position:Position=ABSENT):
        Haume.__init__(self,controleur,position)
        Defensif_proportion.__init__(self,taux_degats)
