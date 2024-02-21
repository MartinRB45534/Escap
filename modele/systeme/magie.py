"""Module magie du package modele.systeme."""

from .skill import Actif
from ..entitee import Agissant
from ..action import ActionMagie

class Magie:
    """Une magie (au sens générique). Servira à générer des actions de magie."""
    def genere(self,skill:Actif,agissant:Agissant,niveau:int) -> ActionMagie:
        """Génère une action de magie."""
        raise NotImplementedError
