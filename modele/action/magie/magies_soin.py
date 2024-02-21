"""
Les magies de soin (et de résurection/réanimation).
"""

from __future__ import annotations
from typing import TYPE_CHECKING
import carte as crt

# Imports des classes parentes
from ..action import NonRepetable
from .magie import CibleAgissant,CibleCase,CibleItem,PorteeLimitee,ActionMagie,CibleAgissants

# Imports utilisés dans le code
from ...entitee.item.cadavre import Cadavre
from ...effet import Reanimation, Resurection, Soin, SoinCase
from ...commons import Deplacement, Forme, Passage

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ...entitee import Agissant
    from ...systeme import Actif, Magie

class ActionMagieAutoSoin(ActionMagie):
    """La magie qui invoque un effet de soin sur son self.agissant."""
    def __init__(self,skill:Actif,magie:Magie,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,gain_pv:float):
        ActionMagie.__init__(self,skill,magie,agissant,gain_xp,cout_pm,latence)
        self.gain_pv = gain_pv

    def action(self):
        self.agissant.effets.append(Soin(self.agissant,self.gain_pv))

class ActionMagieSoin(ActionMagieAutoSoin, CibleAgissant):
    """La magie qui invoque un effet de soin sur un agissant ciblé."""
    def __init__(self,skill:Actif,magie:Magie,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,gain_pv:float):
        ActionMagieAutoSoin.__init__(self,skill,magie,agissant,gain_xp,cout_pm,latence,gain_pv)
        CibleAgissant.__init__(self,skill,magie,agissant,gain_xp,cout_pm,latence)

    def action(self):
        if not self.cible: # NOONE is falsy
            self.interrompt()
        else:
            self.cible.effets.append(Soin(self.agissant,self.gain_pv))

class ActionMagieMultiSoin(ActionMagieAutoSoin, CibleAgissants):
    """La magie qui invoque un effet de soin sur des agissants ciblés."""
    def __init__(self,skill:Actif,magie:Magie,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,gain_pv:float):
        ActionMagieAutoSoin.__init__(self,skill,magie,agissant,gain_xp,cout_pm,latence,gain_pv)
        CibleAgissants.__init__(self,skill,magie,agissant,gain_xp,cout_pm,latence)

    def action(self):
        for cible in self.cible:
            cible.effets.append(Soin(self.agissant,self.gain_pv))

class ActionMagieSoinDeZone(ActionMagieAutoSoin, CibleCase):
    """La magie qui invoque un effet de soin sur une zone."""
    def __init__(self,skill:Actif,magie:Magie,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,gain_pv:float,portee:float):
        ActionMagieAutoSoin.__init__(self,skill,magie,agissant,gain_xp,cout_pm,latence,gain_pv)
        CibleCase.__init__(self,skill,magie,agissant,gain_xp,cout_pm,latence)
        self.portee = portee

    def action(self):
        if self.cible == crt.POSITION_ABSENTE:
            self.interrompt()
        else:
            poss = self.agissant.labyrinthe.a_portee(self.cible,self.portee,Deplacement.SPATIAL,Forme.CERCLE,Passage(True, False, False, True, True))
            for pos in poss:
                case = self.agissant.labyrinthe.get_case(pos)
                case.effets.add(SoinCase(self.gain_pv,self.agissant))

magies_soin: dict[tuple[bool, bool, bool], type[ActionMagieAutoSoin]] = {
    (False, False, False): ActionMagieAutoSoin,
    (True, False, False): ActionMagieSoin,
    (True, True, False): ActionMagieMultiSoin,
    (False, True, False): ActionMagieAutoSoin, # Pas possible
    (True, False, True): ActionMagieSoin, # Pas possible
    (False, False, True): ActionMagieSoinDeZone,
    (True, True, True): ActionMagieAutoSoin, # Pas possible
    (False, True, True): ActionMagieAutoSoin # Pas possible
}
"""
(cible, cible_multiple, zone) -> ActionMagieAutoSoin
"""

class ActionMagieResurection(CibleItem, NonRepetable):
    """La magie qui invoque un effet de resurection."""
    def __init__(self,skill:Actif,magie:Magie,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float):
        CibleItem.__init__(self,skill,magie,agissant,gain_xp,cout_pm,latence)
        NonRepetable.__init__(self,agissant,latence)

    def action(self):
        if not self.cible: # NOTHING is falsy
            self.interrompt()
        else:
            assert isinstance(self.cible, Cadavre)
            self.cible.effets.append(Resurection())

class ActionMagieResurectionCase(CibleCase,PorteeLimitee):
    """La magie qui invoque un effet de resurection sur une case."""
    def __init__(self,skill:Actif,magie:Magie,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,portee_limite:float):
        CibleCase.__init__(self,skill,magie,agissant,gain_xp,cout_pm,latence)
        PorteeLimitee.__init__(self,skill,magie,agissant,gain_xp,cout_pm,latence,portee_limite)

    def action(self):
        if self.cible == crt.POSITION_ABSENTE:
            self.interrompt()
        else:
            case = self.agissant.labyrinthe.get_case(self.cible)
            for item in case.items:
                if isinstance(item,Cadavre):
                    item.effets.append(Resurection())

class ActionMagieResurectionDeZone(CibleCase,PorteeLimitee):
    """La magie qui invoque un effet de resurection sur tous les cadavres d'une zone."""
    def __init__(self,skill:Actif,magie:Magie,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,portee:float,portee_limite:float):
        CibleCase.__init__(self,skill,magie,agissant,gain_xp,cout_pm,latence)
        PorteeLimitee.__init__(self,skill,magie,agissant,gain_xp,cout_pm,latence,portee_limite)
        self.portee = portee

    def action(self):
        if self.cible == crt.POSITION_ABSENTE:
            self.interrompt()
        else:
            zone = self.agissant.labyrinthe.a_portee(self.cible,self.portee,Deplacement.SPATIAL,Forme.CERCLE,Passage(True, False, False, True, True))
            for position in zone:
                for item in self.agissant.labyrinthe.get_case(position).items:
                    if isinstance(item,Cadavre):
                        item.effets.append(Resurection())

magies_resurection: dict[tuple[bool, bool],
    type[ActionMagieResurection|ActionMagieResurectionCase|ActionMagieResurectionDeZone]] = {
    (False, False): ActionMagieResurection,
    (True, False): ActionMagieResurectionCase,
    (True, True): ActionMagieResurectionDeZone,
    (False, True): ActionMagieResurection # Pas possible
}
"""
(case, zone) -> ActionMagieResurection
"""

class ActionMagieReanimation(CibleItem, NonRepetable):
    """La magie qui invoque un effet de reanimation."""
    def __init__(self,skill:Actif,magie:Magie,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,taux_pv:float,superiorite:float):
        CibleItem.__init__(self,skill,magie,agissant,gain_xp,cout_pm,latence)
        NonRepetable.__init__(self,agissant,latence)
        self.taux_pv = taux_pv
        self.superiorite = superiorite

    def action(self):
        if not self.cible: # NOTHING is falsy
            self.interrompt()
        else:
            assert isinstance(self.cible, Cadavre)
            if self.cible.priorite+self.superiorite < self.agissant.priorite:
                self.cible.effets.append(Reanimation(self.taux_pv,self.agissant.esprit))

class ActionMagieReanimationCase(CibleCase,PorteeLimitee):
    """La magie qui invoque un effet de reanimation sur une case."""
    def __init__(self,skill:Actif,magie:Magie,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,taux_pv:float,superiorite:float,portee_limite:float):
        CibleCase.__init__(self,skill,magie,agissant,gain_xp,cout_pm,latence)
        PorteeLimitee.__init__(self,skill,magie,agissant,gain_xp,cout_pm,latence,portee_limite)
        self.taux_pv = taux_pv
        self.superiorite = superiorite

    def action(self):
        if self.cible == crt.POSITION_ABSENTE:
            self.interrompt()
        else:
            case = self.agissant.labyrinthe.get_case(self.cible)
            for item in case.items:
                if isinstance(item,Cadavre):
                    if item.priorite+self.superiorite < self.agissant.priorite:
                        item.effets.append(Reanimation(self.taux_pv,self.agissant.esprit))

class ActionMagieReanimationDeZone(CibleCase,PorteeLimitee):
    """La magie qui invoque un effet de reanimation sur tous les cadavres d'une zone."""
    def __init__(self,skill:Actif,magie:Magie,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,taux_pv:float,portee:float,portee_limite:float,superiorite:float):
        CibleCase.__init__(self,skill,magie,agissant,gain_xp,cout_pm,latence)
        PorteeLimitee.__init__(self,skill,magie,agissant,gain_xp,cout_pm,latence,portee_limite)
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

magies_reanimation: dict[tuple[bool, bool], type[ActionMagie]] = {
    (False, False): ActionMagieReanimation,
    (True, False): ActionMagieReanimationCase,
    (True, True): ActionMagieReanimationDeZone,
    (False, True): ActionMagieReanimation # Pas possible
}
"""
(case, zone) -> ActionMagieReanimation
"""
