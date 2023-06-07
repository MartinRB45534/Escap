from __future__ import annotations
from typing import TYPE_CHECKING

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ..Controleur import Controleur
    from ..Labyrinthe.Structure_spatiale.Position import Position

# Imports des classes parentes
from ..Entitee.Agissant.Gobelin.Base_gobelin import Base_gobelin
from ..Entitee.Agissant.Role.Dps import Dps

# Valeurs par défaut des paramètres
from ..Labyrinthe.Structure_spatiale.Position import ABSENT

class Gobelin(Base_gobelin,Dps):
    """Un gobelin qui dirige un groupe.
       Bonnes stats, augmente l'efficacité de l'esprit."""
    def __init__(self,controleur:Controleur,niveau:int,position:Position=ABSENT):
        Base_gobelin.__init__(self,controleur,"gobelin",niveau,position)

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
        return [f"Un gobelin (niveau {self.niveau})",f"ID : {self.ID}","Stats :",f"{self.pv}/{self.pv_max} PV",f"{self.pm}/{self.pm_max} PM",self.statut,"Les gobelins sont des monstres humanoïdes verts de petite taille. Généralement faibles, on les rencontre souvent en compagnie d'autres gobelins. Attention au nombre, et à leurs congénères plus spécialisés."]
