from __future__ import annotations

# Pas d'import pour les annotations

# Imports des classes parentes
from .Position import Position
from .Etage import Etage

class Etage_absent(Etage):
    """Classe représentant l'étage de la position absente."""
    def __init__(self):
        self.nom = "Absent"
        self.largeur = -1
        self.hauteur = -1
        self.positions = set()

    def __contains__(self, item):
        return item is POSITION_ABSENTE

ETAGE_ABSENT = Etage_absent()

class Position_absent(Position):
    """Classe représentant la position de ce qui n'est pas sur la carte."""
    def __init__(self):
        self.etage=ETAGE_ABSENT
        self.x=-1
        self.y=-1
        self.etage.positions.add(self)

POSITION_ABSENTE = Position_absent()