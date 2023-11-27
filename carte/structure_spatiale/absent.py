from __future__ import annotations
from typing import Any

# Pas d'import pour les annotations

# Imports des classes parentes
from .position import Position
from .etage import Etage

class Absent:
    """Classe représentant ce qui n'est pas sur la carte."""
    def __bool__(self):
        return False # Absents are falsy (often used in place of None)

class EtageAbsent(Etage):
    """Classe représentant l'étage de la position absente."""
    def __init__(self):
        super().__init__("Absent", -1, -1)
        self.positions:set[Position] = set()

    def __contains__(self, item:Any):
        return item is POSITION_ABSENTE

ETAGE_ABSENT = EtageAbsent()

class PositionAbsent(Position):
    """Classe représentant la position de ce qui n'est pas sur la carte."""
    def __init__(self):
        super().__init__(ETAGE_ABSENT, -1, -1)
        self.etage.positions.add(self)

POSITION_ABSENTE = PositionAbsent()
