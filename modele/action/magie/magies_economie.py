"""
Contient trois magies à coût ajustable.
"""

from __future__ import annotations

# Imports des classes parentes
from .magie import MagieCout
from .magies_attaques import MagieAttaque, MagieAttaqueDistance, MagieAttaqueDirigee, MagieAttaqueDistanceDirigee

# Imports utilisés dans le code
from ...effet import ReserveMana,InvestissementMana

class MagieReserve(MagieCout):
    """La magie qui fait une réserve de mana."""
    taux: float

    def action(self):
        self.agissant.effets.add(ReserveMana(self.agissant,self.cout*self.taux))

class MagieInvestissement(MagieCout):
    """La magie qui crée un investissement."""
    taux: float
    duree: float

    def action(self):
        self.agissant.effets.add(InvestissementMana(self.duree,self.cout*self.taux))

class MagieAttaqueVariable(MagieCout,MagieAttaque):
    """La magie qui crée une explosion de mana."""
    taux_degats: float

    def set_cout(self,cout:float):
        MagieCout.set_cout(self,cout)
        self.degats = cout*self.taux_degats

class MagieAttaqueVariableDistance(MagieAttaqueVariable,MagieAttaqueDistance):
    """La magie qui crée une explosion de mana à distance."""

class MagieAttaqueVariableDirigee(MagieAttaqueVariable,MagieAttaqueDirigee):
    """La magie qui crée une explosion de mana dirigée."""

class MagieAttaqueVariableDistanceDirigee(MagieAttaqueVariable,MagieAttaqueDistanceDirigee):
    """La magie qui crée une explosion de mana à distance dirigée."""

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
