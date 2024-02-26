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
    from ...entitee import Agissant
    from ...systeme import Actif

class MagieAutoSoin(Magie):
    """La magie qui invoque un effet de soin sur son self.agissant."""
    gain_pv: float
    def __init__(self,skill:Actif,agissant:Agissant):
        Magie.__init__(self,skill,agissant)

    def action(self):
        self.agissant.effets.add(Soin(self.agissant,self.gain_pv))

class MagieSoin(MagieAutoSoin, CibleAgissant):
    """La magie qui invoque un effet de soin sur un agissant ciblé."""
    def __init__(self,skill:Actif,agissant:Agissant):
        MagieAutoSoin.__init__(self,skill,agissant)
        CibleAgissant.__init__(self,skill,agissant)

    def action(self):
        if not self.cible: # NOONE is falsy
            self.interrompt()
        else:
            self.cible.effets.add(Soin(self.agissant,self.gain_pv))

class MagieMultiSoin(MagieAutoSoin, CibleAgissants):
    """La magie qui invoque un effet de soin sur des agissants ciblés."""
    def __init__(self,skill:Actif,agissant:Agissant):
        MagieAutoSoin.__init__(self,skill,agissant)
        CibleAgissants.__init__(self,skill,agissant)

    def action(self):
        for cible in self.cible:
            cible.effets.add(Soin(self.agissant,self.gain_pv))

class MagieSoinDeZone(MagieAutoSoin, CibleCase):
    """La magie qui invoque un effet de soin sur une zone."""
    def __init__(self,skill:Actif,agissant:Agissant,portee:float):
        MagieAutoSoin.__init__(self,skill,agissant)
        CibleCase.__init__(self,skill,agissant)
        self.portee = portee

    def action(self):
        if self.cible == crt.POSITION_ABSENTE:
            self.interrompt()
        else:
            poss = self.agissant.labyrinthe.a_portee(self.cible,self.portee,Deplacement.SPATIAL,Forme.CERCLE,Passage(True, False, False, True, True))
            for pos in poss:
                case = self.agissant.labyrinthe.get_case(pos)
                case.effets.add(SoinCase(self.gain_pv,self.agissant))

magies_soin: dict[tuple[bool, bool, bool], type[MagieAutoSoin]] = {
    (False, False, False): MagieAutoSoin,
    (True, False, False): MagieSoin,
    (True, True, False): MagieMultiSoin,
    (False, True, False): MagieAutoSoin, # Pas possible
    (True, False, True): MagieSoin, # Pas possible
    (False, False, True): MagieSoinDeZone,
    (True, True, True): MagieAutoSoin, # Pas possible
    (False, True, True): MagieAutoSoin # Pas possible
}
"""
(cible, cible_multiple, zone) -> MagieAutoSoin
"""

class MagieResurection(Magie):
    """La magie qui invoque un effet de resurection."""

class MagieResurectionItem(MagieResurection, CibleItem, NonRepetable):
    """La magie qui invoque un effet de resurection."""
    def __init__(self,skill:Actif,agissant:Agissant):
        MagieResurection.__init__(self,skill,agissant)
        CibleItem.__init__(self,skill,agissant)
        NonRepetable.__init__(self,agissant)

    def action(self):
        if not self.cible: # NOTHING is falsy
            self.interrompt()
        else:
            assert isinstance(self.cible, Cadavre)
            self.cible.effets.add(Resurection())

class MagieResurectionCase(MagieResurection, CibleCase, PorteeLimitee):
    """La magie qui invoque un effet de resurection sur une case."""
    def __init__(self,skill:Actif,agissant:Agissant):
        MagieResurection.__init__(self,skill,agissant)
        CibleCase.__init__(self,skill,agissant)
        PorteeLimitee.__init__(self,skill,agissant)

    def action(self):
        if self.cible == crt.POSITION_ABSENTE:
            self.interrompt()
        else:
            case = self.agissant.labyrinthe.get_case(self.cible)
            for item in case.items:
                if isinstance(item,Cadavre):
                    item.effets.add(Resurection())

class MagieResurectionDeZone(MagieResurection, CibleCase, PorteeLimitee):
    """La magie qui invoque un effet de resurection sur tous les cadavres d'une zone."""
    portee: float
    def __init__(self,skill:Actif,agissant:Agissant):
        MagieResurection.__init__(self,skill,agissant)
        CibleCase.__init__(self,skill,agissant)
        PorteeLimitee.__init__(self,skill,agissant)

    def action(self):
        if self.cible == crt.POSITION_ABSENTE:
            self.interrompt()
        else:
            zone = self.agissant.labyrinthe.a_portee(self.cible,self.portee,Deplacement.SPATIAL,Forme.CERCLE,Passage(True, False, False, True, True))
            for position in zone:
                for item in self.agissant.labyrinthe.get_case(position).items:
                    if isinstance(item,Cadavre):
                        item.effets.add(Resurection())

magies_resurection: dict[tuple[bool, bool],
    type[MagieResurection]] = {
    (False, False): MagieResurectionItem,
    (True, False): MagieResurectionCase,
    (True, True): MagieResurectionDeZone,
    (False, True): MagieResurectionItem # Pas possible
}
"""
(case, zone) -> MagieResurection
"""

class MagieReanimation(Magie):
    """La magie qui invoque un effet de reanimation."""
    taux_pv: float
    superiorite: float

class MagieReanimationItem(MagieReanimation, CibleItem, NonRepetable):
    """La magie qui invoque un effet de reanimation."""
    def __init__(self,skill:Actif,agissant:Agissant):
        MagieReanimation.__init__(self,skill,agissant)
        CibleItem.__init__(self,skill,agissant)
        NonRepetable.__init__(self,agissant)

    def action(self):
        if not self.cible: # NOTHING is falsy
            self.interrompt()
        else:
            assert isinstance(self.cible, Cadavre)
            if self.cible.priorite+self.superiorite < self.agissant.priorite:
                self.cible.effets.add(Reanimation(self.taux_pv,self.agissant.esprit))

class MagieReanimationCase(MagieReanimation, CibleCase, PorteeLimitee):
    """La magie qui invoque un effet de reanimation sur une case."""
    def __init__(self,skill:Actif,agissant:Agissant):
        MagieReanimation.__init__(self,skill,agissant)
        CibleCase.__init__(self,skill,agissant)
        PorteeLimitee.__init__(self,skill,agissant)

    def action(self):
        if self.cible == crt.POSITION_ABSENTE:
            self.interrompt()
        else:
            case = self.agissant.labyrinthe.get_case(self.cible)
            for item in case.items:
                if isinstance(item,Cadavre):
                    if item.priorite+self.superiorite < self.agissant.priorite:
                        item.effets.add(Reanimation(self.taux_pv,self.agissant.esprit))

class MagieReanimationDeZone(MagieReanimation, CibleCase, PorteeLimitee):
    """La magie qui invoque un effet de reanimation sur tous les cadavres d'une zone."""
    portee: float
    def __init__(self,skill:Actif,agissant:Agissant):
        MagieReanimation.__init__(self,skill,agissant)
        CibleCase.__init__(self,skill,agissant)
        PorteeLimitee.__init__(self,skill,agissant)

    def action(self):
        if self.cible == crt.POSITION_ABSENTE:
            self.interrompt()
        else:
            zone = self.agissant.labyrinthe.a_portee(self.cible,self.portee,Deplacement.SPATIAL,Forme.CERCLE,Passage(True, False, False, True, True))
            for position in zone:
                for item in self.agissant.labyrinthe.get_case(position).items:
                    if isinstance(item,Cadavre):
                        if item.priorite+self.superiorite < self.agissant.priorite:
                            item.effets.add(Reanimation(self.taux_pv,self.agissant.esprit))

magies_reanimation: dict[tuple[bool, bool],
    type[MagieReanimation]] = {
    (False, False): MagieReanimationItem,
    (True, False): MagieReanimationCase,
    (True, True): MagieReanimationDeZone,
    (False, True): MagieReanimationItem # Pas possible
}
"""
(case, zone) -> MagieReanimation
"""
