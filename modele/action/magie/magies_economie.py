"""
Contient trois magies à coût ajustable.
"""

from __future__ import annotations
from typing import TYPE_CHECKING

# Imports des classes parentes
from .magie import ActionMagieCout
from .magies_attaque.attaques import ActionMagieAttaque, ActionMagieAttaqueDistance, ActionMagieAttaqueDirigee, ActionMagieAttaqueDistanceDirigee

# Imports utilisés dans le code
from ...effet import ReserveMana,InvestissementMana
from ...commons import Deplacement, Forme, Passage

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ...entitee import Agissant
    from ...systeme import Actif, Magie
    from ...commons import Element

class ActionMagieReserve(ActionMagieCout):
    """La magie qui fait une réserve de mana."""
    nom = "magie reserve"
    def __init__(self,skill:Actif,magie:Magie,agissant:Agissant,gain_xp:float,latence:float,taux:float):
        ActionMagieCout.__init__(self,skill,magie,agissant,gain_xp,0,latence)
        self.taux = taux

    def action(self):
        self.agissant.effets.append(ReserveMana(self.agissant,self.cout*self.taux))

class ActionMagieInvestissement(ActionMagieCout):
    """La magie qui crée un investissement."""
    nom = "magie investissement"
    def __init__(self,skill:Actif,magie:Magie,agissant:Agissant,gain_xp:float,latence:float,taux:float,duree:float):
        ActionMagieCout.__init__(self,skill,magie,agissant,gain_xp,0,latence)
        self.duree = duree
        self.taux = taux

    def action(self):
        self.agissant.effets.append(InvestissementMana(self.duree,self.cout*self.taux))

class ActionMagieAttaqueVariable(ActionMagieCout,ActionMagieAttaque):
    """La magie qui crée une explosion de mana."""
    def __init__(self,skill:Actif,magie:Magie,agissant:Agissant,gain_xp:float,taux_degats:float,portee:float,element:Element,deplacement:Deplacement,forme:Forme,passage:Passage,latence:float,taux_perce:float,inverse:bool):
        ActionMagieCout.__init__(self,skill,magie,agissant,gain_xp,0,latence)
        ActionMagieAttaque.__init__(self,skill,magie,agissant,gain_xp,0,portee,0,element,deplacement,forme,passage,latence,taux_perce,inverse)
        self.taux_degats = taux_degats

    def set_cout(self,cout:float):
        ActionMagieCout.set_cout(self,cout)
        self.degats = cout*self.taux_degats

class ActionMagieAttaqueVariableDistance(ActionMagieAttaqueVariable,ActionMagieAttaqueDistance):
    """La magie qui crée une explosion de mana à distance."""
    def __init__(self,skill:Actif,magie:Magie,agissant:Agissant,gain_xp:float,taux_degats:float,portee:float,element:Element,deplacement:Deplacement,forme:Forme,passage:Passage,latence:float,taux_perce:float,inverse:bool):
        ActionMagieAttaqueVariable.__init__(self,skill,magie,agissant,gain_xp,taux_degats,portee,element,deplacement,forme,passage,latence,taux_perce,inverse)
        ActionMagieAttaqueDistance.__init__(self,skill,magie,agissant,gain_xp,0,portee,0,element,deplacement,forme,passage,latence,taux_perce,inverse)

class ActionMagieAttaqueVariableDirigee(ActionMagieAttaqueVariable,ActionMagieAttaqueDirigee):
    """La magie qui crée une explosion de mana dirigée."""
    def __init__(self,skill:Actif,magie:Magie,agissant:Agissant,gain_xp:float,taux_degats:float,portee:float,element:Element,deplacement:Deplacement,forme:Forme,passage:Passage,latence:float,taux_perce:float,inverse:bool):
        ActionMagieAttaqueVariable.__init__(self,skill,magie,agissant,gain_xp,taux_degats,portee,element,deplacement,forme,passage,latence,taux_perce,inverse)
        ActionMagieAttaqueDirigee.__init__(self,skill,magie,agissant,gain_xp,0,portee,0,element,deplacement,forme,passage,latence,taux_perce,inverse)

class ActionMagieAttaqueVariableDistanceDirigee(ActionMagieAttaqueVariable,ActionMagieAttaqueDistanceDirigee):
    """La magie qui crée une explosion de mana à distance dirigée."""
    def __init__(self,skill:Actif,magie:Magie,agissant:Agissant,gain_xp:float,taux_degats:float,portee:float,element:Element,deplacement:Deplacement,forme:Forme,passage:Passage,latence:float,taux_perce:float,inverse:bool):
        ActionMagieAttaqueVariable.__init__(self,skill,magie,agissant,gain_xp,taux_degats,portee,element,deplacement,forme,passage,latence,taux_perce,inverse)
        ActionMagieAttaqueDistanceDirigee.__init__(self,skill,magie,agissant,gain_xp,0,portee,0,element,deplacement,forme,passage,latence,taux_perce,inverse)

magies_attaque: dict[tuple[bool, bool, bool], type[ActionMagieAttaque]] = {
    (False, False, False): ActionMagieAttaque,
    (False, False, True): ActionMagieAttaqueVariable,
    (False, True, False): ActionMagieAttaqueDistance,
    (False, True, True): ActionMagieAttaqueVariableDistance,
    (True, False, False): ActionMagieAttaqueDirigee,
    (True, False, True): ActionMagieAttaqueVariableDirigee,
    (True, True, False): ActionMagieAttaqueDistanceDirigee,
    (True, True, True): ActionMagieAttaqueVariableDistanceDirigee
}
"""
(dirigee, distance, cout_variable) -> ActionMagieAttaque
"""
