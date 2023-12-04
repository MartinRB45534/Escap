"""
Contient trois magies à coût ajustable.
"""

from __future__ import annotations
from typing import TYPE_CHECKING

# Imports des classes parentes
from .magie import MagieCout
from .magies_attaque.attaques_corps_a_corps import MagieAttaqueCorpACorp

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

class MagieExplosionDeMana(MagieCout,MagieAttaqueCorpACorp):
    """La magie qui crée une explosion de mana."""
    nom = "magie explosion de mana"
    def __init__(self,skill:Actif,agissant:Agissant,gain_xp:float,latence:float,taux_degats:float,portee:float,element:Element):
        MagieCout.__init__(self,skill,agissant,gain_xp,0,latence)
        MagieAttaqueCorpACorp.__init__(self,skill,agissant,gain_xp,0,portee,0,element,Deplacement.MAGIQUE,Forme.CERCLE,Passage(False, True, True, False, True),latence)
        self.taux_degats = taux_degats

    def set_cout(self,cout:float):
        super().set_cout(cout)
        self.degats = cout*self.taux_degats
