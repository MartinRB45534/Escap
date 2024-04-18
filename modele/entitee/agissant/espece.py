"""Contient les classes Espece et Especes."""

from __future__ import annotations

class Espece:
    """
    Les espèces au sens premier : gobelin, slime, humain, etc.
    """
    def __init__(self, nom:str, nb_doigts:int, immunites:dict[str, float]):
        self.nom = nom
        self.nb_doigts = nb_doigts
        self.immunites = immunites

    def __contains__(self, item:Espece):
        return item is self

class Especes(Espece):
    """
    Les espèces complexes : le joueur, les ombriuls, etc.
    """
    # Parce que les ombriuls peuvent avoir une autre espèce (comme gobelin pour un gobelin corrompu)
    # Le joueur peut "perdre" son humanité pour éviter l'aggro de certains monstres
    def __init__(self, especes:list[Espece]):
        immunites:dict[str, float] = {}
        for espece in especes:
            for maladie, immunite in espece.immunites.items():
                immunites[maladie] = max(immunites.get(maladie, 0), immunite)
        Espece.__init__(self, especes[0].nom, especes[0].nb_doigts, immunites)
        self.especes = especes

    def __contains__(self, item:Espece):
        return item in self.especes
