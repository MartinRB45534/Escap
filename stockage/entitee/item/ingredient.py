"""
Fichier contenant la classe de stockage des armes.
"""

from __future__ import annotations
from json import loads as parse

import modele as mdl

from ...stockage import StockageCategorieNivelee
from ..entitee import EntiteeNivele

class IngredientNivele(EntiteeNivele):
    """Un ingrédient toute simple."""

    champs = {
            "fantome": bool,
            "poids": float,
            "frottements": float,
        }

    niveles = {
            "fantome": False,
            "poids": True,
            "frottements": True,
        }

    acceptors = {
            "fantome": lambda _: True,
            "poids": lambda poids: float(poids) >= 0,
            "frottements": lambda frottements: float(frottements) >= 0,
        }

    avertissements = {
            "fantome": "Cet avertissement n'est pas censé apparaître.",
            "poids": "Le poids doit être positif.",
            "frottements": "Le frottement doit être positif.",
        }

    conditionnels = {
            "fantome": lambda dictionnaire: True,
            "poids": lambda dictionnaire: True,
            "frottements": lambda dictionnaire: True,
        }

    multiple = {
            "fantome": False,
            "poids": False,
            "frottements": False,
        }

    def __init__(self, nom: str, fantome: bool,
                 poids:list[float], frottements:list[float]):
        EntiteeNivele.__init__(self, nom)
        self.fantome = fantome
        self.poids = poids
        self.frottements = frottements

    def check(self) -> bool:
        return (all([poid >= 0 for poid in self.poids]) and
                all([frottement >= 0 for frottement in self.frottements]))

    def stringify(self) -> str:
        return f"""{{
    "type": "ingredient",
    "nivele": true,
    "nom": "{self.nom}",
    "fantome": {self.fantome},
    "poids": {self.poids},
    "frottements": {self.frottements}"
}}"""

    @classmethod
    def parse(cls, json: str):
        """Parse un json en IngredientNivele."""
        dictionnaire = parse(json)
        return IngredientNivele(dictionnaire["nom"], dictionnaire["fantome"], dictionnaire["poids"], dictionnaire["frottements"])

    def make(self, niveau: int) -> mdl.Ingredient:
        """Crée un IngredientSimple à partir de l'instance."""
        arme = mdl.Ingredient(mdl.NOWHERE, self.poids[niveau], self.frottements[niveau])
        arme.nom = self.nom
        arme.fantome = self.fantome
        return arme

class Ingredients(StockageCategorieNivelee):
    """Les informations des ingredients."""
    nom = "Ingredients"
    titre_nouveau = "Nouvel ingrédient"
    description = "Les ingrédients "
    avertissement = "Il existe déjà un ingrédient avec ce nom !"
    elements = {
        "Ingredient": IngredientNivele
    }
