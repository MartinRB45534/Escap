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
        for ID in esprit.corps.keys():
            corp = self.controleur[ID]
            if corp.statut == "attaque":
                cibles.append([esprit.get_importance(corp.get_impact()),ID])
        if len(cibles) == 1:
            if self.peut_caster():
                self.skill_courant = skill
                self.magie_courante = self.caste()
                self.cible_magie = cibles[0][-1]
                agissant = self.controleur[cibles[0][-1]]
                agissant.statut = "attaque boostée"
                defaut = "soutien"
                self.statut = "soutien"
        elif cibles != []:
            if self.peut_multi_caster():
                self.skill_courant = skill
                self.magie_courante = self.multi_caste()
                self.cible_magie = [cible[-1] for cible in cibles]
                for cible in cibles:
                    agissant = self.controleur[cible[-1]]
                    agissant.statut = "attaque boostée"
                defaut = "soutien"
                self.statut = "soutien"
            elif self.peut_caster():
                new_cibles = sorted(cibles, key=itemgetter(0))
                self.skill_courant = skill
                self.magie_courante = self.caste()
                self.cible_magie = new_cibles[0][-1]
                agissant = self.controleur[new_cibles[0][-1]]
                agissant.statut = "attaque boostée"
                defaut = "soutien"
                self.statut = "soutien"
        return defaut
