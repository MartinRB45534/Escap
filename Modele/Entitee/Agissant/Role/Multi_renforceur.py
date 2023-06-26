from __future__ import annotations
from typing import TYPE_CHECKING, List, Tuple

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ..Agissant import Agissant

# Imports des classes parentes
from .Renforceur import Renforceur
from .Mage import Multi_mage

class Multi_renforceur(Renforceur,Multi_mage):
    """Les agissants qui peuvent booster plusieurs alliés à la fois."""

    def agit_en_vue(self,defaut:str = ""):
        cibles:List[Tuple[float,Agissant]] = []
        skill = type(self.get_skill_magique())
        for corp in self.esprit.corps:
            if corp.statut == "attaque":
                cibles.append((self.esprit.get_importance(corp.get_impact()),corp))
        if len(cibles) == 1:
            if self.peut_caster():
                skill = self.get_skill_magique()
                action = skill.fait(self,self.caste())
                assert isinstance(action,Cible_agissant)
                action.cible = cibles[0][-1]
                self.fait(action)
                defaut = "soutien"
        elif cibles:
            if self.peut_multi_caster():
                skill = self.get_skill_magique()
                action = skill.fait(self,self.multi_caste())
                assert isinstance(action,Cible_agissants)
                action.cible = [cible[-1] for cible in cibles]
                self.fait(action)
                defaut = "soutien"
            elif self.peut_caster():
                new_cibles = sorted(cibles, key=itemgetter(0))
                skill = self.get_skill_magique()
                action = skill.fait(self,self.caste())
                assert isinstance(action,Cible_agissant)
                action.cible = new_cibles[0][-1]
                self.fait(action)
                defaut = "soutien"
        return defaut

# Imports utilisés dans le code
from ....Effet.Action.Magie.Magie import Cible_agissant,Cible_agissants
from operator import itemgetter