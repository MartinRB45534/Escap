from __future__ import annotations
from typing import TYPE_CHECKING, List

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from Jeu.Entitee.Agissant.Agissant import Agissant

# Pas de classe parente

class Action:
    """
    Les actions sont ce que les agissants font. Elles sont appelées par le controleur jusqu'à être terminées, puis retirées.
    """
    def __init__(self,agissant:Agissant,latence:float):
        self.agissant = agissant # Pour ne pas avoir à repasser l'agissant en paramètre à chaque fois
        self.latence:float = 0 # Le temps écoulé depuis le début de l'action
        self.latence_max = latence # Le temps que l'action doit durer
        self.taux_vitesse = {} # Les taux de vitesse de l'action (impactés par la glace, etc.)

    def execute(self):
        """L'action est appelée à chaque tour."""
        self.latence += self.get_vitesse()
        if self.latence >= self.latence_max:
            self.termine()
            return True
        return False

    def termine(self):
        """L'action est terminée."""
        pass

    def interrompt(self):
        """L'action est interrompue."""
        pass

    def action(self):
        """L'action est appelée à certains moments."""
        pass

    def get_vitesse(self):
        vitesse = 1
        for taux in self.taux_vitesse.values() :
            vitesse *= taux
        return vitesse

    # Il faut que l'action soit affichée, comme un skin par-dessus l'agissant

class Action_final(Action):
    """
    Action qui se fait à la fin.
    """
    def termine(self):
        """L'action est terminée."""
        super().termine()
        self.action()

class Action_initial(Action):
    """
    Action qui se fait au début.
    """
    def execute(self):
        """L'action est appelée à chaque tour."""
        if self.latence == 0:
            self.action()
        return super().execute()
        
class Action_continu(Action):
    """
    Action qui se fait à chaque tour.
    """
    def execute(self):
        """L'action est appelée à chaque tour."""
        self.latence += self.get_vitesse()
        self.action()
        if self.latence >= self.latence_max:
            self.termine()
            return True
        return False
    
class Action_fractionnaire(Action):
    """
    Action qui se fait un nombre fixe de fois, régulièrement.
    """
    def __init__(self,agissant:Agissant,latence:float,parts:int):
        super().__init__(agissant,latence)
        self.parts = parts # Le nombre de fois que l'action doit être faite
        self.rempli = 0 # Le nombre de fois que l'action a été faite

    def execute(self):
        """L'action est appelée à chaque tour."""
        self.latence += self.get_vitesse()
        new_rempli = int(self.latence / self.latence_max * self.parts)
        while self.rempli < new_rempli:
            self.rempli += 1
            self.action()
        if self.latence >= self.latence_max:
            self.termine()
            return True
        return False
    
class Action_parcellaire(Action):
    """
    Action qui se fait un nombre fixe de fois, irrégulièrement.
    """
    def __init__(self,agissant:Agissant,latences:List[float]):
        super().__init__(agissant,sum(latences))
        self.latences = latences # Les latences entre chaque action
        self.rempli = 0 # Le nombre de fois que l'action a été faite

    def execute(self):
        """L'action est appelée à chaque tour."""
        self.latence += self.get_vitesse()
        while self.latence >= sum(self.latences[:self.rempli+1]):
            self.rempli += 1
            self.action()
        if self.latence >= self.latence_max:
            self.termine()
            return True
        return False