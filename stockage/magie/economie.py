"""
Fichier contenant la classe de stockage des magies d'attaques.
"""

from __future__ import annotations
from json import loads as parse

import modele as mdl

from .magie import MagieNivele

class MagieReserveNivelee(MagieNivele):
    """Une magie de réserve."""

    champs = {
            "latence": float,
            "gain_xp": float,
            "taux_pm": float
        }

    niveles = {
            "latence": True,
            "gain_xp": True,
            "taux_pm": True
        }

    acceptors = {
            "latence": lambda latence: float(latence) >= 0,
            "gain_xp": lambda gain_xp: float(gain_xp) >= 0,
            "taux_pm": lambda taux_pm: 0 <= float(taux_pm) <= 1
        }

    avertissements = {
            "latence": "La latence doit être positive.",
            "gain_xp": "Le gain d'expérience doit être positif.",
            "taux_pm": "Le taux de points de mana doit être compris entre 0 et 1."
        }

    conditionnels = {
            "latence": lambda dictionnaire: True,
            "gain_xp": lambda dictionnaire: True,
            "taux_pm": lambda dictionnaire: True
        }

    multiple = {
            "latence": False,
            "gain_xp": False,
            "taux_pm": False
        }

    def __init__(self, nom: str, latence: list[float], gain_xp: list[float],
                 taux_pm: list[float]):
        MagieNivele.__init__(self, nom)
        self.latence = latence
        self.gain_xp = gain_xp
        self.taux_pm = taux_pm

    def check(self) -> bool:
        return (all(latence >= 0 for latence in self.latence) and
                all(gain >= 0 for gain in self.gain_xp) and
                all(0 <= taux_pm <= 1 for taux_pm in self.taux_pm))

    def stringify(self) -> str:
        return f"""{{
    "type": "magie_reserve",
    "nivele": true,
    "nom": "{self.nom}",
    "latence": {self.latence},
    "gain_xp": {self.gain_xp},
    "taux_pm": {self.taux_pm}
}}"""

    @classmethod
    def parse(cls, json: str):
        """Parse un json en BouclierNivele."""
        dictionnaire = parse(json)
        return MagieReserveNivelee(dictionnaire["nom"], dictionnaire["latence"], dictionnaire["gain_xp"], dictionnaire["taux_pm"])

    def make(self, niveau: int):
        """Crée une magie à partir de l'instance."""
        class MagieReserveNiveau(mdl.MagieReserve, mdl.Nomme):
            """Une magie de réserve."""
            taux = self.taux_pm[niveau]
            latence_max = self.latence[niveau]
            gain_xp = self.gain_xp[niveau]
        MagieReserveNiveau.nom = self.nom
        MagieReserveNiveau.niveau = niveau
        return MagieReserveNiveau

class MagieInvestissementNivelee(MagieNivele):
    """Une magie d'investissement."""

    champs = {
            "latence": float,
            "gain_xp": float,
            "taux_pm": float,
            "duree": float
        }
    
    niveles = {
            "latence": True,
            "gain_xp": True,
            "taux_pm": True,
            "duree": True
        }

    acceptors = {
            "latence": lambda latence: float(latence) >= 0,
            "gain_xp": lambda gain_xp: float(gain_xp) >= 0,
            "taux_pm": lambda taux_pm: float(taux_pm) >= 1,
            "duree": lambda duree: float(duree) >= 0
        }

    avertissements = {
            "latence": "La latence doit être positive.",
            "gain_xp": "Le gain d'expérience doit être positif.",
            "taux_pm": "Le taux d'invesstissement doit être supérieur ou égal à 1.",
            "duree": "La durée doit être positive."
        }

    conditionnels = {
            "latence": lambda dictionnaire: True,
            "gain_xp": lambda dictionnaire: True,
            "taux_pm": lambda dictionnaire: True,
            "duree": lambda dictionnaire: True
        }

    multiple = {
            "latence": False,
            "gain_xp": False,
            "taux_pm": False,
            "duree": False
        }

    def __init__(self, nom: str, latence: list[float], gain_xp: list[float],
                 taux_pm: list[float], duree: list[float]):
        MagieNivele.__init__(self, nom)
        self.latence = latence
        self.gain_xp = gain_xp
        self.taux_pm = taux_pm
        self.duree = duree

    def check(self) -> bool:
        return (all(latence >= 0 for latence in self.latence) and
                all(gain >= 0 for gain in self.gain_xp) and
                all(taux_pm >= 1 for taux_pm in self.taux_pm) and
                all(duree >= 0 for duree in self.duree))

    def stringify(self) -> str:
        return f"""{{
    "type": "magie_investissement",
    "nivele": true,
    "nom": "{self.nom}",
    "latence": {self.latence},
    "gain_xp": {self.gain_xp},
    "taux_pm": {self.taux_pm},
    "duree": {self.duree}
}}"""

    @classmethod
    def parse(cls, json: str):
        """Parse un json en BouclierNivele."""
        dictionnaire = parse(json)
        return MagieInvestissementNivelee(dictionnaire["nom"], dictionnaire["latence"], dictionnaire["gain_xp"], dictionnaire["taux_pm"], dictionnaire["duree"])
    
    def make(self, niveau: int):
        """Crée une magie à partir de l'instance."""
        class MagieInvestissementNiveau(mdl.MagieInvestissement, mdl.Nomme):
            """Une magie d'investissement."""
            taux = self.taux_pm[niveau]
            latence_max = self.latence[niveau]
            gain_xp = self.gain_xp[niveau]
            duree = self.duree[niveau]
        MagieInvestissementNiveau.nom = self.nom
        MagieInvestissementNiveau.niveau = niveau
        return MagieInvestissementNiveau
