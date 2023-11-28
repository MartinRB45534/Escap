"""
Fichier contenant la classe de stockage des projectiles.
"""

from __future__ import annotations
from typing import Callable
from json import loads as parse

import modele as mdl

from ...stockage import StockageCategorie, StockageNivele, StockageUnique, StockageGlobal
from ..entitee import Entitee, EntiteeNivele

class Projectiles(StockageCategorie):
    """Les informations des projectiles."""
    nom = "Projectiles"
    titre_nouveau = "Nouveau projectile"
    description = "Les projectiles sont des items consommables qui s'activent avec du mana. Les projectiles vierges n'ont pas encore d'effet placé, tandis que les projectiles préécrits ont besoin d'un effet à la création."
    avertissement = "Il existe déjà un item avec ce nom !"

    @property
    def all_noms(self) -> set[str]:
        return StockageGlobal.global_.items.all_noms()

    @classmethod
    @property
    def elements(cls) -> dict[str, type[StockageUnique]|tuple[type[StockageUnique], type[StockageNivele]]]:
        return {
            
        }

class Projectile(Entitee):
    """Un projectile."""
    def __init__(self, nom: str, fantome: bool,
                 percant: bool, fleche: bool, explosif: bool, fragile: bool, magique: bool,
                 element:mdl.Element, poids:float, frottements:float, portee:float, degats:float):
        Entitee.__init__(self, nom)
        self.fantome = fantome
        self.percant = percant
        self.fleche = fleche
        self.explosif = explosif
        self.fragile = fragile
        self.magique = magique
        self.element = element
        self.poids = poids
        self.frottements = frottements
        self.portee = portee
        self.degats = degats

    def check(self) -> bool:
        return (self.poids >= 0 and
                self.frottements >= 0 and
                self.portee >= 0 and
                self.degats >= 0)
    
    def stringify(self) -> str:
        return f"""{{
    "type": "projectile",
    "nivele": false,
    "nom": "{self.nom}",
    "fantome": {self.fantome},
    "percant": {self.percant},
    "fleche": {self.fleche},
    "explosif": {self.explosif},
    "fragile": {self.fragile},
    "magique": {self.magique},
    "element": "{self.element},
    "poids": {self.poids},
    "frottements": {self.frottements},
    "portee": {self.portee},
    "degats": {self.degats}"
}}"""
    
    @classmethod
    def parse(cls, json: str):
        """Parse un json en Projectile."""
        dictionnaire = parse(json)
        return Projectile(dictionnaire["nom"], dictionnaire["fantome"], dictionnaire["percant"], dictionnaire["fleche"], dictionnaire["explosif"], dictionnaire["fragile"], dictionnaire["magique"], dictionnaire["element"], dictionnaire["poids"], dictionnaire["frottements"], dictionnaire["portee"], dictionnaire["degats"])
    
    @classmethod
    @property
    def champs(cls) -> dict[str, type[int|str|float|bool|mdl.Element]]:
        return {
            "fantome": bool,
            "percant": bool,
            "fleche": bool,
            "explosif": bool,
            "fragile": bool,
            "magique": bool,
            "element": mdl.Element,
            "poids": float,
            "frottements": float,
            "portee": float,
            "degats": float
        }
    
    @classmethod
    @property
    def acceptors(cls) -> dict[str, Callable[[str], bool]]:
        return {
            "fantome": lambda _: True,
            "percant": lambda _: True,
            "fleche": lambda _: True,
            "explosif": lambda _: True,
            "fragile": lambda _: True,
            "magique": lambda _: True,
            "element": lambda element: element in mdl.Element,
            "poids": lambda poids: float(poids) >= 0,
            "frottements": lambda frottements: float(frottements) >= 0,
            "portee": lambda portee: float(portee) >= 0,
            "degats": lambda degats: float(degats) >= 0
        }
    
    @classmethod
    @property
    def avertissements(cls) -> dict[str, str]:
        return {
            "fantome": "Cet avertissement n'est pas censé apparaître.",
            "percant": "Cet avertissement n'est pas censé apparaître.",
            "fleche": "Cet avertissement n'est pas censé apparaître.",
            "explosif": "Cet avertissement n'est pas censé apparaître.",
            "fragile": "Cet avertissement n'est pas censé apparaître.",
            "magique": "Cet avertissement n'est pas censé apparaître.",
            "element": "Choisissez un élément.",
            "poids": "Le poids doit être positif.",
            "frottements": "Le frottement doit être positif.",
            "portee": "La portée doit être positive.",
            "degats": "Les dégats doivent être positifs."
        }

    def make(self) -> mdl.Projectile:
        """Crée un Projectile à partir de l'instance."""
        projectile = mdl.projectiles[(self.percant, self.fleche, self.explosif, self.fragile, self.magique)](mdl.NOWHERE, 0, self.poids, self.frottements, self.portee, self.degats, self.element)
        projectile.nom = self.nom
        projectile.fantome = self.fantome
        return projectile

class ProjectileNivele(EntiteeNivele):
    """Un projectile nivele."""
    def __init__(self, nom: str, fantome: bool,
                 percant: bool, fleche: bool, explosif: bool, fragile: bool, magique: bool,
                 element:mdl.Element, poids:float, frottements:float, portee:float, degats:float):
        EntiteeNivele.__init__(self, nom)
        self.fantome = fantome
        self.percant = percant
        self.fleche = fleche
        self.explosif = explosif
        self.fragile = fragile
        self.magique = magique
        self.element = element
        self.poids = poids
        self.frottements = frottements
        self.portee = portee
        self.degats = degats

    def check(self) -> bool:
        return (self.poids >= 0 and
                self.frottements >= 0 and
                self.portee >= 0 and
                self.degats >= 0)
    
    def stringify(self) -> str:
        return f"""{{
    "type": "projectile",
    "nivele": true,
    "nom": "{self.nom}",
    "fantome": {self.fantome},
    "percant": {self.percant},
    "fleche": {self.fleche},
    "explosif": {self.explosif},
    "fragile": {self.fragile},
    "magique": {self.magique},
    "element": "{self.element},
    "poids": {self.poids},
    "frottements": {self.frottements},
    "portee": {self.portee},
    "degats": {self.degats}"
}}"""
    
    @classmethod
    def parse(cls, json: str):
        """Parse un json en ProjectileNivele."""
        dictionnaire = parse(json)
        return ProjectileNivele(dictionnaire["nom"], dictionnaire["fantome"], dictionnaire["percant"], dictionnaire["fleche"], dictionnaire["explosif"], dictionnaire["fragile"], dictionnaire["magique"], dictionnaire["element"], dictionnaire["poids"], dictionnaire["frottements"], dictionnaire["portee"], dictionnaire["degats"])

    @classmethod
    @property
    def champs(cls) -> dict[str, type[int|str|float|bool|mdl.Element]]:
        return {
            "fantome": bool,
            "percant": bool,
            "fleche": bool,
            "explosif": bool,
            "fragile": bool,
            "magique": bool,
            "element": mdl.Element,
            "poids": float,
            "frottements": float,
            "portee": float,
            "degats": float
        }

    @classmethod
    @property
    def acceptors(cls) -> dict[str, Callable[[str], bool]]:
        return {
            "fantome": lambda _: True,
            "percant": lambda _: True,
            "fleche": lambda _: True,
            "explosif": lambda _: True,
            "fragile": lambda _: True,
            "magique": lambda _: True,
            "element": lambda element: element in mdl.Element,
            "poids": lambda poids: float(poids) >= 0,
            "frottements": lambda frottements: float(frottements) >= 0,
            "portee": lambda portee: float(portee) >= 0,
            "degats": lambda degats: float(degats) >= 0
        }

    @classmethod
    @property
    def avertissements(cls) -> dict[str, str]:
        return {
            "fantome": "Cet avertissement n'est pas censé apparaître.",
            "percant": "Cet avertissement n'est pas censé apparaître.",
            "fleche": "Cet avertissement n'est pas censé apparaître.",
            "explosif": "Cet avertissement n'est pas censé apparaître.",
            "fragile": "Cet avertissement n'est pas censé apparaître.",
            "magique": "Cet avertissement n'est pas censé apparaître.",
            "element": "Choisissez un élément.",
            "poids": "Le poids doit être positif.",
            "frottements": "Le frottement doit être positif.",
            "portee": "La portée doit être positive.",
            "degats": "Les dégats doivent être positifs."
        }

    def make(self, niveau: int) -> mdl.Projectile:
        """Crée un ProjectileNivele à partir de l'instance."""
        projectile = mdl.projectiles[(self.percant, self.fleche, self.explosif, self.fragile, self.magique)](mdl.NOWHERE, niveau, self.poids, self.frottements, self.portee, self.degats, self.element)
        projectile.nom = self.nom
        projectile.fantome = self.fantome
        return projectile
