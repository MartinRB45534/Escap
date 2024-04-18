"""
Classe de stockage des espèces.
"""

from __future__ import annotations
from json import loads as parse

import modele as mdl

from .stockage import StockageCategorieUnique, StockageUnique
from .maladie import Maladies, MaladieNivele, FamillesMaladies, FamilleMaladie

class Espece(StockageUnique):
    """Les informations d'une espèce."""

    champs= {
            "nb_doigts": int,
            "maladie": Maladies,
            "immunite": float,
            "famille": FamillesMaladies,
            "immunite_famille": float
        }

    acceptors= {
            "nb_doigts": lambda nb_doigts: int(nb_doigts) > 0,
            "maladie": lambda maladie: maladie in Maladies.global_.trouve_stockage(Maladies).all_noms,
            "immunite": lambda immunite: float(immunite) >= 0,
            "famille": lambda famille: famille in FamillesMaladies.global_.trouve_stockage(FamillesMaladies).all_noms,
            "immunite_famille": lambda immunite_famille: float(immunite_famille) >= 0
        }

    avertissements= {
            "nb_doigts": "Le nombre de doigts doit être strictement positif.",
            "maladie": "Il faut choisir une maladie existante (peut-être qu'il n'en existe pas).",
            "immunite": "L'immunité doit être positive.",
            "famille": "Il faut choisir une famille de maladies existante (peut-être qu'il n'en existe pas).",
            "immunite_famille": "L'immunité doit être positive."
        }

    multiple= {
            "maladie": True,
            "famille": True
        }

    comultiple= {
            "maladie": ["immunite"],
            "famille": ["immunite_famille"]
        }

    def __init__(self, nom: str, nb_doigts: int, maladie: list[MaladieNivele], immunite: list[float],
                 famille: list[FamilleMaladie], immunite_famille: list[float]):
        StockageUnique.__init__(self, nom)
        self.nb_doigts = nb_doigts
        self.maladie = maladie
        self.immunite = immunite
        self.famille = famille
        self.immunite_famille = immunite_famille
        self.espece: mdl.Espece|None = None

    def check(self) -> bool:
        return (self.nb_doigts > 0 and
                all([immunite >= 0 for immunite in self.immunite]) and
                len(self.maladie) == len(self.immunite) and
                all([immunite_famille >= 0 for immunite_famille in self.immunite_famille]) and
                len(self.famille) == len(self.immunite_famille))

    def stringify(self) -> str:
        return f"""{{
    "nom": "{self.nom}",
    "nb_doigts": {self.nb_doigts},
    "maladie": {self.maladie},
    "immunite": {self.immunite},
    "famille": {self.famille},
    "immunite_famille": {self.immunite_famille}
}}"""

    @classmethod
    def parse(cls, json: str):
        dictionnaire = parse(json)
        return cls(dictionnaire["nom"], dictionnaire["nb_doigts"], dictionnaire["maladie"], dictionnaire["immunite"], dictionnaire["famille"], dictionnaire["immunite_famille"])

    def make(self) -> mdl.Espece:
        """Retourne l'espèce correspondante."""
        if self.espece is None:
            immunites:dict[str, float] = {}
            for maladie, immunite in zip(self.maladie, self.immunite, strict=True):
                immunites[maladie.nom] = immunite
            for famille, immunite_famille in zip(self.famille, self.immunite_famille, strict=True):
                immunites[famille.nom] = immunite_famille
            self.espece = mdl.Espece(self.nom, self.nb_doigts, immunites)
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
