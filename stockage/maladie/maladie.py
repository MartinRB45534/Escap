"""
Fichier contenant la classe de stockage des armes.
"""

from __future__ import annotations
from json import loads as parse

import modele as mdl

from ..stockage import StockageCategorieNivelee, StockageNivele
from .famille import FamillesMaladies

class MaladieNivele(StockageNivele):
    """Une maladie."""

    champs = {
            "_famille": FamillesMaladies,
            "contagiosite": float,
            "infectabilite": float,
            "persistence": float,
            "distance": float,
            "virulence": float,
            "perte_contagiosite": float,
            "perte_infectabilite": float,
            "perte_persistence": float,
            "perte_contagiosite_famille": float,
            "perte_infectabilite_famille": float,
            "perte_persistence_famille": float,
            "guerit_sans_contagiosite": bool,
            "guerit_sans_infectabilite": bool,
            "guerit_sans_persistence": bool,
            "mixte": bool,
            "transmissibilite": float,
            "portee": float,
            "duree_max": float,
            "tirgnonose": bool,
            "fibaluse": bool,
            "fibaluse_force": bool,
            "fibaluse_vision": bool,
            "fibaluse_pv": bool,
            "fibaluse_pm": bool,
            "fibaluse_vitesse": bool,
            "fibaluse_affinite": bool,
            "terre": bool,
            "feu": bool,
            "glace": bool,
            "ombre": bool,
            "ibsutiomialgie": bool,
        }

    niveles = {
            "contagiosite": True,
            "infectabilite": True,
            "persistence": True,
            "distance": True,
            "virulence": True,
            "perte_contagiosite": True,
            "perte_infectabilite": True,
            "perte_persistence": True,
            "perte_contagiosite_famille": True,
            "perte_infectabilite_famille": True,
            "perte_persistence_famille": True,
            "transmissibilite": True,
            "portee": True,
            "duree_max": True,
        }

    acceptors = {
            "_famille": lambda famille: famille in FamillesMaladies.global_.trouve_stockage(FamillesMaladies).all_noms,
            "contagiosite": lambda contagiosite: float(contagiosite) >= 0,
            "infectabilite": lambda infectabilite: float(infectabilite) >= 0,
            "persistence": lambda persistence: float(persistence) >= 0,
            "distance": lambda distance: float(distance) >= 0,
            "virulence": lambda virulence: float(virulence) >= 0,
            "perte_contagiosite": lambda perte_contagiosite: float(perte_contagiosite) >= 0,
            "perte_infectabilite": lambda perte_infectabilite: float(perte_infectabilite) >= 0,
            "perte_persistence": lambda perte_persistence: float(perte_persistence) >= 0,
            "perte_contagiosite_famille": lambda perte_contagiosite_famille: float(perte_contagiosite_famille) >= 0,
            "perte_infectabilite_famille": lambda perte_infectabilite_famille: float(perte_infectabilite_famille) >= 0,
            "perte_persistence_famille": lambda perte_persistence_famille: float(perte_persistence_famille) >= 0,
            "transmissibilite": lambda transmissibilite: float(transmissibilite) >= 0,
            "portee": lambda portee: float(portee) >= 0,
            "duree_max": lambda duree_max: float(duree_max) >= 0,
        }

    avertissements = {
            "_famille": "Il faut choisir une famille existante (peut-être qu'il n'en existe pas encore).",
            "contagiosite": "La contagiosité doit être positive.",
            "infectabilite": "L'infectabilité doit être positive.",
            "persistence": "La persistance doit être positive.",
            "distance": "La distance doit être positive.",
            "virulence": "La virulence doit être positive.",
            "perte_contagiosite": "La perte de contagiosité doit être positive.",
            "perte_infectabilite": "La perte d'infectabilité doit être positive.",
            "perte_persistence": "La perte de persistance doit être positive.",
            "perte_contagiosite_famille": "La perte de contagiosité de famille doit être positive.",
            "perte_infectabilite_famille": "La perte d'infectabilité de famille doit être positive.",
            "perte_persistence_famille": "La perte de persistance de famille doit être positive.",
            "transmissibilite": "La transmissibilité doit être positive.",
            "portee": "La portée doit être positive.",
            "duree_max": "La durée maximale doit être positive.",
        }

    conditionnels = {
            "transmissibilite": lambda dictionnaire: dictionnaire["mixte"] == "True",
            "portee": lambda dictionnaire: dictionnaire["mixte"] == "True",
            "duree_max": lambda dictionnaire: dictionnaire["mixte"] == "True",
            "fibaluse_force": lambda dictionnaire: dictionnaire["fibaluse"] == "False",
            "fibaluse_vision": lambda dictionnaire: dictionnaire["fibaluse"] == "False",
            "fibaluse_pv": lambda dictionnaire: dictionnaire["fibaluse"] == "False",
            "fibaluse_pm": lambda dictionnaire: dictionnaire["fibaluse"] == "False",
            "fibaluse_vitesse": lambda dictionnaire: dictionnaire["fibaluse"] == "False",
            "fibaluse_affinite": lambda dictionnaire: dictionnaire["fibaluse"] == "False",
            "terre": lambda dictionnaire: dictionnaire["fibaluse"] == "True",
            "feu": lambda dictionnaire: dictionnaire["fibaluse"] == "True",
            "glace": lambda dictionnaire: dictionnaire["fibaluse"] == "True",
            "ombre": lambda dictionnaire: dictionnaire["fibaluse"] == "True",
        }

    def __init__(self, nom: str, famille: str, contagiosite: list[float],
                 infectabilite: list[float], persistence: list[float], distance: list[float],
                 virulence: list[float], perte_contagiosite: list[float],
                 perte_infectabilite: list[float], perte_persistence: list[float],
                 perte_contagiosite_famille: list[float], perte_infectabilite_famille: list[float],
                 perte_persistence_famille: list[float], guerit_sans_contagiosite: bool,
                 guerit_sans_infectabilite: bool, guerit_sans_persistence: bool, mixte: bool,
                 transmissibilite: list[float], portee: list[float], duree_max: list[float],
                 tirgnonose: bool, fibaluse: bool, fibaluse_force: bool, fibaluse_vision: bool,
                 fibaluse_pv: bool, fibaluse_pm: bool, fibaluse_vitesse: bool,
                 fibaluse_affinite: bool, terre: bool, feu: bool, glace: bool, ombre: bool,
                 ibsutiomialgie: bool):
        StockageNivele.__init__(self, nom)
        self.famille = famille
        self.contagiosite = contagiosite
        self.infectabilite = infectabilite
        self.persistence = persistence
        self.distance = distance
        self.virulence = virulence
        self.perte_contagiosite = perte_contagiosite
        self.perte_infectabilite = perte_infectabilite
        self.perte_persistence = perte_persistence
        self.perte_contagiosite_famille = perte_contagiosite_famille
        self.perte_infectabilite_famille = perte_infectabilite_famille
        self.perte_persistence_famille = perte_persistence_famille
        self.guerit_sans_contagiosite = guerit_sans_contagiosite
        self.guerit_sans_infectabilite = guerit_sans_infectabilite
        self.guerit_sans_persistence = guerit_sans_persistence
        self.mixte = mixte
        self.transmissibilite = transmissibilite
        self.portee = portee
        self.duree_max = duree_max
        self.tirgnonose = tirgnonose
        self.fibaluse = fibaluse
        self.fibaluse_force = fibaluse_force
        self.fibaluse_vision = fibaluse_vision
        self.fibaluse_pv = fibaluse_pv
        self.fibaluse_pm = fibaluse_pm
        self.fibaluse_vitesse = fibaluse_vitesse
        self.fibaluse_affinite = fibaluse_affinite
        self.terre = terre
        self.feu = feu
        self.glace = glace
        self.ombre = ombre
        self.ibsutiomialgie = ibsutiomialgie

    def check(self) -> bool:
        return (self.famille in FamillesMaladies.global_.trouve_stockage(FamillesMaladies).all_noms and
                all([contagiosite >= 0 for contagiosite in self.contagiosite]) and
                all([infectabilite >= 0 for infectabilite in self.infectabilite]) and
                all([persistence >= 0 for persistence in self.persistence]) and
                all([distance >= 0 for distance in self.distance]) and
                all([virulence >= 0 for virulence in self.virulence]) and
                all([perte_contagiosite >= 0 for perte_contagiosite in self.perte_contagiosite]) and
                all([perte_infectabilite >= 0 for perte_infectabilite in self.perte_infectabilite]) and
                all([perte_persistence >= 0 for perte_persistence in self.perte_persistence]) and
                all([perte_contagiosite_famille >= 0 for perte_contagiosite_famille in self.perte_contagiosite_famille]) and
                all([perte_infectabilite_famille >= 0 for perte_infectabilite_famille in self.perte_infectabilite_famille]) and
                all([perte_persistence_famille >= 0 for perte_persistence_famille in self.perte_persistence_famille]) and
                all([transmissibilite >= 0 for transmissibilite in self.transmissibilite]) and
                all([portee >= 0 for portee in self.portee]) and
                all([duree_max >= 0 for duree_max in self.duree_max]) and
                not (self.fibaluse and (self.fibaluse_force or self.fibaluse_vision or self.fibaluse_pv or self.fibaluse_pm or self.fibaluse_vitesse or self.fibaluse_affinite)))

    def stringify(self) -> str:
        return f"""{{
    "type": "arme",
    "nivele": true,
    "nom": "{self.nom}",
    "_famille": "{self.famille}",
    "contagiosite": {self.contagiosite},
    "infectabilite": {self.infectabilite},
    "persistence": {self.persistence},
    "distance": {self.distance},
    "virulence": {self.virulence},
    "perte_contagiosite": {self.perte_contagiosite},
    "perte_infectabilite": {self.perte_infectabilite},
    "perte_persistence": {self.perte_persistence},
    "perte_contagiosite_famille": {self.perte_contagiosite_famille},
    "perte_infectabilite_famille": {self.perte_infectabilite_famille},
    "perte_persistence_famille": {self.perte_persistence_famille},
    "guerit_sans_contagiosite": {self.guerit_sans_contagiosite},
    "guerit_sans_infectabilite": {self.guerit_sans_infectabilite},
    "guerit_sans_persistence": {self.guerit_sans_persistence},
    "mixte": {self.mixte},
    "transmissibilite": {self.transmissibilite},
    "portee": {self.portee},
    "duree_max": {self.duree_max},
    "tirgnonose": {self.tirgnonose},
    "fibaluse": {self.fibaluse},
    "fibaluse_force": {self.fibaluse_force},
    "fibaluse_vision": {self.fibaluse_vision},
    "fibaluse_pv": {self.fibaluse_pv},
    "fibaluse_pm": {self.fibaluse_pm},
    "fibaluse_vitesse": {self.fibaluse_vitesse},
    "fibaluse_affinite": {self.fibaluse_affinite},
    "terre": {self.terre},
    "feu": {self.feu},
    "glace": {self.glace},
    "ombre": {self.ombre},
    "ibsutiomialgie": {self.ibsutiomialgie}
}}"""

    @classmethod
    def parse(cls, json: str):
        """Parse un json en ArmeNivele."""
        dictionnaire = parse(json)
        return MaladieNivele(dictionnaire["nom"], dictionnaire["_famille"], dictionnaire["contagiosite"], dictionnaire["infectabilite"], dictionnaire["persistence"], dictionnaire["distance"], dictionnaire["virulence"], dictionnaire["perte_contagiosite"], dictionnaire["perte_infectabilite"], dictionnaire["perte_persistence"], dictionnaire["perte_contagiosite_famille"], dictionnaire["perte_infectabilite_famille"], dictionnaire["perte_persistence_famille"], dictionnaire["guerit_sans_contagiosite"], dictionnaire["guerit_sans_infectabilite"], dictionnaire["guerit_sans_persistence"], dictionnaire["mixte"], dictionnaire["transmissibilite"], dictionnaire["portee"], dictionnaire["duree_max"], dictionnaire["tirgnonose"], dictionnaire["fibaluse"], dictionnaire["fibaluse_force"], dictionnaire["fibaluse_vision"], dictionnaire["fibaluse_pv"], dictionnaire["fibaluse_pm"], dictionnaire["fibaluse_vitesse"], dictionnaire["fibaluse_affinite"], dictionnaire["terre"], dictionnaire["feu"], dictionnaire["glace"], dictionnaire["ombre"], dictionnaire["ibsutiomialgie"])

    def make(self, niveau: int) -> type[mdl.Maladie]:
        """Crée une ArmeSimple à partir de l'instance."""
        classe = mdl.maladies[(self.tirgnonose, self.fibaluse, self.fibaluse_force, self.fibaluse_vision, self.fibaluse_pv, self.fibaluse_pm, self.fibaluse_vitesse, self.fibaluse_affinite, self.ibsutiomialgie, self.mixte)]
        famille_instance = FamillesMaladies.global_.trouve_stockage(FamillesMaladies).make(self.famille)
        assert isinstance(famille_instance, mdl.FamilleMaladie), f"Erreur : {self.famille} n'est pas une famille !?"
        class MaladieNiveau(classe, mdl.Nomme):
            """Une maladie."""
            famille = famille_instance
            contagiosite = self.contagiosite[niveau]
            infectabilite = self.infectabilite[niveau]
            persistence = self.persistence[niveau]
            distance = self.distance[niveau]
            virulence = self.virulence[niveau]
            perte_contagiosite = self.perte_contagiosite[niveau]
            perte_infectabilite = self.perte_infectabilite[niveau]
            perte_persistence = self.perte_persistence[niveau]
            perte_contagiosite_famille = self.perte_contagiosite_famille[niveau]
            perte_infectabilite_famille = self.perte_infectabilite_famille[niveau]
            perte_persistence_famille = self.perte_persistence_famille[niveau]
            guerit_sans_contagiosite = self.guerit_sans_contagiosite
            guerit_sans_infectabilite = self.guerit_sans_infectabilite
            guerit_sans_persistence = self.guerit_sans_persistence
            transmissibilite = self.transmissibilite[niveau] if self.mixte else 0
            portee = self.portee[niveau] if self.mixte else 0
            duree_max = self.duree_max[niveau] if self.mixte else 0
            elements: set[mdl.Element] = set()
            if self.terre:
                elements.add(mdl.Element.TERRE)
            if self.feu:
                elements.add(mdl.Element.FEU)
            if self.glace:
                elements.add(mdl.Element.GLACE)
            if self.ombre:
                elements.add(mdl.Element.OMBRE)
        MaladieNiveau.nom = self.nom
        MaladieNiveau.niveau = niveau
        return MaladieNiveau

class Maladies(StockageCategorieNivelee):
    """Les informations des maladies."""
    nom = "Maladies"
    titre_nouveau = "Nouvelle maladie"
    description = "Les maladies sont des effets qui affectent les agissants. Je déconseille de mélanger les différents types de maladies (tirgnonose, fibaluse, ibsutiomialgie) mais c'est possible."
    avertissement = "Il existe déjà une maladie avec ce nom !"
    elements = {
        "Maladie": MaladieNivele
    }
