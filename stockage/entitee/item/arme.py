"""
Fichier contenant la classe de stockage des armes.
"""

from __future__ import annotations
from typing import Callable
from json import loads as parse

import modele as mdl

from ...stockage import StockageCategorieNivelee, StockageNivele
from ..entitee import EntiteeNivele

class Armes(StockageCategorieNivelee):
    """Les informations des armes."""
    nom = "Armes"
    titre_nouveau = "Nouvelle arme"
    description = "Les armes sont destinés à être équippées. Elles permettent d'effectuer des attaques différentes. Les épées et les lances en particulier interagissent avec certains skills."
    avertissement = "Il existe déjà une arme avec ce nom !"

    @property
    def elements(self) -> dict[str, type[StockageNivele]]:
        return {
            "Epee": EpeeNivele,
            "Lance": LanceNivele,
            "Autre": ArmeNivele
        }

class ArmeNivele(EntiteeNivele):
    """Une arme toute simple."""
    def __init__(self, nom: str, fantome: bool,
                 element:mdl.Element, poids:list[float], frottements:list[float], portee:list[float], tranchant:list[float]):
        EntiteeNivele.__init__(self, nom)
        self.fantome = fantome
        self.element = element
        self.poids = poids
        self.frottements = frottements
        self.portee = portee
        self.tranchant = tranchant

    def check(self) -> bool:
        return (all([poids >= 0 for poids in self.poids]) and
                all([frottements >= 0 for frottements in self.frottements]) and
                all([portee >= 0 for portee in self.portee]) and
                all([tranchant >= 0 for tranchant in self.tranchant]))

    def stringify(self) -> str:
        return f"""{{
    "type": "arme",
    "nivele": true,
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
        """Parse un json en ArmeNivele."""
        dictionnaire = parse(json)
        return ArmeNivele(dictionnaire["nom"], dictionnaire["fantome"], dictionnaire["element"], dictionnaire["poids"], dictionnaire["frottements"], dictionnaire["portee"], dictionnaire["tranchant"])

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
    def niveles(cls) -> dict[str, bool]:
        return {
            "fantome": False,
            "element": False,
            "poids": False,
            "frottements": False,
            "portee": True,
            "tranchant": True
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
            "tranchant": "Le tranchant doit être positif."
        }
    
    @classmethod
    @property
    def conditionnels(cls) -> dict[str, Callable[[dict[str, str]], bool]]:
        return {
            "fantome": lambda dictionnaire: True,
            "element": lambda dictionnaire: True,
            "poids": lambda dictionnaire: True,
            "frottements": lambda dictionnaire: True,
            "portee": lambda dictionnaire: True,
            "tranchant": lambda dictionnaire: True
        }

    def make(self, niveau: int) -> mdl.Arme:
        """Crée un ArmeSimple à partir de l'instance."""
        arme = mdl.Arme(mdl.NOWHERE, self.poids[niveau], self.frottements[niveau], self.element, self.tranchant[niveau], self.portee[niveau])
        arme.nom = self.nom
        arme.fantome = self.fantome
        return arme

class EpeeNivele(ArmeNivele):
    """Une épée."""
    def make(self, niveau: int) -> mdl.Epee:
        """Crée une Epee à partir de l'instance."""
        epee = mdl.Epee(mdl.NOWHERE, self.poids[niveau], self.frottements[niveau], self.element, self.tranchant[niveau], self.portee[niveau])
        epee.nom = self.nom
        epee.fantome = self.fantome
        return epee

class LanceNivele(ArmeNivele):
    """Une lance."""
    def make(self, niveau: int) -> mdl.Lance:
        """Crée une Lance à partir de l'instance."""
        lance = mdl.Lance(mdl.NOWHERE, self.poids[niveau], self.frottements[niveau], self.element, self.tranchant[niveau], self.portee[niveau])
        lance.nom = self.nom
        lance.fantome = self.fantome
        return lance
