from __future__ import annotations
from typing import TYPE_CHECKING, List,Tuple

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ..agissant import Agissant

# Imports des classes parentes
from .soigneur import Soigneur
from .mage import Multi_mage

class Multi_soigneur(Soigneur,Multi_mage):
    """Les soigneurs capables de soigner plusieurs agissants à la fois."""

    def agit_en_vue(self,defaut:str = ""):
        cibles:List[Tuple[float,Agissant]] = []
        skill = type(self.get_skill_magique())
        for corp in self.esprit.corps:
            if corp.etat == EtatsAgissants.VIVANT and corp.statistiques.pv < corp.statistiques.pv_max:
                cibles.append((corp.statistiques.pv,corp))
        if len(cibles) == 1:
            if self.peut_caster():
                new_cibles = sorted(cibles, key=itemgetter(0))
                skill = self.get_skill_magique()
                action = skill.fait(self,self.caste())
                assert isinstance(action,Cible_agissant)
                action.cible = new_cibles[0][-1]
                self.fait(action)
                defaut = "soin"
        elif cibles:
            if self.peut_multi_caster():
                skill = self.get_skill_magique()
                action = skill.fait(self,self.multi_caste())
                assert isinstance(action,Cible_agissants)
                action.cible = [cible[-1] for cible in cibles]
                self.fait(action)
                defaut = "soin"
            elif self.peut_caster():
                new_cibles = sorted(cibles, key=itemgetter(0))
                skill = self.get_skill_magique()
                action = skill.fait(self,self.caste())
                assert isinstance(action,Cible_agissant)
                action.cible = new_cibles[0][-1]
                self.fait(action)
                defaut = "soin"
        return defaut

# Imports utilisés dans le code
from operator import itemgetter
from ....effet.action.magie.magie import Cible_agissant,Cible_agissants
from ..etats import EtatsAgissants