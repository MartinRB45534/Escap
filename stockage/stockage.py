"""
Classes mères des classes de stockage.
"""

from __future__ import annotations
from typing import Self, Optional, TYPE_CHECKING

import modele as mdl
import carte as crt

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from .entitee import Items
    from .espece import Especes

class Stockage:
    """Classe mère des classes de stockage."""
    niveau = False
    def __init__(self, nom: str):
        self.nom = nom

    def check(self) -> bool:
        """Vérifie que les informations sont valides."""
        return False

    def stringify(self) -> str:
        """Retourne le JSON de l'objet."""
        raise NotImplementedError

    @classmethod
    def parse(cls, json: str) -> Stockage:
        """Retourne l'objet correspondant au JSON."""
        raise NotImplementedError

class StockageNivele(Stockage):
    """Classe mère des classes de stockage de niveau."""
    niveau = True
    def stringify(self) -> str:
        raise NotImplementedError

    @classmethod
    def parse(cls, json: str) -> StockageNivele:
        raise NotImplementedError

class StockageGlobal(Stockage):
    """Le stockage global, qui devrait tout contenir."""
    global_:Self

    def __init__(self):
        Stockage.__init__(self, "Global")
        self.items:Items
        self.especes:Especes

    def check(self) -> bool:
        return True

    def stringify(self) -> str:
        """Retourne le JSON de l'objet."""
        return f"""{{
    "Items": {self.items.stringify()}
}}"""

    @classmethod
    def parse(cls, json: str) -> StockageGlobal:
        """Retourne l'objet correspondant au JSON."""
        raise NotImplementedError

    def make_item(self, nom: str, labyrinthe: mdl.Labyrinthe, position: crt.Position, niveau:Optional[int]=None) -> mdl.Item:
        """Retourne l'item correspondant."""
        return self.items.make(nom, labyrinthe, position, niveau)
    
    def make_espece(self, nom:str) -> mdl.Espece:
        """Retourne l'espèce correspondante."""
        return self.especes.make(nom)

StockageGlobal.global_ = StockageGlobal()
