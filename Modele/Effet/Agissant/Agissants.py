"""
Contient quelques effets divers.
"""

from __future__ import annotations
from typing import TYPE_CHECKING, Type

# Imports des classes parentes
from .agissant import EffetAgissant
from ..timings import OnFinTourAgissant

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ...entitee.agissant.agissant import Agissant
    from ...action.magie.magie import Magie
    from ...entitee.agissant.role.mage import Mage

class Enseignement(EffetAgissant):
    """Effet qui enseigne une magie au joueur."""
    def __init__(self,magie:Type[Magie]):
        self.magie = magie

    def enseigne(self,agissant:Mage):
        """Enseigne la magie au joueur."""
        skill = agissant.get_skill_magique()
        skill.ajoute(self.magie)

class Dopage(EffetAgissant):
    """Effet qui "dope" la prochaine attaque du joueur."""
    def __init__(self,responsable:Agissant,taux_degats:float):
        self.responsable = responsable
        self.taux_degats = taux_degats

    def dope(self,taux:float):
        """Dope le taux de dégâts."""
        return taux*self.taux_degats

class Instakill(OnFinTourAgissant):
    """L'effet d'instakill. S'il réussit, la victime voit ses PV descendre à 0. Sinon, rien.""" #Comment retirer aussi les PM, si la victime a la persévérance (essence magique) ?
    def __init__(self,responsable:Agissant,priorite:float):
        self.responsable = responsable
        self.priorite = priorite

    def fin_tour(self,agissant:Agissant):
        if agissant.priorite < self.priorite :
            agissant.instakill(self.responsable)
        else :
            pass
            # porteur.echape_instakill(self.responsable)
