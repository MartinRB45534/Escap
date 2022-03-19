from Jeu.Entitee.Agissant.Gobelin.Gobelin import *

class Explorateur_gobelin(Fuyard,Gobelin):
    """Un gobelin rapide et trop curieux.
       Il a une meilleure vitesse que les gobelins de base, qui l'avantage aussi en combat."""
    def __init__(self,controleur,position,niveau):
        Agissant.__init__(self,controleur,position,"explorateur_gobelin",niveau)

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
