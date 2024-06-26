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
            "poids": True,
            "frottements": True,
        }

    acceptors = {
            "poids": lambda poids: float(poids) >= 0,
            "frottements": lambda frottements: float(frottements) >= 0,
        }

    avertissements = {
            "poids": "Le poids doit être positif.",
            "frottements": "Le frottement doit être positif.",
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

    def make(self, niveau: int) -> type[mdl.Ingredient]:
        """Crée un IngredientSimple à partir de l'instance."""
        class IngredientNiveau(mdl.Ingredient, mdl.Nomme):
            """Un ingrédient."""
            poids = self.poids[niveau]
            frottements = self.frottements[niveau]
            fantome = self.fantome
        IngredientNiveau.nom = self.nom
        IngredientNiveau.niveau = niveau
        return IngredientNiveau

class Ingredients(StockageCategorieNivelee):
    """Les informations des ingredients."""
    nom = "Ingredients"
    titre_nouveau = "Nouvel ingrédient"
    description = "Les ingrédients "
    avertissement = "Il existe déjà un ingrédient avec ce nom !"
    elements = {
        "Ingredient": IngredientNivele
    }
