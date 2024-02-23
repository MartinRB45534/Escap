"""
Contient les classes des actions de caste (lancer un sort ou un parchemin).
"""

from __future__ import annotations
from typing import TYPE_CHECKING

# Imports des classes parentes
from .action import Action

# Imports utilisés dans le code
from ..commons import Element

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ..entitee.agissant.agissant import Agissant

class Caste(Action):
    """
    L'action de caster (un parchemin ou une magie)
    """
    cout: float
    def __init__(self, agissant: Agissant):
        Action.__init__(self, agissant)
        self.mana: float = 0

    def paye(self):
        """On essaye de payer le coût du sort."""
        if self.agissant.peut_payer(self.cout):
            self.mana = self.cout
            self.agissant.paye(self.cout)
        else:
            self.interrompt()

    def interrompt(self):
        """L'action est interrompue. Le sort missfire."""
        self.agissant.subit(self.mana, Element.TERRE) # Est-ce que c'est une punition trop dure pour les interruptions ?

    def get_skin(self):
        """Retourne le skin de l'action."""

class CasteFinal(Caste):
    """
    Lorsque le mana est absorbé à la fin du cast.
    """
    def termine(self):
        """L'action est terminée."""
        self.paye()
        return super().termine()

class CasteInitial(Caste):
    """
    Lorsque le mana est absorbé au début du cast.
    """
    def execute(self):
        """L'action est appelée à chaque tour."""
        if self.latence == 0:
            self.paye()
        return super().execute()

class CasteContinu(Caste):
    """
    Lorsque le mana est absorbé à chaque tour.
    """
    def paye(self):
        """On essaye de payer une partie du coût du sort."""
        cout = (self.latence/self.latence_max)*self.cout - self.mana
        if self.agissant.peut_payer(cout):
            self.mana += cout
            self.agissant.paye(cout)
        else:
            self.interrompt()

    def execute(self):
        self.latence += self.get_vitesse()
        self.paye()
        if self.latence >= self.latence_max:
            return self.termine()
        return False

class CasteFractionnaire(Caste):
    """
    Lorsque le mana est absorbé par fractions.
    """
    def __init__(self, agissant: Agissant):
        Caste.__init__(self, agissant)
        self.parts: int = 1

    def paye(self):
        """On essaye de payer une partie du coût du sort."""
        parts_accomplies = int((self.latence/self.latence_max)*self.parts)
        cout = parts_accomplies*self.cout/self.parts - self.mana
        if self.agissant.peut_payer(cout):
            self.mana += cout
            self.agissant.paye(cout)
        else:
            self.interrompt()

    def execute(self):
        self.latence += self.get_vitesse()
        self.paye()
        if self.latence >= self.latence_max:
            return self.termine()
        return False
