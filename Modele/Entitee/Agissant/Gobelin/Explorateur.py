from __future__ import annotations
from typing import TYPE_CHECKING

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from Old_Jeu.Controleur import Controleur
    from Old_Jeu.Labyrinthe.Structure_spatiale.Position import Position

# Imports des classes parentes
from Old_Jeu.Entitee.Agissant.Gobelin.Base_gobelin import Base_gobelin
from Old_Jeu.Entitee.Agissant.Role.Fuyard import Fuyard

# Valeurs par défaut des paramètres
from Old_Jeu.Labyrinthe.Structure_spatiale.Position import ABSENT

class Explorateur_gobelin(Fuyard,Base_gobelin):
    """Un gobelin rapide et trop curieux.
       Il a une meilleure vitesse que les gobelins de base, qui l'avantage aussi en combat."""
    def __init__(self,controleur:Controleur,niveau:int,position:Position=ABSENT):
        Base_gobelin.__init__(self,controleur,"explorateur_gobelin",niveau,position)

    def get_offenses(self):
        offenses = self.offenses
        self.offenses = []
        if self.etat != "vivant" or self.controleur is None:
            etat = "incapacite"
        elif self.pv <= self.pv_max//2:
            etat = "fuite"
        else:
            etat = "attaque"
        return offenses, etat
