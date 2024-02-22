"""
Fichier contenant la classe de stockage des parchemins.
"""

from __future__ import annotations
from json import loads as parse

import modele as mdl

from ...stockage import StockageCategorieNivelee
from ...magie import Magies, MagieNivele
from ..entitee import EntiteeNivele

class ParcheminViergeNivele(EntiteeNivele):
    """Les informations d'un parchemin vierge."""

    champs = {
            "fantome": bool,
            "latence_impregne": float,
            "taux_cout_caste": float,
            "taux_cout_impregne": float,
            "taux_latence_caste": float,
            "taux_latence_impregne": float
        }

    niveles = {
            "fantome": False,
            "latence_impregne": True,
            "taux_cout_caste": True,
            "taux_cout_impregne": True,
            "taux_latence_caste": True,
            "taux_latence_impregne": True
        }

    acceptors = {
            "fantome": lambda _: True,
            "latence_impregne": lambda latence: float(latence) >= 0,
            "taux_cout_caste": lambda taux: float(taux) >= 0,
            "taux_cout_impregne": lambda taux: float(taux) >= 0,
            "taux_latence_caste": lambda taux: float(taux) >= 0,
            "taux_latence_impregne": lambda taux: float(taux) >= 0
        }

    avertissements = {
            "fantome": "Please file a bug report.",
            "latence_impregne": "La latence d'impregnation doit être positive.",
            "taux_cout_caste": "Le taux de cout de caste doit être positif.",
            "taux_cout_impregne": "Le taux de cout d'impregnation doit être positif.",
            "taux_latence_caste": "Le taux de latence de caste doit être positif.",
            "taux_latence_impregne": "Le taux de latence d'impregnation doit être positif."
        }

    conditionnels = {
            "fantome": lambda dictionnaire: True,
            "latence_impregne": lambda dictionnaire: True,
            "taux_cout_caste": lambda dictionnaire: True,
            "taux_cout_impregne": lambda dictionnaire: True,
            "taux_latence_caste": lambda dictionnaire: True,
            "taux_latence_impregne": lambda dictionnaire: True
        }

    multiple = {
            "fantome": False,
            "latence_impregne": False,
            "taux_cout_caste": False,
            "taux_cout_impregne": False,
            "taux_latence_caste": False,
            "taux_latence_impregne": False
        }

    def __init__(self, nom: str, fantome: bool, latence_impregne:list[float],
                 taux_cout_caste:list[float], taux_cout_impregne:list[float],
                 taux_latence_caste:list[float], taux_latence_impregne:list[float]):
        EntiteeNivele.__init__(self, nom)
        self.fantome = fantome
        self.latence_impregne = latence_impregne
        self.taux_cout_caste = taux_cout_caste
        self.taux_cout_impregne = taux_cout_impregne
        self.taux_latence_caste = taux_latence_caste
        self.taux_latence_impregne = taux_latence_impregne

    def check(self) -> bool:
        return (len(self.latence_impregne) == 10 and
                len(self.taux_cout_caste) == 10 and
                len(self.taux_cout_impregne) == 10 and
                len(self.taux_latence_caste) == 10 and
                len(self.taux_latence_impregne) == 10 and
                all([latence >= 0 for latence in self.latence_impregne]) and
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
    "latence_impregne": {self.latence_impregne},
    "taux_cout_caste": {self.taux_cout_caste},
    "taux_cout_impregne": {self.taux_cout_impregne},
    "taux_latence_caste": {self.taux_latence_caste},
    "taux_latence_impregne": {self.taux_latence_impregne}
}}"""

    @classmethod
    def parse(cls, json: str):
        dictionnaire = parse(json)
        return cls(dictionnaire["nom"], dictionnaire["fantome"], dictionnaire["latence_impregne"], dictionnaire["taux_cout_caste"], dictionnaire["taux_cout_impregne"], dictionnaire["taux_latence_caste"], dictionnaire["taux_latence_impregne"])

    def make(self, niveau:int) -> mdl.ParcheminVierge:
        """Retourne le parchemin correspondant."""
        impregne = mdl.Impregne(mdl.NOONE, self.latence_impregne[niveau], mdl.NOWRITTING,
                             self.taux_cout_impregne[niveau], self.taux_cout_caste[niveau],
                             self.taux_latence_impregne[niveau], self.taux_latence_caste[niveau])
        parchemin = mdl.ParcheminVierge(mdl.NOWHERE, impregne)
        parchemin.nom = self.nom
        parchemin.fantome = self.fantome
        return parchemin
    
class ParcheminMagieNivele(EntiteeNivele):
    """Les informations d'un parchemin préécrit."""

    champs = {
            "fantome": bool,
            "magie": Magies,
            "taux_cout_caste": float,
            "taux_latence_caste": float
        }
    
    niveles = {
            "fantome": False,
            "magie": False,
            "taux_cout_caste": True,
            "taux_latence_caste": True
        }
    
    acceptors = {
            "fantome": lambda _: True,
            "magie": lambda magie: magie in Magies.global_.trouve_stockage(Magies).all_noms,
            "taux_cout_caste": lambda taux: float(taux) >= 0,
            "taux_latence_caste": lambda taux: float(taux) >= 0
        }
    
    avertissements = {
            "fantome": "Please file a bug report.",
            "magie": "La magie n'existe pas.",
            "taux_cout_caste": "Le taux de cout de caste doit être positif.",
            "taux_latence_caste": "Le taux de latence de caste doit être positif."
        }
    
    conditionnels = {
            "fantome": lambda dictionnaire: True,
            "magie": lambda dictionnaire: True,
            "taux_cout_caste": lambda dictionnaire: True,
            "taux_latence_caste": lambda dictionnaire: True
        }
    
    multiple = {
            "fantome": False,
            "magie": False,
            "taux_cout_caste": False,
            "taux_latence_caste": False
        }
    
    def __init__(self, nom: str, fantome: bool, magie: MagieNivele, taux_cout_caste: float, taux_latence_caste: float):
        EntiteeNivele.__init__(self, nom)
        self.fantome = fantome
        self.magie = magie
        self.taux_cout_caste = taux_cout_caste
        self.taux_latence_caste = taux_latence_caste

    def check(self) -> bool:
        return (self.taux_cout_caste >= 0 and
                self.taux_latence_caste >= 0)
    
    def stringify(self) -> str:
        return f"""{{
    "type": "parchemin magie",
    "nivele": true,
    "nom": "{self.nom}",
    "fantome": {self.fantome},
    "magie": "{self.magie}",
    "taux_cout_caste": {self.taux_cout_caste},
    "taux_latence_caste": {self.taux_latence_caste}
}}"""
    
    @classmethod
    def parse(cls, json: str):
        dictionnaire = parse(json)
        return cls(dictionnaire["nom"], dictionnaire["fantome"], dictionnaire["magie"], dictionnaire["taux_cout_caste"], dictionnaire["taux_latence_caste"])
    
    def make(self, niveau:int) -> mdl.ParcheminVierge:
        """Retourne le parchemin correspondant."""
        magie = self.magie.make(niveau)
        parchemin = mdl.ParcheminVierge(mdl.NOWHERE, magie.genere(mdl.SKILL_ISSUE, mdl.NOONE, niveau))
        parchemin.nom = self.nom
        parchemin.fantome = self.fantome
        return parchemin

class Parchemins(StockageCategorieNivelee):
    """Les informations des parchemins."""
    nom = "Parchemins"
    titre_nouveau = "Nouveau parchemin"
    description = "Les parchemins sont des items consommables qui s'activent avec du mana. Les parchemins vierges n'ont pas encore d'effet placé, tandis que les parchemins préécrits ont besoin d'un effet à la création."
    avertissement = "Il existe déjà un parchemin avec ce nom !"
    elements = {
        "parchemin vierge": ParcheminViergeNivele
    }
