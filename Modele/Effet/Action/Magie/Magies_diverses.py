from __future__ import annotations
from typing import TYPE_CHECKING, List, Optional, Set
import carte as crt

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ....entitee.agissant.agissant import Agissant
    from ....entitee.item.item import Item
    from ....systeme.skill.actif import Actif
    from ....labyrinthe.case import Case

# Imports des classes parentes
from ..action import Non_repetable
from .magie import Magie, Cible_agissant, Cible_agissants, Cible_cases

class Magie_blizzard(Magie):
    """La magie qui crée un effet de blizzard autour de l'agissant."""
    nom = "magie blizzard"
    def __init__(self,skill:Actif,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,portee:float,gain_latence:float,niveau:int):
        Magie.__init__(self,skill,agissant,gain_xp,cout_pm,latence,niveau)
        self.portee = portee
        self.gain_latence = gain_latence

    def action(self):
        zone = self.agissant.labyrinthe.a_portee(self.agissant.position,self.portee,Deplacement.SPATIAL,Forme.CERCLE,Passage(False,False,False,False,False))
        for position in zone:
            self.agissant.labyrinthe.get_case(position).effets.add(Blizzard(self.niveau,self.gain_latence))

class Magie_obscurite(Magie):
    """La magie qui crée un effet d'obscurite autour de l'agissant."""
    nom = "magie obscurite"
    def __init__(self,skill:Actif,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,portee:float,gain_opacite:float,niveau:int):
        Magie.__init__(self,skill,agissant,gain_xp,cout_pm,latence,niveau)
        self.portee = portee
        self.gain_opacite = gain_opacite

    def action(self):
        zone = self.agissant.labyrinthe.a_portee(self.agissant.position,self.portee,Deplacement.SPATIAL,Forme.CERCLE,Passage(False,False,False,False,False))
        for position in zone:
            self.agissant.labyrinthe.get_case(position).effets.add(Obscurite(self.niveau,self.gain_opacite))

class Magie_instakill(Cible_agissant, Non_repetable):
    """La magie qui crée un effet d'instakill sur un agissant."""
    nom = "magie instakill"
    def __init__(self,skill:Actif,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,superiorite:float,niveau:int,cible:Optional[Agissant]=None):
        Magie.__init__(self,skill,agissant,gain_xp,cout_pm,latence,niveau)
        Cible_agissant.__init__(self,cible)
        self.superiorite = superiorite

    def action(self):
        if self.cible is None:
            self.interrompt()
        else:
            self.cible.effets.append(Instakill(self.agissant,self.agissant.priorite - self.superiorite))

class Magie_protection_sacree(Cible_agissants):
    """La magie qui crée un effet de protection sacrée sur des agissants."""
    nom = "magie protection sacrée"
    def __init__(self,skill:Actif,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,duree:float,pv:float,niveau:int,cible:List[Agissant]=[]):
        Magie.__init__(self,skill,agissant,gain_xp,cout_pm,latence,niveau)
        Cible_agissants.__init__(self,cible)
        self.duree = duree
        self.pv = pv

    def action(self):
        if self.cible == []:
            self.interrompt()
        else:
            for cible in self.cible:
                cible.effets.append(ProtectionSacree(self.duree,self.pv)) #Ajouter une direction ?

class Magie_teleportation(Cible_cases, Non_repetable):
    """La magie qui téléporte des entitées."""
    nom = "magie téléportation"
    def __init__(self,skill:Actif,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,niveau:int,cases:List[crt.Position]=[]):
        Magie.__init__(self,skill,agissant,gain_xp,cout_pm,latence,niveau)
        Cible_cases.__init__(self,cases)

    def action(self):
        if self.cible == []:
            self.interrompt()
        else:
            agissants : List[Optional[Agissant]] = []
            items : List[Set[Item]] = []
            cases : List[Case] = []
            for position in self.cible:
                case = self.agissant.labyrinthe.get_case(position)
                if case.decors is not None:
                    continue
                cases.append(case)
                if case.agissant is not None:
                    case.part(case.agissant)
                agissants.append(case.agissant)
                items.append(case.items)
                case.items = set()
            
            for i in range(len(cases)):
                agissant = agissants[i]
                if agissant is not None:
                    cases[i-1].arrive(agissant)
                    agissant.position = cases[i-1].position
                cases[i-1].items = items[i]
                for item in cases[i-1].items:
                    item.position = cases[i-1].position

# Imports utilisés dans le code
from ...effets_divers import Instakill, Blizzard, Obscurite
from ...effets_protection import ProtectionSacree
from ....labyrinthe.deplacement import Deplacement
from ....labyrinthe.forme import Forme
from ....labyrinthe.passage import Passage