from Jeu.Entitees.Agissant.Agissant import *

class Attaquant_magique_agissant(Agissant):
    """Les agissants qui combattent en lançant des attaques magiques de loin sur des agissants."""

    def agit_en_vue(self,esprit,defaut = ""):
        cibles = []
        #On cherche l'ennemi le plus puissant en vue
        for colonne in self.vue:
            for case in colonne:
                for ID in case[6]:
                    if ID in esprit.ennemis.keys() and not self.controleur.est_item(ID):
                        cibles.append([esprit.ennemis[ID][0],ID])
        skill = trouve_skill(self.classe_principale,Skill_magie)
        if cibles != [] and self.peut_caster(skill.niveau):
            new_cibles = sorted(cibles, key=lambda ennemi: ennemi[0])
            self.skill_courant = Skill_magie
            self.magie_courante = self.caste()
            self.cible_magie = new_cibles[-1][-1]
            defaut = "attaque"
            self.statut = "attaque"
        return defaut

    def get_impact(self):
        if self.cible_magie != None:
            return self.controleur.get_entitee(self.cible_magie).position
        else:
            return Agissant.get_impact(self)