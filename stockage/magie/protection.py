"""
Fichier contenant la classe de stockage des magies de protection.
"""

from __future__ import annotations
from json import loads as parse

import modele as mdl

from .magie import MagieNivele

class MagieProtectionNivelee(MagieNivele):
    """Une magie de protection."""

    champs = {
            "cible": bool,
            "cible_multiple": bool,
            "zone": bool,
            "latence": float,
            "gain_xp": float,
            "cout_pm": float,
            "duree": float,
            "pv": float,
            "portee": float,
            "resistance_elementaire": bool,
            "element": mdl.Element,
            "taux_pv": float
        }

    niveles = {
            "latence": True,
            "gain_xp": True,
            "cout_pm": True,
            "duree": True,
            "pv": True,
            "taux_pv": True,
        }

    acceptors = {
            "latence": lambda latence: float(latence) >= 0,
            "gain_xp": lambda gain_xp: float(gain_xp) >= 0,
            "cout_pm": lambda cout_pm: float(cout_pm) >= 0,
            "duree": lambda duree: float(duree) >= 0,
            "pv": lambda pv: float(pv) >= 0,
            "portee": lambda portee: float(portee) >= 0,
            "taux_pv": lambda taux_pv: 0 <= float(taux_pv) <= 1,
        }

    avertissements = {
            "latence": "La latence doit être positive.",
            "gain_xp": "Le gain d'expérience doit être positif.",
            "cout_pm": "Le coût en points de mana doit être positif.",
            "duree": "La durée doit être positive.",
            "pv": "Le gain de points de vie doit être positif.",
            "portee": "La portée doit être positive.",
            "taux_pv": "Le taux de points de vie doit être compris entre 0 et 1.",
        }

    conditionnels = {
            "zone": lambda dictionnaire: dictionnaire["cible"]=="False" and dictionnaire["cible_multiple"]=="False",
            "portee": lambda dictionnaire: dictionnaire["zone"]=="True",
            "element": lambda dictionnaire: dictionnaire["resistance_elementaire"]=="True",
            "taux_pv": lambda dictionnaire: dictionnaire["resistance_elementaire"]=="True"
        }

    def __init__(self, nom: str, cible: bool, cible_multiple: bool, zone: bool,
                 latence: list[float], gain_xp: list[float], cout_pm: list[float],
                 duree: list[float], pv: list[float], portee: list[float],
                 resistance_elementaire: bool, element: mdl.Element, taux_pv: list[float]):
        MagieNivele.__init__(self, nom)
        self.latence = latence
        self.gain_xp = gain_xp
        self.cible = cible
        self.cible_multiple = cible_multiple
        self.zone = zone
        self.cout_pm = cout_pm
        self.duree = duree
        self.pv = pv
        self.portee = portee
        self.resistance_elementaire = resistance_elementaire
        self.element = element
        self.taux_pv = taux_pv

    def check(self) -> bool:
        return (all(latence >= 0 for latence in self.latence) and
                all(gain >= 0 for gain in self.gain_xp) and
                all(cout_pm >= 0 for cout_pm in self.cout_pm) and
                all(duree >= 0 for duree in self.duree) and
                all(pv >= 0 for pv in self.pv) and
                all(0 <= taux_pv <= 1 for taux_pv in self.taux_pv))

    def stringify(self) -> str:
        return f"""{{
    "type": "magie_protection",
    "nivele": true,
    "nom": "{self.nom}",
    "cible": {self.cible},
    "cible_multiple": {self.cible_multiple},
    "zone": {self.zone},
    "latence": {self.latence},
    "gain_xp": {self.gain_xp},
    "cout_pm": {self.cout_pm},
    "duree": {self.duree},
    "pv": {self.pv},
    "portee": {self.portee},
    "resistance_elementaire": {self.resistance_elementaire},
    "element": "{self.element}",
    "taux_pv": {self.taux_pv}
}}"""

    @classmethod
    def parse(cls, json: str):
        """Parse un json en BouclierNivele."""
        dictionnaire = parse(json)
        return MagieProtectionNivelee(dictionnaire["nom"], dictionnaire["cible"], dictionnaire["cible_multiple"], dictionnaire["zone"], dictionnaire["latence"], dictionnaire["gain_xp"], dictionnaire["cout_pm"], dictionnaire["duree"], dictionnaire["pv"], dictionnaire["portee"], dictionnaire["resistance_elementaire"], mdl.Element(dictionnaire["element"]), dictionnaire["taux_pv"])

    def make(self, niveau: int):
        """Crée une magie à partir de l'instance."""
        classe = mdl.magies_protection[(self.cible, self.cible_multiple, self.zone, self.resistance_elementaire)]
        class MagieProtectionNiveau(classe, mdl.Nomme):
            """Une magie de protection."""
            duree = self.duree[niveau]
            pv = self.pv[niveau]
            latence_max = self.latence[niveau]
            gain_xp = self.gain_xp[niveau]
            cout = self.cout_pm[niveau]
            if self.zone:
                portee = self.portee
            if self.resistance_elementaire:
                element = self.element
                taux = self.taux_pv[niveau]
        MagieProtectionNiveau.nom = self.nom
        MagieProtectionNiveau.niveau = niveau
        return MagieProtectionNiveau
