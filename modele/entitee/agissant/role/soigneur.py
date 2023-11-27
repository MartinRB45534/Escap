from __future__ import annotations
from typing import TYPE_CHECKING

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ..agissant import Agissant

# Imports des classes parentes
from .mage import Mage

class Soigneur(Mage):
    """Les agissants capables de soigner les autres."""

    def agit_en_vue(self,defaut:str = ""):
        cibles:list[tuple[float,Agissant]] = []
        skill = type(self.get_skill_magique())
        for corp in self.esprit.corps:
            if corp.etat == EtatsAgissants.VIVANT and corp.statistiques.pv < corp.statistiques.pv_max:
                cibles.append((corp.statistiques.pv,corp))
        if cibles and self.peut_caster():
            new_cibles = sorted(cibles, key=itemgetter(0))
            skill = self.get_skill_magique()
            action = skill.fait(self,self.caste())
            assert isinstance(action,CibleAgissant)
            action.cible = new_cibles[0][-1]
            self.fait(action)
            defaut = "soin"
        return defaut

# Imports utilisés dans le code
from ..agissant import Agissant
from ....commons.etats_agissant import EtatsAgissants
from ....action.magie.magie import CibleAgissant
from operator import itemgetter