from __future__ import annotations
from typing import TYPE_CHECKING

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from Jeu.Controleur import Controleur
    from Jeu.Labyrinthe.Structure_spatiale.Position import Position

# Imports des classes parentes
from Jeu.Entitee.Agissant.Gobelin.Base_gobelin import Base_gobelin

# Valeurs par défaut des paramètres
from Jeu.Labyrinthe.Structure_spatiale.Position import ABSENT

class Chef_gobelin(Base_gobelin):
    """Un gobelin qui dirige un groupe.
       Bonnes stats, augmente l'efficacité de l'esprit."""
    def __init__(self,controleur:Controleur,niveau:int,position:Position=ABSENT):
        Base_gobelin.__init__(self,controleur,"chef_gobelin",niveau,position)

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
        return [f"Un chef gobelin (niveau {self.niveau})",f"ID : {self}","Stats :",f"{self.pv}/{self.pv_max} PV",f"{self.pm}/{self.pm_max} PM",self.statut,"Les gobelins forment une société organisée, dirigée par un chef. Ce dernier doit se remarquer par sa force, pourtant il ne se sépare presque jamais de sa garde rapprochée..."]
