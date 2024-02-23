"""
Classes mères des classes de stockage.
"""

from __future__ import annotations
from typing import Self, Optional,  Callable, TypeVar, TYPE_CHECKING
from json import loads as parse
from enum import StrEnum

if TYPE_CHECKING:
    from .stockageglobal import StockageGlobal

class Stockage:
    """Classe mère des classes de stockage."""
    global_:StockageGlobal
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
    def __init__(self, nom:str):
        Stockage.__init__(self, nom)
        self.dependants: set[StockageUnique|StockageNivele] = set()

    champs: dict[str, type[int|str|float|bool|StrEnum]]
    """Retourne les champs de l'objet."""

    acceptors: dict[str, Callable[[str], bool]]
    """Retourne les fonctions de vérification des champs."""

    avertissements: dict[str, str]
    """Retourne les avertissements des champs."""

    conditionnels: dict[str, Callable[[dict[str, str|list[str]]], bool]]
    """Retourne les fonctions qui déterminent les champs à afficher."""

    multiple: dict[str, bool]
    """Retourne si les champs sont multiples. Seuls certains champs peuvent être multiples."""

    def make(self) -> object:
        """Retourne l'objet correspondant."""
        raise NotImplementedError

    def set_dependances(self):
        """Se rajoute aux dépendants des objets dont il dépend"""

    def unset_dependances(self):
        """Se retire des dépendants des objets dont il dépend"""

class StockageNivele(Stockage):
    """Stocke un élément avec un niveau."""
    def __init__(self, nom: str):
        Stockage.__init__(self, nom)
        self.dependants: set[StockageUnique|StockageNivele] = set()
        self.classe = None

    champs: dict[str, type[int|str|float|bool|StrEnum|StockageCategorieUnique|StockageCategorieNivelee|StockageSurCategorie]] = NotImplemented
    """Retourne les champs de l'objet."""

    niveles: dict[str, bool] = NotImplemented
    """Retourne si les champs sont niveles."""

    acceptors: dict[str, Callable[[str], bool]] = NotImplemented
    """Retourne les fonctions de vérification des champs."""

    avertissements: dict[str, str] = NotImplemented
    """Retourne les avertissements des champs."""

    conditionnels: dict[str, Callable[[dict[str, str|list[str]]], bool]] = NotImplemented
    """Retourne les fonctions qui déterminent les champs à afficher."""

    multiple: dict[str, bool] = NotImplemented
    """Retourne si les champs sont multiples. Seuls certains champs peuvent être multiples."""

    def make(self, niveau: int) -> type:
        """Retourne l'objet correspondant."""
        raise NotImplementedError

    def remake(self, niveau: int) -> type:
        """Pour assurer l'unicité."""
        if not self.classe:
            self.classe = self.make(niveau)
        return self.classe

    def set_dependances(self):
        """Se rajoute aux dépendants des objets dont il dépend"""

    def unset_dependances(self):
        """Se retire des dépendants des objets dont il dépend"""

class StockageCategorieUnique(Stockage):
    """Stocke une catégorie d'éléments, pas un élément ni une catégorie de catégories."""
    nom: str
    titre_nouveau: str
    description: str
    avertissement: str
    elements: dict[str, type[StockageUnique]]

    def __init__(self):
        Stockage.__init__(self, self.nom)
        self.contenu:dict[str, StockageUnique] = {}

    def check(self) -> bool:
        return all([contenu.check() for contenu in self.contenu.values()])

    def acceptor(self, nom: str) -> bool:
        """Vérifie que le nom est valide."""
        return not nom in self.all_noms

    @property
    def all_noms(self) -> set[str]:
        """Retourne tous les noms des éléments."""
        return set(self.contenu.keys())

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
            type_element = categorie.elements[element["type"]]
            categorie.contenu[element["nom"]] = type_element.parse(element)
        return categorie

    def make(self, nom: str, niveau:Optional[int]=None) -> object:
        """Retourne l'objet correspondant."""
        if nom not in self.contenu:
            raise ValueError(f"L'élément {nom} n'existe pas.")
        stockage = self.contenu[nom]
        if niveau is not None:
            raise ValueError(
                f"L'élément {nom} n'est pas nivele, il ne faut donc pas spécifier de niveau."
            )
        return stockage.make()

    def set_all_dependances(self):
        """Set les dépendances de ses éléments"""
        for contenu in self.contenu.values():
            contenu.set_dependances()

    def warn_nom(self, nom:str) -> str:
        """Précise qui a déjà ce nom."""
        for contenu in self.contenu:
            if contenu == nom:
                return self.avertissement
        return ""

class StockageCategorieNivelee(Stockage):
    """Stocke une catégorie d'éléments, pas un élément ni une catégorie de catégories."""
    nom: str
    titre_nouveau: str
    description: str
    avertissement: str
    elements: dict[str, type[StockageNivele]]

    def __init__(self):
        Stockage.__init__(self, self.nom)
        self.contenu:dict[str, StockageNivele] = {}

    def check(self) -> bool:
        return all([contenu.check() for contenu in self.contenu.values()])

    def acceptor(self, nom: str) -> bool:
        """Vérifie que le nom est valide."""
        return not nom in self.all_noms

    @property
    def all_noms(self) -> set[str]:
        """Retourne tous les noms des éléments."""
        return set(self.contenu.keys())

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
            type_element = categorie.elements[element["type"]]
            categorie.contenu[element["nom"]] = type_element.parse(element)
        return categorie

    def make(self, nom: str, niveau:Optional[int]=None) -> object:
        """Retourne l'objet correspondant."""
        if nom not in self.contenu:
            raise ValueError(f"L'élément {nom} n'existe pas.")
        stockage = self.contenu[nom]
        if niveau is None:
            raise ValueError(
                f"L'élément {nom} est nivele, il faut donc spécifier un niveau."
            )
        return stockage.remake(niveau)

    def set_all_dependances(self):
        """Set les dépendances de ses éléments"""
        for contenu in self.contenu.values():
            contenu.set_dependances()

    def warn_nom(self, nom:str) -> str:
        """Précise qui a déjà ce nom."""
        for contenu in self.contenu:
            if contenu == nom:
                return self.avertissement
        return ""

class StockageSurCategorie(Stockage):
    """Stocke une catégorie de catégories, pas un élément ni une catégorie d'éléments."""
    nom:str
    elements:dict[str, type[StockageCategorieUnique|StockageCategorieNivelee|StockageSurCategorie]]

    def __init__(self):
        Stockage.__init__(self, self.nom)
        self.contenu:dict[str, StockageCategorieUnique|StockageCategorieNivelee|StockageSurCategorie] = {
            nom: type_()
            for nom, type_ in self.elements.items()
        }

    def check(self) -> bool:
        return all([contenu.check() for contenu in self.contenu.values()])

    def acceptor(self, nom: str) -> bool:
        """Vérifie que le nom est valide."""
        return not nom in self.all_noms

    @property
    def all_noms(self) -> set[str]:
        """Retourne tous les noms des catégories."""
        return set(sum([list(contenu.all_noms) for contenu in self.contenu.values()], [])) # type: ignore # Sinon mon linter se plaint du [] non typé

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
            for type_element in categorie.elements:
                if element["type"] == type_element:
                    categorie.contenu[element["nom"]] = categorie.elements[type_element].parse(element)
                    break
        return categorie

    def make(self, nom: str, niveau:Optional[int]=None) -> object:
        """Retourne l'objet correspondant."""
        for contenu in self.contenu.values():
            try:
                return contenu.make(nom, niveau)
            except ValueError:
                pass
        raise ValueError(f"L'élément {nom} n'existe pas.")

    StockageCategorie = TypeVar("StockageCategorie")
    def trouve_stockage(self, type_:type[StockageCategorie]) -> StockageCategorie:
        """Renvoie le stockage de ce type."""
        for contenu in self.contenu.values():
            if isinstance(contenu, type_):
                return contenu
            if isinstance(contenu, StockageSurCategorie):
                try:
                    return contenu.trouve_stockage(type_)
                except ValueError:
                    pass
        raise ValueError(f"Le stockage de type {type_} n'existe pas.")

    def set_all_dependances(self):
        """Set les dépendances des sous-éléments."""
        for contenu in self.contenu.values():
            contenu.set_all_dependances()

    def warn_nom(self, nom:str) -> str:
        """Précise qui a déjà ce nom."""
        warn = ""
        for contenu in self.contenu.values():
            warn = warn or contenu.warn_nom(nom)
        return warn
