"""
Ce fichier contient les classes des magies de type boost.
"""

from __future__ import annotations
from typing import TYPE_CHECKING, List$1

# Imports des classes parentes
from ..magie import Magie, CibleAgissant, CibleAgissants

# Imports utilisés dans le code
from ....effet.agissant.agissants import Dopage

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ....entitee.agissant.agissant import Agissant
    from ....systeme.skill.actif import Actif

class MagieDopage(Magie):
    """La magie qui crée un effet de dopage sur l'agissant."""
    nom = "magie dopage"
    def __init__(self,skill:Actif,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,taux:float,duree:float,niveau:int):
        Magie.__init__(self,skill,agissant,gain_xp,cout_pm,latence,niveau)
        self.taux = taux
        self.duree = duree

    def action(self):
        self.agissant.effets.append(Dopage(self.agissant,self.taux))

class MagieBoost(CibleAgissant):
    """La magie qui crée un effet de dopage sur un autre agissant."""
    nom = "magie boost"
    def __init__(self,skill:Actif,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,taux:float,duree:float,niveau:int,cible:Agissant):
        CibleAgissant.__init__(self,skill,agissant,gain_xp,cout_pm,latence,niveau,cible)
        self.taux = taux
        self.duree = duree

    def action(self):
        if not self.cible: # NOONE is falsy
            self.interrompt()
        else:
            self.cible.effets.append(Dopage(self.agissant,self.taux))

class MagieMultiBoost(CibleAgissants):
    """La magie qui crée un effet de dopage sur plusieurs autres agissants."""
    nom = "magie multi boost"
    def __init__(self,skill:Actif,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,taux:float,duree:float,niveau:int,cible:List[Agissant]):
        CibleAgissants.__init__(self,skill,agissant,gain_xp,cout_pm,latence,niveau,cible)
        self.cible:List[Agissant] = cible
        self.taux = taux
        self.duree = duree

    def action(self):
        for cible in self.cible:
            cible.effets.append(Dopage(self.agissant,self.taux))
