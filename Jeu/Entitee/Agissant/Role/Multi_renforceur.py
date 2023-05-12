from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Jeu.Esprit.Esprit import Esprit

from operator import itemgetter
from Jeu.Entitee.Agissant.Role.Renforceur import *

class Multi_renforceur(Renforceur,Multi_mage):
    """Les agissants qui peuvent booster plusieurs alliés à la fois."""

    def agit_en_vue(self,esprit:Esprit,defaut = ""):
        cibles = []
        skill = type(self.get_skill_magique())
        for corp in esprit.corps:
            if corp.statut == "attaque":
                cibles.append([esprit.get_importance(corp.get_impact()),corp])
        if len(cibles) == 1:
            if self.peut_caster():
                self.utilise(skill)
                self.set_magie_courante(self.caste())
                self.cible_magie = cibles[0][-1]
                self.cible_magie.set_statut("attaque boostée")
                defaut = "soutien"
                self.set_statut("soutien")
        elif cibles != []:
            if self.peut_multi_caster():
                self.utilise(skill)
                self.set_magie_courante(self.multi_caste())
                self.cible_magie = [cible[-1] for cible in cibles]
                for cible in cibles:
                    cible[-1].set_statut("attaque boostée")
                defaut = "soutien"
                self.set_statut("soutien")
            elif self.peut_caster():
                new_cibles = sorted(cibles, key=itemgetter(0))
                self.utilise(skill)
                self.set_magie_courante(self.caste())
                self.cible_magie = new_cibles[0][-1]
                self.cible_magie.set_statut("attaque boostée")
                defaut = "soutien"
                self.set_statut("soutien")
        return defaut
