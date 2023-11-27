"""
Fichier contenant la classe de stockage des parchemins.
"""

from __future__ import annotations
from typing import Callable
from json import loads as parse

import modele as mdl

from ...stockage import StockageCategorie, StockageNivele, StockageUnique, StockageGlobal
from ..entitee import Entitee, EntiteeNivele

class Parchemins(StockageCategorie):
    """Les informations des parchemins."""
    nom = "Parchemins"
    titre_nouveau = "Nouveau parchemin"
    description = "Les parchemins sont des items consommables qui s'activent avec du mana. Les parchemins vierges n'ont pas encore d'effet placé, tandis que les parchemins préécrits ont besoin d'un effet à la création."
    avertissement = "Il existe déjà un item avec ce nom !"

    @property
    def all_noms(self) -> set[str]:
        return StockageGlobal.global_.items.all_noms()

    @classmethod
    @property
    def elements(cls) -> dict[str, type[StockageUnique]|tuple[type[StockageUnique], type[StockageNivele]]]:
        return {
            "parchemin vierge": (ParcheminVierge, ParcheminViergeNivele)
        }

class ParcheminVierge(Entitee):
    """Les informations d'un parchemin vierge."""
    def __init__(self, nom: str, latence_impregne:float,
                 taux_cout_caste: float, taux_cout_impregne: float,
                 taux_latence_caste: float, taux_latence_impregne: float):
        Entitee.__init__(self, nom)
        self.latence_impregne = latence_impregne
        self.taux_cout_caste = taux_cout_caste
        self.taux_cout_impregne = taux_cout_impregne
        self.taux_latence_caste = taux_latence_caste
        self.taux_latence_impregne = taux_latence_impregne

    def check(self) -> bool:
        return (self.latence_impregne >= 0 and
                self.taux_cout_caste >= 0 and
                self.taux_cout_impregne >= 0 and
                self.taux_latence_caste >= 0 and
                self.taux_latence_impregne >= 0)

    def stringify(self) -> str:
        return f"""{{
    "type": "parchemin vierge",
    "nivele": false,
    "nom": "{self.nom}",
    "latence_impregne": {self.latence_impregne},
    "taux_cout_caste": {self.taux_cout_caste},
    "taux_cout_impregne": {self.taux_cout_impregne},
    "taux_latence_caste": {self.taux_latence_caste},
    "taux_latence_impregne": {self.taux_latence_impregne}
}}"""

    @classmethod
    def parse(cls, json: str) -> ParcheminVierge:
        dictionnaire = parse(json)
        return ParcheminVierge(dictionnaire["nom"], dictionnaire["latence_impregne"], dictionnaire["taux_cout_caste"], dictionnaire["taux_cout_impregne"], dictionnaire["taux_latence_caste"], dictionnaire["taux_latence_impregne"])

    @classmethod
    @property
    def champs(cls) -> dict[str, type[int|str|float]]:
        return {
            "latence_impregne": float,
            "taux_cout_caste": float,
            "taux_cout_impregne": float,
            "taux_latence_caste": float,
            "taux_latence_impregne": float
        }

    @classmethod
    @property
    def acceptors(cls) -> dict[str, Callable[[str], bool]]:
        return {
            "latence_impregne": lambda latence: float(latence) >= 0,
            "taux_cout_caste": lambda taux: float(taux) >= 0,
            "taux_cout_impregne": lambda taux: float(taux) >= 0,
            "taux_latence_caste": lambda taux: float(taux) >= 0,
            "taux_latence_impregne": lambda taux: float(taux) >= 0
        }

    @classmethod
    @property
    def avertissements(cls) -> dict[str, str]:
        return {
            "latence_impregne": "La latence d'impregnation doit être positive.",
            "taux_cout_caste": "Le taux de cout de caste doit être positif.",
            "taux_cout_impregne": "Le taux de cout d'impregnation doit être positif.",
            "taux_latence_caste": "Le taux de latence de caste doit être positif.",
            "taux_latence_impregne": "Le taux de latence d'impregnation doit être positif."
        }

    def make(self) -> mdl.ParcheminVierge:
        """Retourne le parchemin correspondant."""
        effet = mdl.Impregne(mdl.NOONE, self.latence_impregne, mdl.NOWRITTING,
                             self.taux_cout_impregne, self.taux_cout_caste,
                             self.taux_latence_impregne, self.taux_latence_caste)
        parchemin = mdl.ParcheminVierge(mdl.NOWHERE, effet)
        return parchemin

class ParcheminViergeNivele(EntiteeNivele):
    """Les informations d'un parchemin vierge."""
    def __init__(self, nom: str, latence_impregne:list[float], taux_cout_caste:list[float],
                 taux_cout_impregne:list[float], taux_latence_caste:list[float],
                 taux_latence_impregne:list[float]):
        EntiteeNivele.__init__(self, nom)
        self.latence_impregne = latence_impregne
        self.taux_cout_caste = taux_cout_caste
        self.taux_cout_impregne = taux_cout_impregne
        self.taux_latence_caste = taux_latence_caste
        self.taux_latence_impregne = taux_latence_impregne

    def check(self) -> bool:
        return (len(self.latence_impregne) == 10 and
                len(self.taux_cout_caste) == 10 and
                len(self.taux_cout_impregne) == 10 and
                len(self.taux_latence_caste) == 10 and
                len(self.taux_latence_impregne) == 10 and
                all([latence >= 0 for latence in self.latence_impregne]) and
                all([taux >= 0 for taux in self.taux_cout_caste]) and
                all([taux >= 0 for taux in self.taux_cout_impregne]) and
                all([taux >= 0 for taux in self.taux_latence_caste]) and
                all([taux >= 0 for taux in self.taux_latence_impregne]))

    def stringify(self) -> str:
        return f"""{{
    "type": "parchemin vierge",
    "nivele": true,
    "latence_impregne": {self.latence_impregne},
    "taux_cout_caste": {self.taux_cout_caste},
    "taux_cout_impregne": {self.taux_cout_impregne},
    "taux_latence_caste": {self.taux_latence_caste},
    "taux_latence_impregne": {self.taux_latence_impregne}
}}"""

    @classmethod
    def parse(cls, json: str) -> ParcheminViergeNivele:
        dictionnaire = parse(json)
        return ParcheminViergeNivele(dictionnaire["nom"],  dictionnaire["latence_impregne"], dictionnaire["taux_cout_caste"], dictionnaire["taux_cout_impregne"], dictionnaire["taux_latence_caste"], dictionnaire["taux_latence_impregne"])

    @classmethod
    @property
    def champs(cls) -> dict[str, type[int|str|float]]:
        return {
            "latence_impregne": float,
            "taux_cout_caste": float,
            "taux_cout_impregne": float,
            "taux_latence_caste": float,
            "taux_latence_impregne": float
        }

    @classmethod
    @property
    def acceptors(cls) -> dict[str, Callable[[str], bool]]:
        return {
            "latence_impregne": lambda latence: float(latence) >= 0,
            "taux_cout_caste": lambda taux: float(taux) >= 0,
            "taux_cout_impregne": lambda taux: float(taux) >= 0,
            "taux_latence_caste": lambda taux: float(taux) >= 0,
            "taux_latence_impregne": lambda taux: float(taux) >= 0
        }

    @classmethod
    @property
    def avertissements(cls) -> dict[str, str]:
        return {
            "latence_impregne": "La latence d'impregnation doit être positive.",
            "taux_cout_caste": "Le taux de cout de caste doit être positif.",
            "taux_cout_impregne": "Le taux de cout d'impregnation doit être positif.",
            "taux_latence_caste": "Le taux de latence de caste doit être positif.",
            "taux_latence_impregne": "Le taux de latence d'impregnation doit être positif."
        }

    def make(self, niveau:int) -> mdl.ParcheminVierge:
        """Retourne le parchemin correspondant."""
        effet = mdl.Impregne(mdl.NOONE, self.latence_impregne[niveau], mdl.NOWRITTING,
                             self.taux_cout_impregne[niveau], self.taux_cout_caste[niveau],
                             self.taux_latence_impregne[niveau], self.taux_latence_caste[niveau])
        parchemin = mdl.ParcheminVierge(mdl.NOWHERE, effet)
        return parchemin
        