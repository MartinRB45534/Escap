"""
Fichier contenant la classe de stockage des projectiles.
"""

from __future__ import annotations
from json import loads as parse

import modele as mdl

from .magie import MagieNivele

class MagieProjectileNivelee(MagieNivele):
    """Une magie de projectile nivele."""

    champs = {
        "latence": float,
        "gain_xp": float,
        "cout_pm": float,
        "fantome": bool,
        "percant": bool,
        "fleche": bool,
        "explosif": bool,
        "element": mdl.Element,
        "poids": float,
        "frottements": float,
        "portee": float,
        "degats": float,
        "decentree": bool,
        "portee_limite": float
    }

    niveles = {
        "latence": True,
        "gain_xp": True,
        "cout_pm": True,
        "fantome": False,
        "percant": False,
        "fleche": False,
        "explosif": False,
        "element": False,
        "poids": True,
        "frottements": True,
        "portee": True,
        "degats": True,
        "decentree": False,
        "portee_limite": True
    }

    acceptors = {
        "latence": lambda latence: float(latence) >= 0,
        "gain_xp": lambda gain_xp: float(gain_xp) >= 0,
        "cout_pm": lambda cout_pm: float(cout_pm) >= 0,
        "fantome": lambda _: True,
        "percant": lambda _: True,
        "fleche": lambda _: True,
        "explosif": lambda _: True,
        "element": lambda element: element in mdl.Element,
        "poids": lambda poids: float(poids) >= 0,
        "frottements": lambda frottements: float(frottements) >= 0,
        "portee": lambda portee: float(portee) >= 0,
        "degats": lambda degats: float(degats) >= 0,
        "decentree": lambda _: True,
        "portee_limite": lambda portee_limite: float(portee_limite) >= 0
    }

    avertissements = {
        "latence": "La latence doit être positive.",
        "gain_xp": "Le gain d'expérience doit être positif.",
        "cout_pm": "Le coût en points de mana doit être positif.",
        "fantome": "Cet avertissement n'est pas censé apparaître.",
        "percant": "Cet avertissement n'est pas censé apparaître.",
        "fleche": "Cet avertissement n'est pas censé apparaître.",
        "explosif": "Cet avertissement n'est pas censé apparaître.",
        "element": "Choisissez un élément.",
        "poids": "Le poids doit être positif.",
        "frottements": "Le frottement doit être positif.",
        "portee": "La portée doit être positive.",
        "degats": "Les dégats doivent être positifs.",
        "decentree": "Cet avertissement n'est pas censé apparaître.",
        "portee_limite": "La portée doit être positive."
    }

    conditionnels = {
        "latence": lambda dictionnaire: True,
        "gain_xp": lambda dictionnaire: True,
        "cout_pm": lambda dictionnaire: True,
        "fantome": lambda dictionnaire: True,
        "percant": lambda dictionnaire: True,
        "fleche": lambda dictionnaire: True,
        "explosif": lambda dictionnaire: True,
        "element": lambda dictionnaire: True,
        "poids": lambda dictionnaire: True,
        "frottements": lambda dictionnaire: True,
        "portee": lambda dictionnaire: True,
        "degats": lambda dictionnaire: True,
        "decentree": lambda dictionnaire: True,
        "portee_limite": lambda dictionnaire: True
    }

    multiple = {
        "latence": False,
        "gain_xp": False,
        "cout_pm": False,
        "fantome": False,
        "percant": False,
        "fleche": False,
        "explosif": False,
        "element": False,
        "poids": False,
        "frottements": False,
        "portee": False,
        "degats": False,
        "decentree": False,
        "portee_limite": False
    }

    def __init__(self, nom: str, latence: list[float], gain_xp: list[float], cout_pm: list[float],
                 fantome: bool, percant: bool, fleche: bool, explosif: bool, element:mdl.Element,
                 poids:list[float], frottements:list[float], portee:list[float], degats:list[float],
                 decentree: bool, portee_limite: list[float]):
        MagieNivele.__init__(self, nom)
        self.latence = latence
        self.gain_xp = gain_xp
        self.cout_pm = cout_pm
        self.fantome = fantome
        self.percant = percant
        self.fleche = fleche
        self.explosif = explosif
        self.element = element
        self.poids = poids
        self.frottements = frottements
        self.portee = portee
        self.degats = degats
        self.decentree = decentree
        self.portee_limite = portee_limite

    def check(self) -> bool:
        return (all(latence >= 0 for latence in self.latence) and
                all(gain >= 0 for gain in self.gain_xp) and
                all(cout_pm >= 0 for cout_pm in self.cout_pm) and
                all([poids >= 0 for poids in self.poids]) and
                all([frottements >= 0 for frottements in self.frottements]) and
                all([portee >= 0 for portee in self.portee]) and
                all([degats >= 0 for degats in self.degats]) and
                all([portee >= 0 for portee in self.portee_limite]))

    def stringify(self) -> str:
        return f"""{{
    "type": "magie_projectile",
    "nivele": true,
    "nom": "{self.nom}",
    "latence": {self.latence},
    "gain_xp": {self.gain_xp},
    "cout_pm": {self.cout_pm},
    "fantome": {self.fantome},
    "percant": {self.percant},
    "fleche": {self.fleche},
    "explosif": {self.explosif},
    "element": "{self.element},
    "poids": {self.poids},
    "frottements": {self.frottements},
    "portee": {self.portee},
    "degats": {self.degats},
    "decentree": {self.decentree},
    "portee_limite": {self.portee_limite}
}}"""

    @classmethod
    def parse(cls, json: str):
        """Parse un json en ProjectileSimpleNivele."""
        dictionnaire = parse(json)
        return MagieProjectileNivelee(dictionnaire["nom"], dictionnaire["latence"], dictionnaire["gain_xp"], dictionnaire["cout_pm"], dictionnaire["fantome"], dictionnaire["percant"], dictionnaire["fleche"], dictionnaire["explosif"], mdl.Element(dictionnaire["element"]), dictionnaire["poids"], dictionnaire["frottements"], dictionnaire["portee"], dictionnaire["degats"], dictionnaire["decentree"], dictionnaire["portee_limite"])

    def make(self, niveau: int) -> mdl.Magie:
        """Crée une magie à partir de l'instance."""
        class GenerateurMagieEnchantement(mdl.Magie):
            """Un "générateur", c'est-à-dire une classe qui génère des instances de Magie."""
            nom = self.nom
            latence = self.latence
            gain_xp = self.gain_xp
            cout_pm = self.cout_pm
            fantome = self.fantome
            percant = self.percant
            fleche = self.fleche
            explosif = self.explosif
            element = self.element
            poids = self.poids
            frottements = self.frottements
            portee = self.portee
            degats = self.degats
            decentree = self.decentree
            portee_limite = self.portee_limite

            def genere(self, skill: mdl.Actif, agissant: mdl.Agissant, niveau: int) -> mdl.InvocationProjectile:
                projectile = mdl.projectiles[(self.percant, self.fleche, self.explosif, False, True)](mdl.NOWHERE, self.poids[niveau], self.frottements[niveau], self.portee[niveau], self.degats[niveau], self.element)
                projectile.nom = self.nom
                projectile.fantome = self.fantome
                if self.decentree:
                    return mdl.ActionMagieProjectileDecentre(skill, self, agissant, self.gain_xp[niveau], self.cout_pm[niveau], self.latence[niveau], projectile, self.portee_limite[niveau])
                else:
                    return mdl.InvocationProjectile(skill, self, agissant, self.gain_xp[niveau], self.cout_pm[niveau], self.latence[niveau], projectile)
        return GenerateurMagieEnchantement()
