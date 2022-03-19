from Jeu.Entitee.Agissant.Role.Renforceur import *

class Multi_renforceur(Renforceur):
    """Les agissants qui peuvent booster plusieurs alliés à la fois."""

    def agit_en_vue(self,esprit,defaut = ""):
        cibles = []
        importance = 0
        #On cherche des alliés à booster
        for ID in esprit.corps.keys():
            agissant = self.controleur.get_entitee(ID)
            if agissant.statut == "attaque":
                new_importance = esprit.get_importance(agissant.get_impact())
                if new_importance > importance:
                    cibles.insert(0,ID)
                    importance = new_importance
                else:
                    cibles.append(ID)
        skill = trouve_skill(self.classe_principale,Skill_magie)
        if len(cibles) == 1:
            if self.peut_payer(cout_pm_boost[skill.niveau-1]):
                self.skill_courant = Skill_magie
                self.magie_courante = "magie boost"
                self.cible_magie = cibles[0]
                agissant = self.controleur.get_entitee(cibles[0])
                agissant.statut = "attaque boostée"
                defaut = "soutien"
                self.statut = "soutien"
        elif cibles != []:
            if self.peut_payer(cout_pm_multi_boost[skill.niveau-1]):
                self.skill_courant = Skill_magie
                self.magie_courante = "magie multi boost"
                self.cible_magie = cibles
                for ID in cibles:
                    agissant = self.controleur.get_entitee(ID)
                    agissant.statut = "attaque boostée"
                defaut = "soutien"
                self.statut = "soutien"
            elif self.peut_payer(cout_pm_boost[skill.niveau-1]):
                self.skill_courant = Skill_magie
                self.magie_courante = "magie boost"
                self.cible_magie = cibles[0]
                agissant = self.controleur.get_entitee(cibles[0])
                agissant.statut = "attaque boostée"
                defaut = "soutien"
                self.statut = "soutien"
        return defaut
