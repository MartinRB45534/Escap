"""
Un effet qui protège un groupe d'agissants.
"""

from __future__ import annotations
from typing import TYPE_CHECKING

from ..timings import OnPostActionAgissant

# Imports utilisés dans le code
from ....commons import EtatsAgissants, Element
from .protections import ProtectionMur, ProtectionElement

if TYPE_CHECKING:
    from ....entitee.agissant.agissant import Agissant

class ProtectionGroupe(OnPostActionAgissant):
    """Effet de protection d'un groupe."""
    def __init__(self,duree:float,degats:float):
        self.affiche = False
        self.phase = "démarrage"
        self.duree = duree
        self.degats = degats

    def post_action(self,porteur:Agissant):
        cibles = []
        if porteur.esprit:
            cibles = porteur.esprit.corps
        else:
            cibles = [porteur]
        for cible in cibles:
            if cible.etat == EtatsAgissants.VIVANT:
                cible.effets.append(ProtectionMur(self.duree,self.degats))

class ProtectionGroupeElement(ProtectionGroupe):
    """Effet de protection d'un groupe contre un élément."""
    def __init__(self,duree:float,degats:float,element:Element):
        ProtectionGroupe.__init__(self,duree,degats)
        self.element = element

    def post_action(self,porteur:Agissant):
        cibles = []
        if porteur.esprit:
            cibles = porteur.esprit.corps
        else:
            cibles = [porteur]
        for cible in cibles:
            if cible.etat == EtatsAgissants.VIVANT:
                cible.effets.append(ProtectionElement(self.duree,self.degats,self.element))