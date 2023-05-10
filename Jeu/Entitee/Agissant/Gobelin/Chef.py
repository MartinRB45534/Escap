from Jeu.Entitee.Agissant.Gobelin.Gobelin import *

class Chef_gobelin(Gobelin):
    """Un gobelin qui dirige un groupe.
       Bonnes stats, augmente l'efficacité de l'esprit."""
    def __init__(self,controleur,position,niveau:int):
        Agissant.__init__(self,controleur,position,"chef_gobelin",niveau)

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
        return [f"Un chef gobelin (niveau {self.niveau})",f"ID : {self.ID}","Stats :",f"{self.pv}/{self.pv_max} PV",f"{self.pm}/{self.pm_max} PM",self.statut,"Les gobelins forment une société organisée, dirigée par un chef. Ce dernier doit se remarquer par sa force, pourtant il ne se sépare presque jamais de sa garde rapprochée..."]
