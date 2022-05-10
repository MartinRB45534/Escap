from operator import itemgetter
from Jeu.Entitee.Agissant.Agissant import *
from Jeu.Systeme.Constantes_magies.Magies import *

class Multi_soigneur(Agissant):
    """Les soigneurs capables de soigner plusieurs agissants à la fois.""" #/!\Est-ce qu'on veut aussi en faire une pour le soin supérieur ou seul le joueur peut l'obtenir ?

    def agit_en_vue(self,esprit,defaut = ""):
        cibles = []
        for ID in esprit.corps.keys():
            corp = self.controleur.get_entitee(ID)
            if corp.etat == "vivant" and corp.pv < corp.pv_max:
                cibles.append([corp.pv,ID])
        if len(cibles) == 1:
            if self.peut_caster():
                self.skill_courant = Skill_magie
                self.magie_courante = self.caste()
                self.cible_magie = cibles[0][-1]
                defaut = "soin"
                self.statut = "soin"
        elif cibles != []:
            if self.peut_multi_caster():
                self.skill_courant = Skill_magie
                self.magie_courante = self.multi_caste()
                self.cible_magie = [cible[-1] for cible in cibles]
                defaut = "soin"
                self.statut = "soin"
            elif self.peut_caster():
                new_cibles = sorted(cibles, key=itemgetter(0))
                self.skill_courant = Skill_magie
                self.magie_courante = self.caste()
                self.cible_magie = new_cibles[0][-1]
                defaut = "soin"
                self.statut = "soin"
        return defaut
