from __future__ import annotations
from typing import TYPE_CHECKING

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from Jeu.Controleur import Controleur
    from Jeu.Labyrinthe.Structure_spatiale.Position import Position

# Imports des classes parentes
from Jeu.Entitee.Agissant.Gobelin.Base_gobelin import Base_gobelin
from Jeu.Entitee.Agissant.Role.Fuyard import Fuyard

# Valeurs par défaut des paramètres
from Jeu.Labyrinthe.Structure_spatiale.Position import ABSENT

class Guerrier_gobelin(Base_gobelin):
    """Un gobelin agressif est avide de sang.
       Il a une meilleure attaque que les gobelins de base."""
    def __init__(self,controleur:Controleur,niveau:int,position:Position=ABSENT):
        Base_gobelin.__init__(self,controleur,"guerrier_gobelin",niveau,position)

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

    def get_texte_descriptif(self):
        return [f"Un guerrier gobelin (niveau {self.niveau})",f"ID : {self.ID}","Stats :",f"{self.pv}/{self.pv_max} PV",f"{self.pm}/{self.pm_max} PM",self.statut,"Le guerrier gobelin brandit un large cimeterre qui inflige de gros dégats. Son armure, en revanche, est presque décorative. Il parcourt le labyrinthe à la recherche de sa prochaine proie, ne laissez pas vos alliés sans surveillance !"]
