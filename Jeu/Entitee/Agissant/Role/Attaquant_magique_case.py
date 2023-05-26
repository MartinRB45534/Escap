from __future__ import annotations

# Pas d'imports pour les annotations

# Imports des classes parentes
from Jeu.Entitee.Agissant.Role.Mage import Mage

class Attaquant_magique_case(Mage):
    """Les agissants qui combattent en lançant des attaques magiques de loin sur des cases."""

    def agit_en_vue(self,defaut = ""):
        cibles = []
        #On cherche l'ennemi le plus puissant en vue
        for case in self.vue:
            if case.agissant is not None and case.agissant in self.esprit.ennemis:
                    cibles.append([self.esprit.ennemis[case.agissant]["importance"],case.case.position])
        if cibles and self.peut_caster():
            new_cibles = sorted(cibles, key=itemgetter(0))
            skill = self.get_skill_magique()
            action = skill.fait(self.caste(),self)
            assert isinstance(action,Cible_case)
            action.cible = new_cibles[-1][-1]
            self.fait(action)
            defaut = "attaque"
            self.set_statut("attaque")
        return defaut

    def get_impact(self):
        if isinstance(self.action,Cible_case) and self.action.cible is not None:
            return self.action.cible
        else:
            return super().get_impact()

# Imports utilisés dans le code
from Jeu.Entitee.Agissant.Agissant import Agissant
from Jeu.Action.Magie.Magie import Cible_case
from operator import itemgetter