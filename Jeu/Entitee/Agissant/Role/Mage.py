from Jeu.Entitee.Agissant.Agissant import *

class Mage(Agissant):
    """Les agissants qui lancent des sorts.
       Ont en général un sort de prédilection."""

    def peut_caster(self): # Utilisé pour déterminer leur comportement
        return False

    def caste(self):
        return None

    def get_magies(self):
        return self.get_skill_magique().menu_magie()

    def get_skill_magique(self) -> Skills_magiques:
        return trouve_skill(self.classe_principale,Skills_magiques)

    def auto_impregne(self,nom:str):
        skill:Skill_magie = trouve_skill(self.classe_principale,Skill_magie)
        latence,magie = skill.utilise(nom)
        self.latence += latence
        cout = magie.cout_pm
        if self.peut_payer(cout):
            self.controleur.joueur.inventaire.consomme_parchemin_vierge()
            self.controleur.unset_phase(AUTO_IMPREGNATION)
            self.paye(cout)
            parch = Parchemin_impregne(None,magie,cout//2)
            self.controleur.ajoute_entitee(parch)
            self.controleur.joueur.inventaire.ajoute(parch)

class Multi_mage(Mage):
    """Les agissants qui lancent des sorts.
       Ont en général un sort de prédilection."""

    def peut_multi_caster(self): # Utilisé pour déterminer leur comportement
        return False

    def multi_caste(self):
        return None