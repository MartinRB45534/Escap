"""
Contient les classes des protections d'agissants.
"""

from __future__ import annotations
from typing import TYPE_CHECKING

# Imports des classes parentes
from .protection import Protection
from ..timings import TimeLimited

if TYPE_CHECKING:
    from ...attaque.attaque import AttaqueParticulier
    from ....commons.elements import Element

class ProtectionMur(Protection, TimeLimited):
    """Une protection qui agit comme un 'mur' autour de l'agissant, c'est à dire qu'elle absorbe les dégats jusqu'à se briser."""
    def __init__(self,temps_restant:float,pv:float):
        Protection.__init__(self)
        TimeLimited.__init__(self,temps_restant)
        self.pv = pv
        self.pv_max = pv #Pour afficher les PVs de la Protection

    def protege(self,attaque:AttaqueParticulier):
        if self.pv < attaque.degats:
            attaque.degats -= self.pv
            self.pv = 0
            self.termine()
        else:
            attaque.degats = 0
            self.pv -= attaque.degats

class ProtectionElement(ProtectionMur):
    """Particulièrement efficace contre un élément spécifique."""
    def __init__(self,temps_restant:float,pv:float,element:Element):
        ProtectionMur.__init__(self,temps_restant,pv)
        self.element = element

    def protege(self,attaque:AttaqueParticulier):
        if attaque.element == self.element:
            if 2*self.pv < attaque.degats:
                attaque.degats -= 2*self.pv
                self.pv = 0
                self.termine()
            else:
                attaque.degats = 0
                self.pv -= attaque.degats
        else:
            ProtectionMur.protege(self,attaque)
