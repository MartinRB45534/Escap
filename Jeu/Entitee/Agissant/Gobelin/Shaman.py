from Jeu.Entitee.Agissant.Gobelin.Gobelin import *

class Shaman_gobelin(Renforceur,Support_lointain,Gobelin):
    """Un gobelin avec un potentiel magique.
       Il peut utiliser un sort de boost."""
    def __init__(self,controleur,position,niveau:int):
        Agissant.__init__(self,controleur,position,"shaman_gobelin",niveau)

    def peut_caster(self):
        return self.peut_payer(cout_pm_boost[trouve_skill(self.classe_principale,Skill_magie).niveau-1])

    def caste(self):
        return "magie boost"

    def boost(self,cible):
        self.skill_courant = Skill_magie
        self.magie_courante = "magie boost"
        self.cible_magie = cible

    def get_offenses(self):
        offenses = self.offenses
        self.offenses = []
        if self.etat != "vivant" or self.controleur == None:
            etat = "incapacite"
        elif self.pv <= 3*self.pv_max//4 or self.pm < 50:
            etat = "fuite"
        else:
            etat = "soutien"
        return offenses, etat

    def get_texte_descriptif(self):
        return [f"Un shaman gobelin (niveau {self.niveau})",f"ID : {self.ID}","Stats :",f"{self.pv}/{self.pv_max} PV",f"{self.pm}/{self.pm_max} PM",self.statut,"Caché à l'arrière, loin des combats, le shaman fourni pourtant aux autres gobelins un renforcement non négligeable. Essayez de le tuer en priorité !"]