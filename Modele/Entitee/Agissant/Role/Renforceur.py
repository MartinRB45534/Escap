from __future__ import annotations
from typing import TYPE_CHECKING, List, Tuple

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ..Entitee.Agissant.Agissant import Agissant

# Imports des classes parentes
from ..Entitee.Agissant.Role.Mage import Mage

class Renforceur(Mage):
    """Les agissants qui boostent les attaques de leurs alliés."""

    def agit_en_vue(self,defaut = ""):
        cibles: List[Tuple[float,Agissant]] = []
        for corp in self.esprit.corps:
            if corp.statut == "attaque":
                cibles.append((self.esprit.get_importance(corp.get_impact()),corp))
        if cibles and self.peut_caster():
            new_cibles = sorted(cibles, key=itemgetter(0))
            skill = self.get_skill_magique()
            action = skill.fait(self,self.caste())
            assert isinstance(action,Cible_agissant)
            action.cible = new_cibles[-1][-1]
            self.fait(action)
            action.cible.set_statut("attaque boostée")
            defaut = "soutien"
            self.set_statut("soutien")
        return defaut

# Imports utilisés dans le code
from ..Action.Magie.Magie import Cible_agissant
from operator import itemgetter