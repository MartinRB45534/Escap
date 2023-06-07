from __future__ import annotations
from typing import TYPE_CHECKING

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ..Controleur import Controleur
    from ..Labyrinthe.Structure_spatiale.Position import Position

# Imports des classes parentes
from ..Entitee.Agissant.Gobelin.Base_gobelin import Base_gobelin
from ..Entitee.Agissant.Role.Attaquant_magique_case import Attaquant_magique_case
from ..Entitee.Agissant.Role.Support import Support

# Valeurs par défaut des paramètres
from ..Labyrinthe.Structure_spatiale.Position import ABSENT

class Mage_gobelin(Attaquant_magique_case,Support,Base_gobelin):
    """Un gobelin avec un potentiel magique.
       Il peut utiliser une attaque magique."""
    def __init__(self,controleur:Controleur,niveau:int,position:Position=ABSENT):
        Base_gobelin.__init__(self,controleur,"mage_gobelin",niveau,position)

    def peut_caster(self):
        skill_magie = self.get_skill_magique()
        return self.peut_payer(cout_pm_petite_secousse[skill_magie.niveau-1])

    def caste(self):
        return "magie petite secousse"

    def attaque(self,direction):
        self.regarde(direction)
        skill_magie = self.get_skill_magique()
        if self.peut_payer(cout_pm_poing_magique[skill_magie.niveau-1]): #Quelle est l'attaque magique des gobelins ?
            action = skill_magie.fait(self,"magie poing magique")
            assert isinstance(action,Magie_poing_magique)
            action.direction = direction
            self.fait(action)
        else:
            skill = trouve_skill(self.classe_principale,Skill_attaque)
            assert skill is not None
            self.fait(skill.fait(self,direction))
        self.set_statut("attaque")

    def get_offenses(self):
        offenses = self.offenses
        self.offenses = []
        if self.etat != "vivant" or self.controleur is None:
            etat = "incapacite"
        elif self.pv <= self.pv_max//2:
            etat = "fuite"
        else:
            etat = "attaque"
        return offenses, etat

    def get_texte_descriptif(self):
        return [f"Un mage gobelin (niveau {self.niveau})",f"ID : {self.ID}","Stats :",f"{self.pv}/{self.pv_max} PV",f"{self.pm}/{self.pm_max} PM",self.statut,"Un gobelin apte à l'utilisation de la magie. Il s'en sert pour donner plus de force à ses poings, mais lui-même n'est pas très solide. Tuez-le avant qu'il ne vous tue, ou laissez-le gaspiller ses PM sur une défense digne de ce nom."]

# Un mage un peu spécial
class Deuxieme_monstre(Mage_gobelin):
    """Le premier mage gobelin."""
    def __init__(self,controleur:Controleur,niveau:int,position:Position=ABSENT):
        Base_gobelin.__init__(self,controleur,"deuxieme_monstre",niveau,position)

    def meurt(self):
        if isinstance(self.controleur.joueur,Heros):
            self.controleur.joueur.magic_kill(self.position)
        super().meurt()

# Imports utilisés dans le code
from ..Systeme.Constantes_magies.Magies import cout_pm_petite_secousse, cout_pm_poing_magique

from ..Systeme.Skill.Skills import Skill_attaque
from ..Action.Magie.Magies_attaque.Poings_magiques import Magie_poing_magique
from ..Entitee.Agissant.Humain.Heros import Heros

from ..Systeme.Classe.Classes import trouve_skill