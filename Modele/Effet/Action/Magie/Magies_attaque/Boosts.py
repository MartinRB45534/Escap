from __future__ import annotations
from typing import TYPE_CHECKING, List, Optional

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from .....entitee.agissant.agissant import Agissant
    from .....systeme.skill.actif import Actif

# Imports des classes parentes
from ...magie.magie import Magie, Cible_agissant, Multi_cible

class Magie_dopage(Magie):
    """La magie qui crée un effet de dopage sur l'agissant."""
    nom = "magie dopage"
    def __init__(self,skill:Actif,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,taux:float,duree:float,niveau:int):
        Magie.__init__(self,skill,agissant,gain_xp,cout_pm,latence,niveau)
        self.taux = taux
        self.duree = duree

    def action(self):
        self.agissant.effets.append(Dopage(self.agissant,self.taux,self.duree))

class Magie_boost(Cible_agissant):
    """La magie qui crée un effet de dopage sur un autre agissant."""
    nom = "magie boost"
    def __init__(self,skill:Actif,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,taux:float,duree:float,niveau:int,cible:Optional[Agissant]=None):
        Magie.__init__(self,skill,agissant,gain_xp,cout_pm,latence,niveau)
        self.cible:Optional[Agissant] = cible
        self.taux = taux
        self.duree = duree

    def action(self):
        if self.cible is None:
            self.interrompt()
        else:
            self.cible.effets.append(Dopage(self.agissant,self.taux,self.duree))

class Magie_multi_boost(Cible_agissant,Multi_cible):
    """La magie qui crée un effet de dopage sur plusieurs autres agissants."""
    nom = "magie multi boost"
    def __init__(self,skill:Actif,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,taux:float,duree:float,niveau:int,cible:List[Agissant]=[]):
        Magie.__init__(self,skill,agissant,gain_xp,cout_pm,latence,niveau)
        self.cible:List[Agissant] = cible
        self.taux = taux
        self.duree = duree

    def action(self):
        for cible in self.cible:
            cible.effets.append(Dopage(self.agissant,self.taux,self.duree))

from ....effets_divers import Dopage