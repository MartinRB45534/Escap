"""
Les magies de soin (et de résurection/réanimation).
"""

from __future__ import annotations
import carte as crt

# Imports des classes parentes
from ..action import NonRepetable
from .magie import CibleAgissant,CibleCase,CibleItem,PorteeLimitee,Magie,CibleAgissants

# Imports utilisés dans le code
from ...effet import Reanimation, Resurection, Soin, SoinCase
from ...commons import Deplacement, Forme, Passage

class MagieAutoSoin(Magie):
    """La magie qui invoque un effet de soin sur son self.agissant."""
    gain_pv: float

    def action(self):
        self.agissant.effets.add(Soin(self.agissant,self.gain_pv))

class MagieSoin(MagieAutoSoin, CibleAgissant):
    """La magie qui invoque un effet de soin sur un agissant ciblé."""

    def action(self):
        if not self.cible: # NOONE is falsy
            self.interrompt()
        else:
            self.cible.effets.add(Soin(self.agissant,self.gain_pv))

class MagieMultiSoin(MagieAutoSoin, CibleAgissants):
    """La magie qui invoque un effet de soin sur des agissants ciblés."""

    def action(self):
        for cible in self.cible:
            cible.effets.add(Soin(self.agissant,self.gain_pv))

class MagieSoinDeZone(MagieAutoSoin, CibleCase):
    """La magie qui invoque un effet de soin sur une zone."""
    portee: float

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

    def action(self):
        if not self.cible: # NOTHING is falsy
            self.interrompt()
        else:
            self.cible.effets.add(Resurection())

class MagieResurectionCase(MagieResurection, CibleCase, PorteeLimitee):
    """La magie qui invoque un effet de resurection sur une case."""

    def action(self):
        if self.cible == crt.POSITION_ABSENTE:
            self.interrompt()
        else:
            case = self.agissant.labyrinthe.get_case(self.cible)
            for item in case.items:
                if item.cadavre:
                    item.effets.add(Resurection())

class MagieResurectionDeZone(MagieResurection, CibleCase, PorteeLimitee):
    """La magie qui invoque un effet de resurection sur tous les cadavres d'une zone."""
    portee: float

    def action(self):
        if self.cible == crt.POSITION_ABSENTE:
            self.interrompt()
        else:
            zone = self.agissant.labyrinthe.a_portee(self.cible,self.portee,Deplacement.SPATIAL,Forme.CERCLE,Passage(True, False, False, True, True))
            for position in zone:
                for item in self.agissant.labyrinthe.get_case(position).items:
                    if item.cadavre:
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

    def action(self):
        if not self.cible: # NOTHING is falsy
            self.interrompt()
        else:
            if self.cible.priorite+self.superiorite < self.agissant.priorite:
                self.cible.effets.add(Reanimation(self.taux_pv,self.agissant.esprit))

class MagieReanimationCase(MagieReanimation, CibleCase, PorteeLimitee):
    """La magie qui invoque un effet de reanimation sur une case."""

    def action(self):
        if self.cible == crt.POSITION_ABSENTE:
            self.interrompt()
        else:
            case = self.agissant.labyrinthe.get_case(self.cible)
            for item in case.items:
                if item.cadavre:
                    if item.priorite+self.superiorite < self.agissant.priorite:
                        item.effets.add(Reanimation(self.taux_pv,self.agissant.esprit))

class MagieReanimationDeZone(MagieReanimation, CibleCase, PorteeLimitee):
    """La magie qui invoque un effet de reanimation sur tous les cadavres d'une zone."""
    portee: float

    def action(self):
        if self.cible == crt.POSITION_ABSENTE:
            self.interrompt()
        else:
            zone = self.agissant.labyrinthe.a_portee(self.cible,self.portee,Deplacement.SPATIAL,Forme.CERCLE,Passage(True, False, False, True, True))
            for position in zone:
                for item in self.agissant.labyrinthe.get_case(position).items:
                    if item.cadavre:
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
