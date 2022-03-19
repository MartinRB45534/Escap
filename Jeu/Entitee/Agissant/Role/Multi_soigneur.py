from Jeu.Entitee.Agissant.Agissant import *
from Jeu.Systeme.Constantes_magies.Magies import *

class Multi_soigneur(Agissant):
    """Les soigneurs capables de soigner plusieurs agissants à la fois.""" #/!\Est-ce qu'on veut aussi en faire une pour le soin supérieur ou seul le joueur peut l'obtenir ?

    def agit_en_vue(self,esprit,defaut = ""):
        cibles = []
        for ID in esprit.corps.keys():
            corp = self.controleur.get_entitee(ID)
            if corp.etat == "vivant" and corp.pv < corp.pv_max:
                cibles.append(ID)
        skill = trouve_skill(self.classe_principale,Skill_magie)
        if len(cibles) == 1:
            if self.peut_payer(cout_pm_soin[skill.niveau-1]):#/!\ J'utilise le fait que le soin et l'auto soin aient le même coût !
                self.skill_courant = Skill_magie
                self.cible_magie = cibles[0]
                defaut = "soin"
                self.statut = "soin"
                if cibles[0] == self.ID:
                    self.magie_courante = "magie auto soin"
                else:
                    self.magie_courante = "magie soin"
        elif cibles != []:
            if self.peut_payer(cout_pm_multi_soin[skill.niveau-1]):
                self.skill_courant = Skill_magie
                self.magie_courante = "magie multi soin"
                self.cible_magie = cibles
                defaut = "soin"
                self.statut = "soin"
            elif self.peut_payer(cout_pm_soin[skill.niveau-1]):#/!\ J'utilise le fait que le soin et l'auto soin aient le même coût !
                self.skill_courant = Skill_magie
                self.cible_magie = cibles[0]
                defaut = "soin"
                self.statut = "soin"
                if cibles[0] == self.ID:
                    self.magie_courante = "magie auto soin"
                else:
                    self.magie_courante = "magie soin"
        return defaut
