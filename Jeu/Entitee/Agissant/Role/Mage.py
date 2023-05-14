from __future__ import annotations

# Pas d'imports pour les annotations

# Imports des classes parentes
from Jeu.Entitee.Agissant.Agissant import Agissant

class Mage(Agissant):
    """Les agissants qui lancent des sorts.
       Ont en général un sort de prédilection."""

    def peut_caster(self): # Utilisé pour déterminer leur comportement
        return False

    def caste(self):
        return None
    
    def set_magie_courante(self,magie):
        self.magie_courante = magie

    def get_magies(self):
        return self.get_skill_magique().menu_magie()

    def get_skill_magique(self) -> Skills_magiques:
        skill = trouve_skill(self.classe_principale,Skills_magiques)
        assert skill is not None
        return skill

    def auto_impregne(self,nom:str):
        skill = self.get_skill_magique()
        latence,magie = skill.utilise(nom)
        self.latence += latence
        cout = magie.cout_pm
        if self.peut_payer(cout):
            self.inventaire.consomme_parchemin_vierge()
            self.controleur.unset_phase(AUTO_IMPREGNATION)
            self.paye(cout)
            parch = Parchemin_impregne(self.controleur,magie,cout//2)
            self.controleur.ajoute_entitee(parch)
            self.inventaire.ajoute(parch)

class Multi_mage(Mage):
    """Les agissants qui lancent des sorts.
       Ont en général un sort de prédilection."""

    def peut_multi_caster(self): # Utilisé pour déterminer leur comportement
        return False

    def multi_caste(self):
        return None
    
# Imports utilisés dans le code
from Jeu.Systeme.Classe import trouve_skill, Skills_magiques
from Jeu.Entitee.Item.Parchemin.Parchemins import Parchemin_impregne
from Jeu.Constantes import AUTO_IMPREGNATION