from Jeu.Skins.Skins import *
from Jeu.Entitee.Agissant.Agissant import *
from Jeu.Entitee.Agissant.Role.Roles import *

class Slime(Dps):
    """Un tas de gelée. Faible, tant qu'il est tout seul et de bas niveau..."""
    def __init__(self,controleur,position,niveau):
        Agissant.__init__(self,controleur,position,"slime",niveau)

    def get_offenses(self):
        offenses = self.offenses
        self.offenses = []
        if self.etat != "vivant" or self.controleur == None:
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
