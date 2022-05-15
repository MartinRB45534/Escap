from operator import itemgetter
from Jeu.Entitee.Agissant.Agissant import *
from Jeu.Systeme.Constantes_magies.Magies import *
from Jeu.Effet.Magie.Magies import *

class Multi_soigneur_protecteur(Agissant):
    """Les multi_soigneurs capables de placer un sort de protection lorsqu'il n'y a personne à soigner.""" #Vraiment juste la peste (en fait même pas la peste)

    def agit_en_vue(self,esprit,defaut = ""):
        cibles = []
        for ID in esprit.corps.keys():
            corp = self.controleur[ID]
            if corp.etat == "vivant" and corp.pv < corp.pv_max:
                cibles.append([corp.pv,ID])
        if len(cibles) == 1:
            if self.peut_caster():
                self.skill_courant = Skill_magie
                self.magie_courante = self.caste()
                self.cible_magie = cibles[0]
                defaut = "soin"
                self.statut = "soin"
        elif cibles != []:
            if self.peut_multi_caster():
                self.skill_courant = Skill_magie
                self.magie_courante = self.multi_caste()
                self.cible_magie = cibles
                defaut = "soin"
                self.statut = "soin"
            elif self.peut_caster():
                new_cibles = sorted(cibles, key=itemgetter(0))
                self.skill_courant = Skill_magie
                self.magie_courante = self.caste()
                self.cible_magie = new_cibles[0][-1]
                defaut = "soin"
                self.statut = "soin"
        elif self.pm == self.pm_max: #On ne l'utilise que rarement... parce qu'il est cher
            for ID in esprit.corps.keys():
                corp = self.controleur[ID]
                if corp.etat == "vivant":
                    libre = True
                    for effet in corp.effets:
                        if isinstance(effet,Protection_sacree): #On ne peut pas avoir deux protections sacrées en même temps
                            libre = False
                    if libre:
                        cibles.append(ID)
            if cibles != []:
                self.skill_courant = Skill_magie
                self.magie_courante = "magie protection sacrée"
                self.cible_magie = cibles
                defaut = "soin"
                self.statut = "soin"
        return defaut
