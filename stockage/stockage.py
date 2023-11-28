"""
Classes mères des classes de stockage.
"""

from __future__ import annotations
from typing import Self, Optional,  Callable, TYPE_CHECKING
from json import loads as parse

import modele as mdl

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
    def champs(cls) -> dict[str, type[int|str|float|bool|mdl.Element]]:
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

    def make(self) -> object:
        """Retourne l'objet correspondant."""
        raise NotImplementedError

class StockageNivele(Stockage):
    """Stocke un élément avec un niveau."""
    @classmethod
    @property
    def champs(cls) -> dict[str, type[int|str|float|bool|mdl.Element]]:
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
    
    def make(self, niveau: int) -> object:
        """Retourne l'objet correspondant."""
        raise NotImplementedError

class StockageCategorie(Stockage):
    """Stocke une catégorie d'éléments, pas un élément ni une catégorie de catégories."""
    nom:str
    titre_nouveau:str
    description:str
    avertissement:str

    def __init__(self):
        Stockage.__init__(self, self.nom)
        self.contenu:dict[str, StockageUnique|StockageNivele] = {}

    def check(self) -> bool:
        return all([contenu.check() for contenu in self.contenu.values()])

    def acceptor(self, nom: str) -> bool:
        """Vérifie que le nom est valide."""
        return not nom in self.all_noms

    @property
    def all_noms(self) -> set[str]:
        """Retourne tous les noms des éléments."""
        return set(self.contenu.keys()) # À surdéfinir pour les items

    def stringify(self) -> str:
        return f"""{{"{self.nom}" : [
        {", ".join([contenu.stringify() for contenu in self.contenu.values()])}
    ]
}}"""

    @classmethod
    def parse(cls, json: str) -> Self:
        dictionnaire = parse(json)
        categorie = cls()
        for element in dictionnaire[categorie.nom]:
            if element["nivele"]:
                type_element = categorie.elements[element["type"]]
                if not isinstance(type_element, tuple):
                    raise ValueError(f"L'élément {element['type']} n'est pas nivele, mais on a trouvé un élément nivele.")
                categorie.contenu[element["nom"]] = type_element[1].parse(element)
            else:
                type_element = categorie.elements[element["type"]]
                if isinstance(type_element, tuple):
                    categorie.contenu[element["nom"]] = type_element[0].parse(element)
                else:
                    categorie.contenu[element["nom"]] = type_element.parse(element)
        return categorie

    def make(self, nom: str, niveau:Optional[int]=None) -> object:
        """Retourne l'objet correspondant."""
        if nom not in self.contenu:
            raise ValueError(f"L'élément {nom} n'existe pas.")
        stockage = self.contenu[nom]
        if isinstance(stockage, StockageNivele):
            if niveau is None:
                raise ValueError(
                    f"L'élément {nom} est nivele, il faut donc spécifier un niveau."
                )
            return stockage.make(niveau)
        if niveau is not None:
            raise ValueError(
                f"L'élément {nom} n'est pas nivele, il ne faut donc pas spécifier de niveau."
            )
        return stockage.make()

    @classmethod
    @property
    def elements(cls) -> dict[str,
        type[StockageUnique]|tuple[type[StockageUnique], type[StockageNivele]]]:
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
    def parse(cls, json: str) -> Self:
        """Retourne l'objet correspondant au JSON."""
        raise NotImplementedError

    def make_item(self, nom: str, niveau:Optional[int]=None) -> mdl.Item:
        """Retourne l'item correspondant."""
        return self.items.make(nom, niveau)
    
    def make_espece(self, nom:str) -> mdl.Espece:
        """Retourne l'espèce correspondante."""
        espece = self.especes.make(nom)
        assert isinstance(espece, mdl.Espece)
        return espece

StockageGlobal.global_ = StockageGlobal()
