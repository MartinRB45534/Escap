"""Contient les classes Espece et Especes."""

from __future__ import annotations

class Espece:
    """
    Les espèces au sens premier : gobelin, slime, humain, etc.
    """
    def __init__(self, nom:str, nb_doigts:int = 10):
        self.nom = nom
        self.nb_doigts = nb_doigts

    def __contains__(self, item:Espece):
        return item is self

class Especes(Espece):
    """
    Les espèces complexes : le joueur, les ombriuls, etc.
    """
    # Parce que les ombriuls peuvent avoir une autre espèce (comme gobelin pour un gobelin corrompu)
    # Le joueur peut "perdre" son humanité pour éviter l'aggro de certains monstres
    def __init__(self, especes:list[Espece]):
        self.especes = especes

    @property
    def nb_doigts(self) -> int:
        return self.especes[0].nb_doigts

    def __contains__(self, item:Espece):
        return item in self.especes
