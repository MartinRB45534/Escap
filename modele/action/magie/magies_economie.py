"""
Contient trois magies à coût ajustable.
"""

from __future__ import annotations
from typing import TYPE_CHECKING

# Imports des classes parentes
from .magie import MagieCout
from .magies_attaques import MagieAttaque, MagieAttaqueDistance, MagieAttaqueDirigee, MagieAttaqueDistanceDirigee

# Imports utilisés dans le code
from ...effet import ReserveMana,InvestissementMana

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ...entitee import Agissant
    from ...systeme import Actif

class MagieReserve(MagieCout):
    """La magie qui fait une réserve de mana."""
    taux: float
    def __init__(self,skill:Actif,agissant:Agissant):
        MagieCout.__init__(self,skill,agissant)

    def action(self):
        self.agissant.effets.append(ReserveMana(self.agissant,self.cout*self.taux))

class MagieInvestissement(MagieCout):
    """La magie qui crée un investissement."""
    taux: float
    duree: float
    def __init__(self,skill:Actif,agissant:Agissant):
        MagieCout.__init__(self,skill,agissant)

    def action(self):
        self.agissant.effets.append(InvestissementMana(self.duree,self.cout*self.taux))

class MagieAttaqueVariable(MagieCout,MagieAttaque):
    """La magie qui crée une explosion de mana."""
    taux_degats: float
    def __init__(self,skill:Actif,agissant:Agissant):
        MagieCout.__init__(self,skill,agissant)
        MagieAttaque.__init__(self,skill,agissant)

    def set_cout(self,cout:float):
        MagieCout.set_cout(self,cout)
        self.degats = cout*self.taux_degats

class MagieAttaqueVariableDistance(MagieAttaqueVariable,MagieAttaqueDistance):
    """La magie qui crée une explosion de mana à distance."""
    def __init__(self,skill:Actif,agissant:Agissant):
        MagieAttaqueVariable.__init__(self,skill,agissant)
        MagieAttaqueDistance.__init__(self,skill,agissant)

class MagieAttaqueVariableDirigee(MagieAttaqueVariable,MagieAttaqueDirigee):
    """La magie qui crée une explosion de mana dirigée."""
    def __init__(self,skill:Actif,agissant:Agissant):
        MagieAttaqueVariable.__init__(self,skill,agissant)
        MagieAttaqueDirigee.__init__(self,skill,agissant)

class MagieAttaqueVariableDistanceDirigee(MagieAttaqueVariable,MagieAttaqueDistanceDirigee):
    """La magie qui crée une explosion de mana à distance dirigée."""
    def __init__(self,skill:Actif,agissant:Agissant):
        MagieAttaqueVariable.__init__(self,skill,agissant)
        MagieAttaqueDistanceDirigee.__init__(self,skill,agissant)

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
