"""
Quelques magies diverses.
"""

from __future__ import annotations
from typing import TYPE_CHECKING

# Imports des classes parentes
from .magie import ActionMagie, CibleAgissant, CibleAgissants, CibleCase

# Imports utilisés dans le code
from ...effet import ProtectionElement, ProtectionMur, ProtectionCaseMur, ProtectionCaseElement
from ...commons import Element, Deplacement, Forme, Passage

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ...entitee import Agissant
    from ...systeme import Actif, Magie

class ActionMagieAutoProtection(ActionMagie):
    """La magie qui crée un effet de protection sur l'agissant."""
    def __init__(self,skill:Actif,magie:Magie,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,duree:float,pv:float):
        ActionMagie.__init__(self,skill,magie,agissant,gain_xp,cout_pm,latence)
        self.duree = duree
        self.pv = pv

    def action(self):
        self.agissant.effets.append(ProtectionMur(self.duree,self.pv))

class ActionMagieProtection(CibleAgissant, ActionMagieAutoProtection):
    """La magie qui crée un effet de protection sur un agissant."""
    def __init__(self,skill:Actif,magie:Magie,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,duree:float,pv:float):
        CibleAgissant.__init__(self,skill,magie,agissant,gain_xp,cout_pm,latence)
        ActionMagieAutoProtection.__init__(self,skill,magie,agissant,gain_xp,cout_pm,latence,duree,pv)

    def action(self):
        if not self.cible:
            self.interrompt()
        else:
            self.cible.effets.append(ProtectionMur(self.duree,self.pv))

class ActionMagieMultiProtection(CibleAgissants, ActionMagieAutoProtection):
    """La magie qui crée un effet de protection sur des agissants."""
    def __init__(self,skill:Actif,magie:Magie,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,duree:float,pv:float):
        CibleAgissants.__init__(self,skill,magie,agissant,gain_xp,cout_pm,latence)
        ActionMagieAutoProtection.__init__(self,skill,magie,agissant,gain_xp,cout_pm,latence,duree,pv)

    def action(self):
        if not self.cible: # [] is falsy
            self.interrompt()
        else:
            for cible in self.cible:
                cible.effets.append(ProtectionMur(self.duree,self.pv))

class ActionMagieProtectionGroupe(ActionMagieAutoProtection):
    """La magie qui crée un effet de protection sur des agissants."""
    def __init__(self,skill:Actif,magie:Magie,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,duree:float,pv:float):
        ActionMagieAutoProtection.__init__(self,skill,magie,agissant,gain_xp,cout_pm,latence,duree,pv)

    def action(self):
        for agissant in self.agissant.esprit.corps:
            agissant.effets.append(ProtectionMur(self.duree,self.pv))

class ActionMagieProtectionZone(CibleCase, ActionMagieAutoProtection):
    """La magie qui crée un effet de protection sur une zone."""
    def __init__(self,skill:Actif,magie:Magie,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,duree:float,pv:float,portee:float):
        CibleCase.__init__(self,skill,magie,agissant,gain_xp,cout_pm,latence)
        ActionMagieAutoProtection.__init__(self,skill,magie,agissant,gain_xp,cout_pm,latence,duree,pv)
        self.portee = portee

    def action(self):
        if not self.cible:
            self.interrompt()
        else:
            poss = self.agissant.labyrinthe.a_portee(self.cible,self.portee,Deplacement.SPATIAL,Forme.CERCLE,Passage(True, False, False, True, True))
            for position in poss:
                case = self.agissant.labyrinthe.get_case(position)
                case.effets.add(ProtectionCaseMur(self.duree,self.pv))

class ActionMagieAutoProtectionElement(ActionMagieAutoProtection):
    """La magie qui crée un effet de protection élémentaire sur l'agissant."""
    def __init__(self,skill:Actif,magie:Magie,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,duree:float,pv:float,element:Element,taux:float):
        ActionMagieAutoProtection.__init__(self,skill,magie,agissant,gain_xp,cout_pm,latence,duree,pv)
        self.element = element
        self.taux = taux

    def action(self):
        self.agissant.effets.append(ProtectionElement(self.duree,self.pv,self.element,self.taux))

class ActionMagieProtectionElement(CibleAgissant, ActionMagieAutoProtectionElement):
    """La magie qui crée un effet de protection élémentaire sur un agissant."""
    def __init__(self,skill:Actif,magie:Magie,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,duree:float,pv:float,element:Element,taux:float):
        CibleAgissant.__init__(self,skill,magie,agissant,gain_xp,cout_pm,latence)
        ActionMagieAutoProtectionElement.__init__(self,skill,magie,agissant,gain_xp,cout_pm,latence,duree,pv,element,taux)

    def action(self):
        if not self.cible:
            self.interrompt()
        else:
            self.cible.effets.append(ProtectionElement(self.duree,self.pv,self.element,self.taux))

class ActionMagieMultiProtectionElement(CibleAgissants, ActionMagieAutoProtectionElement):
    """La magie qui crée un effet de protection élémentaire sur des agissants."""
    def __init__(self,skill:Actif,magie:Magie,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,duree:float,pv:float,element:Element,taux:float):
        CibleAgissants.__init__(self,skill,magie,agissant,gain_xp,cout_pm,latence)
        ActionMagieAutoProtectionElement.__init__(self,skill,magie,agissant,gain_xp,cout_pm,latence,duree,pv,element,taux)

    def action(self):
        if not self.cible: # [] is falsy
            self.interrompt()
        else:
            for cible in self.cible:
                cible.effets.append(ProtectionElement(self.duree,self.pv,self.element,self.taux))

class ActionMagieProtectionGroupeElement(ActionMagieAutoProtectionElement):
    """La magie qui crée un effet de protection élémentaire sur des agissants."""
    def __init__(self,skill:Actif,magie:Magie,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,duree:float,pv:float,element:Element,taux:float):
        ActionMagieAutoProtectionElement.__init__(self,skill,magie,agissant,gain_xp,cout_pm,latence,duree,pv,element,taux)

    def action(self):
        for agissant in self.agissant.esprit.corps:
            agissant.effets.append(ProtectionElement(self.duree,self.pv,self.element,self.taux))

class ActionMagieProtectionZoneElement(CibleCase, ActionMagieAutoProtectionElement):
    """La magie qui crée un effet de protection élémentaire sur une zone."""
    def __init__(self,skill:Actif,magie:Magie,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,duree:float,pv:float,element:Element,taux:float,portee:float):
        CibleCase.__init__(self,skill,magie,agissant,gain_xp,cout_pm,latence)
        ActionMagieAutoProtectionElement.__init__(self,skill,magie,agissant,gain_xp,cout_pm,latence,duree,pv,element,taux)
        self.portee = portee

    def action(self):
        if not self.cible:
            self.interrompt()
        else:
            poss = self.agissant.labyrinthe.a_portee(self.cible,self.portee,Deplacement.SPATIAL,Forme.CERCLE,Passage(True, False, False, True, True))
            for position in poss:
                case = self.agissant.labyrinthe.get_case(position)
                case.effets.add(ProtectionCaseElement(self.duree,self.pv,self.element,self.taux))

magies_protection: dict[tuple[bool, bool, bool, bool],type[ActionMagieAutoProtection]] = {
    (False, False, False, False): ActionMagieAutoProtection,
    (True, False, False, False): ActionMagieProtection,
    (True, True, False, False): ActionMagieMultiProtection,
    (False, True, False, False): ActionMagieProtectionGroupe,
    (False, False, True, False): ActionMagieProtectionZone,
    (True, False, True, False): ActionMagieAutoProtection, # Pas possible
    (False, True, True, False): ActionMagieAutoProtection, # Pas possible
    (True, True, True, False): ActionMagieAutoProtection, # Pas possible
    (False, False, False, True): ActionMagieAutoProtectionElement,
    (True, False, False, True): ActionMagieProtectionElement,
    (True, True, False, True): ActionMagieMultiProtectionElement,
    (False, True, False, True): ActionMagieProtectionGroupeElement,
    (False, False, True, True): ActionMagieProtectionZoneElement,
    (True, False, True, True): ActionMagieAutoProtectionElement, # Pas possible
    (False, True, True, True): ActionMagieAutoProtectionElement, # Pas possible
    (True, True, True, True): ActionMagieAutoProtectionElement # Pas possible
}
"""
(cible, cible_multiple, zone, resistance_elementaire) -> ActionMagieAutoProtection|ActionMagieAutoProtectionElement
"""
