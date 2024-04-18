"""
Fichier contenant la classe de stockage des armes.
"""

from __future__ import annotations
from json import loads as parse
from enum import StrEnum

import modele as mdl

from ...stockage import StockageCategorieNivelee
from ..entitee import EntiteeNivele
from ...espece import Especes, Espece

class ArmeNivele(EntiteeNivele):
    """Une arme toute simple."""

    champs = {
            "fantome": bool,
            "element": mdl.Element,
            "poids": float,
            "frottements": float,
            "type_arme": StrEnum("type_arme",
                                 {"Epee": "Epee",
                                  "Lance": "Lance",
                                  "Autre": "Autre"}),
            "portee": float,
            "tranchant": float,
            "tribal": bool,
            "_espece": Especes,
            "_taux_stats": float,
        }

    niveles = {
            "poids": True,
            "frottements": True,
            "portee": True,
            "tranchant": True,
            "_taux_stats": True,
        }

    acceptors = {
            "poids": lambda poids: float(poids) >= 0,
            "frottements": lambda frottements: float(frottements) >= 0,
            "portee": lambda portee: float(portee) >= 0,
            "tranchant": lambda tranchant: float(tranchant) >= 0,
            "_espece": lambda espece: espece in Especes.global_.trouve_stockage(Especes).all_noms,
            "_taux_stats": lambda taux_stats: float(taux_stats) >= 0,
        }

    avertissements = {
            "poids": "Le poids doit être positif.",
            "frottements": "Le frottement doit être positif.",
            "portee": "La portée doit être positive.",
            "tranchant": "Le tranchant doit être positif.",
            "_espece": "Il faut choisir une espèce existante (peut-être qu'il n'en existe pas).",
            "_taux_stats": "Le taux de stats doit être positif.",
        }

    conditionnels = {
            "_espece": lambda dictionnaire: dictionnaire["tribal"]=="True",
            "_taux_stats": lambda dictionnaire: dictionnaire["tribal"]=="True"
        }

    def __init__(self, nom: str, fantome: bool,
                 element:mdl.Element, poids: list[float], frottements: list[float],
                 type_arme:str, portee:list[float], tranchant:list[float],
                 tribal: bool, espece: Espece|None, _taux_stats: list[int]):
        EntiteeNivele.__init__(self, nom)
        self.fantome = fantome
        self.element = element
        self.poids = poids
        self.frottements = frottements
        self.type_arme = type_arme
        self.portee = portee
        self.tranchant = tranchant
        self.tribal = tribal
        self._espece = espece
        self._taux_stats = _taux_stats

    def check(self) -> bool:
        return (all([poid >= 0 for poid in self.poids]) and
                all([frottement >= 0 for frottement in self.frottements]) and
                self.type_arme in ["Epee", "Lance", "Autre"] and
                all(portee >= 0 for portee in self.portee) and
                all(tranchant >= 0 for tranchant in self.tranchant) and
                (not self.tribal or bool(self._espece)) and
                all([taux >= 0 for taux in self._taux_stats]))

    def stringify(self) -> str:
        return f"""{{
    "type": "arme",
    "nivele": true,
    "nom": "{self.nom}",
    "fantome": {self.fantome},
    "element": "{self.element}",
    "poids": {self.poids},
    "frottements": {self.frottements},
    "type_arme": "{self.type_arme}",
    "portee": {self.portee},
    "tranchant": {self.tranchant},
    "tribal": {self.tribal},
    "_espece": "{self._espece}",
    "_taux_stats": {self._taux_stats}
}}"""

    @classmethod
    def parse(cls, json: str):
        """Parse un json en ArmeNivele."""
        dictionnaire = parse(json)
        return ArmeNivele(dictionnaire["nom"], dictionnaire["fantome"], mdl.Element(dictionnaire["element"]), dictionnaire["poids"], dictionnaire["frottements"], dictionnaire["type_arme"], dictionnaire["portee"], dictionnaire["tranchant"], dictionnaire["tribal"], dictionnaire["_espece"], dictionnaire["_taux_stats"])

    def make(self, niveau: int):
        """Crée une ArmeSimple à partir de l'instance."""
        classe = mdl.armes[(self.type_arme, self.tribal)]
        if self.tribal:
            assert self._espece, "Erreur : il faut une espèce pour un équipement tribal !"
            _espece = self._espece.make()
            assert isinstance(_espece, mdl.Espece), f"Erreur : {self._espece} n'est pas une espèce !?"
        else:
            _espece = None
        class ArmeNiveau(classe, mdl.Nomme):
            """Une arme."""
            poids = self.poids[niveau]
            frottements = self.frottements[niveau]
            element = self.element
            tranchant = self.tranchant[niveau]
            portee = self.portee[niveau]
            espece = _espece
            taux = self._taux_stats[niveau] if self.tribal else 0
            fantome = self.fantome
        ArmeNiveau.nom = self.nom
        ArmeNiveau.niveau = niveau
        return ArmeNiveau

class Armes(StockageCategorieNivelee):
    """Les informations des armes."""
    nom = "Armes"
    titre_nouveau = "Nouvelle arme"
    description = "Les armes sont destinés à être équippées. Elles permettent d'effectuer des attaques différentes. Les épées et les lances en particulier interagissent avec certains skills."
    avertissement = "Il existe déjà une arme avec ce nom !"
    elements = {
        "Arme": ArmeNivele
    }
