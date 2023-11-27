from __future__ import annotations
from typing import TYPE_CHECKING

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ..agissant import Agissant

# Imports des classes parentes
from .renforceur import Renforceur
from .mage import Multi_mage

class Multi_renforceur(Renforceur,Multi_mage):
    """Les agissants qui peuvent booster plusieurs alliés à la fois."""

    def agit_en_vue(self,defaut:str = ""):
        cibles:list[tuple[float,Agissant]] = []
        skill = type(self.get_skill_magique())
        for corp in self.esprit.corps:
            if corp.statut == "attaque":
                cibles.append((self.esprit.get_importance(corp.get_impact()),corp))
        if len(cibles) == 1:
            if self.peut_caster():
                skill = self.get_skill_magique()
                action = skill.fait(self,self.caste())
                assert isinstance(action,CibleAgissant)
                action.cible = cibles[0][-1]
                self.fait(action)
                defaut = "soutien"
        elif cibles:
            if self.peut_multi_caster():
                skill = self.get_skill_magique()
                action = skill.fait(self,self.multi_caste())
                assert isinstance(action,CibleAgissants)
                action.cible = [cible[-1] for cible in cibles]
                self.fait(action)
                defaut = "soutien"
            elif self.peut_caster():
                new_cibles = sorted(cibles, key=itemgetter(0))
                skill = self.get_skill_magique()
                action = skill.fait(self,self.caste())
                assert isinstance(action,CibleAgissant)
                action.cible = new_cibles[0][-1]
                self.fait(action)
                defaut = "soutien"
        return defaut

# Imports utilisés dans le code
from ....action.magie.magie import CibleAgissant,CibleAgissants
from operator import itemgetter