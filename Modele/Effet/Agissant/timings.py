"""Les timings des effets agissants."""

from __future__ import annotations
from typing import TYPE_CHECKING

# Imports de la classe parente
from .agissant import EffetAgissant
from ..time_limited import TimeLimited

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ...entitee.agissant.agissant import Agissant

class OnDebutTourAgissant(EffetAgissant):
    """La classe des effets appelés au début du tour d'un agissant."""
    def debut_tour(self,_agissant:Agissant) -> None:
        """L'effet est appelé au début du tour de l'agissant."""

class OnPostDecisionAgissant(EffetAgissant): #Un modificateur de comportement (un seul pour l'instant)
    """La classe des effets appelés entre les décisions et les actions."""
    def post_decision(self,_agissant:Agissant) -> None:
        """L'effet est appelé entre les décisions et les actions de l'agissant."""

class OnPostActionAgissant(EffetAgissant): #Pas sûr que ça soit utile
    """La classe des effets appelés après les actions d'un agissant."""
    def post_action(self,_agissant:Agissant) -> None:
        """L'effet est appelé après les actions de l'agissant."""

class OnFinTourAgissant(EffetAgissant): #Maladies par exemple
    """La classe des effets appelés à la fin du tour."""
    def fin_tour(self,_agissant:Agissant) -> None:
        """L'effet est appelé à la fin du tour de l'agissant."""

class TimeLimitedAgissant(EffetAgissant, TimeLimited):
    """Un TimeLimited qui a quelque chose à faire, sur un agissant"""
    def action(self,agissant:Agissant):
        """Une action exécutée sur un agissant."""
