from Jeu.Entitee.Agissant.Agissant import *
from Jeu.Systeme.Constantes_magies.Magies import *
from Jeu.Effet.Magie.Magies import *

class Multi_soigneur_protecteur(Agissant):
    """Les multi_soigneurs capables de placer un sort de protection lorsqu'il n'y a personne à soigner.""" #Vraiment juste la peste

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
        elif self.pv == self.pv_max: #On ne l'utilise que rarement... parce qu'il est cher
            for ID in esprit.corps.keys():
                corp = self.controleur.get_entitee(ID)
                if corp.etat == "vivant":
                    libre = True
                    for effet in corp.effets:
                        if isinstance(effet,Protection_sacree): #On ne peut pas avoir deux protections sacrées en même temps
                            libre = False
                    if libre:
                        cibles.append(ID)
            if cibles != []:
                skill = trouve_skill(self.classe_principale,Skill_magie)
                self.skill_courant = Skill_magie
                self.magie_courante = "magie protection sacrée"
                self.cible_magie = cibles
                defaut = "soin"
                self.statut = "soin"
        return defaut
