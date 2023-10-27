"""
Définiles effets qui ont un timing à respecter.
"""
from __future__ import annotations
from typing import TYPE_CHECKING

from .effet import Effet
from .item.item import EffetItem
from .case.case import EffetCase
from .agissant.agissant import EffetAgissant

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ..entitee.agissant.agissant import Agissant
    from ..entitee.item.item import Item
    from ..entitee.item.cadavre import Cadavre
    from ..labyrinthe.case import Case

class OnDebutTourAgissant(EffetAgissant):
    """La classe des effets appelés au début du tour d'un agissant."""
    def debut_tour(self,_agissant:Agissant) -> None:
        """L'effet est appelé au début du tour de l'agissant."""

class OnDebutTourItem(EffetItem):
    """La classe des effets appelés au début du tour d'un item."""
    def debut_tour(self,_item:Item) -> None:
        """L'effet est appelé au début du tour de l'item."""

class OnDebutTourCase(EffetCase): #Aucun effet n'est de ce type pour l'instant
    """La classe des effets appelés au début du tour d'une case."""
    def debut_tour(self,_case:Case) -> None:
        """L'effet est appelé au début du tour de la case."""

class OnPostDecisionAgissant(EffetAgissant): #Un modificateur de comportement (un seul pour l'instant)
    """La classe des effets appelés entre les décisions et les actions."""
    def post_decision(self,_agissant:Agissant) -> None:
        """L'effet est appelé entre les décisions et les actions de l'agissant."""

class OnPostActionAgissant(EffetAgissant): #Pas sûr que ça soit utile
    """La classe des effets appelés après les actions d'un agissant."""
    def post_action(self,_agissant:Agissant) -> None:
        """L'effet est appelé après les actions de l'agissant."""

class OnPostActionCase(EffetCase): #Pas sûr que ça soit utile
    """La classe des effets appelés après les actions d'une case."""
    def post_action(self,_case:Case) -> None:
        """L'effet est appelé après les actions de la case."""

class OnFinTourAgissant(EffetAgissant): #Maladies par exemple
    """La classe des effets appelés à la fin du tour."""
    def fin_tour(self,_agissant:Agissant) -> None:
        """L'effet est appelé à la fin du tour de l'agissant."""

class OnFinTourItem(EffetItem): #Le sursis par exemple
    """La classe des effets appelés à la fin du tour."""
    def fin_tour(self,_item:Item) -> None:
        """L'effet est appelé à la fin du tour de l'item."""

class OnFinTourCadavre(EffetItem): #La résurection par exemple
    """La classe des effets appelés à la fin du tour."""
    def fin_tour(self,_cadavre:Cadavre) -> None:
        """L'effet est appelé à la fin du tour du cadavre."""

class OnFinTourCase(EffetCase): #Aucun effet n'est de ce type pour l'instant
    """La classe des effets appelés à la fin du tour."""
    def fin_tour(self,_case:Case) -> None:
        """L'effet est appelé à la fin du tour de la case."""

class TimeLimited(Effet):
    """La classe des effets limités par le temps."""
    def __init__(self,temps_restant:float):
        self.temps_restant=temps_restant

    def wait(self):
        """L'effet attend un tour. S'il doit faire quelque chose, il le signale à l'agissant."""
        self.temps_restant -= 1

    def termine(self) -> bool:
        return self.temps_restant <= 0

class Enchantement(TimeLimited):
    """La classe des effets qui enchantent quelque chose."""
