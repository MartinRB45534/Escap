"""
Contient la classe Action.
"""

from __future__ import annotations
from typing import TYPE_CHECKING

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ..entitee.agissant.agissant import Agissant

# Pas de classe parente

class Action:
    """
    Les actions sont ce que les agissants font.
    Elles sont appelées par le controleur jusqu'à être terminées, puis retirées.
    """
    latence_max: float
    def __init__(self, agissant: Agissant):
        self.agissant = agissant # Pour ne pas avoir à repasser l'agissant en paramètre à chaque fois
        self.latence: float = 0 # Le temps écoulé depuis le début de l'action
        self.taux_vitesse: dict[str,float] = {} # Les taux de vitesse de l'agissant
        self.repete = False # Si l'action doit être répétée
        self.repetitions = 0 # Le nombre de fois que l'action a été répétée

    def execute(self):
        """L'action est appelée à chaque tour."""
        self.latence += self.get_vitesse()
        if self.latence >= self.latence_max:
            return self.termine()
        return False

    def termine(self):
        """L'action est terminée."""
        if self.repete:
            self.reinit()
            return False
        return True

    def reinit(self):
        """L'action est réinitialisée."""
        self.latence = 0
        self.repetitions += 1

    def interrompt(self):
        """L'action est interrompue."""

    def action(self):
        """L'action est appelée à certains moments."""

    def get_vitesse(self):
        """Retourne la vitesse de l'agissant."""
        vitesse = self.agissant.vitesse
        for taux in self.taux_vitesse.values():
            vitesse *= taux
        return vitesse

    def set_repete(self):
        """L'action doit être répétée."""
        self.repete = True

    def unset_repete(self):
        """L'action ne doit pas être répétée."""
        self.repete = False
        if self.repetitions > 0:
            self.interrompt()
            return True
        return False

    # Il faut que l'action soit affichée, comme un skin par-dessus l'agissant

class NonRepetable(Action):
    """
    Action qui ne peut pas se répéter (ramasser un objet, rescussiter un allié, etc.)
    """
    def set_repete(self):
        pass

    def unset_repete(self):
        return False

class ActionFinal(Action):
    """
    Action qui se fait à la fin.
    """
    def termine(self):
        """L'action est terminée."""
        res = Action.termine(self)
        self.action()
        return res

class ActionInitial(Action):
    """
    Action qui se fait au début.
    """
    def execute(self):
        """L'action est appelée à chaque tour."""
        if self.latence == 0:
            self.action()
        return Action.execute(self)

class ActionContinu(Action):
    """
    Action qui se fait à chaque tour.
    """
    def execute(self):
        """L'action est appelée à chaque tour."""
        self.latence += self.get_vitesse()
        self.action()
        if self.latence >= self.latence_max:
            return self.termine()
        return False

class ActionFractionnaire(Action):
    """
    Action qui se fait un nombre fixe de fois, régulièrement.
    """
    parts: int
    def __init__(self, agissant: Agissant):
        Action.__init__(self, agissant)
        self.rempli = 0 # Le nombre de fois que l'action a été faite

    def execute(self):
        """L'action est appelée à chaque tour."""
        self.latence += self.get_vitesse()
        new_rempli = int(self.latence / self.latence_max * self.parts)
        while self.rempli < new_rempli:
            self.rempli += 1
            self.action()
        if self.latence >= self.latence_max:
            return self.termine()
        return False

    def reinit(self):
        """L'action est réinitialisée."""
        self.rempli = 0
        Action.reinit(self)

class ActionParcellaire(Action):
    """
    Action qui se fait un nombre fixe de fois, irrégulièrement.
    """
    latences: list[float]
    def __init__(self,agissant:Agissant):
        Action.__init__(self, agissant)
        self.rempli = 0 # Le nombre de fois que l'action a été faite

    def execute(self):
        """L'action est appelée à chaque tour."""
        self.latence += self.get_vitesse()
        while self.latence >= sum(self.latences[:self.rempli+1]):
            self.rempli += 1
            self.action()
        if self.latence >= self.latence_max:
            return self.termine()
        return False

    def reinit(self):
        """L'action est réinitialisée."""
        self.rempli = 0
        Action.reinit(self)
