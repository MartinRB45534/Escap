from __future__ import annotations
from typing import TYPE_CHECKING

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ..agissant import Agissant

# Imports des classes parentes
from .mage import Mage

class Renforceur(Mage):
    """Les agissants qui boostent les attaques de leurs alliés."""

    def agit_en_vue(self,defaut:str = ""):
        cibles: list[tuple[float,Agissant]] = []
        for corp in self.esprit.corps:
            if corp.statut == "attaque":
                cibles.append((self.esprit.get_importance(corp.get_impact()),corp))
        if cibles and self.peut_caster():
            new_cibles = sorted(cibles, key=itemgetter(0))
            skill = self.get_skill_magique()
            action = skill.fait(self,self.caste())
            assert isinstance(action,CibleAgissant)
            action.cible = new_cibles[-1][-1]
            self.fait(action)
            defaut = "soutien"
        return defaut

# Imports utilisés dans le code
from ....action.magie.magie import CibleAgissant
from operator import itemgetter