"""
Fichier contenant la classe de stockage des projectiles.
"""

from __future__ import annotations
from json import loads as parse

import modele as mdl

from ...stockage import StockageCategorieNivelee
from ..entitee import EntiteeNivele

class ProjectileSimpleNivele(EntiteeNivele):
    """Un projectile nivele."""

    champs = {
        "fantome": bool,
        "percant": bool,
        "fleche": bool,
        "explosif": bool,
        "element": mdl.Element,
        "poids": float,
        "frottements": float,
        "portee": float,
        "degats": float
    }

    niveles = {
        "fantome": False,
        "percant": False,
        "fleche": False,
        "explosif": False,
        "element": False,
        "poids": True,
        "frottements": True,
        "portee": True,
        "degats": True
    }

    acceptors = {
        "fantome": lambda _: True,
        "percant": lambda _: True,
        "fleche": lambda _: True,
        "explosif": lambda _: True,
        "element": lambda element: element in mdl.Element,
        "poids": lambda poids: float(poids) >= 0,
        "frottements": lambda frottements: float(frottements) >= 0,
        "portee": lambda portee: float(portee) >= 0,
        "degats": lambda degats: float(degats) >= 0
    }

    avertissements = {
        "fantome": "Cet avertissement n'est pas censé apparaître.",
        "percant": "Cet avertissement n'est pas censé apparaître.",
        "fleche": "Cet avertissement n'est pas censé apparaître.",
        "explosif": "Cet avertissement n'est pas censé apparaître.",
        "element": "Choisissez un élément.",
        "poids": "Le poids doit être positif.",
        "frottements": "Le frottement doit être positif.",
        "portee": "La portée doit être positive.",
        "degats": "Les dégats doivent être positifs."
    }

    conditionnels = {
        "fantome": lambda dictionnaire: True,
        "percant": lambda dictionnaire: True,
        "fleche": lambda dictionnaire: True,
        "explosif": lambda dictionnaire: True,
        "element": lambda dictionnaire: True,
        "poids": lambda dictionnaire: True,
        "frottements": lambda dictionnaire: True,
        "portee": lambda dictionnaire: True,
        "degats": lambda dictionnaire: True
    }

    multiple = {
        "fantome": False,
        "percant": False,
        "fleche": False,
        "explosif": False,
        "element": False,
        "poids": False,
        "frottements": False,
        "portee": False,
        "degats": False
    }

    def __init__(self, nom: str, fantome: bool,
                 percant: bool, fleche: bool, explosif: bool,
                 element:mdl.Element, poids:list[float], frottements:list[float], portee:list[float], degats:list[float]):
        EntiteeNivele.__init__(self, nom)
        self.fantome = fantome
        self.percant = percant
        self.fleche = fleche
        self.explosif = explosif
        self.element = element
        self.poids = poids
        self.frottements = frottements
        self.portee = portee
        self.degats = degats

    def check(self) -> bool:
        return (all([poids >= 0 for poids in self.poids]) and
                all([frottements >= 0 for frottements in self.frottements]) and
                all([portee >= 0 for portee in self.portee]) and
                all([degats >= 0 for degats in self.degats]))

    def stringify(self) -> str:
        return f"""{{
    "type": "projectile",
    "nivele": true,
    "nom": "{self.nom}",
    "fantome": {self.fantome},
    "percant": {self.percant},
    "fleche": {self.fleche},
    "explosif": {self.explosif},
    "element": "{self.element},
    "poids": {self.poids},
    "frottements": {self.frottements},
    "portee": {self.portee},
    "degats": {self.degats}"
}}"""

    @classmethod
    def parse(cls, json: str):
        """Parse un json en ProjectileSimpleNivele."""
        dictionnaire = parse(json)
        return ProjectileSimpleNivele(dictionnaire["nom"], dictionnaire["fantome"], dictionnaire["percant"], dictionnaire["fleche"], dictionnaire["explosif"], mdl.Element(dictionnaire["element"]), dictionnaire["poids"], dictionnaire["frottements"], dictionnaire["portee"], dictionnaire["degats"])

    def make(self, niveau: int):
        """Crée un ProjectileSimple à partir de l'instance."""
        classe = mdl.projectiles[(self.percant, self.fleche, self.explosif, False, False)]
        class ProjectileSimpleNiveau(classe, mdl.Nomme):
            """Un projectile."""
            poids = self.poids[niveau]
            frottements = self.frottements[niveau]
            portee = self.portee[niveau]
            degats = self.degats[niveau]
            element = self.element
            fantome = self.fantome
        ProjectileSimpleNiveau.nom = self.nom
        ProjectileSimpleNiveau.niveau = niveau
        return ProjectileSimpleNiveau

class Projectiles(StockageCategorieNivelee):
    """Les informations des projectiles."""
    nom = "Projectiles"
    titre_nouveau = "Nouveau projectile"
    description = "Les projectiles sont destinés à être lancés. Un projectile percant peut traverser un agissant s'il le tue, un projectile fragile se brise à l'impact. Les fleches sont affectées différemment par certains skills et sont toujours percantes. Les explosifs sont affectés différemment par certains skills et devraient théoriquement être fragiles. Les projectiles magiques serviront pour les sorts de création de projectiles et sont toujours evanescent (disparaissent à l'impact ou à l'arrêt), donc fragiles."
    avertissement = "Il existe déjà un projectile avec ce nom !"
    elements = {
        "ProjectileSimple": ProjectileSimpleNivele
    }
