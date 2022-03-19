from Jeu.Entitee.Agissant.Role.Mage import *
from Jeu.Systeme.Constantes_magies.Magies import *

class Renforceur(Mage):
    """Les agissants qui boostent les attaques de leurs alliés."""

    def agit_en_vue(self,esprit,defaut = ""):
        cible = None
        importance = 0
        #On cherche des alliés à booster
        for ID in esprit.corps.keys():
            agissant = self.controleur.get_entitee(ID)
            if agissant.statut == "attaque":
                new_importance = esprit.get_importance(agissant.get_impact())
                if new_importance > importance:
                    cible = ID
                    importance = new_importance
        skill = trouve_skill(self.classe_principale,Skill_magie)
        if cible != None and self.peut_payer(cout_pm_boost[skill.niveau-1]):
            self.skill_courant = Skill_magie
            self.magie_courante = "magie boost"
            self.cible_magie = cible
            agissant = self.controleur.get_entitee(cible)
            agissant.statut = "attaque boostée"
            defaut = "soutien"
            self.statut = "soutien"
        return defaut
