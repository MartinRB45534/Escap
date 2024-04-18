"""
Fichier contenant la classe de stockage des magies d'attaques.
"""

from __future__ import annotations
from json import loads as parse

import modele as mdl

from .magie import MagieNivele

class MagieAttaqueNivele(MagieNivele):
    """Une magie d'attaque."""

    champs = {
            "dirigee": bool,
            "distance": bool,
            "latence": float,
            "gain_xp": float,
            "cout_variable": bool,
            "cout": float,
            "taux_degats": float,
            "degats": float,
            "portee": float,
            "element": mdl.Element,
            "deplacement": mdl.Deplacement,
            "forme": mdl.Forme,
            "passe_mur": bool,
            "passe_teleporteur": bool,
            "passe_escalier": bool,
            "passe_barriere": bool,
            "passe_porte": bool,
            "perce": bool,
            "taux_perce": float,
            "inverse": bool
        }

    niveles = {
            "latence": True,
            "gain_xp": True,
            "cout": True,
            "taux_degats": True,
            "degats": True,
            "portee": True,
            "taux_perce": True,
        }

    acceptors = {
            "latence": lambda latence: float(latence) >= 0,
            "gain_xp": lambda gain_xp: float(gain_xp) >= 0,
            "cout": lambda cout: float(cout) >= 0,
            "taux_degats": lambda taux_degats: float(taux_degats) >= 0,
            "degats": lambda degats: float(degats) >= 0,
            "portee": lambda portee: float(portee) >= 0,
            "taux_perce": lambda taux_perce: 0 <= float(taux_perce) <= 1,
        }

    avertissements = {
            "latence": "La latence doit être positive.",
            "gain_xp": "Le gain d'expérience doit être positif.",
            "cout": "Le coût doit être positif.",
            "taux_degats": "Le taux de dégâts doit être positif.",
            "degats": "Les dégâts doivent être positifs.",
            "portee": "La portée doit être positive.",
            "taux_perce": "Le taux de percement doit être compris entre 0 et 1.",
        }

    conditionnels = {
            "cout": lambda dictionnaire: dictionnaire["cout_variable"]=="False",
            "taux_degats": lambda dictionnaire: dictionnaire["cout_variable"]=="True",
            "degats": lambda dictionnaire: dictionnaire["cout_variable"]=="False",
            "taux_perce": lambda dictionnaire: dictionnaire["perce"]=="True",
        }

    def __init__(self, nom: str, dirigee: bool, distance: bool, latence: list[float],
                 gain_xp: list[float], cout_variable: bool, cout: list[float],
                 taux_degats: list[float], degats: list[float], portee: list[float], element: mdl.Element,
                 deplacement: mdl.Deplacement, forme: mdl.Forme, passe_mur: bool,
                 passe_teleporteur: bool, passe_escalier: bool, passe_barriere: bool,
                 passe_porte: bool, perce: bool, taux_perce: list[float], inverse: bool):
        MagieNivele.__init__(self, nom)
        self.latence = latence
        self.gain_xp = gain_xp
        self.dirigee = dirigee
        self.distance = distance
        self.cout_variable = cout_variable
        self.cout = cout
        self.taux_degats = taux_degats
        self.degats = degats
        self.portee = portee
        self.element = element
        self.deplacement = deplacement
        self.forme = forme
        self.passe_mur = passe_mur
        self.passe_teleporteur = passe_teleporteur
        self.passe_escalier = passe_escalier
        self.passe_barriere = passe_barriere
        self.passe_porte = passe_porte
        self.perce = perce
        self.taux_perce = taux_perce
        self.inverse = inverse

    def check(self) -> bool:
        return (all(latence >= 0 for latence in self.latence) and
                all(gain >= 0 for gain in self.gain_xp) and
                all(cout >= 0 for cout in self.cout) and
                all(taux_degats >= 0 for taux_degats in self.taux_degats) and
                all(degats >= 0 for degats in self.degats) and
                all(portee >= 0 for portee in self.portee) and
                all(0 <= taux_perce <= 1 for taux_perce in self.taux_perce))

    def stringify(self) -> str:
        return f"""{{
    "type": "magie_attaque",
    "nivele": true,
    "nom": "{self.nom}",
    "dirigee": {self.dirigee},
    "distance": {self.distance},
    "latence": {self.latence},
    "gain_xp": {self.gain_xp},
    "cout_variable": {self.cout_variable},
    "cout": {self.cout},
    "taux_degats": {self.taux_degats},
    "degats": {self.degats},
    "portee": {self.portee},
    "element": "{self.element}",
    "deplacement": "{self.deplacement}",
    "forme": "{self.forme}",
    "passe_mur": {self.passe_mur},
    "passe_teleporteur": {self.passe_teleporteur},
    "passe_escalier": {self.passe_escalier},
    "passe_barriere": {self.passe_barriere},
    "passe_porte": {self.passe_porte},
    "perce": {self.perce},
    "taux_perce": {self.taux_perce},
    "inverse": {self.inverse}
}}"""

    @classmethod
    def parse(cls, json: str):
        """Parse un json en BouclierNivele."""
        dictionnaire = parse(json)
        return MagieAttaqueNivele(dictionnaire["nom"], dictionnaire["dirigee"], dictionnaire["distance"], dictionnaire["latence"], dictionnaire["gain_xp"], dictionnaire["cout_variable"], dictionnaire["cout"], dictionnaire["taux_degats"], dictionnaire["degats"], dictionnaire["portee"], mdl.Element(dictionnaire["element"]), mdl.Deplacement(dictionnaire["deplacement"]), mdl.Forme(dictionnaire["forme"]), dictionnaire["passe_mur"], dictionnaire["passe_teleporteur"], dictionnaire["passe_escalier"], dictionnaire["passe_barriere"], dictionnaire["passe_porte"], dictionnaire["perce"], dictionnaire["taux_perce"], dictionnaire["inverse"])

    def make(self, niveau: int):
        """Crée une magie à partir de l'instance."""
        classe = mdl.magies_attaque[(self.dirigee, self.distance, self.cout_variable)]
        class MagieAttaqueNiveau(classe, mdl.Nomme):
            """Une magie d'attaque."""
            portee = self.portee[niveau]
            degats = self.degats[niveau]
            element = self.element
            deplacement = self.deplacement
            forme = self.forme
            passage = mdl.Passage(self.passe_mur, self.passe_teleporteur, self.passe_escalier,
                                  self.passe_barriere, self.passe_porte)
            taux_perce = self.taux_perce[niveau]
            inverse = self.inverse
            latence_max = self.latence[niveau]
            gain_xp = self.gain_xp[niveau]
            cout = self.cout[niveau]
            if self.cout_variable:
                taux_degats = self.taux_degats[niveau]
        MagieAttaqueNiveau.nom = self.nom
        MagieAttaqueNiveau.niveau = niveau
        return MagieAttaqueNiveau
