"""
Classes mères des classes de stockage.
"""

from __future__ import annotations
from typing import Self, Optional, Type, Callable, Tuple, TYPE_CHECKING

import modele as mdl
import carte as crt

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from .entitee import Items
    from .espece import Especes

class Stockage:
    """Classe mère des classes de stockage."""
    def __init__(self, nom: str):
        self.nom = nom

    def check(self) -> bool:
        """Vérifie que les informations sont valides."""
        return False

    def stringify(self) -> str:
        """Retourne le JSON de l'objet."""
        raise NotImplementedError

    @classmethod
    def parse(cls, json: str) -> Self:
        """Retourne l'objet correspondant au JSON."""
        raise NotImplementedError

class StockageUnique(Stockage):
    """Stocke un élément, pas une catégorie d'éléments."""
    @classmethod
    @property
    def champs(cls) -> dict[str, Type[int|str|float]]:
        """Retourne les champs de l'objet."""
        raise NotImplementedError

    @classmethod
    @property
    def acceptors(cls) -> dict[str, Callable[[str], bool]]:
        """Retourne les fonctions de vérification des champs."""
        raise NotImplementedError

    @classmethod
    @property
    def avertissements(cls) -> dict[str, str]:
        """Retourne les avertissements des champs."""
        raise NotImplementedError

class StockageNivele(Stockage):
    """Stocke un élément avec un niveau."""
    @classmethod
    @property
    def champs(cls) -> dict[str, Type[int|str|float]]:
        """Retourne les champs de l'objet."""
        raise NotImplementedError

    @classmethod
    @property
    def acceptors(cls) -> dict[str, Callable[[str], bool]]:
        """Retourne les fonctions de vérification des champs."""
        raise NotImplementedError

    @classmethod
    @property
    def avertissements(cls) -> dict[str, str]:
        """Retourne les avertissements des champs."""
        raise NotImplementedError

class StockageCategorie(Stockage):
    """Stocke une catégorie d'éléments, pas un élément ni une catégorie de catégories."""
    @classmethod
    @property
    def elements(cls) -> dict[str, Type[StockageUnique]|Tuple[Type[StockageUnique], Type[StockageNivele]]]:
        """Retourne les éléments de la catégorie."""
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
