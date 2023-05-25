from __future__ import annotations

# Pas d'imports pour les annotations

# Imports des classes parentes
from Jeu.Entitee.Agissant.Role.Mage import Mage

class Renforceur(Mage):
    """Les agissants qui boostent les attaques de leurs alliés."""

    def agit_en_vue(self,defaut = ""):
        cibles = []
        skill = type(self.get_skill_magique())
        for corp in self.esprit.corps:
            if corp.statut == "attaque":
                cibles.append([self.esprit.get_importance(corp.get_impact()),corp])
        if cibles and self.peut_caster():
            new_cibles = sorted(cibles, key=itemgetter(0))
            self.utilise(skill)
            self.set_magie_courante(self.caste())
            self.cible_magie = new_cibles[0][-1]
            self.cible_magie.set_statut("attaque boostée")
            defaut = "soutien"
            self.set_statut("soutien")
        return defaut

# Imports utilisés dans le code
from Jeu.Entitee.Agissant.Agissant import Agissant
from Jeu.Systeme.Classe import Skill_magie
from operator import itemgetter