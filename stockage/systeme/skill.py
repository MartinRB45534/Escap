"""
Fichier contenant la classe de stockage des armes.
"""

from __future__ import annotations
from json import loads as parse

import modele as mdl

from ..stockage import StockageCategorieNivelee, StockageNivele

class SkillNivele(StockageNivele):
    """Une arme toute simple."""

    champs = {
            "fantome": bool,
            "element": mdl.Element,
            "poids": float,
            "frottements": float,
            "portee": float,
            "tranchant": float
        }

    niveles = {
            "fantome": False,
            "element": False,
            "poids": False,
            "frottements": False,
            "portee": True,
            "tranchant": True
        }

    acceptors = {
            "fantome": lambda _: True,
            "element": lambda _: True,
            "poids": lambda poids: float(poids) >= 0,
            "frottements": lambda frottements: float(frottements) >= 0,
            "portee": lambda portee: float(portee) >= 0,
            "tranchant": lambda tranchant: float(tranchant) >= 0
        }

    avertissements = {
            "fantome": "Cet avertissement n'est pas censé apparaître.",
            "element": "Cet avertissement n'est pas censé apparaître non plus.",
            "poids": "Le poids doit être positif.",
            "frottements": "Le frottement doit être positif.",
            "portee": "La portée doit être positive.",
            "tranchant": "Le tranchant doit être positif."
        }

    conditionnels = {
            "fantome": lambda dictionnaire: True,
            "element": lambda dictionnaire: True,
            "poids": lambda dictionnaire: True,
            "frottements": lambda dictionnaire: True,
            "portee": lambda dictionnaire: True,
            "tranchant": lambda dictionnaire: True
        }

    multiple = {
            "fantome": False,
            "element": False,
            "poids": False,
            "frottements": False,
            "portee": False,
            "tranchant": False
        }

    def __init__(self, nom: str, fantome: bool,
                 element:mdl.Element, poids:float, frottements:float,
                 portee:list[float], tranchant:list[float]):
        EntiteeNivele.__init__(self, nom)
        self.fantome = fantome
        self.element = element
        self.poids = poids
        self.frottements = frottements
        self.portee = portee
        self.tranchant = tranchant

    def check(self) -> bool:
        return (self.poids >= 0 and
                self.frottements >= 0 and
                all(portee >= 0 for portee in self.portee) and
                all(tranchant >= 0 for tranchant in self.tranchant))

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
        return ArmeNivele(dictionnaire["nom"], dictionnaire["fantome"], mdl.Element(dictionnaire["element"]), dictionnaire["poids"], dictionnaire["frottements"], dictionnaire["portee"], dictionnaire["tranchant"])

    def make(self, niveau: int) -> mdl.Arme:
        """Crée un ArmeSimple à partir de l'instance."""
        arme = mdl.Arme(mdl.NOWHERE, self.poids, self.frottements, self.element, self.tranchant[niveau], self.portee[niveau])
        arme.nom = self.nom
        arme.fantome = self.fantome
        return arme

class EpeeNivele(ArmeNivele):
    """Une épée."""
    def make(self, niveau: int) -> mdl.Epee:
        """Crée une Epee à partir de l'instance."""
        epee = mdl.Epee(mdl.NOWHERE, self.poids, self.frottements, self.element, self.tranchant[niveau], self.portee[niveau])
        epee.nom = self.nom
        epee.fantome = self.fantome
        return epee

class LanceNivele(ArmeNivele):
    """Une lance."""
    def make(self, niveau: int) -> mdl.Lance:
        """Crée une Lance à partir de l'instance."""
        lance = mdl.Lance(mdl.NOWHERE, self.poids, self.frottements, self.element, self.tranchant[niveau], self.portee[niveau])
        lance.nom = self.nom
        lance.fantome = self.fantome
        return lance

class Armes(StockageCategorieNivelee):
    """Les informations des armes."""
    nom = "Armes"
    titre_nouveau = "Nouvelle arme"
    description = "Les armes sont destinés à être équippées. Elles permettent d'effectuer des attaques différentes. Les épées et les lances en particulier interagissent avec certains skills."
    avertissement = "Il existe déjà une arme avec ce nom !"
    elements = {
        "Epee": EpeeNivele,
        "Lance": LanceNivele,
        "Autre": ArmeNivele
    }
