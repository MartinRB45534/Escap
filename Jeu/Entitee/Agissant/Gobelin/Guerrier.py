from Jeu.Entitee.Agissant.Gobelin.Gobelin import *

class Guerrier_gobelin(Gobelin):
    """Un gobelin agressif est avide de sang.
       Il a une meilleure attaque que les gobelins de base."""
    def __init__(self,controleur,position,niveau):
        Agissant.__init__(self,controleur,position,"guerrier_gobelin",niveau)

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

    def get_texte_descriptif(self):
        return [f"Un guerrier gobelin (niveau {self.niveau})",f"ID : {self.ID}","Stats :",f"{self.pv}/{self.pv_max} PV",f"{self.pm}/{self.pm_max} PM",self.statut,"Le guerrier gobelin brandit un large cimeterre qui inflige de gros dégats. Son armure, en revanche, est presque décorative. Il parcourt le labyrinthe à la recherche de sa prochaine proie, ne laissez pas vos alliés sans surveillance !"]
