from __future__ import annotations

# Pas d'imports pour les annotations

# Imports des classes parentes
from Jeu.Entitee.Agissant.Role.Mage import Mage

class Soigneur(Mage):
    """Les agissants capables de soigner les autres."""

    def agit_en_vue(self,defaut = ""):
        cibles = []
        skill = type(self.get_skill_magique())
        for corp in self.esprit.corps:
            assert isinstance(corp,Agissant)
            if corp.etat == "vivant" and corp.pv < corp.pv_max:
                cibles.append([corp.pv,corp])
        if cibles != [] and self.peut_caster():
            new_cibles = sorted(cibles, key=itemgetter(0))
            self.utilise(skill)
            self.set_magie_courante(self.caste())
            self.cible_magie = new_cibles[0][-1]
            defaut = "soin"
            self.set_statut("soin")
        return defaut

# Imports utilisés dans le code
from Jeu.Entitee.Agissant.Agissant import Agissant
from Jeu.Systeme.Classe import Skill_magie
from operator import itemgetter