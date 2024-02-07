"""
Fichier contenant la classe de stockage des Equippements.
"""

from __future__ import annotations
from typing import Callable
from json import loads as parse

import modele as mdl

from ...stockage import StockageCategorieNivelee, StockageNivele
from ..entitee import EntiteeNivele

class Equippements(StockageCategorieNivelee):
    """Les informations des équippements."""
    nom = "Equippements"
    titre_nouveau = "Nouvel équippement"
    description = "Les équippement sont destinés à être équippés. Ils peuvent avoir des effets variés."
    avertissement = "Il existe déjà un équippement avec ce nom !"

    @property
    def elements(self) -> dict[str, type[StockageNivele]]:
        return {
            "Equippement": EquippementNivele
        }

class EquippementNivele(EntiteeNivele):
    """Une Equippement toute simple."""
    def __init__(self, nom: str, fantome: bool, poids:float, frottements:float,
                 type_equippement: str, defensif: str, degats: list[float],
                 pv: str, _pv: list[int], pm: str, _pm: list[int],
                 accelerateur: bool, vitesse: list[int], anoblisseur: bool,
                 priorite: list[int], elementaire: bool, element: mdl.Element,
                 _affinite: list[int], tribal: bool, espece: mdl.Espece,
                 _taux_stats: list[int]):
        EntiteeNivele.__init__(self, nom)
        self.fantome = fantome
        self.poids = poids
        self.frottements = frottements
        self.type_equippement = type_equippement
        self.defensif = defensif
        self._degats = degats
        self.pv = pv
        self._pv = _pv
        self.pm = pm
        self._pm = _pm
        self.accelerateur = accelerateur
        self._vitesse = vitesse
        self.anoblisseur = anoblisseur
        self._priorite = priorite
        self.elementaire = elementaire
        self._element = element
        self._affinite = _affinite
        self.tribal = tribal
        self._espece = espece
        self._taux_stats = _taux_stats

    def check(self) -> bool:
        return (self.poids >= 0 and
                self.frottements >= 0 and
                self.type_equippement in ["Anneau", "Armure", "Heaume"] and
                all([degats >= 0 for degats in self._degats]))

    def stringify(self) -> str:
        return f"""{{
    "type": "Equippement",
    "nivele": true,
    "nom": "{self.nom}",
    "fantome": {self.fantome},
    "poids": {self.poids},
    "frottements": {self.frottements},
    "type_equippement": "{self.type_equippement}"

}}"""

    @classmethod
    def parse(cls, json: str):
        """Parse un json en EquippementNivele."""
        dictionnaire = parse(json)
        return EquippementNivele(dictionnaire["nom"], dictionnaire["fantome"], dictionnaire["poids"], dictionnaire["frottements"], dictionnaire["type_equippement"], dictionnaire["defensif"], dictionnaire["degats"], dictionnaire["pv"], dictionnaire["_pv"], dictionnaire["pm"], dictionnaire["_pm"], dictionnaire["accelerateur"], dictionnaire["vitesse"], dictionnaire["anoblisseur"], dictionnaire["priorite"], dictionnaire["elementaire"], mdl.Element(dictionnaire["element"]), dictionnaire["_affinite"], dictionnaire["tribal"], mdl.Espece(dictionnaire["espece"]), dictionnaire["_taux_stats"])

    @classmethod
    @property
    def champs(cls) -> dict[str, type[int|str|float|bool|mdl.Element]]:
        return {
            "fantome": bool,
            "poids": float,
            "frottements": float,
            "type_equippement": str,
        }

    @classmethod
    @property
    def niveles(cls) -> dict[str, bool]:
        return {
            "fantome": False,
            "poids": False,
            "frottements": False,
            "type_equippement": False,
        }

    @classmethod
    @property
    def acceptors(cls) -> dict[str, Callable[[str], bool]]:
        return {
            "fantome": lambda _: True,
            "poids": lambda poids: float(poids) >= 0,
            "frottements": lambda frottements: float(frottements) >= 0,
            "type_equippement": lambda type_equippement:
                type_equippement in ["Anneau", "Armure", "Heaume"]
        }

    @classmethod
    @property
    def avertissements(cls) -> dict[str, str]:
        return {
            "fantome": "Cet avertissement n'est pas censé apparaître.",
            "poids": "Le poids doit être positif.",
            "frottements": "Le frottement doit être positif.",
            "type_equippement": "Il faut choisir un type d'équippement."
        }

    @classmethod
    @property
    def conditionnels(cls) -> dict[str, Callable[[dict[str, str|list[str]]], bool]]:
        return {
            "fantome": lambda dictionnaire: True,
            "poids": lambda dictionnaire: True,
            "frottements": lambda dictionnaire: True,
            "type_equippement": lambda dictionnaire: True
        }

    @classmethod
    @property
    def multiple(cls) -> dict[str, bool]:
        return {
            "fantome": False,
            "poids": False,
            "frottements": False,
            "type_equippement": False,
        }

    def make(self, niveau: int) -> mdl.Equippement:
        """Crée un EquippementSimple à partir de l'instance."""
        equippement = mdl.equippements[(self.type_equippement, self.defensif, self.pv, self.pm, self.accelerateur, self.anoblisseur, self.elementaire, self.tribal)](mdl.NOWHERE, self.poids, self.frottements, self._degats[niveau] if self.defensif else 0, self._pv[niveau] if self.pv else 0, self._pm[niveau] if self.pm else 0, self._vitesse[niveau] if self.accelerateur else 0, self._priorite[niveau] if self.anoblisseur else 0, self._element if self.elementaire else None, self._affinite[niveau] if self.elementaire else 0, self._espece if self.tribal else None, self._taux_stats[niveau] if self.tribal else 0)
        equippement.nom = self.nom
        equippement.fantome = self.fantome
        return equippement
