"""
Ce fichier contient les classes des magies de type boost.
"""

from __future__ import annotations
from typing import TYPE_CHECKING

# Imports des classes parentes
from ..magie import ActionMagie, CibleAgissant, CibleAgissants

# Imports utilisés dans le code
from ....effet.agissant.agissants import Dopage

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ....entitee import Agissant
    from ....systeme import Actif, Magie

class ActionMagieDopage(ActionMagie):
    """La magie qui crée un effet de dopage sur l'agissant."""
    nom = "magie dopage"
    def __init__(self,skill:Actif,magie:Magie,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,taux:float,duree:float):
        ActionMagie.__init__(self,skill,magie,agissant,gain_xp,cout_pm,latence)
        self.taux = taux
        self.duree = duree

    def action(self):
        self.agissant.effets.append(Dopage(self.agissant,self.taux))

class ActionMagieBoost(ActionMagieDopage,CibleAgissant):
    """La magie qui crée un effet de dopage sur un autre agissant."""
    nom = "magie boost"
    def __init__(self,skill:Actif,magie:Magie,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,taux:float,duree:float):
        ActionMagieDopage.__init__(self,skill,magie,agissant,gain_xp,cout_pm,latence,taux,duree)
        CibleAgissant.__init__(self,skill,magie,agissant,gain_xp,cout_pm,latence)

    def action(self):
        if not self.cible: # NOONE is falsy
            self.interrompt()
        else:
            self.cible.effets.append(Dopage(self.agissant,self.taux))

class ActionMagieMultiBoost(ActionMagieDopage,CibleAgissants):
    """La magie qui crée un effet de dopage sur plusieurs autres agissants."""
    nom = "magie multi boost"
    def __init__(self,skill:Actif,magie:Magie,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,taux:float,duree:float):
        ActionMagieDopage.__init__(self,skill,magie,agissant,gain_xp,cout_pm,latence,taux,duree)
        CibleAgissants.__init__(self,skill,magie,agissant,gain_xp,cout_pm,latence)

    def action(self):
        for cible in self.cible:
            cible.effets.append(Dopage(self.agissant,self.taux))

magies_boost: dict[tuple[bool, bool], type[ActionMagieDopage]] = {
    (False, False): ActionMagieDopage,
    (True, False): ActionMagieBoost,
    (True, True): ActionMagieMultiBoost,
    (False, True): ActionMagieDopage # Pas possible
}
"""
(cible, cible_multiple) -> ActionMagieDopage
"""
