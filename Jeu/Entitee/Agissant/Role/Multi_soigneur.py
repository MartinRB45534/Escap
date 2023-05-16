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
                self.utilise(skill)
                self.set_magie_courante(self.caste())
                self.cible_magie = cibles[0][-1]
                defaut = "soin"
                self.set_statut("soin")
        elif cibles:
            if self.peut_multi_caster():
                self.utilise(skill)
                self.set_magie_courante(self.multi_caste())
                self.cible_magie = [cible[-1] for cible in cibles]
                defaut = "soin"
                self.set_statut("soin")
            elif self.peut_caster():
                new_cibles = sorted(cibles, key=itemgetter(0))
                self.utilise(skill)
                self.set_magie_courante(self.caste())
                self.cible_magie = new_cibles[0][-1]
                defaut = "soin"
                self.set_statut("soin")
        return defaut

# Imports utilisés dans le code
from operator import itemgetter