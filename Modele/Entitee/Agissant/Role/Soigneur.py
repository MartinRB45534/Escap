from __future__ import annotations
from typing import TYPE_CHECKING, List, Tuple

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ..Agissant import Agissant

# Imports des classes parentes
from .Mage import Mage

class Soigneur(Mage):
    """Les agissants capables de soigner les autres."""

    def agit_en_vue(self,defaut:str = ""):
        cibles:List[Tuple[float,Agissant]] = []
        skill = type(self.get_skill_magique())
        for corp in self.esprit.corps:
            if corp.etat == Etats_agissants.VIVANT and corp.statistiques.pv < corp.statistiques.pv_max:
                cibles.append((corp.statistiques.pv,corp))
        if cibles and self.peut_caster():
            new_cibles = sorted(cibles, key=itemgetter(0))
            skill = self.get_skill_magique()
            action = skill.fait(self,self.caste())
            assert isinstance(action,Cible_agissant)
            action.cible = new_cibles[0][-1]
            self.fait(action)
            defaut = "soin"
        return defaut

# Imports utilisés dans le code
from ..Agissant import Agissant
from ..Etats import Etats_agissants
from ....Action.Magie.Magie import Cible_agissant
from operator import itemgetter