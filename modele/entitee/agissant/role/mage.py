from __future__ import annotations
from typing import TYPE_CHECKING

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ...item.parchemin import Parchemin

# Imports des classes parentes
from ..agissant import Agissant

class Mage(Agissant):
    """Les agissants qui lancent des sorts.
       Ont en général un sort de prédilection."""

    def peut_caster(self): # Utilisé pour déterminer leur comportement
        return False

    def caste(self):
        return ""
    
    # def set_magie_courante(self,magie):
    #     self.magie_courante = magie

    def get_magies(self):
        return self.get_skill_magique().menu_magie()

    def get_skill_magique(self) -> SkillsMagiques:
        skill = trouve_skill(self.classe_principale,SkillsMagiques)
        assert skill is not None
        return skill

    def impregne(self,nom:str,parch:Parchemin):
        skill = self.get_skill_magique()
        magie = skill.fait(self,nom)
        if parch.impregne is None:
            return False
        if self.action is not None:
            self.action.interrompt()
        self.action = parch.impregne(self,parch)
        self.action.set_magie(magie)
        return True

class Multi_mage(Mage):
    """Les agissants qui lancent des sorts.
       Ont en général un sort de prédilection."""

    def peut_multi_caster(self): # Utilisé pour déterminer leur comportement
        return False

    def multi_caste(self):
        return ""
    
# Imports utilisés dans le code

from ....systeme.classe.classes import trouve_skill
from ....systeme.skill.actif import SkillsMagiques