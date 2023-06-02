from __future__ import annotations
from typing import TYPE_CHECKING

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from Jeu.Controleur import Controleur
    from Jeu.Labyrinthe.Structure_spatiale.Position import Position
    from Jeu.Labyrinthe.Structure_spatiale.Direction import Direction

# Imports des classes parentes
from Jeu.Entitee.Agissant.Role.Mage import Mage
from Jeu.Entitee.Agissant.Role.Attaquant_magique_poing import Attaquant_magique_poing
from Jeu.Entitee.Agissant.Role.Dps import Dps

# Valeurs par défaut des paramètres
from Jeu.Labyrinthe.Structure_spatiale.Position import ABSENT

class Ombriul(Dps,Attaquant_magique_poing): #/!\ Retravailler l'ombriul pour utiliser les rôles
    """Une créature des ténèbres, non-endémique du labyrinthe."""
    def __init__(self,controleur:Controleur,niveau:int,position:Position=ABSENT):
        Agissant.__init__(self,controleur,"ombriul",niveau,position)

    def get_offenses(self):
        offenses = self.offenses
        self.offenses = []
        if self.etat != "vivant" or self.controleur is None:
            etat = "incapacite"
        elif self.pv <= self.pv_max//6:
            etat = "fuite"
        else:
            etat = "attaque"
        return offenses, etat
    
    def peut_frapper(self):
        return self.peut_payer(cout_pm_poing_sombre[self.classe_principale.niveau-1])
    
    def frappe(self):
        return "magie poing sombre"

    def get_skin(self):
        if self.etat == "vivant":
            return SKIN_CORPS_OMBRIUL
        else:
            return SKIN_CADAVRE

    def get_skin_tete(self):
        return SKIN_TETE_OMBRIUL

    def get_texte_descriptif(self):
        return [f"Un ombriul (niveau {self.niveau})",f"ID : {self.ID}","Stats :",f"{self.pv}/{self.pv_max} PV",f"{self.pm}/{self.pm_max} PM",self.statut,"Les ombriuls ne font pas partie des espèces endémiques au labyrinthe. Ils y prolifèrent depuis quelques temps grâce à l'ombre, qui est leur élément de prédilection."]

# Imports utilisés dans le code
from Jeu.Entitee.Agissant.Agissant import Agissant
from Affichage.Skins.Skins import SKIN_CORPS_OMBRIUL, SKIN_TETE_OMBRIUL, SKIN_CADAVRE
from Jeu.Systeme.Constantes_magies.Magies import cout_pm_poing_sombre