"""
Deux effets de case : obscurité et blizzard.
"""
from __future__ import annotations
from typing import TYPE_CHECKING

# Imports des classes parentes
from .case import EffetCase
from ..time_limited import TimeLimited
from .timings import OnDebutTourCase

# Imports utilisés dans les variables de classe
from ...commons import Element

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ...labyrinthe.case import Case
    from ...entitee.agissant.agissant import Agissant

class DegatsCase(OnDebutTourCase): #Très distinct des attaques
    """Evenement de dégats."""
    element:Element = Element.TERRE
    def __init__(self,degats:float,responsable:Agissant):
        OnDebutTourCase.__init__(self)
        self.degats = degats
        self.responsable = responsable

    def debut_tour(self, case: Case) -> None:
        occupant = case.agissant
        if occupant is not None and occupant.esprit != self.responsable.esprit :
            occupant.subit(self.degats,self.element)

class Ralenti(OnDebutTourCase): #Peut immobiliser si le gain de latence est supérieur à la vitesse
    """Evenement de ralentissement."""
    def __init__(self,gain_latence:float):
        OnDebutTourCase.__init__(self)
        self.gain_latence = gain_latence

    def debut_tour(self, case: Case) -> None:
        occupants = case.items | {case.agissant} if case.agissant is not None else case.items
        for occupant in occupants :
            if occupant.action is not None:
                occupant.action.latence += self.gain_latence

class Opacite(EffetCase):
    """Evenement d'assombrissement."""
    def __init__(self,gain_opacite:float):
        EffetCase.__init__(self)
        self.gain_opacite = gain_opacite

class Blizzard(TimeLimited, Ralenti): # Un long ralentissement
    """Evenement de blizzard."""
    def __init__(self,duree:float,gain_latence:float):
        TimeLimited.__init__(self,duree)
        Ralenti.__init__(self,gain_latence)

class Obscurite(TimeLimited, Opacite):
    """Evenement d'obscurité."""
    def __init__(self,duree:float,gain_opacite:float):
        TimeLimited.__init__(self,duree)
        Opacite.__init__(self,gain_opacite)
