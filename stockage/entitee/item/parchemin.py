"""
Fichier contenant la classe de stockage des parchemins.
"""

from __future__ import annotations
from json import loads as parse

import modele as mdl
import carte as crt

from ...stockage import StockageCategorieNivelee
from ...magie import Magies, MagieNivele
from ..entitee import EntiteeNivele

class ParcheminViergeNivele(EntiteeNivele):
    """Les informations d'un parchemin vierge."""

    champs = {
            "fantome": bool,
            "poids": float,
            "frottements": float,
            "latence_impregne": float,
            "taux_cout_caste": float,
            "taux_cout_impregne": float,
            "taux_latence_caste": float,
            "taux_latence_impregne": float,
        }

    niveles = {
            "poids": True,
            "frottements": True,
            "latence_impregne": True,
            "taux_cout_caste": True,
            "taux_cout_impregne": True,
            "taux_latence_caste": True,
            "taux_latence_impregne": True,
        }

    acceptors = {
            "poids": lambda poids: float(poids) >= 0,
            "frottements": lambda frottements: float(frottements) >= 0,
            "latence_impregne": lambda latence: float(latence) >= 0,
            "taux_cout_caste": lambda taux: float(taux) >= 0,
            "taux_cout_impregne": lambda taux: float(taux) >= 0,
            "taux_latence_caste": lambda taux: float(taux) >= 0,
            "taux_latence_impregne": lambda taux: float(taux) >= 0,
        }

    avertissements = {
            "poids": "Le poids doit être positif.",
            "frottements": "Le frottement doit être positif.",
            "latence_impregne": "La latence d'impregnation doit être positive.",
            "taux_cout_caste": "Le taux de cout de caste doit être positif.",
            "taux_cout_impregne": "Le taux de cout d'impregnation doit être positif.",
            "taux_latence_caste": "Le taux de latence de caste doit être positif.",
            "taux_latence_impregne": "Le taux de latence d'impregnation doit être positif.",
        }

    def __init__(self, nom: str, poids: list[float], frottements: list[float],
                 fantome: bool, latence_impregne:list[float],
                 taux_cout_caste:list[float], taux_cout_impregne:list[float],
                 taux_latence_caste:list[float], taux_latence_impregne:list[float]):
        EntiteeNivele.__init__(self, nom)
        self.fantome = fantome
        self.poids = poids
        self.frottements = frottements
        self.latence_impregne = latence_impregne
        self.taux_cout_caste = taux_cout_caste
        self.taux_cout_impregne = taux_cout_impregne
        self.taux_latence_caste = taux_latence_caste
        self.taux_latence_impregne = taux_latence_impregne

    def check(self) -> bool:
        return (all([latence >= 0 for latence in self.latence_impregne]) and
                all([poids >= 0 for poids in self.poids]) and
                all([frottements >= 0 for frottements in self.frottements]) and
                all([taux >= 0 for taux in self.taux_cout_caste]) and
                all([taux >= 0 for taux in self.taux_cout_impregne]) and
                all([taux >= 0 for taux in self.taux_latence_caste]) and
                all([taux >= 0 for taux in self.taux_latence_impregne]))

    def stringify(self) -> str:
        return f"""{{
    "type": "parchemin vierge",
    "nivele": true,
    "nom": "{self.nom}",
    "fantome": {self.fantome},
    "poids": {self.poids},
    "frottements": {self.frottements},
    "latence_impregne": {self.latence_impregne},
    "taux_cout_caste": {self.taux_cout_caste},
    "taux_cout_impregne": {self.taux_cout_impregne},
    "taux_latence_caste": {self.taux_latence_caste},
    "taux_latence_impregne": {self.taux_latence_impregne}
}}"""

    @classmethod
    def parse(cls, json: str):
        dictionnaire = parse(json)
        return cls(dictionnaire["nom"], dictionnaire["fantome"], dictionnaire["poids"], dictionnaire["frottements"], dictionnaire["latence_impregne"], dictionnaire["taux_cout_caste"], dictionnaire["taux_cout_impregne"], dictionnaire["taux_latence_caste"], dictionnaire["taux_latence_impregne"])

    def make(self, niveau:int) -> type[mdl.ParcheminVierge]:
        """Retourne le parchemin correspondant."""
        class ParcheminViergeNiveau(mdl.ParcheminVierge, mdl.Nomme):
            """Un parchemin vierge."""
            poids = self.poids[niveau]
            frottements = self.frottements[niveau]
            latence_impregne = self.latence_impregne[niveau]
            taux_cout_caste = self.taux_cout_caste[niveau]
            taux_cout_impregne = self.taux_cout_impregne[niveau]
            taux_latence_caste = self.taux_latence_caste[niveau]
            taux_latence_impregne = self.taux_latence_impregne[niveau]
            fantome = self.fantome
        ParcheminViergeNiveau.nom = self.nom
        ParcheminViergeNiveau.niveau = niveau
        return ParcheminViergeNiveau

class ParcheminMagieNivele(EntiteeNivele):
    """Les informations d'un parchemin préécrit."""

    champs = {
            "fantome": bool,
            "poids": float,
            "frottements": float,
            "magie": Magies,
            "taux_cout_caste": float,
            "taux_latence_caste": float
        }
    
    niveles = {
            "fantome": False,
            "poids": False,
            "frottements": False,
            "magie": False,
            "taux_cout_caste": True,
            "taux_latence_caste": True
        }
    
    acceptors = {
            "fantome": lambda _: True,
            "poids": lambda poids: float(poids) >= 0,
            "frottements": lambda frottements: float(frottements) >= 0,
            "magie": lambda magie: magie in Magies.global_.trouve_stockage(Magies).all_noms,
            "taux_cout_caste": lambda taux: float(taux) >= 0,
            "taux_latence_caste": lambda taux: float(taux) >= 0
        }
    
    avertissements = {
            "fantome": "Please file a bug report.",
            "poids": "Le poids doit être positif.",
            "frottements": "Le frottement doit être positif.",
            "magie": "La magie n'existe pas.",
            "taux_cout_caste": "Le taux de cout de caste doit être positif.",
            "taux_latence_caste": "Le taux de latence de caste doit être positif."
        }
    
    conditionnels = {
            "fantome": lambda dictionnaire: True,
            "poids": lambda dictionnaire: True,
            "frottements": lambda dictionnaire: True,
            "magie": lambda dictionnaire: True,
            "taux_cout_caste": lambda dictionnaire: True,
            "taux_latence_caste": lambda dictionnaire: True
        }
    
    multiple = {
            "fantome": False,
            "poids": False,
            "frottements": False,
            "magie": False,
            "taux_cout_caste": False,
            "taux_latence_caste": False
        }
    
    def __init__(self, nom: str, fantome: bool, poids: list[float], frottements: list[float],
                 magie: MagieNivele, taux_cout_caste: list[float], taux_latence_caste: list[float]):
        EntiteeNivele.__init__(self, nom)
        self.fantome = fantome
        self.poids = poids
        self.frottements = frottements
        self.magie = magie
        self.taux_cout_caste = taux_cout_caste
        self.taux_latence_caste = taux_latence_caste

    def check(self) -> bool:
        return (all([poids >= 0 for poids in self.poids]) and
                all([frottements >= 0 for frottements in self.frottements]) and
                all([taux >= 0 for taux in self.taux_cout_caste]) and
                all([taux >= 0 for taux in self.taux_latence_caste]))
    
    def stringify(self) -> str:
        return f"""{{
    "type": "parchemin magie",
    "nivele": true,
    "nom": "{self.nom}",
    "fantome": {self.fantome},
    "poids": {self.poids},
    "frottements": {self.frottements},
    "magie": "{self.magie}",
    "taux_cout_caste": {self.taux_cout_caste},
    "taux_latence_caste": {self.taux_latence_caste}
}}"""
    
    @classmethod
    def parse(cls, json: str):
        dictionnaire = parse(json)
        return cls(dictionnaire["nom"], dictionnaire["fantome"], dictionnaire["poids"], dictionnaire["frottements"], dictionnaire["magie"], dictionnaire["taux_cout_caste"], dictionnaire["taux_latence_caste"])

    def make(self, niveau:int) -> type[mdl.ParcheminImpregne]:
        """Retourne le parchemin correspondant."""
        class ParcheminMagieNiveau(mdl.ParcheminImpregne, mdl.Nomme):
            """Un parchemin avec une magie préécrite."""
            poids = self.poids[niveau]
            frottements = self.frottements[niveau]
            magie = self.magie.remake(niveau)
            taux_cout_caste = self.taux_cout_caste[niveau]
            taux_latence_caste = self.taux_latence_caste[niveau]
            fantome = self.fantome
            def __init__(self, position: crt.Position):
                mdl.ParcheminImpregne.__init__(self, position)
                self.action_portee = self.magie(mdl.SKILL_ISSUE, mdl.NOONE)
        ParcheminMagieNiveau.nom = self.nom
        ParcheminMagieNiveau.niveau = niveau
        return ParcheminMagieNiveau

class Parchemins(StockageCategorieNivelee):
    """Les informations des parchemins."""
    nom = "Parchemins"
    titre_nouveau = "Nouveau parchemin"
    description = "Les parchemins sont des items consommables qui s'activent avec du mana. Les parchemins vierges n'ont pas encore d'effet placé, tandis que les parchemins préécrits ont besoin d'un effet à la création."
    avertissement = "Il existe déjà un parchemin avec ce nom !"
    elements = {
        "parchemin vierge": ParcheminViergeNivele,
        "parchemin magie": ParcheminMagieNivele
    }
