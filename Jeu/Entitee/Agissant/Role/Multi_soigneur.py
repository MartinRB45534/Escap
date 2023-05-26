from __future__ import annotations
from typing import TYPE_CHECKING

# Pas d'imports pour les annotations

# Imports des classes parentes
from Jeu.Entitee.Agissant.Role.Soigneur import Soigneur
from Jeu.Entitee.Agissant.Role.Mage import Multi_mage

class Multi_soigneur(Soigneur,Multi_mage):
    """Les soigneurs capables de soigner plusieurs agissants à la fois."""

    def agit_en_vue(self,defaut = ""):
        cibles = []
        skill = type(self.get_skill_magique())
        for corp in self.esprit.corps:
            if corp.etat == "vivant" and corp.pv < corp.pv_max:
                cibles.append([corp.pv,corp])
        if len(cibles) == 1:
            if self.peut_caster():
                new_cibles = sorted(cibles, key=itemgetter(0))
                skill = self.get_skill_magique()
                action = skill.fait(self.caste(),self)
                assert isinstance(action,Cible_agissant)
                action.cible = new_cibles[0][-1]
                self.fait(action)
                defaut = "soin"
                self.set_statut("soin")
        elif cibles:
            if self.peut_multi_caster():
                skill = self.get_skill_magique()
                action = skill.fait(self.multi_caste(),self)
                assert isinstance(action,Cible_agissants)
                action.cible = [cible[-1] for cible in cibles]
                self.fait(action)
                defaut = "soin"
                self.set_statut("soin")
            elif self.peut_caster():
                new_cibles = sorted(cibles, key=itemgetter(0))
                skill = self.get_skill_magique()
                action = skill.fait(self.caste(),self)
                assert isinstance(action,Cible_agissant)
                action.cible = new_cibles[0][-1]
                self.fait(action)
                defaut = "soin"
                self.set_statut("soin")
        return defaut

# Imports utilisés dans le code
from operator import itemgetter
from Jeu.Action.Magie.Magie import Cible_agissant,Cible_agissants