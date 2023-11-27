"""
Les magies de soin (et de résurection/réanimation).
"""

from __future__ import annotations
from typing import TYPE_CHECKING
import carte as crt

# Imports des classes parentes
from ..action import NonRepetable
from .magie import CibleAgissant,CibleCase,CibleItem,PorteeLimitee,Magie,CibleAgissants

# Imports utilisés dans le code
from ...entitee.item.cadavre import Cadavre
from ...effet import Reanimation, Resurection, Soin, SoinCase
from ...commons import Deplacement, Forme, Passage

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ...entitee.agissant.agissant import Agissant
    from ...systeme.skill.actif import Actif

class MagieSoin(CibleAgissant):
    """La magie qui invoque un effet de soin sur un agissant ciblé."""
    nom = "magie soin"
    def __init__(self,skill:Actif,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,gain_pv:float,niveau:int,cible:Agissant):
        CibleAgissant.__init__(self,skill,agissant,gain_xp,cout_pm,latence,niveau,cible)
        self.gain_pv = gain_pv

    def action(self):
        if not self.cible: # NOONE is falsy
            self.interrompt()
        else:
            self.cible.effets.append(Soin(self.agissant,self.gain_pv))

class MagieMultiSoin(CibleAgissants):
    """La magie qui invoque un effet de soin sur des agissants ciblés."""
    nom = "magie multi soin"
    def __init__(self,skill:Actif,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,gain_pv:float,niveau:int,cible:list[Agissant]):
        CibleAgissants.__init__(self,skill,agissant,gain_xp,cout_pm,latence,niveau,cible)
        self.gain_pv = gain_pv

    def action(self):
        for cible in self.cible:
            cible.effets.append(Soin(self.agissant,self.gain_pv))

class MagieSoinDeZone(CibleCase):
    """La magie qui invoque un effet de soin sur une zone."""
    nom = "magie zone de soin"
    def __init__(self,niveau:int,skill:Actif,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,gain_pv:float,portee:float,case:crt.Position=crt.POSITION_ABSENTE):
        CibleCase.__init__(self,skill,agissant,gain_xp,cout_pm,latence,niveau,case)
        self.gain_pv = gain_pv
        self.portee = portee

    def action(self):
        if self.cible == crt.POSITION_ABSENTE:
            self.interrompt()
        else:
            poss = self.agissant.labyrinthe.a_portee(self.cible,self.portee,Deplacement.SPATIAL,Forme.CERCLE,Passage(True, False, False, True, True))
            for pos in poss:
                case = self.agissant.labyrinthe.get_case(pos)
                case.effets.add(SoinCase(self.gain_pv,self.agissant))

class MagieAutoSoin(Magie):
    """La magie qui invoque un effet de soin sur son self.agissant."""
    nom = "magie auto soin"
    def __init__(self,skill:Actif,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,gain_pv:float,niveau:int):
        Magie.__init__(self,skill,agissant,gain_xp,cout_pm,latence,niveau)
        self.gain_pv = gain_pv
        self.niveau = niveau

class MagieResurection(CibleItem, NonRepetable):
    """La magie qui invoque un effet de resurection."""
    nom = "magie resurection"
    def __init__(self,skill:Actif,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,niveau:int,item:Cadavre):
        CibleItem.__init__(self,skill,agissant,gain_xp,cout_pm,latence,niveau,item)
        NonRepetable.__init__(self,agissant,latence)

    def action(self):
        if not self.cible: # NOTHING is falsy
            self.interrompt()
        else:
            assert isinstance(self.cible, Cadavre)
            self.cible.effets.append(Resurection())

class MagieReanimationDeZone(CibleCase,PorteeLimitee):
    """La magie qui invoque un effet de reanimation sur tous les cadavres d'une zone."""
    nom = "magie reanimation"
    def __init__(self,niveau:int,skill:Actif,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,taux_pv:float,portee:float,portee_limite:float,superiorite:int,case:crt.Position=crt.POSITION_ABSENTE):
        CibleCase.__init__(self,skill,agissant,gain_xp,cout_pm,latence,niveau,case)
        PorteeLimitee.__init__(self,skill,agissant,gain_xp,cout_pm,latence,niveau,portee_limite)
        self.taux_pv = taux_pv
        self.portee = portee
        self.superiorite = superiorite

    def action(self):
        if self.cible == crt.POSITION_ABSENTE:
            self.interrompt()
        else:
            zone = self.agissant.labyrinthe.a_portee(self.cible,self.portee,Deplacement.SPATIAL,Forme.CERCLE,Passage(True, False, False, True, True))
            for position in zone:
                for item in self.agissant.labyrinthe.get_case(position).items:
                    if isinstance(item,Cadavre):
                        if item.priorite+self.superiorite < self.agissant.priorite:
                            item.effets.append(Reanimation(self.taux_pv,self.agissant.esprit))
