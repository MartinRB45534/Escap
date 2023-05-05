from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Jeu.Esprit.Esprit import Esprit

from operator import itemgetter
from Jeu.Entitee.Agissant.Role.Mage import *

class Attaquant_magique_case(Mage):
    """Les agissants qui combattent en lançant des attaques magiques de loin sur des cases."""

    def agit_en_vue(self,esprit:Esprit,defaut = ""):
        cibles = []
        #On cherche l'ennemi le plus puissant en vue
        for case in self.vue:
            for ID in case.entitees:
                if ID in esprit.ennemis.keys() and not self.controleur.est_item(ID):
                    cibles.append([esprit.ennemis[ID][0],case[0]])
        if cibles != [] and self.peut_caster():
            new_cibles = sorted(cibles, key=itemgetter(0))
            self.skill_courant = Skill_magie
            self.magie_courante = self.caste()
            self.cible_magie = new_cibles[-1][-1]
            defaut = "attaque"
            self.statut = "attaque"
        return defaut

    def get_impact(self):
        if self.cible_magie != None:
            return self.cible_magie
        else:
            return Agissant.get_impact(self)
