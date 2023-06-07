from __future__ import annotations
from typing import TYPE_CHECKING

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ...Entitee.Agissant.Agissant import Agissant
    from ...Systeme.Skill.Actif import Actif
    from ...Systeme.Elements import Element

# Imports des classes parentes
from .Magie import Magie, Magie_cout
from .Magies_attaque.Attaques_corps_a_corps import Magie_attaque_corp_a_corp

class Magie_reserve(Magie_cout):
    """La magie qui fait une réserve de mana."""
    nom = "magie reserve"
    def __init__(self,skill:Actif,agissant:Agissant,gain_xp:float,latence:float,taux:float,niveau:int):
        Magie.__init__(self,skill,agissant,gain_xp,0,latence,niveau)
        self.taux = taux

    def action(self):
        self.agissant.effets.append(Reserve_mana(self.cout*self.taux))

class Magie_investissement(Magie_cout):
    """La magie qui crée un investissement."""
    nom = "magie investissement"
    def __init__(self,skill:Actif,agissant:Agissant,gain_xp:float,latence:float,taux:float,duree:float,niveau:int):
        Magie.__init__(self,skill,agissant,gain_xp,0,latence,niveau)
        self.duree = duree
        self.taux = taux

    def action(self):
        self.agissant.effets.append(Investissement_mana(self.duree,self.cout*self.taux))

class Magie_explosion_de_mana(Magie_cout,Magie_attaque_corp_a_corp):
    """La magie qui crée une explosion de mana."""
    nom = "magie explosion de mana"
    def __init__(self,skill:Actif,agissant:Agissant,gain_xp:float,latence:float,taux_degats:float,portee:float,element:Element,niveau:int):
        Magie_attaque_corp_a_corp.__init__(self,skill,agissant,gain_xp,0,portee,0,element,"C__S___",latence,niveau)
        self.taux_degats = taux_degats

    def set_cout(self,cout:float):
        super().set_cout(cout)
        self.degats = cout*self.taux_degats

# Imports utilisés dans le code
from ...Effet.Effets_divers import Reserve_mana,Investissement_mana