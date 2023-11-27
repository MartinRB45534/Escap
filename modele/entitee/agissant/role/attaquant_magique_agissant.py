from __future__ import annotations
from typing import TYPE_CHECKING

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ..agissant import Agissant

# Imports des classes parentes
from .mage import Mage

class Attaquant_magique_agissant(Mage):
    """Les agissants qui combattent en lançant des attaques magiques de loin sur des agissants."""

    def agit_en_vue(self,defaut:str = ""):
        cibles:list[tuple[float,Agissant]] = []
        #On cherche l'ennemi le plus puissant en vue
        for pos in self.vue:
            case = self.vue.get_case(pos)
            if case.agissant is not None and case.agissant.id in [ennemi.id for ennemi in self.esprit.ennemis]:
                cibles.append((self.esprit.ennemis[case.agissant]["importance"],case.agissant))
        if cibles and self.peut_caster():
            new_cibles = sorted(cibles, key=itemgetter(0))
            skill = self.get_skill_magique()
            action = skill.fait(self,self.caste())
            assert isinstance(action,CibleAgissant)
            action.cible = new_cibles[-1][-1]
            self.fait(action)
            defaut = "attaque"
        return defaut

    def get_impact(self):
        if isinstance(self.action,CibleAgissant) and self.action.cible:
            return self.action.cible.position
        else:
            return super().get_impact()

# Imports utilisés dans le code
from ..agissant import Agissant
from ....action.magie.magie import CibleAgissant
from operator import itemgetter