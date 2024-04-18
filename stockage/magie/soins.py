"""
Fichier contenant la classe de stockage des magies de soin et assimilées.
"""

from __future__ import annotations
from json import loads as parse

import modele as mdl

from .magie import MagieNivele

class MagieSoinNivelee(MagieNivele):
    """Une magie de soin."""

    champs = {
            "cible": bool,
            "cible_multiple": bool,
            "zone": bool,
            "latence": float,
            "gain_xp": float,
            "cout_pm": float,
            "gain_pv": float,
            "portee": float
        }

    niveles = {
            "latence": True,
            "gain_xp": True,
            "cout_pm": True,
            "gain_pv": True,
            "portee": True
        }

    acceptors = {
            "latence": lambda latence: float(latence) >= 0,
            "gain_xp": lambda gain_xp: float(gain_xp) >= 0,
            "cout_pm": lambda cout_pm: float(cout_pm) >= 0,
            "gain_pv": lambda gain_pv: float(gain_pv) >= 0,
            "portee": lambda portee: float(portee) >= 0,
        }

    avertissements = {
            "latence": "La latence doit être positive.",
            "gain_xp": "Le gain d'expérience doit être positif.",
            "cout_pm": "Le coût en points de mana doit être positif.",
            "gain_pv": "Le gain de points de vie doit être positif.",
            "portee": "La portée doit être positive.",
        }

    conditionnels = {
            "cible_multiple": lambda dictionnaire: dictionnaire["cible"]=="True",
            "zone": lambda dictionnaire: dictionnaire["cible"]=="False",
        }

    def __init__(self, nom: str, cible: bool, cible_multiple: bool, zone: bool, latence: list[float],
                 gain_xp: list[float], cout_pm: list[float], gain_pv: list[float], portee: list[float]):
        MagieNivele.__init__(self, nom)
        self.latence = latence
        self.gain_xp = gain_xp
        self.cible = cible
        self.cible_multiple = cible_multiple
        self.zone = zone
        self.cout_pm = cout_pm
        self.gain_pv = gain_pv
        self.portee = portee

    def check(self) -> bool:
        return (all(latence >= 0 for latence in self.latence) and
                all(gain >= 0 for gain in self.gain_xp) and
                all(cout_pm >= 0 for cout_pm in self.cout_pm) and
                all(gain_pv >= 0 for gain_pv in self.gain_pv) and
                all(portee >= 0 for portee in self.portee))

    def stringify(self) -> str:
        return f"""{{
    "type": "magie_soin",
    "nivele": true,
    "nom": "{self.nom}",
    "cible": {self.cible},
    "cible_multiple": {self.cible_multiple},
    "zone": {self.zone},
    "latence": {self.latence},
    "gain_xp": {self.gain_xp},
    "cout_pm": {self.cout_pm},
    "gain_pv": {self.gain_pv},
    "portee": {self.portee}
}}"""
    
    @classmethod
    def parse(cls, json: str):
        """Parse un json en BouclierNivele."""
        dictionnaire = parse(json)
        return MagieSoinNivelee(dictionnaire["nom"], dictionnaire["cible"], dictionnaire["cible_multiple"], dictionnaire["zone"], dictionnaire["latence"], dictionnaire["gain_xp"], dictionnaire["cout_pm"], dictionnaire["gain_pv"], dictionnaire["portee"])

    def make(self, niveau: int):
        """Crée une magie à partir de l'instance."""
        classe = mdl.magies_soin[(self.cible, self.cible_multiple, self.zone)]
        class MagieSoinNiveau(classe, mdl.Nomme):
            """Une magie de soin."""
            gain_pv = self.gain_pv[niveau]
            latence = self.latence[niveau]
            gain_xp = self.gain_xp[niveau]
            cout = self.cout_pm[niveau]
            if self.zone:
                portee = self.portee
        MagieSoinNiveau.nom = self.nom
        MagieSoinNiveau.niveau = niveau
        return MagieSoinNiveau

class MagieResurectionNivele(MagieNivele):
    """Une magie de résurection."""

    champs = {
            "case": bool,
            "zone": bool,
            "latence": float,
            "gain_xp": float,
            "cout_pm": float,
            "gain_pv": float,
            "portee_limite": float,
            "portee": float
        }

    niveles = {
            "case": False,
            "zone": False,
            "latence": True,
            "gain_xp": True,
            "cout_pm": True,
            "gain_pv": True,
            "portee_limite": True,
            "portee": True
        }

    acceptors = {
            "case": lambda _: True,
            "zone": lambda _: True,
            "latence": lambda latence: float(latence) >= 0,
            "gain_xp": lambda gain_xp: float(gain_xp) >= 0,
            "cout_pm": lambda cout_pm: float(cout_pm) >= 0,
            "gain_pv": lambda gain_pv: float(gain_pv) >= 0,
            "portee_limite": lambda portee_limite: float(portee_limite) >= 0,
            "portee": lambda portee: float(portee) >= 0
        }

    avertissements = {
            "case": "Cet avertissement n'est pas censé apparaître.",
            "zone": "Cet avertissement n'est pas censé apparaître.",
            "latence": "La latence doit être positive.",
            "gain_xp": "Le gain d'expérience doit être positif.",
            "cout_pm": "Le coût en points de mana doit être positif.",
            "gain_pv": "Le gain de points de vie doit être positif.",
            "portee_limite": "La portée limite doit être positive.",
            "portee": "La portée doit être positive."
        }

    conditionnels = {
            "case": lambda dictionnaire: True,
            "zone": lambda dictionnaire: dictionnaire["case"]=="True",
            "latence": lambda dictionnaire: True,
            "gain_xp": lambda dictionnaire: True,
            "cout_pm": lambda dictionnaire: True,
            "portee_limite": lambda dictionnaire: dictionnaire["case"]=="True",
            "portee": lambda dictionnaire: dictionnaire["zone"]=="True"
        }

    multiple = {
            "case": False,
            "zone": False,
            "latence": False,
            "gain_xp": False,
            "cout_pm": False,
            "portee_limite": False,
            "portee": False
        }

    def __init__(self, nom: str, case: bool, zone: bool, latence: list[float],
                 gain_xp: list[float], cout_pm: list[float],
                 portee_limite: list[float], portee: list[float]):
        MagieNivele.__init__(self, nom)
        self.latence = latence
        self.gain_xp = gain_xp
        self.case = case
        self.zone = zone
        self.cout_pm = cout_pm
        self.portee_limite = portee_limite
        self.portee = portee

    def check(self) -> bool:
        return (all(latence >= 0 for latence in self.latence) and
                all(gain >= 0 for gain in self.gain_xp) and
                all(cout_pm >= 0 for cout_pm in self.cout_pm) and
                all(portee_limite >= 0 for portee_limite in self.portee_limite) and
                all(portee >= 0 for portee in self.portee))

    def stringify(self) -> str:
        return f"""{{
    "type": "magie_resurection",
    "nivele": true,
    "nom": "{self.nom}",
    "case": {self.case},
    "zone": {self.zone},
    "latence": {self.latence},
    "gain_xp": {self.gain_xp},
    "cout_pm": {self.cout_pm},
    "portee_limite": {self.portee_limite},
    "portee": {self.portee}
}}"""
    
    @classmethod
    def parse(cls, json: str):
        """Parse un json en BouclierNivele."""
        dictionnaire = parse(json)
        return MagieResurectionNivele(dictionnaire["nom"], dictionnaire["case"], dictionnaire["zone"], dictionnaire["latence"], dictionnaire["gain_xp"], dictionnaire["cout_pm"], dictionnaire["portee_limite"], dictionnaire["portee"])

    def make(self, niveau: int):
        """Crée une magie à partir de l'instance."""
        classe = mdl.magies_resurection[(self.case, self.zone)]
        class MagieResurectionNiveau(classe, mdl.Nomme):
            """Une magie de résurection."""
            latence = self.latence[niveau]
            gain_xp = self.gain_xp[niveau]
            cout = self.cout_pm[niveau]
            if self.case:
                portee_limite = self.portee_limite
            if self.zone:
                portee = self.portee
        MagieResurectionNiveau.nom = self.nom
        MagieResurectionNiveau.niveau = niveau
        return MagieResurectionNiveau

class MagieReanimationNivele(MagieNivele):
    """Une magie de réanimation."""

    champs = {
            "case": bool,
            "zone": bool,
            "latence": float,
            "gain_xp": float,
            "cout_pm": float,
            "taux_pv": float,
            "superiorite": float,
            "portee_limite": float,
            "portee": float
        }

    niveles = {
            "case": False,
            "zone": False,
            "latence": True,
            "gain_xp": True,
            "cout_pm": True,
            "taux_pv": True,
            "superiorite": True,
            "portee_limite": True,
            "portee": True
        }

    acceptors = {
            "case": lambda _: True,
            "zone": lambda _: True,
            "latence": lambda latence: float(latence) >= 0,
            "gain_xp": lambda gain_xp: float(gain_xp) >= 0,
            "cout_pm": lambda cout_pm: float(cout_pm) >= 0,
            "taux_pv": lambda taux_pv: 0 <= float(taux_pv) <= 1,
            "superiorite": lambda superiorite: float(superiorite) >= 0,
            "portee_limite": lambda portee_limite: float(portee_limite) >= 0,
            "portee": lambda portee: float(portee) >= 0
        }

    avertissements = {
            "case": "Cet avertissement n'est pas censé apparaître.",
            "zone": "Cet avertissement n'est pas censé apparaître.",
            "latence": "La latence doit être positive.",
            "gain_xp": "Le gain d'expérience doit être positif.",
            "cout_pm": "Le coût en points de mana doit être positif.",
            "taux_pv": "Le taux de points de vie doit être compris entre 0 et 1.",
            "superiorite": "La supériorité doit être positive.",
            "portee_limite": "La portée limite doit être positive.",
            "portee": "La portée doit être positive."
        }

    conditionnels = {
            "case": lambda dictionnaire: True,
            "zone": lambda dictionnaire: dictionnaire["case"]=="True",
            "latence": lambda dictionnaire: True,
            "gain_xp": lambda dictionnaire: True,
            "cout_pm": lambda dictionnaire: True,
            "taux_pv": lambda dictionnaire: True,
            "superiorite": lambda dictionnaire: True,
            "portee_limite": lambda dictionnaire: dictionnaire["case"]=="True",
            "portee": lambda dictionnaire: dictionnaire["zone"]=="True"
        }

    multiple = {
            "case": False,
            "zone": False,
            "latence": False,
            "gain_xp": False,
            "cout_pm": False,
            "taux_pv": False,
            "superiorite": False,
            "portee_limite": False,
            "portee": False
        }

    def __init__(self, nom: str, case: bool, zone: bool, latence: list[float],
                 gain_xp: list[float], cout_pm: list[float],
                 taux_pv: list[float], superiorite: list[float], portee_limite: list[float],
                 portee: list[float]):
        MagieNivele.__init__(self, nom)
        self.latence = latence
        self.gain_xp = gain_xp
        self.case = case
        self.zone = zone
        self.cout_pm = cout_pm
        self.taux_pv = taux_pv
        self.superiorite = superiorite
        self.portee_limite = portee_limite
        self.portee = portee

    def check(self) -> bool:
        return (all(latence >= 0 for latence in self.latence) and
                all(gain >= 0 for gain in self.gain_xp) and
                all(cout_pm >= 0 for cout_pm in self.cout_pm) and
                all(0 <= taux_pv <= 1 for taux_pv in self.taux_pv) and
                all(superiorite >= 0 for superiorite in self.superiorite) and
                all(portee_limite >= 0 for portee_limite in self.portee_limite) and
                all(portee >= 0 for portee in self.portee))

    def stringify(self) -> str:
        return f"""{{
    "type": "magie_reanimation",
    "nivele": true,
    "nom": "{self.nom}",
    "case": {self.case},
    "zone": {self.zone},
    "latence": {self.latence},
    "gain_xp": {self.gain_xp},
    "cout_pm": {self.cout_pm},
    "taux_pv": {self.taux_pv},
    "superiorite": {self.superiorite},
    "portee_limite": {self.portee_limite},
    "portee": {self.portee}
}}"""

    @classmethod
    def parse(cls, json: str):
        """Parse un json en BouclierNivele."""
        dictionnaire = parse(json)
        return MagieReanimationNivele(dictionnaire["nom"], dictionnaire["case"], dictionnaire["zone"], dictionnaire["latence"], dictionnaire["gain_xp"], dictionnaire["cout_pm"], dictionnaire["taux_pv"], dictionnaire["superiorite"], dictionnaire["portee_limite"], dictionnaire["portee"])

    def make(self, niveau: int):
        """Crée une magie à partir de l'instance."""
        classe = mdl.magies_reanimation[(self.case, self.zone)]
        class MagieReanimationNiveau(classe, mdl.Nomme):
            """Une magie de réanimation."""
            taux_pv = self.taux_pv[niveau]
            superiorite = self.superiorite[niveau]
            latence = self.latence[niveau]
            gain_xp = self.gain_xp[niveau]
            cout = self.cout_pm[niveau]
            if self.case:
                portee_limite = self.portee_limite
            if self.zone:
                portee = self.portee
        MagieReanimationNiveau.nom = self.nom
        MagieReanimationNiveau.niveau = niveau
        return MagieReanimationNiveau
