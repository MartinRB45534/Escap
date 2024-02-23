"""
Quelques magies diverses.
"""

from __future__ import annotations
from typing import TYPE_CHECKING

# Imports des classes parentes
from .magie import Magie, CibleAgissant, CibleAgissants, CibleCase

# Imports utilisés dans le code
from ...effet import ProtectionElement, ProtectionMur, ProtectionCaseMur, ProtectionCaseElement
from ...commons import Element, Deplacement, Forme, Passage

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ...entitee import Agissant
    from ...systeme import Actif

class MagieAutoProtection(Magie):
    """La magie qui crée un effet de protection sur l'agissant."""
    duree: float
    pv: float
    def __init__(self,skill:Actif,agissant:Agissant):
        Magie.__init__(self,skill,agissant)

    def action(self):
        self.agissant.effets.append(ProtectionMur(self.duree,self.pv))

class MagieProtection(CibleAgissant, MagieAutoProtection):
    """La magie qui crée un effet de protection sur un agissant."""
    def __init__(self,skill:Actif,agissant:Agissant):
        CibleAgissant.__init__(self,skill,agissant)
        MagieAutoProtection.__init__(self,skill,agissant)

    def action(self):
        if not self.cible:
            self.interrompt()
        else:
            self.cible.effets.append(ProtectionMur(self.duree,self.pv))

class MagieMultiProtection(CibleAgissants, MagieAutoProtection):
    """La magie qui crée un effet de protection sur des agissants."""
    def __init__(self,skill:Actif,agissant:Agissant):
        CibleAgissants.__init__(self,skill,agissant)
        MagieAutoProtection.__init__(self,skill,agissant)

    def action(self):
        if not self.cible: # [] is falsy
            self.interrompt()
        else:
            for cible in self.cible:
                cible.effets.append(ProtectionMur(self.duree,self.pv))

class MagieProtectionGroupe(MagieAutoProtection):
    """La magie qui crée un effet de protection sur des agissants."""
    def __init__(self,skill:Actif,agissant:Agissant):
        MagieAutoProtection.__init__(self,skill,agissant)

    def action(self):
        for agissant in self.agissant.esprit.corps:
            agissant.effets.append(ProtectionMur(self.duree,self.pv))

class MagieProtectionZone(CibleCase, MagieAutoProtection):
    """La magie qui crée un effet de protection sur une zone."""
    portee: float
    def __init__(self,skill:Actif,agissant:Agissant):
        CibleCase.__init__(self,skill,agissant)
        MagieAutoProtection.__init__(self,skill,agissant)

    def action(self):
        if not self.cible:
            self.interrompt()
        else:
            poss = self.agissant.labyrinthe.a_portee(self.cible,self.portee,Deplacement.SPATIAL,Forme.CERCLE,Passage(True, False, False, True, True))
            for position in poss:
                case = self.agissant.labyrinthe.get_case(position)
                case.effets.add(ProtectionCaseMur(self.duree,self.pv))

class MagieAutoProtectionElement(MagieAutoProtection):
    """La magie qui crée un effet de protection élémentaire sur l'agissant."""
    element: Element
    taux: float
    def __init__(self,skill:Actif,agissant:Agissant):
        MagieAutoProtection.__init__(self,skill,agissant)

    def action(self):
        self.agissant.effets.append(ProtectionElement(self.duree,self.pv,self.element,self.taux))

class MagieProtectionElement(CibleAgissant, MagieAutoProtectionElement):
    """La magie qui crée un effet de protection élémentaire sur un agissant."""
    def __init__(self,skill:Actif,agissant:Agissant):
        CibleAgissant.__init__(self,skill,agissant)
        MagieAutoProtectionElement.__init__(self,skill,agissant)

    def action(self):
        if not self.cible:
            self.interrompt()
        else:
            self.cible.effets.append(ProtectionElement(self.duree,self.pv,self.element,self.taux))

class MagieMultiProtectionElement(CibleAgissants, MagieAutoProtectionElement):
    """La magie qui crée un effet de protection élémentaire sur des agissants."""
    def __init__(self,skill:Actif,agissant:Agissant):
        CibleAgissants.__init__(self,skill,agissant)
        MagieAutoProtectionElement.__init__(self,skill,agissant)

    def action(self):
        if not self.cible: # [] is falsy
            self.interrompt()
        else:
            for cible in self.cible:
                cible.effets.append(ProtectionElement(self.duree,self.pv,self.element,self.taux))

class MagieProtectionGroupeElement(MagieAutoProtectionElement):
    """La magie qui crée un effet de protection élémentaire sur des agissants."""
    def __init__(self,skill:Actif,agissant:Agissant):
        MagieAutoProtectionElement.__init__(self,skill,agissant)

    def action(self):
        for agissant in self.agissant.esprit.corps:
            agissant.effets.append(ProtectionElement(self.duree,self.pv,self.element,self.taux))

class MagieProtectionZoneElement(CibleCase, MagieAutoProtectionElement):
    """La magie qui crée un effet de protection élémentaire sur une zone."""
    portee: float
    def __init__(self,skill:Actif,agissant:Agissant):
        CibleCase.__init__(self,skill,agissant)
        MagieAutoProtectionElement.__init__(self,skill,agissant)

    def action(self):
        if not self.cible:
            self.interrompt()
        else:
            poss = self.agissant.labyrinthe.a_portee(self.cible,self.portee,Deplacement.SPATIAL,Forme.CERCLE,Passage(True, False, False, True, True))
            for position in poss:
                case = self.agissant.labyrinthe.get_case(position)
                case.effets.add(ProtectionCaseElement(self.duree,self.pv,self.element,self.taux))

magies_protection: dict[tuple[bool, bool, bool, bool],type[MagieAutoProtection]] = {
    (False, False, False, False): MagieAutoProtection,
    (True, False, False, False): MagieProtection,
    (True, True, False, False): MagieMultiProtection,
    (False, True, False, False): MagieProtectionGroupe,
    (False, False, True, False): MagieProtectionZone,
    (True, False, True, False): MagieAutoProtection, # Pas possible
    (False, True, True, False): MagieAutoProtection, # Pas possible
    (True, True, True, False): MagieAutoProtection, # Pas possible
    (False, False, False, True): MagieAutoProtectionElement,
    (True, False, False, True): MagieProtectionElement,
    (True, True, False, True): MagieMultiProtectionElement,
    (False, True, False, True): MagieProtectionGroupeElement,
    (False, False, True, True): MagieProtectionZoneElement,
    (True, False, True, True): MagieAutoProtectionElement, # Pas possible
    (False, True, True, True): MagieAutoProtectionElement, # Pas possible
    (True, True, True, True): MagieAutoProtectionElement # Pas possible
}
"""
(cible, cible_multiple, zone, resistance_elementaire) -> MagieAutoProtection|MagieAutoProtectionElement
"""
