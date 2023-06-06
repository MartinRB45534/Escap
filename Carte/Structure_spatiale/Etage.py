from __future__ import annotations

# Pas d'import pour les annotations

# Pas de classe parente

class Etage:
    """Classe représentant un étage de la carte."""
    def __init__(self, nom: str, largeur: int, hauteur: int):
        self.nom = nom
        self.largeur = largeur
        self.hauteur = hauteur
        self.positions = {Position(self, x, y) for x in range(largeur) for y in range(hauteur)}

    def __contains__(self, item):
        if isinstance(item,Position):
            return item in self.positions
        return False
    
    def get_pos(self,x:int,y:int):
        """Renvoie la position de coordonnées (x,y) sur cet étage."""
        # On cherche la position dans self.positions
        for pos in self.positions:
            if pos.x == x and pos.y == y:
                return pos
        # Si on ne l'a pas trouvée, on renvoie la position absente
        return POSITION_ABSENTE

    def __str__(self):
        return self.nom
    
from .Position import Position
from .Absent import POSITION_ABSENTE