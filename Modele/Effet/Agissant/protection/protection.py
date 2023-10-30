"""Contient la classe Protection."""

from __future__ import annotations
from ..agissant import EffetAgissant
from ..attaque import AttaqueParticulier

class Protection(EffetAgissant):
    """Une protection qui agit comme une armure autour de l'agissant, c'est à dire qu'elle absorbe les dégats jusqu'à se briser."""

    def protege(self,attaque:AttaqueParticulier):
        """Protège l'agissant de l'attaque, dans la mesure du possible."""
