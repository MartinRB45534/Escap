"""
Fichier contenant la classe de stockage des Equippements.
"""

from __future__ import annotations
from json import loads as parse
from enum import StrEnum

import modele as mdl

from ...stockage import StockageCategorieNivelee
from ..entitee import EntiteeNivele
from ...espece import Especes

class EquippementNivele(EntiteeNivele):
    """Un Equippement tout simple."""

    champs = {
            "fantome": bool,
            "poids": float,
            "frottements": float,
            "type_equippement": StrEnum("type_equippement", [("Anneau", "Anneau"), ("Armure", "Armure"), ("Heaume", "Heaume")]),
            "defensif": StrEnum("defensif", [("non", "Pas d'effet défensif"), ("Plafond", "Dégats plafonnés"), ("Proportionnel", "Réduction proportionnelle des dégats"), ("Seuil", "Nullification des dégats en dessous d'un seuil"), ("Valeur", "Réduction des dégats d'une valeur fixe")]),
            "_degats": float,
            "pv": StrEnum("pv", [("non", "Pas d'effet sur les PVs"), ("PompeAPV", "Régénération des PVs d'un montant fixe"), ("RenforceRegenPV", "Augmentation proportionnelle de la régénération des PVs")]),
            "_pv": float,
            "pm": StrEnum("pm", [("non", "Pas d'effet sur les PMs"), ("PompeAPM", "Régénération des PMs d'un montant fixe"), ("RenforceRegenPM", "Augmentation proportionnelle de la régénération des PMs")]),
            "_pm": float,
            "accelerateur": bool,
            "_vitesse": float,
            "anoblisseur": bool,
            "_priorite": float,
            "elementaire": bool,
            "_element": mdl.Element,
            "_affinite": float,
            "tribal": bool,
            "_espece": Especes,
            "_taux_stats": float
        }

    niveles = {
            "fantome": False,
            "poids": False,
            "frottements": False,
            "type_equippement": False,
            "defensif": False,
            "_degats": True,
            "pv": False,
            "_pv": True,
            "pm": False,
            "_pm": True,
            "accelerateur": False,
            "_vitesse": True,
            "anoblisseur": False,
            "_priorite": True,
            "elementaire": False,
            "_element": False,
            "_affinite": True,
            "tribal": False,
            "_espece": False,
            "_taux_stats": True
        }

    acceptors = {
            "fantome": lambda _: True,
            "poids": lambda poids: float(poids) >= 0,
            "frottements": lambda frottements: float(frottements) >= 0,
            "type_equippement": lambda _: True,
            "defensif": lambda _: True,
            "_degats": lambda degats: float(degats) >= 0,
            "pv": lambda _: True,
            "_pv": lambda pv: float(pv) >= 0,
            "pm": lambda _: True,
            "_pm": lambda pm: float(pm) >= 0,
            "accelerateur": lambda _: True,
            "_vitesse": lambda vitesse: float(vitesse) >= 0,
            "anoblisseur": lambda _: True,
            "_priorite": lambda priorite: float(priorite) >= 0,
            "elementaire": lambda _: True,
            "_element": lambda _: True,
            "_affinite": lambda affinite: float(affinite) >= 0,
            "tribal": lambda _: True,
            "_espece": lambda _: True,
            "_taux_stats": lambda taux_stats: float(taux_stats) >= 0
        }

    avertissements = {
            "fantome": "Cet avertissement n'est pas censé apparaître.",
            "poids": "Le poids doit être positif.",
            "frottements": "Le frottement doit être positif.",
            "type_equippement": "Cet avertissement n'est pas censé apparaître non plus.",
            "defensif": "Cet avertissement n'est pas censé apparaître non plus.",
            "_degats": "Les dégats doivent être positifs.",
            "pv": "Cet avertissement n'est pas censé apparaître non plus.",
            "_pv": "La régénération pv doit être positive.",
            "pm": "Cet avertissement n'est pas censé apparaître non plus.",
            "_pm": "La régénération pm doit être positive.",
            "accelerateur": "Cet avertissement n'est pas censé apparaître non plus.",
            "_vitesse": "La vitesse doit être positive.",
            "anoblisseur": "Cet avertissement n'est pas censé apparaître non plus.",
            "_priorite": "La priorité doit être positive.",
            "elementaire": "Cet avertissement n'est pas censé apparaître non plus.",
            "_element": "Cet avertissement n'est pas censé apparaître non plus.",
            "_affinite": "L'affinité doit être positive.",
            "tribal": "Cet avertissement n'est pas censé apparaître non plus.",
            "_espece": "Cet avertissement n'est pas censé apparaître non plus.",
            "_taux_stats": "Le taux de stats doit être positif."
        }

    conditionnels = {
            "fantome": lambda dictionnaire: True,
            "poids": lambda dictionnaire: True,
            "frottements": lambda dictionnaire: True,
            "type_equippement": lambda dictionnaire: True,
            "defensif": lambda dictionnaire: True,
            "_degats": lambda dictionnaire: dictionnaire["defensif"] != "non",
            "pv": lambda dictionnaire: True,
            "_pv": lambda dictionnaire: dictionnaire["pv"] != "non",
            "pm": lambda dictionnaire: True,
            "_pm": lambda dictionnaire: dictionnaire["pm"] != "non",
            "accelerateur": lambda dictionnaire: True,
            "_vitesse": lambda dictionnaire: dictionnaire["accelerateur"]=="True",
            "anoblisseur": lambda dictionnaire: True,
            "_priorite": lambda dictionnaire: dictionnaire["anoblisseur"]=="True",
            "elementaire": lambda dictionnaire: True,
            "_element": lambda dictionnaire: dictionnaire["elementaire"]=="True",
            "_affinite": lambda dictionnaire: dictionnaire["elementaire"]=="True",
            "tribal": lambda dictionnaire: True,
            "_espece": lambda dictionnaire: dictionnaire["tribal"]=="True",
            "_taux_stats": lambda dictionnaire: dictionnaire["tribal"]=="True"
        }

    multiple = {
            "fantome": False,
            "poids": False,
            "frottements": False,
            "type_equippement": False,
            "defensif": False,
            "_degats": False,
            "pv": False,
            "_pv": False,
            "pm": False,
            "_pm": False,
            "accelerateur": False,
            "_vitesse": False,
            "anoblisseur": False,
            "_priorite": False,
            "elementaire": False,
            "_element": False,
            "_affinite": False,
            "tribal": False,
            "_espece": False,
            "_taux_stats": False
        }

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
    "type_equippement": "{self.type_equippement}",
    "defensif": "{self.defensif}",
    "_degats": {self._degats},
    "pv": "{self.pv}",
    "_pv": {self._pv},
    "pm": "{self.pm}",
    "_pm": {self._pm},
    "accelerateur": {self.accelerateur},
    "_vitesse": {self._vitesse},
    "anoblisseur": {self.anoblisseur},
    "_priorite": {self._priorite},
    "elementaire": {self.elementaire},
    "_element": "{self._element}",
    "_affinite": {self._affinite},
    "tribal": {self.tribal},
    "_espece": "{self._espece}",
    "_taux_stats": {self._taux_stats}
}}"""

    @classmethod
    def parse(cls, json: str):
        """Parse un json en EquippementNivele."""
        dictionnaire = parse(json)
        return EquippementNivele(dictionnaire["nom"], dictionnaire["fantome"], dictionnaire["poids"], dictionnaire["frottements"], dictionnaire["type_equippement"], dictionnaire["defensif"], dictionnaire["degats"], dictionnaire["pv"], dictionnaire["_pv"], dictionnaire["pm"], dictionnaire["_pm"], dictionnaire["accelerateur"], dictionnaire["vitesse"], dictionnaire["anoblisseur"], dictionnaire["priorite"], dictionnaire["elementaire"], mdl.Element(dictionnaire["element"]), dictionnaire["_affinite"], dictionnaire["tribal"], mdl.Espece(dictionnaire["espece"]), dictionnaire["_taux_stats"])

    def make(self, niveau: int) -> mdl.Equippement:
        """Crée un EquippementSimple à partir de l'instance."""
        equippement = mdl.equippements[(self.type_equippement, self.defensif, self.pv, self.pm, self.accelerateur, self.anoblisseur, self.elementaire, self.tribal)](mdl.NOWHERE, self.poids, self.frottements, self._degats[niveau] if self.defensif else 0, self._pv[niveau] if self.pv else 0, self._pm[niveau] if self.pm else 0, self._vitesse[niveau] if self.accelerateur else 0, self._priorite[niveau] if self.anoblisseur else 0, self._element if self.elementaire else None, self._affinite[niveau] if self.elementaire else 0, self._espece if self.tribal else None, self._taux_stats[niveau] if self.tribal else 0)
        equippement.nom = self.nom
        equippement.fantome = self.fantome
        return equippement

class Equippements(StockageCategorieNivelee):
    """Les informations des équippements."""
    nom = "Equippements"
    titre_nouveau = "Nouvel équippement"
    description = "Les équippement sont destinés à être équippés. Ils peuvent avoir des effets variés."
    avertissement = "Il existe déjà un équippement avec ce nom !"
    elements = {
        "Equippement": EquippementNivele
    }
