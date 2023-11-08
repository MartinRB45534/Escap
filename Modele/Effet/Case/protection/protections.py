"""
Contient les classes de protection des cases.
"""

from __future__ import annotations
from typing import TYPE_CHECKING, List
from warnings import warn
import carte as crt

from .protection import ProtectionCase
from ...time_limited import TimeLimited

if TYPE_CHECKING:
    from ....entitee.item.equippement.degainable.bouclier.bouclier import Bouclier
    from ..attaque import AttaqueCase
    from ....commons.elements import Element

class ProtectionCaseBouclier(ProtectionCase,TimeLimited):
    """La case protégée par le bouclier est 'entourée' par ce dernier, c'est à dire que pour y rentrer par certains côtés, une attaque doit d'abord être affectée par le bouclier."""
    def __init__(self,temps_restant:float,bouclier:Bouclier,directions:List[crt.Direction]):
        ProtectionCase.__init__(self)
        TimeLimited.__init__(self,temps_restant)
        self.bouclier = bouclier #Techniquement c'est le bouclier qui intercepte.
        self.directions = directions

    def protege(self,attaque:AttaqueCase):
        if attaque.direction is None:
            warn("L'attaque n'a pas de direction, elle ne peut donc pas être interceptée par le bouclier.")
        elif attaque.direction.oppose in self.directions:
            self.bouclier.intercepte(attaque)

class ProtectionCaseMur(ProtectionCase,TimeLimited):
    """Une ProtectionCase qui agit comme un 'mur' autour de l'agissant, c'est à dire qu'elle absorbe les dégats jusqu'à se briser."""
    def __init__(self,temps_restant:float,pv:float):
        ProtectionCase.__init__(self)
        TimeLimited.__init__(self,temps_restant)
        self.pv = pv
        self.pv_max = pv #Pour afficher les PVs de la ProtectionCase

    def protege(self,attaque:AttaqueCase):
        if self.pv < attaque.degats:
            attaque.degats -= self.pv
            self.pv = 0
            self.termine()
        else:
            attaque.degats = 0 #Une attaque perçante peut quand même passer
            self.pv -= attaque.degats

class ProtectionCaseElement(ProtectionCaseMur):
    """Particulièrement efficace contre un élément spécifique."""
    def __init__(self,temps_restant:float,pv:float,element:Element):
        ProtectionCaseMur.__init__(self,temps_restant,pv)
        self.element = element

    def protege(self,attaque:AttaqueCase):
        if attaque.element == self.element:
            if 2*self.pv < attaque.degats:
                attaque.degats -= 2*self.pv
                self.pv = 0
                self.termine()
            else:
                attaque.degats = 0 #Une attaque perçante peut quand même passer
                self.pv -= attaque.degats//2
        else:
            ProtectionCaseMur.protege(self,attaque)
