"""
Quelques magies diverses.
"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional

# Imports des classes parentes
from ..action import NonRepetable
from .magie import Magie, CibleAgissant, CibleCases

# Imports utilisés dans le code
from ...effet import Instakill, Blizzard, Obscurite
from ...commons import Deplacement, Forme, Passage

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ...entitee import Agissant, Item
    from ...systeme import Actif
    from ...labyrinthe import Case

class MagieBlizzard(Magie):
    """La magie qui crée un effet de blizzard autour de l'agissant."""
    portee: float
    duree: float
    gain_latence: float
    def __init__(self,skill:Actif,agissant:Agissant):
        Magie.__init__(self,skill,agissant)

    def action(self):
        zone = self.agissant.labyrinthe.a_portee(
            self.agissant.position,self.portee,Deplacement.SPATIAL,Forme.CERCLE,
            Passage(False,False,False,False,False))
        for position in zone:
            case = self.agissant.labyrinthe.get_case(position)
            case.effets.add(Blizzard(self.duree,self.gain_latence))

class MagieObscurite(Magie):
    """La magie qui crée un effet d'obscurite autour de l'agissant."""
    portee: float
    duree: float
    gain_opacite: float
    def __init__(self,skill:Actif,agissant:Agissant):
        Magie.__init__(self,skill,agissant)

    def action(self):
        zone = self.agissant.labyrinthe.a_portee(
            self.agissant.position,self.portee,Deplacement.SPATIAL,Forme.CERCLE,
            Passage(False,False,False,False,False))
        for position in zone:
            case = self.agissant.labyrinthe.get_case(position)
            case.effets.add(Obscurite(self.duree,self.gain_opacite))

class MagieInstakill(CibleAgissant, NonRepetable):
    """La magie qui crée un effet d'instakill sur un agissant."""
    superiorite: float
    def __init__(self,skill:Actif,agissant:Agissant):
        CibleAgissant.__init__(self,skill,agissant)
        NonRepetable.__init__(self,agissant)

    def action(self):
        if not self.cible: # NOONE is falsy
            self.interrompt()
        else:
            self.cible.effets.append(
                Instakill(self.agissant,self.agissant.priorite - self.superiorite))

class MagieTeleportation(CibleCases, NonRepetable):
    """La magie qui téléporte des entitées."""
    def __init__(self,skill:Actif,agissant:Agissant):
        CibleCases.__init__(self,skill,agissant)
        NonRepetable.__init__(self,agissant)

    def action(self):
        if not self.cible: # [] is falsy
            self.interrompt()
        else:
            agissants : list[Optional[Agissant]] = []
            items : list[set[Item]] = []
            cases : list[Case] = []
            for position in self.cible:
                case = self.agissant.labyrinthe.get_case(position)
                if case.decors is not None:
                    continue
                cases.append(case)
                agissants.append(case.agissant)
                case.agissant = None
                items.append(case.items)
                case.items = set()

            for i in range(len(cases)):
                agissant = agissants[i]
                if agissant is not None:
                    cases[i-1].agissant_arrive(agissant)
                    agissant.position = cases[i-1].position
                cases[i-1].items = items[i]
                for item in cases[i-1].items:
                    item.position = cases[i-1].position
