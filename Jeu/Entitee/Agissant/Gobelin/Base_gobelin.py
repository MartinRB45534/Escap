from __future__ import annotations
from typing import TYPE_CHECKING

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from Jeu.Controleur import Controleur
    from Jeu.Labyrinthe.Structure_spatiale.Position import Position

# Imports des classes parentes
from Jeu.Entitee.Agissant.Agissant import Agissant

# Valeurs par défaut des paramètres
from Jeu.Labyrinthe.Structure_spatiale.Position import ABSENT

class Base_gobelin(Agissant):
    """Le monstre de base. Faible, souvent en groupe."""
    def __init__(self,controleur:Controleur,identite:str,niveau:int,position:Position=ABSENT):
        Agissant.__init__(self,controleur,identite,niveau,position)

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

    def get_skin(self):
        if self.etat == "vivant":
            return SKIN_CORPS_GOBELIN
        else:
            return SKIN_CADAVRE

    def get_skin_tete(self):
        return SKIN_TETE_GOBELIN

    def get_texte_descriptif(self):
        return [f"Un gobelin (niveau {self.niveau})",f"ID : {self.ID}","Stats :",f"{self.pv}/{self.pv_max} PV",f"{self.pm}/{self.pm_max} PM",self.statut,"Ce gobelin là ne devrait pas exister..."]

    #Est-ce qu'il a besoin d'une méthode spécifique ? Pour les offenses peut-être ?

# Imports utilisés dans le code
from Jeu.Entitee.Agissant.Agissant import Agissant
from Affichage.Skins.Skins import SKIN_CORPS_GOBELIN, SKIN_TETE_GOBELIN, SKIN_CADAVRE