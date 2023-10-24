from __future__ import annotations
from typing import TYPE_CHECKING, List, Tuple

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ..agissant import Agissant

# Imports des classes parentes
from .mage import Mage

class Attaquant_magique_agissant(Mage):
    """Les agissants qui combattent en lançant des attaques magiques de loin sur des agissants."""

    def agit_en_vue(self,defaut:str = ""):
        cibles:List[Tuple[float,Agissant]] = []
        #On cherche l'ennemi le plus puissant en vue
        for pos in self.vue:
            case = self.vue.get_case(pos)
            if case.agissant is not None and case.agissant.ID in [ennemi.ID for ennemi in self.esprit.ennemis]:
                cibles.append((self.esprit.ennemis[case.agissant]["importance"],case.agissant))
        if cibles and self.peut_caster():
            new_cibles = sorted(cibles, key=itemgetter(0))
            skill = self.get_skill_magique()
            action = skill.fait(self,self.caste())
            assert isinstance(action,Cible_agissant)
            action.cible = new_cibles[-1][-1]
            self.fait(action)
            defaut = "attaque"
        return defaut

    def get_impact(self):
        if isinstance(self.action,Cible_agissant) and self.action.cible is not None:
            return self.action.cible.position
        else:
            return super().get_impact()

# Imports utilisés dans le code
from ..agissant import Agissant
from ....effet.action.magie.magie import Cible_agissant
from operator import itemgetter