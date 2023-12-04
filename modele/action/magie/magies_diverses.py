"""
Quelques magies diverses.
"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import carte as crt

# Imports des classes parentes
from ..action import NonRepetable
from .magie import Magie, CibleAgissant, CibleAgissants, CibleCases

# Imports utilisés dans le code
from ...effet import Instakill, Blizzard, Obscurite, ProtectionElement
from ...commons import Deplacement, Forme, Passage, Element

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ...entitee.agissant.agissant import Agissant
    from ...entitee.item.item import Item
    from ...systeme.skill.actif import Actif
    from ...labyrinthe.case import Case

class MagieBlizzard(Magie):
    """La magie qui crée un effet de blizzard autour de l'agissant."""
    nom = "magie blizzard"
    def __init__(self,skill:Actif,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,portee:float,duree:float,gain_latence:float):
        Magie.__init__(self,skill,agissant,gain_xp,cout_pm,latence)
        self.portee = portee
        self.duree = duree
        self.gain_latence = gain_latence

    def action(self):
        zone = self.agissant.labyrinthe.a_portee(self.agissant.position,self.portee,Deplacement.SPATIAL,Forme.CERCLE,Passage(False,False,False,False,False))
        for position in zone:
            case = self.agissant.labyrinthe.get_case(position)
            case.effets.add(Blizzard(self.duree,self.gain_latence))

class MagieObscurite(Magie):
    """La magie qui crée un effet d'obscurite autour de l'agissant."""
    nom = "magie obscurite"
    def __init__(self,skill:Actif,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,portee:float,duree:float,gain_opacite:float):
        Magie.__init__(self,skill,agissant,gain_xp,cout_pm,latence)
        self.portee = portee
        self.duree = duree
        self.gain_opacite = gain_opacite

    def action(self):
        zone = self.agissant.labyrinthe.a_portee(self.agissant.position,self.portee,Deplacement.SPATIAL,Forme.CERCLE,Passage(False,False,False,False,False))
        for position in zone:
            case = self.agissant.labyrinthe.get_case(position)
            case.effets.add(Obscurite(self.duree,self.gain_opacite))

class MagieInstakill(CibleAgissant, NonRepetable):
    """La magie qui crée un effet d'instakill sur un agissant."""
    nom = "magie instakill"
    def __init__(self,skill:Actif,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,superiorite:float,cible:Agissant):
        CibleAgissant.__init__(self,skill,agissant,gain_xp,cout_pm,latence,cible)
        NonRepetable.__init__(self,agissant,latence)
        self.superiorite = superiorite

    def action(self):
        if not self.cible: # NOONE is falsy
            self.interrompt()
        else:
            self.cible.effets.append(Instakill(self.agissant,self.agissant.priorite - self.superiorite))

class MagieProtectionSacree(CibleAgissants):
    """La magie qui crée un effet de protection sacrée sur des agissants."""
    nom = "magie protection sacrée"
    def __init__(self,skill:Actif,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,duree:float,pv:float,cible:list[Agissant]):
        CibleAgissants.__init__(self,skill,agissant,gain_xp,cout_pm,latence,cible)
        self.duree = duree
        self.pv = pv

    def action(self):
        if self.cible == []:
            self.interrompt()
        else:
            for cible in self.cible:
                cible.effets.append(ProtectionElement(self.duree,self.pv,Element.OMBRE)) #Ajouter une direction ?

class MagieTeleportation(CibleCases, NonRepetable):
    """La magie qui téléporte des entitées."""
    nom = "magie téléportation"
    def __init__(self,skill:Actif,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,cases:list[crt.Position]):
        CibleCases.__init__(self,skill,agissant,gain_xp,cout_pm,latence,cases)
        NonRepetable.__init__(self,agissant,latence)

    def action(self):
        if self.cible == []:
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
