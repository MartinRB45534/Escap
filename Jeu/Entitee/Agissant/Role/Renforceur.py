from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Jeu.Esprit.Esprit import Esprit

from operator import itemgetter
from Jeu.Entitee.Agissant.Role.Mage import *
from Jeu.Systeme.Constantes_magies.Magies import *

class Renforceur(Mage):
    """Les agissants qui boostent les attaques de leurs alliés."""

    def agit_en_vue(self,esprit:Esprit,defaut = ""):
        cibles = []
        skill = type(self.get_skill_magique())
        for ID in esprit.corps:
            corp = self.controleur[ID]
            if corp.statut == "attaque":
                cibles.append([esprit.get_importance(corp.get_impact()),ID])
        if cibles != [] and self.peut_caster():
            new_cibles = sorted(cibles, key=itemgetter(0))
            self.utilise(skill)
            self.set_magie_courante(self.caste())
            self.cible_magie = new_cibles[0][-1]
            agissant:Agissant = self.controleur[new_cibles[0][-1]]
            agissant.set_statut("attaque boostée")
            defaut = "soutien"
            self.set_statut("soutien")
        return defaut
