"""Les timings des effets des cases."""

from __future__ import annotations
from typing import TYPE_CHECKING

# Imports de la classe parente
from .case import EffetCase

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ...labyrinthe.case import Case

class OnDebutTourCase(EffetCase): #Aucun effet n'est de ce type pour l'instant
    """La classe des effets appelés au début du tour d'une case."""
    def debut_tour(self,_case:Case) -> None:
        """L'effet est appelé au début du tour de la case."""

class OnPostActionCase(EffetCase): #Pas sûr que ça soit utile
    """La classe des effets appelés après les actions d'une case."""
    def post_action(self,_case:Case) -> None:
        """L'effet est appelé après les actions de la case."""

class OnFinTourCase(EffetCase): #Aucun effet n'est de ce type pour l'instant
    """La classe des effets appelés à la fin du tour."""
    def fin_tour(self,_case:Case) -> None:
        """L'effet est appelé à la fin du tour de la case."""
