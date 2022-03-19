from Jeu.Skins.Skins import *
from Jeu.Entitee.Agissant.Agissant import *
from Jeu.Entitee.Agissant.Role.Roles import *

class Gobelin(Dps):
    """Le monstre de base. Faible, souvent en groupe."""
    def __init__(self,controleur,position,niveau):
        Agissant.__init__(self,controleur,position,"gobelin",niveau)

    def get_offenses(self):
        offenses = self.offenses
        self.offenses = []
        if self.etat != "vivant" or self.controleur == None:
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
        return [f"Un gobelin (niveau {self.niveau})",f"ID : {self.ID}","Stats :",f"{self.pv}/{self.pv_max} PV",f"{self.pm}/{self.pm_max} PM",self.statut,"Les gobelins sont des monstres humanoïdes verts de petite taille. Généralement faibles, on les rencontre souvent en compagnie d'autres gobelins. Attention au nombre, et à leurs congénères plus spécialisés."]

    #Est-ce qu'il a besoin d'une méthode spécifique ? Pour les offenses peut-être ?