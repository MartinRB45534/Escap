"""Contient la classe ProtectionCase."""

from __future__ import annotations
from ..case import EffetCase
from ..attaque import AttaqueCase

class ProtectionCase(EffetCase):
    """Une protection qui agit comme un 'mur' autour de l'agissant, c'est à dire qu'elle absorbe les dégats jusqu'à se briser."""

    def protege(self,attaque:AttaqueCase):
        """Protège la case de l'attaque, dans la mesure du possible."""
