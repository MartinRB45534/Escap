from __future__ import annotations
from typing import TYPE_CHECKING

# Pas d'imports pour les annotations

# Imports des classes parentes
from Jeu.Entitee.Agissant.Role.Multi_soigneur import Multi_soigneur

class Multi_soigneur_protecteur(Multi_soigneur):
    """Les multi_soigneurs capables de placer un sort de protection lorsqu'il n'y a personne à soigner.""" #Vraiment juste la peste (en fait même pas la peste)

    def agit_en_vue(self,defaut = ""):
        cibles = []
        for corp in self.esprit.corps:
            if corp.etat == "vivant" and corp.pv < corp.pv_max:
                cibles.append([corp.pv,corp])
        if len(cibles) == 1:
            if self.peut_caster():
                self.utilise(Skill_magie)
                self.set_magie_courante(self.caste())
                self.cible_magie = cibles[0]
                defaut = "soin"
                self.set_statut("soin")
        elif cibles != []:
            if self.peut_multi_caster():
                self.utilise(Skill_magie)
                self.set_magie_courante(self.multi_caste())
                self.cible_magie = cibles
                defaut = "soin"
                self.set_statut("soin")
            elif self.peut_caster():
                new_cibles = sorted(cibles, key=itemgetter(0))
                self.utilise(Skill_magie)
                self.set_magie_courante(self.caste())
                self.cible_magie = new_cibles[0][-1]
                defaut = "soin"
                self.set_statut("soin")
        elif self.pm == self.pm_max: #On ne l'utilise que rarement... parce qu'il est cher
            for corp in self.esprit.corps:
                if corp.etat == "vivant":
                    libre = True
                    for effet in corp.effets:
                        if isinstance(effet,Protection_sacree): #On ne peut pas avoir deux protections sacrées en même temps
                            libre = False
                    if libre:
                        cibles.append(corp)
            if cibles != []:
                self.utilise(Skill_magie)
                self.set_magie_courante("magie protection sacrée")
                self.cible_magie = cibles
                defaut = "soin"
                self.set_statut("soin")
        return defaut

# Imports utilisés dans le code
from Jeu.Effet.Effets_protection import Protection_sacree
from Jeu.Systeme.Classe import Skill_magie
from operator import itemgetter