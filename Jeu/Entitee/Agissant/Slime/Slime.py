from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Type, List, Tuple, Dict

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from Jeu.Controleur import Controleur
    from Jeu.Labyrinthe.Structure_spatiale.Position import Position

# Imports des classes parentes
from Jeu.Entitee.Agissant.Role.Dps import Dps

# Valeurs par défaut des paramètres
from Jeu.Labyrinthe.Structure_spatiale.Position import ABSENT

class Slime(Dps):
    """Un tas de gelée. Faible, tant qu'il est tout seul et de bas niveau..."""
    def __init__(self,controleur:Controleur,niveau:int,position:Position=ABSENT):
        Agissant.__init__(self,controleur,"slime",niveau,position)

    def get_offenses(self):
        offenses = self.offenses
        self.offenses = []
        if self.etat != "vivant" or self.controleur is None:
            etat = "incapacite"
        elif self.pv <= self.pv_max//9:
            etat = "fuite"
        else:
            etat = "attaque"
        return offenses, etat

    def get_skin(self):
        if self.etat == "vivant":
            return SKIN_VIDE
        else:
            return SKIN_CADAVRE

    def get_skin_tete(self):
        return SKIN_SLIME

    def get_texte_descriptif(self):
        return [f"Un slime (niveau {self.niveau})",f"ID : {self.ID}","Stats :",f"{self.pv}/{self.pv_max} PV",f"{self.pm}/{self.pm_max} PM",self.statut,"'Il faut tuer le slime lorsqu'il est frais !' diront les connaisseurs. Le slime peut se démultiplier, s'unifier à d'autres slimes, et absorbe les cadavres pour s'approprier leurs capacités. Il est aussi capable de se remettre de ses blessures en un temps record."]

# Imports utilisés dans le code
from Jeu.Entitee.Agissant.Agissant import Agissant
from Affichage.Skins.Skins import SKIN_VIDE, SKIN_SLIME, SKIN_CADAVRE