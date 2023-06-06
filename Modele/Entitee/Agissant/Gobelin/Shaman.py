from __future__ import annotations
from typing import TYPE_CHECKING

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from Old_Jeu.Controleur import Controleur
    from Old_Jeu.Labyrinthe.Structure_spatiale.Position import Position

# Imports des classes parentes
from Old_Jeu.Entitee.Agissant.Gobelin.Base_gobelin import Base_gobelin
from Old_Jeu.Entitee.Agissant.Role.Renforceur import Renforceur
from Old_Jeu.Entitee.Agissant.Role.Support_lointain import Support_lointain

# Valeurs par défaut des paramètres
from Old_Jeu.Labyrinthe.Structure_spatiale.Position import ABSENT

class Shaman_gobelin(Renforceur,Support_lointain,Base_gobelin):
    """Un gobelin avec un potentiel magique.
       Il peut utiliser un sort de boost."""
    def __init__(self,controleur:Controleur,niveau:int,position:Position=ABSENT):
        Base_gobelin.__init__(self,controleur,"shaman_gobelin",niveau,position)

    def peut_caster(self):
        skill_magie = self.get_skill_magique()
        return self.peut_payer(cout_pm_boost[skill_magie.niveau-1])

    def caste(self):
        return "magie boost"

    def boost(self,cible):
        action = self.get_skill_magique().fait(self.caste(),self)
        assert isinstance(action,Magie_boost)
        action.cible = cible
        self.fait(action)

    def get_offenses(self):
        offenses = self.offenses
        self.offenses = []
        if self.etat != "vivant" or self.controleur is None:
            etat = "incapacite"
        elif self.pv <= 3*self.pv_max//4 or self.pm < 50:
            etat = "fuite"
        else:
            etat = "soutien"
        return offenses, etat

    def get_texte_descriptif(self):
        return [f"Un shaman gobelin (niveau {self.niveau})",f"ID : {self.ID}","Stats :",f"{self.pv}/{self.pv_max} PV",f"{self.pm}/{self.pm_max} PM",self.statut,"Caché à l'arrière, loin des combats, le shaman fourni pourtant aux autres gobelins un renforcement non négligeable. Essayez de le tuer en priorité !"]

# Imports utilisés dans le code
from Old_Jeu.Systeme.Constantes_magies.Magies import cout_pm_boost
from Old_Jeu.Action.Magie.Magies_attaque.Boosts import Magie_boost