"""
Les stockages d'entitées.
Caractérisés par le fait de nécessiter un labyrinthe et une position pour instancier l'entitée.
"""

from __future__ import annotations

import modele as mdl

from ..stockage import StockageNivele

class EntiteeNivele(StockageNivele):
    """Classe mère des classes de stockage d'entitées."""
    def make(self, niveau: int) -> mdl.Entitee:
        """Retourne l'entité correspondante."""
        raise NotImplementedError
