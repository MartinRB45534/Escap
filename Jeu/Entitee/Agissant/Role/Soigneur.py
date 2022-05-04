from operator import itemgetter
from Jeu.Entitee.Agissant.Role.Mage import *
from Jeu.Systeme.Constantes_magies.Magies import *

class Soigneur(Mage):
    """Les agissants capables de soigner les autres."""

    def agit_en_vue(self,esprit,defaut = ""):
        cibles = []
        for ID in esprit.corps.keys():
            corp = self.controleur.get_entitee(ID)
            if corp.etat == "vivant" and corp.pv < corp.pv_max:
                cibles.append([corp.pv,ID])
        if cibles != [] and self.peut_caster():
            new_cibles = sorted(cibles, key=itemgetter(0))
            self.skill_courant = Skill_magie
            self.magie_courante = self.caste()
            self.cible_magie = new_cibles[0][-1]
            defaut = "soin"
            self.statut = "soin"
        return defaut
