from __future__ import annotations
from typing import TYPE_CHECKING

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from Jeu.Entitee.Agissant.Agissant import Agissant
    from Jeu.Systeme.Skill import Skill_intrasec

# Pas de classe parente

class Action:
    """
    Les actions sont ce que les agissants font. Elles sont appelées par le controleur jusqu'à être terminées, puis retirées.
    """
    def __init__(self,agissant:Agissant,latence:float):
        self.agissant = agissant # Pour ne pas avoir à repasser l'agissant en paramètre à chaque fois
        self.latence = 0 # Le temps écoulé depuis le début de l'action
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

    def get_vitesse(self):
        vitesse = 1
        for taux in self.taux_vitesse.values() :
            vitesse *= taux
        return vitesse

    # Il faut que l'action soit affichée, comme un skin par-dessus l'agissant

class Action_skill(Action):
    """
    Les actions provoquées par un skill.
    """
    def __init__(self,agissant:Agissant,latence:float,skill:Skill_intrasec,xp:float):
        super().__init__(agissant,latence)
        self.skill = skill
        self.xp = xp

    def termine(self):
        """L'action est terminée."""
        self.skill.xp_new += self.xp