from __future__ import annotations
from typing import TYPE_CHECKING

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from Jeu.Entitee.Agissant.Agissant import Agissant

# Imports des classes parentes
from Jeu.Action.Action import Action

class Caste(Action):
    """
    L'action de caster (un parchemin ou une magie)
    """
    def __init__(self,agissant:Agissant,latence:float):
        super().__init__(agissant,latence)
        self.mana:float = 0
        self.cout:float

    def interrompt(self):
        """L'action est interrompue. Le sort missfire."""
        self.agissant.subit(NoOne(), self.mana) # Est-ce que c'est une punition trop dure pour les interruptions ?
        
    def get_skin(self):
        pass

class Caste_final(Caste):
    """
    Lorsque le mana est absorbé à la fin du cast.
    """
    def execute(self):
        """L'action est appelée à chaque tour."""
        self.latence += self.get_vitesse()
        if self.latence >= self.latence_max:
            if self.agissant.peut_payer(self.cout):
                self.mana = self.cout
                self.agissant.paye(self.cout)
                self.termine()
            else:
                self.interrompt() # Pas punitif puisqu'aucun mana n'a encore été dépensé.
            return True
        return False
        
class Caste_initial(Caste):
    """
    Lorsque le mana est absorbé au début du cast.
    """
    def execute(self):
        """L'action est appelée à chaque tour."""
        if self.latence == 0:
            if self.agissant.peut_payer(self.cout):
                self.mana = self.cout
                self.agissant.paye(self.cout)
            else:
                self.interrompt() # Pas punitif puisqu'aucun mana n'a encore été dépensé, et pas de temps de perdu non plus.
                return True
        self.latence += self.get_vitesse()
        if self.latence >= self.latence_max:
            self.termine()
            return True
        return False
        
class Caste_continu(Caste):
    """
    Lorsque le mana est absorbé à chaque tour.
    """
    def execute(self):
        self.latence += self.get_vitesse()
        diff = (self.latence/self.latence_max)*self.cout - self.mana
        if diff > 0:
            if self.agissant.peut_payer(diff):
                self.mana += diff
                self.agissant.paye(diff)
            else:
                self.interrompt() # Peut être beaucoup plus punitif puisqu'on a dépensé presque autant qu'on pouvait.
                return True
        if self.latence >= self.latence_max:
            self.termine()
            return True
        return False
    
class Caste_fractionnaire(Caste):
    """
    Lorsque le mana est absorbé par fractions.
    """
    def __init__(self, agissant: Agissant, latence: float):
        super().__init__(agissant, latence)
        self.parts: int = 1

    def execute(self):
        self.latence += self.get_vitesse()
        parts_accomplies = int((self.latence/self.latence_max)*self.parts)
        diff = parts_accomplies*self.cout/self.parts - self.mana
        if diff > 0:
            if self.agissant.peut_payer(diff):
                self.mana += diff
                self.agissant.paye(diff)
            else:
                self.interrompt() # Peut être plus ou moins punitif selon le nombre de parts et le remplissage de la dernière part.
        if self.latence >= self.latence_max:
            self.termine()
            return True
        return False

# Imports utilisés dans le code
from Jeu.Entitee.Agissant.Agissant import Agissant, NoOne