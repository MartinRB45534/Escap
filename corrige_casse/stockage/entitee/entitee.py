"""
Les stockages d'entitées.
Caractérisés par le fait de nécessiter un labyrinthe et une position pour instancier l'entitée.
"""

from __future__ import annotations

import modele as mdl
import carte as crt

from ..stockage import StockageUnique, StockageNivele

class Entitee(StockageUnique):
    """Classe mère des classes de stockage d'entitées."""
    def make(self, labyrinthe: mdl.Labyrinthe, position: crt.Position) -> mdl.Entitee:
        """Retourne l'entité correspondante."""
        raise NotImplementedError

class EntiteeNivele(StockageNivele):
    """Classe mère des classes de stockage d'entitées de niveau."""
    def make(self, labyrinthe: mdl.Labyrinthe, position: crt.Position, niveau: int) -> mdl.Entitee:
        """Retourne l'entité correspondante."""
        raise NotImplementedError
