from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Jeu.Esprit.Esprit import Esprit

from operator import itemgetter
from Jeu.Entitee.Agissant.Role.Mage import *

class Attaquant_magique_agissant(Mage):
    """Les agissants qui combattent en lançant des attaques magiques de loin sur des agissants."""

    def agit_en_vue(self,defaut = ""):
        cibles = []
        #On cherche l'ennemi le plus puissant en vue
        for case in self.vue:
            if case.agissant is not None and case.agissant in self.esprit.ennemis:
                    cibles.append([self.esprit.ennemis[case.agissant]["importance"],case.agissant])
        if cibles != [] and self.peut_caster():
            new_cibles = sorted(cibles, key=itemgetter(0))
            self.utilise(Skill_magie)
            self.set_magie_courante(self.caste())
            self.cible_magie = new_cibles[-1][-1]
            defaut = "attaque"
            self.set_statut("attaque")
        return defaut

    def get_impact(self):
        if isinstance(self.cible_magie,Agissant):
            return self.cible_magie.position
        else:
            return Agissant.get_impact(self)
