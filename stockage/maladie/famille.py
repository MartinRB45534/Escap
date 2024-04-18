"""
Classe de stockage des espèces.
"""

from __future__ import annotations
from json import loads as parse

import modele as mdl

from ..stockage import StockageCategorieUnique, StockageUnique

class FamilleMaladie(StockageUnique):
    """Les informations d'une famille de maladies."""

    champs= {}

    def __init__(self, nom: str):
        StockageUnique.__init__(self, nom)
        self.famille: mdl.FamilleMaladie|None = None

    def check(self) -> bool:
        return True

    def stringify(self) -> str:
        return f"""{{
    "nom": "{self.nom}"
}}"""

    @classmethod
    def parse(cls, json: str):
        dictionnaire = parse(json)
        return cls(dictionnaire["nom"])

    def make(self) -> mdl.FamilleMaladie:
        """Retourne l'espèce correspondante."""
        if self.famille is None:
            self.famille = mdl.FamilleMaladie(self.nom)
        return self.famille # Il faut que ce soit le même objet à chaque fois

class FamillesMaladies(StockageCategorieUnique):
    """Les informations des familles de aladies."""
    nom = "Familles de Maladies"
    titre_nouveau = "Nouvelle famille de maladies"
    description = "Chaque maladie doit appartenir à une famille. Certaines maladies peuvent donner une immunité à d'autres maladies de la même famille."
    avertissement = "Il existe déjà une famille avec ce nom !"
    elements = {
        "especes": FamilleMaladie
    }
