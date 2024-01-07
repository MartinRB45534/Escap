"""
Classe de stockage des espèces.
"""

from __future__ import annotations
from typing import Optional,  Callable
from json import loads as parse

import modele as mdl

from .stockage import StockageCategorieUnique, StockageUnique

class Especes(StockageCategorieUnique):
    """Les informations des espèces."""
    nom = "Especes"
    titre_nouveau = "Nouvelle espèce"
    description = "Chaque espèce a un nom et un nombre de doigts possiblement nul (nombre d'anneaux qu'elle peut porter). Chaque agissant a une ou plusieurs espèces (seule la première est prise en compte pour les doigts). Certains éléments du jeu interagissent avec les espèces."
    avertissement = "Il existe déjà une espèce avec ce nom !"

    @property
    def elements(self) -> dict[str, type[StockageUnique]]:
        return {
            "especes": Espece
        }

class Espece(StockageUnique):
    """Les informations d'une espèce."""
    def __init__(self, nom: str, nb_doigts: int):
        StockageUnique.__init__(self, nom)
        self.nb_doigts = nb_doigts
        self.espece:Optional[mdl.Espece] = None

    def check(self) -> bool:
        return self.nb_doigts > 0

    def stringify(self) -> str:
        return f"""{{
    "nom": "{self.nom}",
    "nb_doigts": {self.nb_doigts}
}}"""

    @classmethod
    def parse(cls, json: str):
        dictionnaire = parse(json)
        return cls(dictionnaire["nom"], dictionnaire["nb_doigts"])

    @classmethod
    @property
    def champs(cls) -> dict[str, type]:
        return {
            "nb_doigts": int
        }

    @classmethod
    @property
    def acceptors(cls) -> dict[str, Callable[[str], bool]]:
        return {
            "nb_doigts": lambda nb_doigts: int(nb_doigts) > 0
        }

    @classmethod
    @property
    def avertissements(cls) -> dict[str, str]:
        return {
            "nb_doigts": "Le nombre de doigts doit être strictement positif."
        }

    @classmethod
    @property
    def conditionnels(cls) -> dict[str, Callable[[dict[str, str|list[str]]], bool]]:
        return {
            "nb_doigts": lambda dictionnaire: True
        }

    @classmethod
    @property
    def multiple(cls) -> dict[str, bool]:
        return{
            "nb_doigts": False
        }

    def make(self) -> mdl.Espece:
        """Retourne l'espèce correspondante."""
        if self.espece is None:
            self.espece = mdl.Espece(self.nom, self.nb_doigts)
        return self.espece # Il faut que ce soit le même objet à chaque fois
