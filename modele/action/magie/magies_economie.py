"""
Contient trois magies à coût ajustable.
"""

from __future__ import annotations
from typing import TYPE_CHECKING

# Imports des classes parentes
from .magie import MagieCout
from .magies_attaque.attaques import MagieAttaque, MagieAttaqueDistance, MagieAttaqueDirigee, MagieAttaqueDistanceDirigee

# Imports utilisés dans le code
from ...effet import ReserveMana,InvestissementMana
from ...commons import Deplacement, Forme, Passage

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ...entitee.agissant.agissant import Agissant
    from ...systeme.skill.actif import Actif
    from ...commons.elements import Element

class MagieReserve(MagieCout):
    """La magie qui fait une réserve de mana."""
    nom = "magie reserve"
    def __init__(self,skill:Actif,agissant:Agissant,gain_xp:float,latence:float,taux:float):
        MagieCout.__init__(self,skill,agissant,gain_xp,0,latence)
        self.taux = taux

    def action(self):
        self.agissant.effets.append(ReserveMana(self.agissant,self.cout*self.taux))

class MagieInvestissement(MagieCout):
    """La magie qui crée un investissement."""
    nom = "magie investissement"
    def __init__(self,skill:Actif,agissant:Agissant,gain_xp:float,latence:float,taux:float,duree:float):
        MagieCout.__init__(self,skill,agissant,gain_xp,0,latence)
        self.duree = duree
        self.taux = taux

    def action(self):
        self.agissant.effets.append(InvestissementMana(self.duree,self.cout*self.taux))

class MagieAttaqueVariable(MagieCout,MagieAttaque):
    """La magie qui crée une explosion de mana."""
    def __init__(self,skill:Actif,agissant:Agissant,gain_xp:float,taux_degats:float,portee:float,element:Element,deplacement:Deplacement,forme:Forme,passage:Passage,latence:float,taux_perce:float,inverse:bool):
        MagieCout.__init__(self,skill,agissant,gain_xp,0,latence)
        MagieAttaque.__init__(self,skill,agissant,gain_xp,0,portee,0,element,deplacement,forme,passage,latence,taux_perce,inverse)
        self.taux_degats = taux_degats

    def set_cout(self,cout:float):
        MagieCout.set_cout(self,cout)
        self.degats = cout*self.taux_degats

class MagieAttaqueVariableDistance(MagieAttaqueVariable,MagieAttaqueDistance):
    """La magie qui crée une explosion de mana à distance."""
    def __init__(self,skill:Actif,agissant:Agissant,gain_xp:float,taux_degats:float,portee:float,element:Element,deplacement:Deplacement,forme:Forme,passage:Passage,latence:float,taux_perce:float,inverse:bool):
        MagieAttaqueVariable.__init__(self,skill,agissant,gain_xp,taux_degats,portee,element,deplacement,forme,passage,latence,taux_perce,inverse)
        MagieAttaqueDistance.__init__(self,skill,agissant,gain_xp,0,portee,0,element,deplacement,forme,passage,latence,taux_perce,inverse)

class MagieAttaqueVariableDirigee(MagieAttaqueVariable,MagieAttaqueDirigee):
    """La magie qui crée une explosion de mana dirigée."""
    def __init__(self,skill:Actif,agissant:Agissant,gain_xp:float,taux_degats:float,portee:float,element:Element,deplacement:Deplacement,forme:Forme,passage:Passage,latence:float,taux_perce:float,inverse:bool):
        MagieAttaqueVariable.__init__(self,skill,agissant,gain_xp,taux_degats,portee,element,deplacement,forme,passage,latence,taux_perce,inverse)
        MagieAttaqueDirigee.__init__(self,skill,agissant,gain_xp,0,portee,0,element,deplacement,forme,passage,latence,taux_perce,inverse)

class MagieAttaqueVariableDistanceDirigee(MagieAttaqueVariable,MagieAttaqueDistanceDirigee):
    """La magie qui crée une explosion de mana à distance dirigée."""
    def __init__(self,skill:Actif,agissant:Agissant,gain_xp:float,taux_degats:float,portee:float,element:Element,deplacement:Deplacement,forme:Forme,passage:Passage,latence:float,taux_perce:float,inverse:bool):
        MagieAttaqueVariable.__init__(self,skill,agissant,gain_xp,taux_degats,portee,element,deplacement,forme,passage,latence,taux_perce,inverse)
        MagieAttaqueDistanceDirigee.__init__(self,skill,agissant,gain_xp,0,portee,0,element,deplacement,forme,passage,latence,taux_perce,inverse)

magies_attaque: dict[tuple[bool, bool, bool], type[MagieAttaque]] = {
    (False, False, False): MagieAttaque,
    (False, False, True): MagieAttaqueVariable,
    (False, True, False): MagieAttaqueDistance,
    (False, True, True): MagieAttaqueVariableDistance,
    (True, False, False): MagieAttaqueDirigee,
    (True, False, True): MagieAttaqueVariableDirigee,
    (True, True, False): MagieAttaqueDistanceDirigee,
    (True, True, True): MagieAttaqueVariableDistanceDirigee
}
"""
(dirigee, distance, cout_variable) -> MagieAttaque
"""
