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
        "portee_limite": float,
    }

    niveles = {
        "latence": True,
        "gain_xp": True,
        "cout_pm": True,
        "poids": True,
        "frottements": True,
        "portee": True,
        "degats": True,
        "portee_limite": True,
    }

    acceptors = {
        "latence": lambda latence: float(latence) >= 0,
        "gain_xp": lambda gain_xp: float(gain_xp) >= 0,
        "cout_pm": lambda cout_pm: float(cout_pm) >= 0,
        "element": lambda element: element in mdl.Element,
        "poids": lambda poids: float(poids) >= 0,
        "frottements": lambda frottements: float(frottements) >= 0,
        "portee": lambda portee: float(portee) >= 0,
        "degats": lambda degats: float(degats) >= 0,
        "decentree": lambda _: True,
        "portee_limite": lambda portee_limite: float(portee_limite) >= 0,
    }

    avertissements = {
        "latence": "La latence doit être positive.",
        "gain_xp": "Le gain d'expérience doit être positif.",
        "cout_pm": "Le coût en points de mana doit être positif.",
        "element": "Choisissez un élément.",
        "poids": "Le poids doit être positif.",
        "frottements": "Le frottement doit être positif.",
        "portee": "La portée doit être positive.",
        "degats": "Les dégats doivent être positifs.",
        "portee_limite": "La portée doit être positive.",
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

    def make(self, niveau: int):
        """Crée une magie à partir de l'instance."""
        classe: type[mdl.InvocationProjectile] = mdl.magies_projectiles[self.decentree]
        classe_projectile = mdl.projectiles_magiques[(self.percant, self.fleche, self.explosif)]
        class ProjectileMagique(classe_projectile):
            """Un projectile magique."""
            fantome = self.fantome
            element = self.element
            poids = self.poids[niveau]
            frottements = self.frottements[niveau]
            portee = self.portee[niveau]
            degats = self.degats[niveau]
        class MagieProjectileNiveau(classe, mdl.Nomme):
            """Une magie de projectile."""
            classe = ProjectileMagique
            latence = self.latence[niveau]
            gain_xp = self.gain_xp[niveau]
            cout = self.cout_pm[niveau]
            if self.decentree:
                portee_limite = self.portee_limite
        MagieProjectileNiveau.nom = self.nom
        MagieProjectileNiveau.niveau = niveau
        return MagieProjectileNiveau
