from Jeu.Skins.Skins import *
from Jeu.Entitees.Agissant.Agissant import *
from Jeu.Entitees.Agissant.Role.Roles import *

class Ombriul(Dps):
    """Une créature des ténèbres, non-endémique du labyrinthe."""
    def __init__(self,controleur,position,niveau):
        Agissant.__init__(self,controleur,position,"ombriul",niveau)

    def get_offenses(self):
        offenses = self.offenses
        self.offenses = []
        if self.etat != "vivant" or self.controleur == None:
            etat = "incapacite"
        elif self.pv <= self.pv_max//6:
            etat = "fuite"
        else:
            etat = "attaque"
        return offenses, etat

    def attaque(self,direction):
        skill = trouve_skill(self.classe_principale,Skill_magie) #Est-ce qu'il a le même Skill_magie que le joueur ?
        self.dir_regard = direction
        if self.peut_payer(cout_pm_poing_magique[skill.niveau-1]): #Quelle est l'attaque magique des gobelins ?
            self.skill_courant = Skill_magie
            self.magie_courante = "magie poing sombre"
            self.dir_magie = direction
        else:
            self.skill_courant = Skill_stomp
        self.statut = "attaque"

    def get_skin(self):
        if self.etat == "vivant":
            return SKIN_CORPS_OMBRIUL
        else:
            return SKIN_CADAVRE

    def get_skin_tete(self):
        return SKIN_TETE_OMBRIUL

    def get_texte_descriptif(self):
        return [f"Un ombriul (niveau {self.niveau})",f"ID : {self.ID}","Stats :",f"{self.pv}/{self.pv_max} PV",f"{self.pm}/{self.pm_max} PM",self.statut,"Les ombriuls ne font pas partie des espèces endémiques au labyrinthe. Ils y prolifèrent depuis quelques temps grâce à l'ombre, qui est leur élément de prédilection."]
