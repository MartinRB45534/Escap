from __future__ import annotations
from typing import List, Tuple
import Carte as crt

# Imports des classes parentes
from .Mage import Mage

class Attaquant_magique_case(Mage):
    """Les agissants qui combattent en lançant des attaques magiques de loin sur des cases."""

    def agit_en_vue(self,defaut:str = ""):
        cibles:List[Tuple[float,crt.Position]] = []
        #On cherche l'ennemi le plus puissant en vue
        for pos in self.vue:
            case = self.vue.get_case(pos)
            if case.agissant is not None and case.agissant.ID in [ennemi.ID for ennemi in self.esprit.ennemis]:
                    cibles.append((self.esprit.ennemis[case.agissant]["importance"],case.position))
        if cibles and self.peut_caster():
            new_cibles = sorted(cibles, key=itemgetter(0))
            skill = self.get_skill_magique()
            action = skill.fait(self,self.caste())
            assert isinstance(action,Cible_case)
            action.cible = new_cibles[-1][-1]
            self.fait(action)
            defaut = "attaque"
        return defaut

    def get_impact(self):
        if isinstance(self.action,Cible_case) and self.action.cible is not None:
            return self.action.cible
        else:
            return super().get_impact()

# Imports utilisés dans le code
from ....Action.Magie.Magie import Cible_case
from operator import itemgetter