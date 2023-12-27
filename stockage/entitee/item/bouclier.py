"""
Fichier contenant la classe de stockage des boucliers.
"""

from __future__ import annotations
from typing import Callable
from json import loads as parse

import modele as mdl

from ...stockage import StockageCategorieNivelee, StockageNivele
from ..entitee import EntiteeNivele

class Boucliers(StockageCategorieNivelee):
    """Les informations des boucliers."""
    nom = "Boucliers"
    titre_nouveau = "Nouveau bouclier"
    description = "Les boucliers sont destinés à être équippés. Ils permettent de défendre une zone contre les attaques."
    avertissement = "Il existe déjà un bouclier avec ce nom !"

    @property
    def elements(self) -> dict[str, type[StockageNivele]]:
        return {
            "Bouclier": BouclierNivele
        }

class BouclierNivele(EntiteeNivele):
    """Une bouclier toute simple."""
    def __init__(self, nom: str, fantome: bool,
                 poids:list[float], frottements:list[float], degats_bloques:list[float], taux_degats:list[float]):
        EntiteeNivele.__init__(self, nom)
        self.fantome = fantome
        self.poids = poids
        self.frottements = frottements
        self.degats_bloques = degats_bloques
        self.taux_degats = taux_degats

    def check(self) -> bool:
        return (all([poids >= 0 for poids in self.poids]) and
                all([frottements >= 0 for frottements in self.frottements]) and
                all([degats_bloques >= 0 for degats_bloques in self.degats_bloques]) and
                all([taux_degats >= 0 for taux_degats in self. taux_degats]))

    def stringify(self) -> str:
        return f"""{{
    "type": "bouclier",
    "nivele": true,
    "nom": "{self.nom}",
    "fantome": {self.fantome},
    "poids": {self.poids},
    "frottements": {self.frottements},
    "degats_bloques": {self.degats_bloques},
    "taux_degats": {self.taux_degats}"
}}"""

    @classmethod
    def parse(cls, json: str):
        """Parse un json en BouclierNivele."""
        dictionnaire = parse(json)
        return BouclierNivele(dictionnaire["nom"], dictionnaire["fantome"], dictionnaire["poids"], dictionnaire["frottements"], dictionnaire["degats_bloques"], dictionnaire["taux_degats"])

    @classmethod
    @property
    def champs(cls) -> dict[str, type[int|str|float|bool|mdl.Element]]:
        return {
            "fantome": bool,
            "poids": float,
            "frottements": float,
            "degats_bloques": float,
            "taux_degats": float
        }

    @classmethod
    @property
    def niveles(cls) -> dict[str, bool]:
        return {
            "fantome": False,
            "poids": False,
            "frottements": False,
            "degats_bloques": True,
            "taux_degats": True
        }

    @classmethod
    @property
    def acceptors(cls) -> dict[str, Callable[[str], bool]]:
        return {
            "fantome": lambda _: True,
            "poids": lambda poids: float(poids) >= 0,
            "frottements": lambda frottements: float(frottements) >= 0,
            "degats_bloques": lambda degats_bloques: float(degats_bloques) >= 0,
            "taux_degats": lambda taux_degats: float(taux_degats) >= 0
        }

    @classmethod
    @property
    def avertissements(cls) -> dict[str, str]:
        return {
            "fantome": "Cet avertissement n'est pas censé apparaître.",
            "poids": "Le poids doit être positif.",
            "frottements": "Le frottement doit être positif.",
            "degats_bloques": "La quantité de dégats bloqués doit être positive.",
            "taux_degats": "Le taux de dégats bloqué doit être positif."
        }

    def make(self, niveau: int) -> mdl.Bouclier:
        """Crée un BouclierSimple à partir de l'instance."""
        bouclier = mdl.Bouclier(mdl.NOWHERE, self.poids[niveau], self.frottements[niveau], self.degats_bloques[niveau], self.taux_degats[niveau])
        bouclier.nom = self.nom
        bouclier.fantome = self.fantome
        return bouclier
