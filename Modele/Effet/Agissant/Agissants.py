from __future__ import annotations
from typing import TYPE_CHECKING, Type

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ...entitee.agissant.agissant import Agissant
    from ..action.magie.magie import Magie


# Imports des classes parentes
from .agissant import Effet_agissant
from ..effet import OneShot

class Enseignement(Effet_agissant,OneShot):
    """Effet qui enseigne une magie au joueur."""
    def __init__(self,agissant:Agissant,magie:Type[Magie]):
        self.agissant = agissant
        self.magie = magie

    def action(self):
        if isinstance(self.agissant,Mage):
            skill = self.agissant.get_skill_magique()
            skill.ajoute(self.magie)

class Dopage(Effet_agissant,OneShot):
    """Effet qui "dope" la prochaine attaque du joueur."""
    def __init__(self,agissant:Agissant,responsable:Agissant,taux_degats:float):
        self.agissant = agissant
        self.responsable = responsable
        self.taux_degats = taux_degats

    def action(self):
        if isinstance(self.agissant.action,Attaque):
            if isinstance(self.agissant.action,Attaque_multiple):
                self.agissant.action.taux = [taux*self.taux_degats for taux in self.agissant.action.taux]
            else:
                self.agissant.action.taux *= self.taux_degats

class Instakill(Effet_agissant,OneShot):
    """L'effet d'instakill. S'il réussit, la victime voit ses PV descendre à 0. Sinon, rien.""" #Comment retirer aussi les PM, si la victime a la persévérance (essence magique) ?
    def __init__(self,agissant:Agissant,responsable:Agissant,priorite:float):
        self.agissant = agissant
        self.responsable = responsable
        self.priorite = priorite

    def action(self):
        if self.agissant.priorite < self.priorite :
            self.agissant.instakill(self.responsable)
        else :
            pass
            # porteur.echape_instakill(self.responsable)

# Imports utilisés dans le code
from ...entitee.agissant.role.mage import Mage
from ..action.attaque import Attaque, Attaque_multiple