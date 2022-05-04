from operator import itemgetter
from Jeu.Entitee.Agissant.Role.Mage import *
from Jeu.Systeme.Constantes_magies.Magies import *

class Renforceur(Mage):
    """Les agissants qui boostent les attaques de leurs alliés."""

    def agit_en_vue(self,esprit,defaut = ""):
        cibles = []
        for ID in esprit.corps.keys():
            corp = self.controleur.get_entitee(ID)
            if corp.statut == "attaque":
                cibles.append([esprit.get_importance(corp.get_impact()),ID])
        if cibles != [] and self.peut_caster():
            new_cibles = sorted(cibles, key=itemgetter(0))
            self.skill_courant = Skill_magie
            self.magie_courante = self.caste()
            self.cible_magie = new_cibles[0][-1]
            agissant = self.controleur.get_entitee(new_cibles[0][-1])
            agissant.statut = "attaque boostée"
            defaut = "soutien"
            self.statut = "soutien"
        return defaut
