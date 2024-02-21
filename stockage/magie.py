"""
Fichier contenant la classe de stockage des boucliers.
"""

from __future__ import annotations
from json import loads as parse
from enum import StrEnum

import modele as mdl

from .stockage import StockageCategorieNivelee, StockageNivele

class MagieNivele(StockageNivele):
    """Classe mère des classes de stockage de magie."""
    def make(self, niveau: int) -> mdl.Magie:
        """Retourne l'entité correspondante."""
        raise NotImplementedError

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
            "dirigee": False,
            "distance": False,
            "latence": True,
            "gain_xp": True,
            "cout_variable": False,
            "cout": True,
            "taux_degats": True,
            "degats": True,
            "portee": True,
            "element": False,
            "deplacement": False,
            "forme": False,
            "passe_mur": False,
            "passe_teleporteur": False,
            "passe_escalier": False,
            "passe_barriere": False,
            "passe_porte": False,
            "perce": False,
            "taux_perce": True,
            "inverse": False
        }

    acceptors = {
            "dirigee": lambda _: True,
            "distance": lambda _: True,
            "latence": lambda latence: float(latence) >= 0,
            "gain_xp": lambda gain_xp: float(gain_xp) >= 0,
            "cout_variable": lambda _: True,
            "cout": lambda cout: float(cout) >= 0,
            "taux_degats": lambda taux_degats: float(taux_degats) >= 0,
            "degats": lambda degats: float(degats) >= 0,
            "portee": lambda portee: float(portee) >= 0,
            "element": lambda element: True,
            "deplacement": lambda deplacement: True,
            "forme": lambda forme: True,
            "passe_mur": lambda _: True,
            "passe_teleporteur": lambda _: True,
            "passe_escalier": lambda _: True,
            "passe_barriere": lambda _: True,
            "passe_porte": lambda _: True,
            "perce": lambda _: True,
            "taux_perce": lambda taux_perce: 0 <= float(taux_perce) <= 1,
            "inverse": lambda _: True
        }

    avertissements = {
            "dirigee": "Cet avertissement n'est pas censé apparaître.",
            "distance": "Cet avertissement n'est pas censé apparaître.",
            "latence": "La latence doit être positive.",
            "gain_xp": "Le gain d'expérience doit être positif.",
            "cout_variable": "Cet avertissement n'est pas censé apparaître.",
            "cout": "Le coût doit être positif.",
            "taux_degats": "Le taux de dégâts doit être positif.",
            "degats": "Les dégâts doivent être positifs.",
            "portee": "La portée doit être positive.",
            "element": "Cet avertissement n'est pas censé apparaître.",
            "deplacement": "Cet avertissement n'est pas censé apparaître.",
            "forme": "Cet avertissement n'est pas censé apparaître.",
            "passe_mur": "Cet avertissement n'est pas censé apparaître.",
            "passe_teleporteur": "Cet avertissement n'est pas censé apparaître.",
            "passe_escalier": "Cet avertissement n'est pas censé apparaître.",
            "passe_barriere": "Cet avertissement n'est pas censé apparaître.",
            "passe_porte": "Cet avertissement n'est pas censé apparaître.",
            "perce": "Cet avertissement n'est pas censé apparaître.",
            "taux_perce": "Le taux de percement doit être compris entre 0 et 1.",
            "inverse": "Cet avertissement n'est pas censé apparaître."
        }

    conditionnels = {
            "dirigee": lambda dictionnaire: True,
            "distance": lambda dictionnaire: True,
            "latence": lambda dictionnaire: True,
            "gain_xp": lambda dictionnaire: True,
            "cout_variable": lambda dictionnaire: True,
            "cout": lambda dictionnaire: dictionnaire["cout_variable"]=="False",
            "taux_degats": lambda dictionnaire: dictionnaire["cout_variable"]=="True",
            "degats": lambda dictionnaire: dictionnaire["cout_variable"]=="False",
            "portee": lambda dictionnaire: True,
            "element": lambda dictionnaire: True,
            "deplacement": lambda dictionnaire: True,
            "forme": lambda dictionnaire: True,
            "passe_mur": lambda dictionnaire: True,
            "passe_teleporteur": lambda dictionnaire: True,
            "passe_escalier": lambda dictionnaire: True,
            "passe_barriere": lambda dictionnaire: True,
            "passe_porte": lambda dictionnaire: True,
            "perce": lambda dictionnaire: True,
            "taux_perce": lambda dictionnaire: dictionnaire["perce"]=="True",
            "inverse": lambda dictionnaire: True
        }

    multiple = {
            "dirigee": False,
            "distance": False,
            "latence": False,
            "gain_xp": False,
            "cout_variable": False,
            "cout": False,
            "taux_degats": False,
            "degats": False,
            "portee": False,
            "element": False,
            "deplacement": False,
            "forme": False,
            "passe_mur": False,
            "passe_teleporteur": False,
            "passe_escalier": False,
            "passe_barriere": False,
            "passe_porte": False,
            "perce": False,
            "taux_perce": False,
            "inverse": False
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

    def make(self, niveau: int) -> mdl.Magie:
        """Crée une magie à partir de l'instance."""
        class GenerateurMagieAttaque(mdl.Magie):
            """Un "générateur", c'est-à-dire une classe qui génère des instances de Magie."""
            nom = self.nom
            dirigee = self.dirigee
            distance = self.distance
            latence = self.latence
            gain_xp = self.gain_xp
            cout_variable = self.cout_variable
            cout = self.cout
            taux_degats = self.taux_degats
            degats = self.degats
            portee = self.portee
            element = self.element
            deplacement = self.deplacement
            forme = self.forme
            passe_mur = self.passe_mur
            passe_teleporteur = self.passe_teleporteur
            passe_escalier = self.passe_escalier
            passe_barriere = self.passe_barriere
            passe_porte = self.passe_porte
            perce = self.perce
            taux_perce = self.taux_perce
            inverse = self.inverse

            def genere(self, skill: mdl.Actif, agissant: mdl.Agissant, niveau: int) -> mdl.ActionMagieAttaque:
                return mdl.magies_attaque[(self.dirigee, self.distance, self.cout_variable)](skill, self, agissant, self.gain_xp[niveau], self.cout[niveau], self.portee[niveau], self.degats[niveau], self.element, self.deplacement, self.forme, mdl.Passage(self.passe_mur, self.passe_teleporteur, self.passe_escalier, self.passe_barriere, self.passe_porte), self.latence[niveau], self.taux_perce[niveau], self.inverse)
        return GenerateurMagieAttaque()

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
            "cible": False,
            "cible_multiple": False,
            "zone": False,
            "latence": True,
            "gain_xp": True,
            "cout_pm": True,
            "gain_pv": True,
            "portee": True
        }

    acceptors = {
            "cible": lambda _: True,
            "cible_multiple": lambda _: True,
            "zone": lambda _: True,
            "latence": lambda latence: float(latence) >= 0,
            "gain_xp": lambda gain_xp: float(gain_xp) >= 0,
            "cout_pm": lambda cout_pm: float(cout_pm) >= 0,
            "gain_pv": lambda gain_pv: float(gain_pv) >= 0,
            "portee": lambda portee: float(portee) >= 0
        }

    avertissements = {
            "cible": "Cet avertissement n'est pas censé apparaître.",
            "cible_multiple": "Cet avertissement n'est pas censé apparaître.",
            "zone": "Cet avertissement n'est pas censé apparaître.",
            "latence": "La latence doit être positive.",
            "gain_xp": "Le gain d'expérience doit être positif.",
            "cout_pm": "Le coût en points de mana doit être positif.",
            "gain_pv": "Le gain de points de vie doit être positif.",
            "portee": "La portée doit être positive."
        }

    conditionnels = {
            "cible": lambda dictionnaire: True,
            "cible_multiple": lambda dictionnaire: dictionnaire["cible"]=="True",
            "zone": lambda dictionnaire: dictionnaire["cible"]=="False",
            "latence": lambda dictionnaire: True,
            "gain_xp": lambda dictionnaire: True,
            "cout_pm": lambda dictionnaire: True,
            "gain_pv": lambda dictionnaire: True,
            "portee": lambda dictionnaire: True
        }
    
    multiple = {
            "cible": False,
            "cible_multiple": False,
            "zone": False,
            "latence": False,
            "gain_xp": False,
            "cout_pm": False,
            "gain_pv": False,
            "portee": False
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
    
    def make(self, niveau: int) -> mdl.Magie:
        """Crée une magie à partir de l'instance."""
        class GenerateurMagieSoin(mdl.Magie):
            """Un "générateur", c'est-à-dire une classe qui génère des instances de Magie."""
            nom = self.nom
            cible = self.cible
            cible_multiple = self.cible_multiple
            zone = self.zone
            latence = self.latence
            gain_xp = self.gain_xp
            cout_pm = self.cout_pm
            gain_pv = self.gain_pv
            portee = self.portee

            def genere(self, skill: mdl.Actif, agissant: mdl.Agissant, niveau: int) -> mdl.ActionMagieAutoSoin:
                magie_soin = mdl.magies_soin[(self.cible, self.cible_multiple, self.zone)]
                if isinstance(magie_soin, mdl.ActionMagieSoinDeZone):
                    return magie_soin(skill, self, agissant, self.gain_xp[niveau], self.cout_pm[niveau], self.latence[niveau], self.gain_pv[niveau], self.portee[niveau])
                else:
                    return magie_soin(skill, self, agissant, self.gain_xp[niveau], self.cout_pm[niveau], self.latence[niveau], self.gain_pv[niveau])
        return GenerateurMagieSoin()
    
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
    
    def make(self, niveau: int) -> mdl.Magie:
        """Crée une magie à partir de l'instance."""
        class GenerateurMagieResurection(mdl.Magie):
            """Un "générateur", c'est-à-dire une classe qui génère des instances de Magie."""
            nom = self.nom
            case = self.case
            zone = self.zone
            latence = self.latence
            gain_xp = self.gain_xp
            cout_pm = self.cout_pm
            portee_limite = self.portee_limite
            portee = self.portee

            def genere(self, skill: mdl.Actif, agissant: mdl.Agissant, niveau: int) -> mdl.ActionMagie:
                magie_resurection = mdl.magies_resurection[(self.case, self.zone)]
                if isinstance(magie_resurection, mdl.ActionMagieResurection):
                    return magie_resurection(skill, self, agissant, self.gain_xp[niveau], self.cout_pm[niveau], self.latence[niveau])
                elif isinstance(magie_resurection, mdl.ActionMagieResurectionCase):
                    return magie_resurection(skill, self, agissant, self.gain_xp[niveau], self.cout_pm[niveau], self.latence[niveau], self.portee_limite[niveau])
                elif isinstance(magie_resurection, mdl.ActionMagieResurectionDeZone):
                    return magie_resurection(skill, self, agissant, self.gain_xp[niveau], self.cout_pm[niveau], self.latence[niveau], self.portee_limite[niveau], self.portee[niveau])
                else:
                    raise ValueError("La magie de résurection n'est pas une magie de résurection.")
        return GenerateurMagieResurection()
    
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
    
    def make(self, niveau: int) -> mdl.Magie:
        """Crée une magie à partir de l'instance."""
        class GenerateurMagieReanimation(mdl.Magie):
            """Un "générateur", c'est-à-dire une classe qui génère des instances de Magie."""
            nom = self.nom
            case = self.case
            zone = self.zone
            latence = self.latence
            gain_xp = self.gain_xp
            cout_pm = self.cout_pm
            taux_pv = self.taux_pv
            superiorite = self.superiorite
            portee_limite = self.portee_limite
            portee = self.portee

            def genere(self, skill: mdl.Actif, agissant: mdl.Agissant, niveau: int) -> mdl.ActionMagie:
                magie_reanimation = mdl.magies_reanimation[(self.case, self.zone)]
                if isinstance(magie_reanimation, mdl.ActionMagieReanimation):
                    return magie_reanimation(skill, self, agissant, self.gain_xp[niveau], self.cout_pm[niveau], self.latence[niveau], self.taux_pv[niveau], self.superiorite[niveau])
                elif isinstance(magie_reanimation, mdl.ActionMagieReanimationCase):
                    return magie_reanimation(skill, self, agissant, self.gain_xp[niveau], self.cout_pm[niveau], self.latence[niveau], self.taux_pv[niveau], self.superiorite[niveau], self.portee_limite[niveau])
                elif isinstance(magie_reanimation, mdl.ActionMagieReanimationDeZone):
                    return magie_reanimation(skill, self, agissant, self.gain_xp[niveau], self.cout_pm[niveau], self.latence[niveau], self.taux_pv[niveau], self.superiorite[niveau], self.portee_limite[niveau], self.portee[niveau])
                else:
                    raise ValueError("La magie de réanimation n'est pas une magie de réanimation.")
        return GenerateurMagieReanimation()
    
class MagieEnchantementNivele(MagieNivele):
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
                                     "affinite": "Affinité élémentale",
                                     "renforcement": "Renforcement d'arme",
                                     "bombe": "Bombe (rend l'item explosif)"
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
            "gain_tranchant": float,
            "gain_portee": float,
            "degats": float,
            "portee": float
    }

    niveles = {
            "latence": True,
            "gain_xp": True,
            "cout_pm": True,
            "duree": True,
            "enchantement": False,
            "taux_confusion": True,
            "taux_poches_trouees": True,
            "gain_force": True,
            "gain_vision": True,
            "gain_pv": True,
            "gain_pm": True,
            "gain_vitesse": True,
            "superiorite": True,
            "affinite": True,
            "element": False,
            "gain_tranchant": True,
            "gain_portee": True,
            "degats": True,
            "portee": True
    }

    acceptors = {
            "latence": lambda latence: float(latence) >= 0,
            "gain_xp": lambda gain_xp: float(gain_xp) >= 0,
            "cout_pm": lambda cout_pm: float(cout_pm) >= 0,
            "duree": lambda duree: float(duree) >= 0,
            "enchantement": lambda enchantement: True,
            "taux_confusion": lambda taux_confusion: 0 <= float(taux_confusion) <= 1,
            "taux_poches_trouees": lambda taux_poches_trouees: 0 <= float(taux_poches_trouees) <= 1,
            "gain_force": lambda gain_force: float(gain_force) >= 0,
            "gain_vision": lambda gain_vision: float(gain_vision) >= 0,
            "gain_pv": lambda gain_pv: float(gain_pv) >= 0,
            "gain_pm": lambda gain_pm: float(gain_pm) >= 0,
            "gain_vitesse": lambda gain_vitesse: float(gain_vitesse) >= 0,
            "superiorite": lambda superiorite: float(superiorite) >= 0,
            "affinite": lambda affinite: float(affinite) >= 0,
            "element": lambda element: True,
            "gain_tranchant": lambda gain_tranchant: float(gain_tranchant) >= 0,
            "gain_portee": lambda gain_portee: float(gain_portee) >= 0,
            "degats": lambda degats: float(degats) >= 0,
            "portee": lambda portee: float(portee) >= 0
        }
    
    avertissements = {
            "latence": "La latence doit être positive.",
            "gain_xp": "Le gain d'expérience doit être positif.",
            "cout_pm": "Le coût en points de mana doit être positif.",
            "duree": "La durée doit être positive.",
            "enchantement": "Cet avertissement n'est pas censé apparaître.",
            "taux_confusion": "Le taux de confusion doit être compris entre 0 et 1.",
            "taux_poches_trouees": "Le taux de poches trouées doit être compris entre 0 et 1.",
            "gain_force": "Le gain de force doit être positif.",
            "gain_vision": "Le gain de vision doit être positif.",
            "gain_pv": "Le gain de points de vie doit être positif.",
            "gain_pm": "Le gain de points de mana doit être positif.",
            "gain_vitesse": "Le gain de vitesse doit être positif.",
            "superiorite": "La supériorité doit être positive.",
            "affinite": "L'affinité élémentale doit être positive.",
            "element": "Cet avertissement n'est pas censé apparaître.",
            "gain_tranchant": "Le gain de tranchant doit être positif.",
            "gain_portee": "Le gain de portée doit être positif.",
            "degats": "Les dégâts doivent être positifs.",
            "portee": "La portée doit être positive."
        }
    
    conditionnels = {
            "latence": lambda dictionnaire: True,
            "gain_xp": lambda dictionnaire: True,
            "cout_pm": lambda dictionnaire: True,
            "duree": lambda dictionnaire: True,
            "enchantement": lambda dictionnaire: True,
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
            "gain_tranchant": lambda dictionnaire: dictionnaire["enchantement"]=="renforcement",
            "gain_portee": lambda dictionnaire: dictionnaire["enchantement"]=="renforcement",
            "degats": lambda dictionnaire: dictionnaire["enchantement"]=="bombe",
            "portee": lambda dictionnaire: dictionnaire["enchantement"]=="bombe"
        }
    
    multiple = {
            "latence": False,
            "gain_xp": False,
            "cout_pm": False,
            "duree": False,
            "enchantement": False,
            "taux_confusion": False,
            "taux_poches_trouees": False,
            "gain_force": False,
            "gain_vision": False,
            "gain_pv": False,
            "gain_pm": False,
            "gain_vitesse": False,
            "superiorite": False,
            "affinite": False,
            "element": False,
            "gain_tranchant": False,
            "gain_portee": False,
            "degats": False,
            "portee": False
        }
    
    def __init__(self, nom: str, latence: list[float], gain_xp: list[float], cout_pm: list[float],
                 duree: list[float], enchantement: str, taux_confusion: list[float],
                 taux_poches_trouees: list[float], gain_force: list[float], gain_vision: list[float],
                 gain_pv: list[float], gain_pm: list[float], gain_vitesse: list[float],
                 superiorite: list[float], affinite: list[float], element: mdl.Element,
                 gain_tranchant: list[float], gain_portee: list[float], degats: list[float],
                 portee: list[float]):
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
        self.gain_tranchant = gain_tranchant
        self.gain_portee = gain_portee
        self.degats = degats
        self.portee = portee

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
                all(affinite >= 0 for affinite in self.affinite) and
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
    "taux_confusion": {self.taux_confusion},
    "taux_poches_trouees": {self.taux_poches_trouees},
    "gain_force": {self.gain_force},
    "gain_vision": {self.gain_vision},
    "gain_pv": {self.gain_pv},
    "gain_pm": {self.gain_pm},
    "gain_vitesse": {self.gain_vitesse},
    "superiorite": {self.superiorite},
    "affinite": {self.affinite},
    "element": "{self.element}",
    "gain_tranchant": {self.gain_tranchant},
    "gain_portee": {self.gain_portee},
    "degats": {self.degats},
    "portee": {self.portee}
}}"""
    
    @classmethod
    def parse(cls, json: str):
        """Parse un json en BouclierNivele."""
        dictionnaire = parse(json)
        return MagieEnchantementNivele(dictionnaire["nom"], dictionnaire["latence"], dictionnaire["gain_xp"], dictionnaire["cout_pm"], dictionnaire["duree"], dictionnaire["enchantement"], dictionnaire["taux_confusion"], dictionnaire["taux_poches_trouees"], dictionnaire["gain_force"], dictionnaire["gain_vision"], dictionnaire["gain_pv"], dictionnaire["gain_pm"], dictionnaire["gain_vitesse"], dictionnaire["superiorite"], dictionnaire["affinite"], dictionnaire["element"], dictionnaire["gain_tranchant"], dictionnaire["gain_portee"], dictionnaire["degats"], dictionnaire["portee"])
    
    def make(self, niveau: int) -> mdl.Magie:
        """Crée une magie à partir de l'instance."""
        class GenerateurMagieEnchantement(mdl.Magie):
            """Un "générateur", c'est-à-dire une classe qui génère des instances de Magie."""
            nom = self.nom
            latence = self.latence
            gain_xp = self.gain_xp
            cout_pm = self.cout_pm
            duree = self.duree
            enchantement = self.enchantement
            taux_confusion = self.taux_confusion
            taux_poches_trouees = self.taux_poches_trouees
            gain_force = self.gain_force
            gain_vision = self.gain_vision
            gain_pv = self.gain_pv
            gain_pm = self.gain_pm
            gain_vitesse = self.gain_vitesse
            superiorite = self.superiorite
            affinite = self.affinite
            element = self.element
            gain_tranchant = self.gain_tranchant
            gain_portee = self.gain_portee
            degats = self.degats
            portee = self.portee

            def genere(self, skill: mdl.Actif, agissant: mdl.Agissant, niveau: int) -> mdl.ActionMagie:
                magie_enchantement = mdl.magies_enchantement[self.enchantement]
                if isinstance(magie_enchantement, mdl.ActionMagieEnchantementAffinite):
                    return magie_enchantement(skill, self, agissant, self.gain_xp[niveau], self.cout_pm[niveau], self.latence[niveau], self.duree[niveau], self.affinite[niveau], self.element)
                elif isinstance(magie_enchantement, mdl.EnchanteAgissant):
                    return magie_enchantement(skill, self, agissant, self.gain_xp[niveau], self.cout_pm[niveau], self.latence[niveau], self.duree[niveau], self.taux_confusion[niveau] if self.enchantement=="confusion" else self.taux_poches_trouees[niveau] if self.enchantement=="poches_trouees" else self.gain_force[niveau] if self.enchantement=="force" else self.gain_vision[niveau] if self.enchantement=="vision" else self.gain_pv[niveau] if self.enchantement=="vitalite" else self.gain_pm[niveau] if self.enchantement=="absorption" else self.gain_vitesse[niveau] if self.enchantement=="celerite" else self.superiorite[niveau] if self.enchantement=="immunite" else ValueError("L'enchantement n'est pas un enchantement d'agissant."))
                elif isinstance(magie_enchantement, mdl.EnchanteItem):
                    return magie_enchantement(skill, self, agissant, self.gain_xp[niveau], self.cout_pm[niveau], self.latence[niveau], self.duree[niveau], self.gain_tranchant[niveau] if self.enchantement=="renforcement" else self.degats[niveau], self.gain_portee[niveau] if self.enchantement=="renforcement" else self.portee[niveau])
                else:
                    raise ValueError("L'enchantement n'est pas un enchantement.")
        return GenerateurMagieEnchantement()
    
class MagieReserveNivelee(MagieNivele):
    """Une magie de réserve."""

    champs = {
            "latence": float,
            "gain_xp": float,
            "cout_pm": float,
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
    
    def __init__(self, nom: str, latence: list[float], gain_xp: list[float], cout_pm: list[float],
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
        return MagieReserveNivelee(dictionnaire["nom"], dictionnaire["latence"], dictionnaire["gain_xp"], dictionnaire["cout_pm"], dictionnaire["taux_pm"])
    
    def make(self, niveau: int) -> mdl.Magie:
        """Crée une magie à partir de l'instance."""
        class GenerateurMagieReserve(mdl.Magie):
            """Un "générateur", c'est-à-dire une classe qui génère des instances de Magie."""
            nom = self.nom
            latence = self.latence
            gain_xp = self.gain_xp
            taux_pm = self.taux_pm

            def genere(self, skill: mdl.Actif, agissant: mdl.Agissant, niveau: int) -> mdl.ActionMagieReserve:
                return mdl.ActionMagieReserve(skill, self, agissant, self.gain_xp[niveau], self.latence[niveau], self.taux_pm[niveau])
            
        return GenerateurMagieReserve()
    
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
    
    def __init__(self, nom: str, latence: list[float], gain_xp: list[float], cout_pm: list[float],
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
        return MagieInvestissementNivelee(dictionnaire["nom"], dictionnaire["latence"], dictionnaire["gain_xp"], dictionnaire["cout_pm"], dictionnaire["taux_pm"], dictionnaire["duree"])
    
    def make(self, niveau: int) -> mdl.Magie:
        """Crée une magie à partir de l'instance."""
        class GenerateurMagieInvestissement(mdl.Magie):
            """Un "générateur", c'est-à-dire une classe qui génère des instances de Magie."""
            nom = self.nom
            latence = self.latence
            gain_xp = self.gain_xp
            taux_pm = self.taux_pm
            duree = self.duree

            def genere(self, skill: mdl.Actif, agissant: mdl.Agissant, niveau: int) -> mdl.ActionMagieInvestissement:
                return mdl.ActionMagieInvestissement(skill, self, agissant, self.gain_xp[niveau], self.latence[niveau], self.taux_pm[niveau], self.duree[niveau])
            
        return GenerateurMagieInvestissement()

class Magies(StockageCategorieNivelee):
    """Les informations des boucliers."""
    nom = "Boucliers"
    titre_nouveau = "Nouveau bouclier"
    description = "Les boucliers sont destinés à être équippés. Ils permettent de défendre une zone contre les attaques."
    avertissement = "Il existe déjà un bouclier avec ce nom !"
    elements = {
        "MagieAttaqueNivele": MagieAttaqueNivele,
        "MagieBoostNivele": MagieBoostNivele,
        "MagieSoinNivelee": MagieSoinNivelee,
        "MagieResurectionNivele": MagieResurectionNivele,
        "MagieReanimationNivele": MagieReanimationNivele,
        "MagieEnchantementNivele": MagieEnchantementNivele,
        "MagieReserveNivelee": MagieReserveNivelee,
        "MagieInvestissementNivelee": MagieInvestissementNivelee
    }
