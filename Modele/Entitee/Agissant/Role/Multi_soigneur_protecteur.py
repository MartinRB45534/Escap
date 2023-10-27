from __future__ import annotations
from typing import TYPE_CHECKING, List, Tuple

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ..agissant import Agissant

# Imports des classes parentes
from .multi_soigneur import Multi_soigneur

class Multi_soigneur_protecteur(Multi_soigneur):
    """Les multi_soigneurs capables de placer un sort de protection lorsqu'il n'y a personne à soigner.""" #Vraiment juste la peste (en fait même pas la peste)

    def agit_en_vue(self,defaut:str = ""):
        cibles:List[Tuple[float,Agissant]] = []
        for corp in self.esprit.corps:
            if corp.etat == EtatsAgissants.VIVANT and corp.statistiques.pv < corp.statistiques.pv_max:
                cibles.append((corp.statistiques.pv,corp))
        if len(cibles) == 1:
            if self.peut_caster():
                skill = self.get_skill_magique()
                action = skill.fait(self,self.caste())
                assert isinstance(action,CibleAgissant)
                action.cible = cibles[0][-1]
                self.fait(action)
                defaut = "soin"
        elif cibles:
            if self.peut_multi_caster():
                skill = self.get_skill_magique()
                action = skill.fait(self,self.multi_caste())
                assert isinstance(action,CibleAgissants)
                action.cible = [cible[-1] for cible in cibles]
                self.fait(action)
                defaut = "soin"
            elif self.peut_caster():
                new_cibles = sorted(cibles, key=itemgetter(0))
                skill = self.get_skill_magique()
                action = skill.fait(self,self.caste())
                assert isinstance(action,CibleAgissant)
                action.cible = new_cibles[0][-1]
                self.fait(action)
                defaut = "soin"
        elif self.pm == self.statistiques.pm_max: #On ne l'utilise que rarement... parce qu'il est cher
            cibles_:List[Agissant] = []
            for corp in self.esprit.corps:
                if corp.etat == EtatsAgissants.VIVANT:
                    libre = True
                    for effet in corp.effets:
                        if isinstance(effet,ProtectionSacree): #On ne peut pas avoir deux protections sacrées en même temps
                            libre = False
                    if libre:
                        cibles_.append(corp)
            if cibles_:
                skill = self.get_skill_magique()
                action = skill.fait(self,"magie protection sacrée")
                assert isinstance(action,CibleAgissants)
                action.cible = cibles_
                self.fait(action)
                defaut = "soin"
        return defaut

# Imports utilisés dans le code
from ....effet.agissant.protection import ProtectionSacree
from ....action.magie.magie import CibleAgissant,CibleAgissants
from ....commons.etats_agissant import EtatsAgissants
from operator import itemgetter