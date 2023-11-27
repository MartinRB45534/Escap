"""
Fichier contenant la classe de stockage des items.
"""

from __future__ import annotations
from typing import Optional
from json import loads as parse

import modele as mdl
import carte as crt

from ...stockage import Stockage, StockageGlobal
from .parchemin import Parchemins

class Items(Stockage):
    """Les informations des parchemins."""
    def __init__(self):
        Stockage.__init__(self, "Items")
        self.parchemin:Parchemins = Parchemins()

    def check(self) -> bool:
        return all([item.check() for item in [self.parchemin]])
    
    def all_noms(self) -> list[str]:
        """Retourne les noms de tous les items."""
        return [nom for nom in self.parchemin.parchemins.keys()]

    def stringify(self) -> str:
        return f"""{{
    "Parchemins": [
        {self.parchemin.stringify()}
    ]
}}"""

    @classmethod
    def parse(cls, json: str) -> Items:
        """Retourne l'objet correspondant au JSON."""
        dictionnaire = parse(json)
        item = Items()
        item.parchemin = Parchemins.parse(dictionnaire["parchemins"][0])
        return item

    def make(self, nom: str, labyrinthe: mdl.Labyrinthe, position: crt.Position,
             niveau:Optional[int]=None) -> mdl.Item:
        """Retourne l'item correspondant."""
        if nom in self.parchemin.parchemins:
            return self.parchemin.make(nom, labyrinthe, position, niveau)
        else:
            raise ValueError(f"L'item {nom} n'existe pas.")

StockageGlobal.global_.items = Items()
