"""Ce module contient la classe des effets limités par le temps."""

from __future__ import annotations

# Imports de la classe parente
from .effet import Effet

class TimeLimited(Effet):
    """La classe des effets limités par le temps."""
    def __init__(self,temps_restant:float):
        self.temps_restant=temps_restant

    def wait(self):
        """L'effet attend un tour. S'il doit faire quelque chose, il le signale à l'agissant."""
        self.temps_restant -= 1

    def termine(self) -> bool:
        return self.temps_restant <= 0
