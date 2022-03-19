from Jeu.Entitee.Agissant.Role.Mage import *
from Jeu.Systeme.Constantes_magies.Magies import *

class Soigneur(Mage):
    """Les agissants capables de soigner les autres."""

    def agit_en_vue(self,esprit,defaut = ""):
        cible = None
        pire = 1
        #On cherche des alliés à soigner
        for ID in esprit.corps.keys():
            corp = self.controleur.get_entitee(ID)
            if corp.etat == "vivant":
                rapport = corp.pv/corp.pv_max
                if rapport < pire:
                    cible = ID
                    pire = rapport
        skill = trouve_skill(self.classe_principale,Skill_magie)
        if cible != None and self.peut_payer(cout_pm_soin[skill.niveau-1]):#/!\ J'utilise le fait que le soin et l'auto soin aient le même coût !
            self.skill_courant = Skill_magie
            self.cible_magie = cible
            defaut = "soin"
            self.statut = "soin"
            if cible == self.ID:
                self.magie_courante = "magie auto soin"
            else:
                self.magie_courante = "magie soin"
        return defaut
