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
            "cible": False,
            "cible_multiple": False,
            "zone": False,
            "latence": True,
            "gain_xp": True,
            "cout_pm": True,
            "duree": True,
            "pv": True,
            "portee": False,
            "resistance_elementaire": False,
            "element": False,
            "taux_pv": True
        }

    acceptors = {
            "cible": lambda _: True,
            "cible_multiple": lambda _: True,
            "zone": lambda _: True,
            "latence": lambda latence: float(latence) >= 0,
            "gain_xp": lambda gain_xp: float(gain_xp) >= 0,
            "cout_pm": lambda cout_pm: float(cout_pm) >= 0,
            "duree": lambda duree: float(duree) >= 0,
            "pv": lambda pv: float(pv) >= 0,
            "portee": lambda portee: float(portee) >= 0,
            "resistance_elementaire": lambda _: True,
            "element": lambda element: True,
            "taux_pv": lambda taux_pv: 0 <= float(taux_pv) <= 1
        }

    avertissements = {
            "cible": "Cet avertissement n'est pas censé apparaître.",
            "cible_multiple": "Cet avertissement n'est pas censé apparaître.",
            "zone": "Cet avertissement n'est pas censé apparaître.",
            "latence": "La latence doit être positive.",
            "gain_xp": "Le gain d'expérience doit être positif.",
            "cout_pm": "Le coût en points de mana doit être positif.",
            "duree": "La durée doit être positive.",
            "pv": "Le gain de points de vie doit être positif.",
            "portee": "La portée doit être positive.",
            "resistance_elementaire": "Cet avertissement n'est pas censé apparaître.",
            "element": "Cet avertissement n'est pas censé apparaître.",
            "taux_pv": "Le taux de points de vie doit être compris entre 0 et 1."
        }

    conditionnels = {
            "cible": lambda dictionnaire: True,
            "cible_multiple": lambda dictionnaire: True,
            "zone": lambda dictionnaire: dictionnaire["cible"]=="False" and dictionnaire["cible_multiple"]=="False",
            "latence": lambda dictionnaire: True,
            "gain_xp": lambda dictionnaire: True,
            "cout_pm": lambda dictionnaire: True,
            "duree": lambda dictionnaire: True,
            "pv": lambda dictionnaire: True,
            "portee": lambda dictionnaire: dictionnaire["zone"]=="True",
            "resistance_elementaire": lambda dictionnaire: True,
            "element": lambda dictionnaire: dictionnaire["resistance_elementaire"]=="True",
            "taux_pv": lambda dictionnaire: dictionnaire["resistance_elementaire"]=="True"
        }

    multiple = {
            "cible": False,
            "cible_multiple": False,
            "zone": False,
            "latence": False,
            "gain_xp": False,
            "cout_pm": False,
            "duree": False,
            "pv": False,
            "portee": False,
            "resistance_elementaire": False,
            "element": False,
            "taux_pv": False
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

    def make(self, niveau: int) -> mdl.Magie:
        """Crée une magie à partir de l'instance."""
        class GenerateurMagieProtection(mdl.Magie):
            """Un "générateur", c'est-à-dire une classe qui génère des instances de Magie."""
            nom = self.nom
            cible = self.cible
            cible_multiple = self.cible_multiple
            zone = self.zone
            latence = self.latence
            gain_xp = self.gain_xp
            cout_pm = self.cout_pm
            duree = self.duree
            pv = self.pv
            portee = self.portee
            resistance_elementaire = self.resistance_elementaire
            element = self.element
            taux_pv = self.taux_pv

            def genere(self, skill: mdl.Actif, agissant: mdl.Agissant, niveau: int) -> mdl.ActionMagieAutoProtection:
                protection = mdl.magies_protection[(self.cible, self.cible_multiple, self.zone, self.resistance_elementaire)]
                if issubclass(protection, mdl.ActionMagieProtectionZoneElement):
                    return protection(skill, self, agissant, self.gain_xp[niveau], self.cout_pm[niveau], self.duree[niveau], self.duree[niveau], self.pv[niveau], self.element, self.taux_pv[niveau], self.portee[niveau])
                elif issubclass(protection, mdl.ActionMagieAutoProtectionElement):
                    return protection(skill, self, agissant, self.gain_xp[niveau], self.cout_pm[niveau], self.duree[niveau], self.duree[niveau], self.pv[niveau], self.element, self.taux_pv[niveau])
                elif issubclass(protection, mdl.ActionMagieProtectionZone):
                    return protection(skill, self, agissant, self.gain_xp[niveau], self.cout_pm[niveau], self.duree[niveau], self.duree[niveau], self.pv[niveau], self.portee[niveau])
                else:
                    return protection(skill, self, agissant, self.gain_xp[niveau], self.cout_pm[niveau], self.duree[niveau], self.duree[niveau], self.pv[niveau])
        return GenerateurMagieProtection()
