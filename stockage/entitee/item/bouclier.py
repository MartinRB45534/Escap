"""
Fichier contenant la classe de stockage des boucliers.
"""

from __future__ import annotations
from json import loads as parse

import modele as mdl

from ...stockage import StockageCategorieNivelee
from ..entitee import EntiteeNivele
from ...espece import Especes, Espece

class BouclierNivele(EntiteeNivele):
    """Un bouclier tout simple."""

    champs = {
            "fantome": bool,
            "poids": float,
            "frottements": float,
            "bloque_quantite": bool,
            "degats_bloques": float,
            "bloque_proportion": bool,
            "taux_degats": float,
            "tribal": bool,
            "_espece": Especes,
            "_taux_stats": float
        }

    niveles = {
            "fantome": False,
            "poids": True,
            "frottements": True,
            "bloque_quantite": False,
            "degats_bloques": True,
            "bloque_proportion": False,
            "taux_degats": True,
            "_espece": False,
            "_taux_stats": True
        }

    acceptors = {
            "fantome": lambda _: True,
            "poids": lambda poids: float(poids) >= 0,
            "frottements": lambda frottements: float(frottements) >= 0,
            "bloque_quantite": lambda _: True,
            "degats_bloques": lambda degats_bloques: float(degats_bloques) >= 0,
            "bloque_proportion": lambda _: True,
            "taux_degats": lambda taux_degats: float(taux_degats) >= 0,
            "tribal": lambda _: True,
            "_espece": lambda espece: espece in Especes.global_.trouve_stockage(Especes).all_noms,
            "_taux_stats": lambda taux_stats: float(taux_stats) >= 0
        }

    avertissements = {
            "fantome": "Cet avertissement n'est pas censé apparaître.",
            "poids": "Le poids doit être positif.",
            "frottements": "Le frottement doit être positif.",
            "bloque_quantite": "Cet avertissement n'est pas censé apparaître.",
            "degats_bloques": "La quantité de dégats bloqués doit être positive.",
            "bloque_proportion": "Cet avertissement n'est pas censé apparaître.",
            "taux_degats": "Le taux de dégats bloqué doit être positif.",
            "tribal": "Cet avertissement n'est pas censé apparaître non plus.",
            "_espece": "Il faut choisir une espèce existante (peut-être qu'il n'en existe pas).",
            "_taux_stats": "Le taux de stats doit être positif."
        }

    conditionnels = {
            "fantome": lambda dictionnaire: True,
            "poids": lambda dictionnaire: True,
            "frottements": lambda dictionnaire: True,
            "bloque_quantite": lambda dictionnaire: True,
            "degats_bloques": lambda dictionnaire: dictionnaire["bloque_quantite"]=="True",
            "bloque_proportion": lambda dictionnaire: True,
            "taux_degats": lambda dictionnaire: dictionnaire["bloque_proportion"]=="True",
            "tribal": lambda dictionnaire: True,
            "_espece": lambda dictionnaire: dictionnaire["tribal"]=="True",
            "_taux_stats": lambda dictionnaire: dictionnaire["tribal"]=="True"
        }

    multiple = {
            "fantome": False,
            "poids": False,
            "frottements": False,
            "bloque_quantite": False,
            "degats_bloques": False,
            "bloque_proportion": False,
            "taux_degats": False,
            "tribal": False,
            "_espece": False,
            "_taux_stats": False
        }

    def __init__(self, nom: str, fantome: bool,
                 poids:list[float], frottements:list[float], bloque_quantite:bool,
                 degats_bloques:list[float], bloque_proportion:bool,
                 taux_degats:list[float], tribal: bool, espece: Espece|None,
                 _taux_stats: list[int]):
        EntiteeNivele.__init__(self, nom)
        self.fantome = fantome
        self.poids = poids
        self.frottements = frottements
        self.bloque_quantite = bloque_quantite
        self.degats_bloques = degats_bloques
        self.bloque_proportion = bloque_proportion
        self.taux_degats = taux_degats
        self.tribal = tribal
        self._espece = espece
        self._taux_stats = _taux_stats

    def check(self) -> bool:
        return (all([poid >= 0 for poid in self.poids]) and
                all([frottement >= 0 for frottement in self.frottements]) and
                all(degats_bloques >= 0 for degats_bloques in self.degats_bloques) and
                all(taux_degats >= 0 for taux_degats in self. taux_degats) and
                (not self.tribal or bool(self._espece)) and
                all([taux >= 0 for taux in self._taux_stats]))

    def stringify(self) -> str:
        return f"""{{
    "type": "bouclier",
    "nivele": true,
    "nom": "{self.nom}",
    "fantome": {self.fantome},
    "poids": {self.poids},
    "frottements": {self.frottements},
    "bloque_quantite": {self.bloque_quantite},
    "degats_bloques": {self.degats_bloques},
    "bloque_proportion": {self.bloque_proportion},
    "taux_degats": {self.taux_degats},
    "tribal": {self.tribal},
    "_espece": "{self._espece}",
    "_taux_stats": {self._taux_stats}
}}"""

    @classmethod
    def parse(cls, json: str):
        """Parse un json en BouclierNivele."""
        dictionnaire = parse(json)
        return BouclierNivele(dictionnaire["nom"], dictionnaire["fantome"], dictionnaire["poids"], dictionnaire["frottements"], dictionnaire["bloque_quantite"], dictionnaire["degats_bloques"], dictionnaire["bloque_proportion"], dictionnaire["taux_degats"], dictionnaire["tribal"], dictionnaire["_espece"], dictionnaire["_taux_stats"])

    def make(self, niveau: int):
        """Crée un BouclierSimple à partir de l'instance."""
        classe = mdl.boucliers[(self.tribal,)]
        if self.tribal:
            assert self._espece, "Erreur : il faut une espèce pour un équipement tribal !"
            _espece = self._espece.make()
            assert isinstance(_espece, mdl.Espece), f"Erreur : {self._espece} n'est pas une espèce !?"
        else:
            _espece = None
        class BouclierNiveau(classe, mdl.Nomme):
            """Une arme."""
            poids = self.poids[niveau]
            frottements = self.frottements[niveau]
            bloque_quantite = self.bloque_quantite
            degats_bloques = self.degats_bloques[niveau]
            bloque_proportion = self.bloque_proportion
            taux_degats = self.taux_degats[niveau]
            espece = _espece
            taux = self._taux_stats[niveau] if self.tribal else 0
            fantome = self.fantome
        BouclierNiveau.nom = self.nom
        BouclierNiveau.niveau = niveau
        return BouclierNiveau

class Boucliers(StockageCategorieNivelee):
    """Les informations des boucliers."""
    nom = "Boucliers"
    titre_nouveau = "Nouveau bouclier"
    description = "Les boucliers sont destinés à être équippés. Ils permettent de défendre une zone contre les attaques."
    avertissement = "Il existe déjà un bouclier avec ce nom !"
    elements = {
        "Bouclier": BouclierNivele
    }
