"""
Fichier contenant la classe de stockage des magies de boost.
"""

from __future__ import annotations
from json import loads as parse

import modele as mdl

from .magie import MagieNivele

class MagieBoostNivele(MagieNivele):
    """Une magie de boost (renforce la prochaine attaque)."""

    champs = {
            "cible": bool,
            "cible_multiple": bool,
            "latence": float,
            "gain_xp": float,
            "cout": float,
            "taux_degats": float,
            "duree": float
        }

    niveles = {
            "cible": False,
            "cible_multiple": False,
            "latence": True,
            "gain_xp": True,
            "cout": True,
            "taux_degats": True,
            "duree": True
        }

    acceptors = {
            "cible": lambda _: True,
            "cible_multiple": lambda _: True,
            "latence": lambda latence: float(latence) >= 0,
            "gain_xp": lambda gain_xp: float(gain_xp) >= 0,
            "cout": lambda cout: float(cout) >= 0,
            "taux_degats": lambda taux_degats: float(taux_degats) >= 0,
            "duree": lambda duree: float(duree) >= 0
        }

    avertissements = {
            "cible": "Cet avertissement n'est pas censé apparaître.",
            "cible_multiple": "Cet avertissement n'est pas censé apparaître.",
            "latence": "La latence doit être positive.",
            "gain_xp": "Le gain d'expérience doit être positif.",
            "cout": "Le coût doit être positif.",
            "taux_degats": "Le taux de dégâts doit être positif.",
            "duree": "La durée doit être positive."
        }

    conditionnels = {
            "cible": lambda dictionnaire: True,
            "cible_multiple": lambda dictionnaire: dictionnaire["cible"]=="True",
            "latence": lambda dictionnaire: True,
            "gain_xp": lambda dictionnaire: True,
            "cout": lambda dictionnaire: True,
            "taux_degats": lambda dictionnaire: True,
            "duree": lambda dictionnaire: True
        }

    multiple = {
            "cible": False,
            "cible_multiple": False,
            "latence": False,
            "gain_xp": False,
            "cout": False,
            "taux_degats": False,
            "duree": False
        }

    def __init__(self, nom: str, cible: bool, cible_multiple: bool, latence: list[float],
                 gain_xp: list[float], cout: list[float], taux_degats: list[float],
                 duree: list[float]):
        MagieNivele.__init__(self, nom)
        self.latence = latence
        self.gain_xp = gain_xp
        self.cible = cible
        self.cible_multiple = cible_multiple
        self.cout = cout
        self.taux_degats = taux_degats
        self.duree = duree

    def check(self) -> bool:
        return (all(latence >= 0 for latence in self.latence) and
                all(gain >= 0 for gain in self.gain_xp) and
                all(cout >= 0 for cout in self.cout) and
                all(taux_degats >= 0 for taux_degats in self.taux_degats) and
                all(duree >= 0 for duree in self.duree))

    def stringify(self) -> str:
        return f"""{{
    "type": "magie_attaque",
    "nivele": true,
    "nom": "{self.nom}",
    "cible": {self.cible},
    "cible_multiple": {self.cible_multiple},
    "latence": {self.latence},
    "gain_xp": {self.gain_xp},
    "cout": {self.cout},
    "taux_degats": {self.taux_degats},
    "duree": {self.duree}
}}"""

    @classmethod
    def parse(cls, json: str):
        """Parse un json en BouclierNivele."""
        dictionnaire = parse(json)
        return MagieBoostNivele(dictionnaire["nom"], dictionnaire["cible"], dictionnaire["cible_multiple"], dictionnaire["latence"], dictionnaire["gain_xp"], dictionnaire["cout"], dictionnaire["taux_degats"], dictionnaire["duree"])

    def make(self, niveau: int) -> mdl.Magie:
        """Crée une magie à partir de l'instance."""
        class GenerateurMagieBoost(mdl.Magie):
            """Un "générateur", c'est-à-dire une classe qui génère des instances de Magie."""
            nom = self.nom
            cible = self.cible
            cible_multiple = self.cible_multiple
            latence = self.latence
            gain_xp = self.gain_xp
            cout = self.cout
            taux_degats = self.taux_degats
            duree = self.duree

            def genere(self, skill: mdl.Actif, agissant: mdl.Agissant, niveau: int) -> mdl.ActionMagieDopage:
                return mdl.magies_boost[(self.cible, self.cible_multiple)](skill, self, agissant, self.gain_xp[niveau], self.cout[niveau], self.latence[niveau], self.taux_degats[niveau], self.duree[niveau])
        return GenerateurMagieBoost()
