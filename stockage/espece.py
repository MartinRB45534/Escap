"""
Classe de stockage des espèces.
"""

from __future__ import annotations
from json import loads as parse

import modele as mdl

from .stockage import StockageCategorieUnique, StockageUnique

class Espece(StockageUnique):
    """Les informations d'une espèce."""

    champs= {
            "nb_doigts": int
        }

    acceptors= {
            "nb_doigts": lambda nb_doigts: int(nb_doigts) > 0
        }

    avertissements= {
            "nb_doigts": "Le nombre de doigts doit être strictement positif."
        }

    conditionnels= {
            "nb_doigts": lambda dictionnaire: True
        }

    multiple= {
            "nb_doigts": False
        }

    def __init__(self, nom: str, nb_doigts: int):
        StockageUnique.__init__(self, nom)
        self.nb_doigts = nb_doigts
        self.espece: mdl.Espece|None = None

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

    def make(self) -> mdl.Espece:
        """Retourne l'espèce correspondante."""
        if self.espece is None:
            self.espece = mdl.Espece(self.nom, self.nb_doigts)
        return self.espece # Il faut que ce soit le même objet à chaque fois

class Especes(StockageCategorieUnique):
    """Les informations des espèces."""
    nom = "Especes"
    titre_nouveau = "Nouvelle espèce"
    description = "Chaque espèce a un nom et un nombre de doigts possiblement nul (nombre d'anneaux qu'elle peut porter). Chaque agissant a une ou plusieurs espèces (seule la première est prise en compte pour les doigts). Certains éléments du jeu interagissent avec les espèces."
    avertissement = "Il existe déjà une espèce avec ce nom !"
    elements = {
            "especes": Espece
        }
