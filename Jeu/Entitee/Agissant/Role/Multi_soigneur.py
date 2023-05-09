from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Jeu.Esprit.Esprit import Esprit

from operator import itemgetter
from Jeu.Entitee.Agissant.Role.Soigneur import *
from Jeu.Systeme.Constantes_magies.Magies import *

class Multi_soigneur(Soigneur,Multi_mage):
    """Les soigneurs capables de soigner plusieurs agissants à la fois."""

    def agit_en_vue(self,esprit:Esprit,defaut = ""):
        cibles = []
        skill = type(self.get_skill_magique())
        for ID in esprit.corps:
            corp = self.controleur[ID]
            if corp.etat == "vivant" and corp.pv < corp.pv_max:
                cibles.append([corp.pv,ID])
        if len(cibles) == 1:
            if self.peut_caster():
                self.utilise(skill)
                self.set_magie_courante(self.caste())
                self.cible_magie = cibles[0][-1]
                defaut = "soin"
                self.set_statut("soin")
        elif cibles != []:
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
