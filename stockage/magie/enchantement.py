"""
Fichier contenant la classe de stockage des enchantements.
"""

from __future__ import annotations
from json import loads as parse
from enum import StrEnum

import modele as mdl

from .magie import MagieNivele

class MagieEnchantementAgissantNivele(MagieNivele):
    """Une magie d'enchantement."""

    champs = {
            "latence": float,
            "gain_xp": float,
            "cout_pm": float,
            "duree": float,
            "enchantement": StrEnum("enchantement",
                                    {"confusion": "Confusion (déplacements randomisés)",
                                     "poches_trouees": "Poches trouées (perte d'objets)",
                                     "force": "Force",
                                     "vision": "Vision",
                                     "vitalite": "Vitalité (régénération de points de vie)",
                                     "absorption": "Absorption (régénération de points de mana)",
                                     "celerite": "Célérité",
                                     "immunite": "Immunité (résistance aux maladies)",
                                     "affinite": "Affinité élémentale"
                                    }),
            "taux_confusion": float,
            "taux_poches_trouees": float,
            "gain_force": float,
            "gain_vision": float,
            "gain_pv": float,
            "gain_pm": float,
            "gain_vitesse": float,
            "superiorite": float,
            "affinite": float,
            "element": mdl.Element,
    }

    niveles = {
            "latence": True,
            "gain_xp": True,
            "cout_pm": True,
            "duree": True,
            "taux_confusion": True,
            "taux_poches_trouees": True,
            "gain_force": True,
            "gain_vision": True,
            "gain_pv": True,
            "gain_pm": True,
            "gain_vitesse": True,
            "superiorite": True,
            "affinite": True,
    }

    acceptors = {
            "latence": lambda latence: float(latence) >= 0,
            "gain_xp": lambda gain_xp: float(gain_xp) >= 0,
            "cout_pm": lambda cout_pm: float(cout_pm) >= 0,
            "duree": lambda duree: float(duree) >= 0,
            "taux_confusion": lambda taux_confusion: 0 <= float(taux_confusion) <= 1,
            "taux_poches_trouees": lambda taux_poches_trouees: 0 <= float(taux_poches_trouees) <= 1,
            "gain_force": lambda gain_force: float(gain_force) >= 0,
            "gain_vision": lambda gain_vision: float(gain_vision) >= 0,
            "gain_pv": lambda gain_pv: float(gain_pv) >= 0,
            "gain_pm": lambda gain_pm: float(gain_pm) >= 0,
            "gain_vitesse": lambda gain_vitesse: float(gain_vitesse) >= 0,
            "superiorite": lambda superiorite: float(superiorite) >= 0,
            "affinite": lambda affinite: float(affinite) >= 0,
        }

    avertissements = {
            "latence": "La latence doit être positive.",
            "gain_xp": "Le gain d'expérience doit être positif.",
            "cout_pm": "Le coût en points de mana doit être positif.",
            "duree": "La durée doit être positive.",
            "taux_confusion": "Le taux de confusion doit être compris entre 0 et 1.",
            "taux_poches_trouees": "Le taux de poches trouées doit être compris entre 0 et 1.",
            "gain_force": "Le gain de force doit être positif.",
            "gain_vision": "Le gain de vision doit être positif.",
            "gain_pv": "Le gain de points de vie doit être positif.",
            "gain_pm": "Le gain de points de mana doit être positif.",
            "gain_vitesse": "Le gain de vitesse doit être positif.",
            "superiorite": "La supériorité doit être positive.",
            "affinite": "L'affinité élémentale doit être positive.",
        }

    conditionnels = {
            "taux_confusion": lambda dictionnaire: dictionnaire["enchantement"]=="confusion",
            "taux_poches_trouees": lambda dictionnaire: dictionnaire["enchantement"]=="poches_trouees",
            "gain_force": lambda dictionnaire: dictionnaire["enchantement"]=="force",
            "gain_vision": lambda dictionnaire: dictionnaire["enchantement"]=="vision",
            "gain_pv": lambda dictionnaire: dictionnaire["enchantement"]=="vitalite",
            "gain_pm": lambda dictionnaire: dictionnaire["enchantement"]=="absorption",
            "gain_vitesse": lambda dictionnaire: dictionnaire["enchantement"]=="celerite",
            "superiorite": lambda dictionnaire: dictionnaire["enchantement"]=="immunite",
            "affinite": lambda dictionnaire: dictionnaire["enchantement"]=="affinite",
            "element": lambda dictionnaire: dictionnaire["enchantement"]=="affinite",
        }

    def __init__(self, nom: str, latence: list[float], gain_xp: list[float], cout_pm: list[float],
                 duree: list[float], enchantement: str, taux_confusion: list[float],
                 taux_poches_trouees: list[float], gain_force: list[float], gain_vision: list[float],
                 gain_pv: list[float], gain_pm: list[float], gain_vitesse: list[float],
                 superiorite: list[float], affinite: list[float], element: mdl.Element):
        MagieNivele.__init__(self, nom)
        self.latence = latence
        self.gain_xp = gain_xp
        self.cout_pm = cout_pm
        self.duree = duree
        self.enchantement = enchantement
        self.taux_confusion = taux_confusion
        self.taux_poches_trouees = taux_poches_trouees
        self.gain_force = gain_force
        self.gain_vision = gain_vision
        self.gain_pv = gain_pv
        self.gain_pm = gain_pm
        self.gain_vitesse = gain_vitesse
        self.superiorite = superiorite
        self.affinite = affinite
        self.element = element

    def check(self) -> bool:
        return (all(latence >= 0 for latence in self.latence) and
                all(gain >= 0 for gain in self.gain_xp) and
                all(cout_pm >= 0 for cout_pm in self.cout_pm) and
                all(duree >= 0 for duree in self.duree) and
                all(0 <= taux_confusion <= 1 for taux_confusion in self.taux_confusion) and
                all(0 <= taux_poches_trouees <= 1 for taux_poches_trouees in self.taux_poches_trouees) and
                all(gain >= 0 for gain in self.gain_force) and
                all(gain >= 0 for gain in self.gain_vision) and
                all(gain >= 0 for gain in self.gain_pv) and
                all(gain >= 0 for gain in self.gain_pm) and
                all(gain >= 0 for gain in self.gain_vitesse) and
                all(superiorite >= 0 for superiorite in self.superiorite) and
                all(affinite >= 0 for affinite in self.affinite))

    def stringify(self) -> str:
        return f"""{{
    "type": "magie_enchantement",
    "nivele": true,
    "nom": "{self.nom}",
    "latence": {self.latence},
    "gain_xp": {self.gain_xp},
    "cout_pm": {self.cout_pm},
    "duree": {self.duree},
    "enchantement": "{self.enchantement}",
    "taux_confusion": {self.taux_confusion},
    "taux_poches_trouees": {self.taux_poches_trouees},
    "gain_force": {self.gain_force},
    "gain_vision": {self.gain_vision},
    "gain_pv": {self.gain_pv},
    "gain_pm": {self.gain_pm},
    "gain_vitesse": {self.gain_vitesse},
    "superiorite": {self.superiorite},
    "affinite": {self.affinite},
    "element": "{self.element}"
}}"""

    @classmethod
    def parse(cls, json: str):
        """Parse un json en BouclierNivele."""
        dictionnaire = parse(json)
        return MagieEnchantementAgissantNivele(dictionnaire["nom"], dictionnaire["latence"], dictionnaire["gain_xp"], dictionnaire["cout_pm"], dictionnaire["duree"], dictionnaire["enchantement"], dictionnaire["taux_confusion"], dictionnaire["taux_poches_trouees"], dictionnaire["gain_force"], dictionnaire["gain_vision"], dictionnaire["gain_pv"], dictionnaire["gain_pm"], dictionnaire["gain_vitesse"], dictionnaire["superiorite"], dictionnaire["affinite"], dictionnaire["element"])

    def make(self, niveau: int):
        """Crée une magie à partir de l'instance."""
        enchantement = mdl.enchantements_agissants[self.enchantement]
        class EnchantementAgissant(enchantement):
            """Un enchantement agissant."""
            match self.enchantement:
                case "confusion":
                    taux_confusion = self.taux_confusion[niveau]
                case "poches_trouees":
                    taux_pertes = self.taux_poches_trouees[niveau]
                case "force":
                    gain_force = self.gain_force[niveau]
                case "vision":
                    gain_vision = self.gain_vision[niveau]
                case "vitalite":
                    gain_pv = self.gain_pv[niveau]
                case "absorption":
                    gain_pm = self.gain_pm[niveau]
                case "celerite":
                    gain_vitesse = self.gain_vitesse[niveau]
                case "immunite":
                    superiorite = self.superiorite[niveau]
                case "affinite":
                    gain_affinite = self.affinite[niveau]
                    element = self.element
                case _:
                    raise ValueError(f"Enchantement inconnu : {self.enchantement}")
        class MagieEnchantementAgissantNiveau(mdl.EnchanteAgissant, mdl.Nomme):
            """Une magie d'enchantement."""
            enchantement = EnchantementAgissant
            duree = self.duree[niveau]
            latence_max = self.latence[niveau]
            gain_xp = self.gain_xp[niveau]
            cout = self.cout_pm[niveau]
        MagieEnchantementAgissantNiveau.nom = self.nom
        MagieEnchantementAgissantNiveau.niveau = niveau
        return MagieEnchantementAgissantNiveau

class MagieEnchantementItemNivele(MagieNivele):
    """Une magie d'enchantement."""

    champs = {
            "latence": float,
            "gain_xp": float,
            "cout_pm": float,
            "duree": float,
            "enchantement": StrEnum("enchantement",
                                    {"renforcement": "Renforcement d'arme",
                                     "bombe": "Bombe (rend l'item explosif)"
                                    }),
            "gain_tranchant": float,
            "gain_portee": float,
            "degats": float,
            "portee": float,
    }

    niveles = {
            "latence": True,
            "gain_xp": True,
            "cout_pm": True,
            "duree": True,
            "gain_tranchant": True,
            "gain_portee": True,
            "degats": True,
            "portee": True,
    }

    acceptors = {
            "latence": lambda latence: float(latence) >= 0,
            "gain_xp": lambda gain_xp: float(gain_xp) >= 0,
            "cout_pm": lambda cout_pm: float(cout_pm) >= 0,
            "duree": lambda duree: float(duree) >= 0,
            "gain_tranchant": lambda gain_tranchant: float(gain_tranchant) >= 0,
            "gain_portee": lambda gain_portee: float(gain_portee) >= 0,
            "degats": lambda degats: float(degats) >= 0,
            "portee": lambda portee: float(portee) >= 0,
        }

    avertissements = {
            "latence": "La latence doit être positive.",
            "gain_xp": "Le gain d'expérience doit être positif.",
            "cout_pm": "Le coût en points de mana doit être positif.",
            "duree": "La durée doit être positive.",
            "gain_tranchant": "Le gain de tranchant doit être positif.",
            "gain_portee": "Le gain de portée doit être positif.",
            "degats": "Les dégâts doivent être positifs.",
            "portee": "La portée doit être positive.",
        }

    conditionnels = {
            "gain_tranchant": lambda dictionnaire: dictionnaire["enchantement"]=="renforcement",
            "gain_portee": lambda dictionnaire: dictionnaire["enchantement"]=="renforcement",
            "degats": lambda dictionnaire: dictionnaire["enchantement"]=="bombe",
            "portee": lambda dictionnaire: dictionnaire["enchantement"]=="bombe",
        }

    def __init__(self, nom: str, latence: list[float], gain_xp: list[float], cout_pm: list[float],
                 duree: list[float], enchantement: str,
                 gain_tranchant: list[float], gain_portee: list[float], degats: list[float],
                 portee: list[float]):
        MagieNivele.__init__(self, nom)
        self.latence = latence
        self.gain_xp = gain_xp
        self.cout_pm = cout_pm
        self.duree = duree
        self.enchantement = enchantement
        self.gain_tranchant = gain_tranchant
        self.gain_portee = gain_portee
        self.degats = degats
        self.portee = portee

    def check(self) -> bool:
        return (all(latence >= 0 for latence in self.latence) and
                all(gain >= 0 for gain in self.gain_xp) and
                all(cout_pm >= 0 for cout_pm in self.cout_pm) and
                all(duree >= 0 for duree in self.duree) and
                all(gain >= 0 for gain in self.gain_tranchant) and
                all(gain >= 0 for gain in self.gain_portee) and
                all(gain >= 0 for gain in self.degats) and
                all(portee >= 0 for portee in self.portee))

    def stringify(self) -> str:
        return f"""{{
    "type": "magie_enchantement",
    "nivele": true,
    "nom": "{self.nom}",
    "latence": {self.latence},
    "gain_xp": {self.gain_xp},
    "cout_pm": {self.cout_pm},
    "duree": {self.duree},
    "enchantement": "{self.enchantement}",
    "gain_tranchant": {self.gain_tranchant},
    "gain_portee": {self.gain_portee},
    "degats": {self.degats},
    "portee": {self.portee}
}}"""

    @classmethod
    def parse(cls, json: str):
        """Parse un json en BouclierNivele."""
        dictionnaire = parse(json)
        return MagieEnchantementItemNivele(dictionnaire["nom"], dictionnaire["latence"], dictionnaire["gain_xp"], dictionnaire["cout_pm"], dictionnaire["duree"], dictionnaire["enchantement"], dictionnaire["gain_tranchant"], dictionnaire["gain_portee"], dictionnaire["degats"], dictionnaire["portee"])

    def make(self, niveau: int):
        """Crée une magie à partir de l'instance."""
        enchantement = mdl.enchantements_items[self.enchantement]
        class EnchantementItem(enchantement):
            """Un enchantement d'item."""
            match self.enchantement:
                case "renforcement":
                    gain_force = self.gain_tranchant[niveau]
                    gain_portee = self.gain_portee[niveau]
                case "bombe":
                    portee = self.portee[niveau]
                    degats = self.degats[niveau]
                case _:
                    raise ValueError(f"Enchantement inconnu : {self.enchantement}")
        class MagieEnchantementItemNiveau(mdl.EnchanteItem, mdl.Nomme):
            """Une magie d'enchantement."""
            enchantement = EnchantementItem
            duree = self.duree[niveau]
            latence_max = self.latence[niveau]
            gain_xp = self.gain_xp[niveau]
            cout = self.cout_pm[niveau]
        MagieEnchantementItemNiveau.nom = self.nom
        MagieEnchantementItemNiveau.niveau = niveau
        return MagieEnchantementItemNiveau
