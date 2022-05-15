from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Jeu.Esprit.Esprit import Esprit

from operator import itemgetter
from Jeu.Entitee.Agissant.Role.Mage import *
from Jeu.Systeme.Constantes_magies.Magies import *

class Soigneur(Mage):
    """Les agissants capables de soigner les autres."""

    def agit_en_vue(self,esprit:Esprit,defaut = ""):
        cibles = []
        skill = type(self.get_skill_magique())
        for ID in esprit.corps.keys():
            corp = self.controleur[ID]
            if corp.etat == "vivant" and corp.pv < corp.pv_max:
                cibles.append([corp.pv,ID])
        if cibles != [] and self.peut_caster():
            new_cibles = sorted(cibles, key=itemgetter(0))
            self.skill_courant = skill
            self.magie_courante = self.caste()
            self.cible_magie = new_cibles[0][-1]
            defaut = "soin"
            self.statut = "soin"
        return defaut
