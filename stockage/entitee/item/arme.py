"""
Fichier contenant la classe de stockage des armes.
"""

from __future__ import annotations
from typing import Callable
from json import loads as parse

import modele as mdl

from ...stockage import StockageCategorie, StockageNivele, StockageUnique
from ..entitee import Entitee, EntiteeNivele

class Arme(StockageCategorie):
    """Les informations des armes."""
    nom = "Armes"
    titre_nouveau = "Nouvelle arme"
    description = "Les armes sont destinées à attaquer. Certains skills boostent certaines armes."
    avertissement = "Il existe déjà un arme avec ce nom !"

    @classmethod
    @property
    def elements(cls) -> dict[str, type[StockageUnique]|tuple[type[StockageUnique], type[StockageNivele]]]:
        return {
            "ArmeSimple": (ArmeSimple, ArmeSimpleNivele)
        }

class ArmeSimple(Entitee):
    """Un arme."""
    def __init__(self, nom: str, fantome: bool,
                 element:mdl.Element, poids:float, frottements:float, portee:float, tranchant:float):
        Entitee.__init__(self, nom)
        self.fantome = fantome
        self.element = element
        self.poids = poids
        self.frottements = frottements
        self.portee = portee
        self.tranchant = tranchant

    def check(self) -> bool:
        return (self.poids >= 0 and
                self.frottements >= 0 and
                self.portee >= 0 and
                self.tranchant >= 0)

    def stringify(self) -> str:
        return f"""{{
    "type": "arme",
    "nivele": false,
    "nom": "{self.nom}",
    "fantome": {self.fantome},
    "element": "{self.element},
    "poids": {self.poids},
    "frottements": {self.frottements},
    "portee": {self.portee},
    "tranchant": {self.tranchant}"
}}"""

    @classmethod
    def parse(cls, json: str):
        """Parse un json en ArmeSimple."""
        dictionnaire = parse(json)
        return ArmeSimple(dictionnaire["nom"], dictionnaire["fantome"], dictionnaire["element"], dictionnaire["poids"], dictionnaire["frottements"], dictionnaire["portee"], dictionnaire["tranchant"])

    @classmethod
    @property
    def champs(cls) -> dict[str, type[int|str|float|bool|mdl.Element]]:
        return {
            "fantome": bool,
            "element": mdl.Element,
            "poids": float,
            "frottements": float,
            "portee": float,
            "tranchant": float
        }
    
    @classmethod
    @property
    def acceptors(cls) -> dict[str, Callable[[str], bool]]:
        return {
            "fantome": lambda _: True,
            "element": lambda element: element in mdl.Element,
            "poids": lambda poids: float(poids) >= 0,
            "frottements": lambda frottements: float(frottements) >= 0,
            "portee": lambda portee: float(portee) >= 0,
            "tranchant": lambda tranchant: float(tranchant) >= 0
        }
    
    @classmethod
    @property
    def avertissements(cls) -> dict[str, str]:
        return {
            "fantome": "Cet avertissement n'est pas censé apparaître.",
            "element": "Choisissez un élément.",
            "poids": "Le poids doit être positif.",
            "frottements": "Le frottement doit être positif.",
            "portee": "La portée doit être positive.",
            "tranchant": "Les dégats doivent être positifs."
        }

    def make(self) -> mdl.Arme:
        """Crée un ArmeSimple à partir de l'instance."""
        arme = mdl.Arme(mdl.NOWHERE, self.poids, self.frottements, self.element, self.tranchant, self.portee)
        arme.nom = self.nom
        arme.fantome = self.fantome
        return arme

class ArmeSimpleNivele(EntiteeNivele):
    """Un arme nivele."""
    def __init__(self, nom: str, fantome: bool,
                 percant: bool, fleche: bool, explosif: bool, fragile: bool, magique: bool,
                 element:mdl.Element, poids:float, frottements:float, portee:float, tranchant:float):
        EntiteeNivele.__init__(self, nom)
        self.fantome = fantome
        self.percant = percant
        self.fleche = fleche
        self.explosif = explosif
        self.fragile = fragile
        self.magique = magique
        self.element = element
        self.poids = poids
        self.frottements = frottements
        self.portee = portee
        self.tranchant = tranchant

    def check(self) -> bool:
        return (self.poids >= 0 and
                self.frottements >= 0 and
                self.portee >= 0 and
                self.tranchant >= 0)
    
    def stringify(self) -> str:
        return f"""{{
    "type": "arme",
    "nivele": true,
    "nom": "{self.nom}",
    "fantome": {self.fantome},
    "percant": {self.percant},
    "fleche": {self.fleche},
    "explosif": {self.explosif},
    "fragile": {self.fragile},
    "magique": {self.magique},
    "element": "{self.element},
    "poids": {self.poids},
    "frottements": {self.frottements},
    "portee": {self.portee},
    "tranchant": {self.tranchant}"
}}"""
    
    @classmethod
    def parse(cls, json: str):
        """Parse un json en ArmeSimpleNivele."""
        dictionnaire = parse(json)
        return ArmeSimpleNivele(dictionnaire["nom"], dictionnaire["fantome"], dictionnaire["percant"], dictionnaire["fleche"], dictionnaire["explosif"], dictionnaire["fragile"], dictionnaire["magique"], dictionnaire["element"], dictionnaire["poids"], dictionnaire["frottements"], dictionnaire["portee"], dictionnaire["tranchant"])

    @classmethod
    @property
    def champs(cls) -> dict[str, type[int|str|float|bool|mdl.Element]]:
        return {
            "fantome": bool,
            "percant": bool,
            "fleche": bool,
            "explosif": bool,
            "fragile": bool,
            "magique": bool,
            "element": mdl.Element,
            "poids": float,
            "frottements": float,
            "portee": float,
            "tranchant": float
        }

    @classmethod
    @property
    def acceptors(cls) -> dict[str, Callable[[str], bool]]:
        return {
            "fantome": lambda _: True,
            "percant": lambda _: True,
            "fleche": lambda _: True,
            "explosif": lambda _: True,
            "fragile": lambda _: True,
            "magique": lambda _: True,
            "element": lambda element: element in mdl.Element,
            "poids": lambda poids: float(poids) >= 0,
            "frottements": lambda frottements: float(frottements) >= 0,
            "portee": lambda portee: float(portee) >= 0,
            "tranchant": lambda tranchant: float(tranchant) >= 0
        }

    @classmethod
    @property
    def avertissements(cls) -> dict[str, str]:
        return {
            "fantome": "Cet avertissement n'est pas censé apparaître.",
            "percant": "Cet avertissement n'est pas censé apparaître.",
            "fleche": "Cet avertissement n'est pas censé apparaître.",
            "explosif": "Cet avertissement n'est pas censé apparaître.",
            "fragile": "Cet avertissement n'est pas censé apparaître.",
            "magique": "Cet avertissement n'est pas censé apparaître.",
            "element": "Choisissez un élément.",
            "poids": "Le poids doit être positif.",
            "frottements": "Le frottement doit être positif.",
            "portee": "La portée doit être positive.",
            "tranchant": "Les dégats doivent être positifs."
        }

    def make(self, niveau: int) -> mdl.ArmeSimple:
        """Crée un ArmeSimple à partir de l'instance."""
        arme = mdl.armes[(self.percant, self.fleche, self.explosif, self.fragile, self.magique)](mdl.NOWHERE, niveau, self.poids, self.frottements, self.portee, self.tranchant, self.element)
        arme.nom = self.nom
        arme.fantome = self.fantome
        return arme
