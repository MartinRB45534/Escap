from __future__ import annotations
from typing import TYPE_CHECKING, List, Optional
import Carte as crt

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ...Entitee.Agissant.Agissant import Agissant
    from ...Systeme.Skill.Actif import Actif

# Imports des classes parentes
from ..Action import Non_repetable
from .Magie import Magie, Cible_agissant, Cible_agissants, Cible_cases

class Magie_blizzard(Magie):
    """La magie qui crée un effet de blizzard autour de l'agissant."""
    nom = "magie blizzard"
    def __init__(self,skill:Actif,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,portee:float,niveau:int):
        Magie.__init__(self,skill,agissant,gain_xp,cout_pm,latence,niveau)
        self.portee = portee

    def action(self):
        cases = self.agissant.controleur.get_cases_touches(self.agissant.position,self.portee)
        for case in cases:
            case.effets.append(Blizzard(self.niveau))

class Magie_obscurite(Magie):
    """La magie qui crée un effet d'obscurite autour de l'agissant."""
    nom = "magie obscurite"
    def __init__(self,skill:Actif,agissant:Agissant,niveau:int,gain_xp:float,cout_pm:float,latence:float,portee:float):
        Magie.__init__(self,skill,agissant,gain_xp,cout_pm,latence,niveau)
        self.portee = portee

    def action(self):
        cases = self.agissant.controleur.get_cases_touches(self.agissant.position,self.portee)
        for case in cases:
            case.effets.append(Obscurite(self.niveau))

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
                cible.effets.append(Protection_sacree(self.duree,self.pv)) #Ajouter une direction ?

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
            for i in range(len(self.cible)):
                for agissant in self.agissant.controleur.trouve_occupants(self.cible[i]):
                    agissant.effets.append(Teleport(self.cible[i-1]))

# Imports utilisés dans le code
from ...Effet.Effets_mouvement.Deplacements import Teleport
from ...Effet.Effets_divers import Instakill, Blizzard, Obscurite
from ...Effet.Effets_protection import Protection_sacree