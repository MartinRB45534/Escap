"""
Fichier contenant la classe de stockage des magies diverses.
"""

from __future__ import annotations
from json import loads as parse

import modele as mdl

from .magie import MagieNivele

class MagieBlizzardNivelee(MagieNivele):
    """Classe de stockage des magies de blizzard."""

    champs = {
        "latence": float,
        "gain_xp": float,
        "cout_pm": float,
        "portee": float,
        "duree": float,
        "gain_latence": float
    }

    niveles = {
        "latence": True,
        "gain_xp": True,
        "cout_pm": True,
        "portee": True,
        "duree": True,
        "gain_latence": True
    }

    acceptors = {
        "latence": lambda latence: float(latence) >= 0,
        "gain_xp": lambda gain_xp: float(gain_xp) >= 0,
        "cout_pm": lambda cout_pm: float(cout_pm) >= 0,
        "portee": lambda portee: float(portee) >= 0,
        "duree": lambda duree: float(duree) >= 0,
        "gain_latence": lambda gain_latence: float(gain_latence) >= 0
    }

    avertissements = {
        "latence": "La latence doit être positive.",
        "gain_xp": "Le gain d'expérience doit être positif.",
        "cout_pm": "Le coût en points de mana doit être positif.",
        "portee": "La portée doit être positive.",
        "duree": "La durée doit être positive.",
        "gain_latence": "Le gain de latence doit être positif."
    }

    conditionnels = {
        "latence": lambda dictionnaire: True,
        "gain_xp": lambda dictionnaire: True,
        "cout_pm": lambda dictionnaire: True,
        "portee": lambda dictionnaire: True,
        "duree": lambda dictionnaire: True,
        "gain_latence": lambda dictionnaire: True
    }

    multiple = {
        "latence": False,
        "gain_xp": False,
        "cout_pm": False,
        "portee": False,
        "duree": False,
        "gain_latence": False
    }

    def __init__(self, nom: str, latence: list[float], gain_xp: list[float],
                 cout_pm: list[float], portee: list[float], duree: list[float],
                 gain_latence: list[float]):
        MagieNivele.__init__(self, nom)
        self.latence = latence
        self.gain_xp = gain_xp
        self.cout_pm = cout_pm
        self.portee = portee
        self.duree = duree
        self.gain_latence = gain_latence

    def check(self) -> bool:
        return (all(latence >= 0 for latence in self.latence) and
                all(gain >= 0 for gain in self.gain_xp) and
                all(cout >= 0 for cout in self.cout_pm) and
                all(portee >= 0 for portee in self.portee) and
                all(duree >= 0 for duree in self.duree) and
                all(gain >= 0 for gain in self.gain_latence))

    def stringify(self) -> str:
        return f"""{{
    "nom": "{self.nom}",
    "nivele": true,
    "latence": {self.latence},
    "gain_xp": {self.gain_xp},
    "cout_pm": {self.cout_pm},
    "portee": {self.portee},
    "duree": {self.duree},
    "gain_latence": {self.gain_latence}
}}"""

    @classmethod
    def parse(cls, json: str):
        dictionnaire = parse(json)
        return MagieBlizzardNivelee(dictionnaire["nom"], dictionnaire["latence"], dictionnaire["gain_xp"], dictionnaire["cout_pm"], dictionnaire["portee"], dictionnaire["duree"], dictionnaire["gain_latence"])

    def make(self, niveau: int) -> mdl.Magie:
        """Crée une magie à partir de l'instance."""
        class GenerateurMagieBlizzard(mdl.Magie):
            """Générateur de magie de blizzard."""
            nom = self.nom
            latence = self.latence
            gain_xp = self.gain_xp
            cout_pm = self.cout_pm
            portee = self.portee
            duree = self.duree
            gain_latence = self.gain_latence

            def genere(self, skill: mdl.Actif, agissant: mdl.Agissant, niveau:int) -> mdl.ActionMagieBlizzard:
                """Génère une action de magie de blizzard."""
                return mdl.ActionMagieBlizzard(skill, self, agissant, self.gain_xp[niveau], self.cout_pm[niveau], self.latence[niveau], self.portee[niveau], self.duree[niveau], self.gain_latence[niveau])
        return GenerateurMagieBlizzard()

class MagieObscuriteNivelee(MagieNivele):
    """Classe de stockage des magies d'obscurité."""

    champs = {
        "latence": float,
        "gain_xp": float,
        "cout_pm": float,
        "portee": float,
        "duree": float,
        "gain_opacite": float
    }

    niveles = {
        "latence": True,
        "gain_xp": True,
        "cout_pm": True,
        "portee": True,
        "duree": True,
        "gain_opacite": True
    }

    acceptors = {
        "latence": lambda latence: float(latence) >= 0,
        "gain_xp": lambda gain_xp: float(gain_xp) >= 0,
        "cout_pm": lambda cout_pm: float(cout_pm) >= 0,
        "portee": lambda portee: float(portee) >= 0,
        "duree": lambda duree: float(duree) >= 0,
        "gain_opacite": lambda gain_opacite: float(gain_opacite) >= 0
    }

    avertissements = {
        "latence": "La latence doit être positive.",
        "gain_xp": "Le gain d'expérience doit être positif.",
        "cout_pm": "Le coût en points de mana doit être positif.",
        "portee": "La portée doit être positive.",
        "duree": "La durée doit être positive.",
        "gain_opacite": "Le gain d'opacité doit être positif."
    }

    conditionnels = {
        "latence": lambda dictionnaire: True,
        "gain_xp": lambda dictionnaire: True,
        "cout_pm": lambda dictionnaire: True,
        "portee": lambda dictionnaire: True,
        "duree": lambda dictionnaire: True,
        "gain_opacite": lambda dictionnaire: True
    }

    multiple = {
        "latence": False,
        "gain_xp": False,
        "cout_pm": False,
        "portee": False,
        "duree": False,
        "gain_opacite": False
    }

    def __init__(self, nom: str, latence: list[float], gain_xp: list[float],
                 cout_pm: list[float], portee: list[float], duree: list[float],
                 gain_opacite: list[float]):
        MagieNivele.__init__(self, nom)
        self.latence = latence
        self.gain_xp = gain_xp
        self.cout_pm = cout_pm
        self.portee = portee
        self.duree = duree
        self.gain_opacite = gain_opacite

    def check(self) -> bool:
        return (all(latence >= 0 for latence in self.latence) and
                all(gain >= 0 for gain in self.gain_xp) and
                all(cout >= 0 for cout in self.cout_pm) and
                all(portee >= 0 for portee in self.portee) and
                all(duree >= 0 for duree in self.duree) and
                all(gain >= 0 for gain in self.gain_opacite))

    def stringify(self) -> str:
        return f"""{{
    "nom": "{self.nom}",
    "nivele": true,
    "latence": {self.latence},
    "gain_xp": {self.gain_xp},
    "cout_pm": {self.cout_pm},
    "portee": {self.portee},
    "duree": {self.duree},
    "gain_opacite": {self.gain_opacite}
}}"""

    @classmethod
    def parse(cls, json: str):
        dictionnaire = parse(json)
        return MagieObscuriteNivelee(dictionnaire["nom"], dictionnaire["latence"], dictionnaire["gain_xp"], dictionnaire["cout_pm"], dictionnaire["portee"], dictionnaire["duree"], dictionnaire["gain_opacite"])

    def make(self, niveau: int) -> mdl.Magie:
        """Crée une magie à partir de l'instance."""
        class GenerateurMagieObscurite(mdl.Magie):
            """Générateur de magie d'obscurité."""
            nom = self.nom
            latence = self.latence
            gain_xp = self.gain_xp
            cout_pm = self.cout_pm
            portee = self.portee
            duree = self.duree
            gain_opacite = self.gain_opacite

            def genere(self, skill: mdl.Actif, agissant: mdl.Agissant, niveau:int) -> mdl.ActionMagieObscurite:
                """Génère une action de magie d'obscurité."""
                return mdl.ActionMagieObscurite(skill, self, agissant, self.gain_xp[niveau], self.cout_pm[niveau], self.latence[niveau], self.portee[niveau], self.duree[niveau], self.gain_opacite[niveau])
        return GenerateurMagieObscurite()
    
class MagieInstakillNivelee(MagieNivele):
    """Classe de stockage des magies d'instakill."""

    champs = {
        "latence": float,
        "gain_xp": float,
        "cout_pm": float,
        "superiorite": float
    }

    niveles = {
        "latence": True,
        "gain_xp": True,
        "cout_pm": True,
        "superiorite": True
    }

    acceptors = {
        "latence": lambda latence: float(latence) >= 0,
        "gain_xp": lambda gain_xp: float(gain_xp) >= 0,
        "cout_pm": lambda cout_pm: float(cout_pm) >= 0,
        "superiorite": lambda superiorite: float(superiorite) >= 0
    }

    avertissements = {
        "latence": "La latence doit être positive.",
        "gain_xp": "Le gain d'expérience doit être positif.",
        "cout_pm": "Le coût en points de mana doit être positif.",
        "superiorite": "La supériorité doit être positive."
    }

    conditionnels = {
        "latence": lambda dictionnaire: True,
        "gain_xp": lambda dictionnaire: True,
        "cout_pm": lambda dictionnaire: True,
        "superiorite": lambda dictionnaire: True
    }

    multiple = {
        "latence": False,
        "gain_xp": False,
        "cout_pm": False,
        "superiorite": False
    }

    def __init__(self, nom: str, latence: list[float], gain_xp: list[float],
                 cout_pm: list[float], superiorite: list[float]):
        MagieNivele.__init__(self, nom)
        self.latence = latence
        self.gain_xp = gain_xp
        self.cout_pm = cout_pm
        self.superiorite = superiorite

    def check(self) -> bool:
        return (all(latence >= 0 for latence in self.latence) and
                all(gain >= 0 for gain in self.gain_xp) and
                all(cout >= 0 for cout in self.cout_pm) and
                all(superiorite >= 0 for superiorite in self.superiorite))

    def stringify(self) -> str:
        return f"""{{
    "nom": "{self.nom}",
    "nivele": true,
    "latence": {self.latence},
    "gain_xp": {self.gain_xp},
    "cout_pm": {self.cout_pm},
    "superiorite": {self.superiorite}
}}"""

    @classmethod
    def parse(cls, json: str):
        dictionnaire = parse(json)
        return MagieInstakillNivelee(dictionnaire["nom"], dictionnaire["latence"], dictionnaire["gain_xp"], dictionnaire["cout_pm"], dictionnaire["superiorite"])

    def make(self, niveau: int) -> mdl.Magie:
        """Crée une magie à partir de l'instance."""
        class GenerateurMagieInstakill(mdl.Magie):
            """Générateur de magie d'instakill."""
            nom = self.nom
            latence = self.latence
            gain_xp = self.gain_xp
            cout_pm = self.cout_pm
            superiorite = self.superiorite

            def genere(self, skill: mdl.Actif, agissant: mdl.Agissant, niveau:int) -> mdl.ActionMagieInstakill:
                """Génère une action de magie d'instakill."""
                return mdl.ActionMagieInstakill(skill, self, agissant, self.gain_xp[niveau], self.cout_pm[niveau], self.latence[niveau], self.superiorite[niveau])
        return GenerateurMagieInstakill()
    
class MagieTeleportationNivelee(MagieNivele):
    """Classe de stockage des magies de téléportation."""

    champs = {
        "latence": float,
        "gain_xp": float,
        "cout_pm": float
    }

    niveles = {
        "latence": True,
        "gain_xp": True,
        "cout_pm": True
    }

    acceptors = {
        "latence": lambda latence: float(latence) >= 0,
        "gain_xp": lambda gain_xp: float(gain_xp) >= 0,
        "cout_pm": lambda cout_pm: float(cout_pm) >= 0
    }

    avertissements = {
        "latence": "La latence doit être positive.",
        "gain_xp": "Le gain d'expérience doit être positif.",
        "cout_pm": "Le coût en points de mana doit être positif."
    }

    conditionnels = {
        "latence": lambda dictionnaire: True,
        "gain_xp": lambda dictionnaire: True,
        "cout_pm": lambda dictionnaire: True
    }

    multiple = {
        "latence": False,
        "gain_xp": False,
        "cout_pm": False
    }

    def __init__(self, nom: str, latence: list[float], gain_xp: list[float],
                 cout_pm: list[float]):
        MagieNivele.__init__(self, nom)
        self.latence = latence
        self.gain_xp = gain_xp
        self.cout_pm = cout_pm

    def check(self) -> bool:
        return (all(latence >= 0 for latence in self.latence) and
                all(gain >= 0 for gain in self.gain_xp) and
                all(cout >= 0 for cout in self.cout_pm))

    def stringify(self) -> str:
        return f"""{{
    "nom": "{self.nom}",
    "nivele": true,
    "latence": {self.latence},
    "gain_xp": {self.gain_xp},
    "cout_pm": {self.cout_pm}
}}"""

    @classmethod
    def parse(cls, json: str):
        dictionnaire = parse(json)
        return MagieTeleportationNivelee(dictionnaire["nom"], dictionnaire["latence"], dictionnaire["gain_xp"], dictionnaire["cout_pm"])

    def make(self, niveau: int) -> mdl.Magie:
        """Crée une magie à partir de l'instance."""
        class GenerateurMagieTeleportation(mdl.Magie):
            """Générateur de magie de téléportation."""
            nom = self.nom
            latence = self.latence
            gain_xp = self.gain_xp
            cout_pm = self.cout_pm

            def genere(self, skill: mdl.Actif, agissant: mdl.Agissant, niveau:int) -> mdl.ActionMagieTeleportation:
                """Génère une action de magie de téléportation."""
                return mdl.ActionMagieTeleportation(skill, self, agissant, self.gain_xp[niveau], self.cout_pm[niveau], self.latence[niveau])
        return GenerateurMagieTeleportation()
