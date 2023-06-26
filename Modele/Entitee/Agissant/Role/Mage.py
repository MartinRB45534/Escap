from __future__ import annotations
from typing import TYPE_CHECKING

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ...Item.Parchemin.Parchemins import Parchemin_vierge

# Imports des classes parentes
from ..Agissant import Agissant

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

    def get_skill_magique(self) -> Skills_magiques:
        skill = trouve_skill(self.classe_principale,Skills_magiques)
        assert skill is not None
        return skill

    def impregne(self,nom:str,parch:Parchemin_vierge):
        skill = self.get_skill_magique()
        magie = skill.fait(self,nom)
        if isinstance(parch.action_portee,Impregne) and parch.action_portee.magie is None:
            parch.action_portee.set_magie(magie)
        else:
            return False
        if self.action is not None:
            self.action.interrompt()
        self.action = parch.action_portee
        return True

class Multi_mage(Mage):
    """Les agissants qui lancent des sorts.
       Ont en général un sort de prédilection."""

    def peut_multi_caster(self): # Utilisé pour déterminer leur comportement
        return False

    def multi_caste(self):
        return ""
    
# Imports utilisés dans le code

from ....Systeme.Classe.Classes import trouve_skill
from ....Systeme.Skill.Actif import Skills_magiques
from ....Effet.Action.Non_skill import Impregne