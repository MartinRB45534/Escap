"""
Fichier contenant la classe de stockage des potions.
"""

from __future__ import annotations
from json import loads as parse
from enum import StrEnum

import modele as mdl

from ...stockage import StockageCategorieNivelee
from ...maladie import Maladies, FamillesMaladies
from ..entitee import EntiteeNivele

class PotionNivele(EntiteeNivele):
    """Les informations d'un potion vierge."""

    champs = {
            "fantome": bool,
            "poids": float,
            "frottements": float,
            "latence_boit": float,
            "effet": StrEnum("effet",
                             {"maladie": "Maladie (à créer séparément)",
                              "poison": "Poison",
                              "soin": "Soin",
                              "antidote": "Antidote (soigne tous les poisons)",
                              "medicament": "Médicament (soigne une maladie ou une famille de maladies)",
                              "vaccin": "Vaccin (immunise contre une maladie ou une famille de maladies)",
                              "boost": "Boost (augmente une statistique)",
                             }),
            "mixte": bool,
            "portee": float,
            "duree_max": float,
            "maladie": Maladies,
            "famille_maladie": FamillesMaladies,
            "progression": float,
            "degats_max": float,
            "gain_pv": float,
            "immunite": float,
            "statistique boostee": StrEnum("statistique boostee",
                                             {"force": "Force (attaque)",
                                              "vision": "Vision (champ de vision)",
                                              "pv": "PV (régénération)",
                                              "pm": "PM (régénération)",
                                              "vitesse": "Vitesse (actions)",
                                              "affinite": "Affinité à un élément",
                                              "affinites": "Affinités à plusieurs éléments",
                                              "stats": "Toutes les statistiques",
                                             }),
            "element": mdl.Element,
            "terre": bool,
            "feu": bool,
            "glace": bool,
            "ombre": bool,
            "multiplicateur": float,
        }

    niveles = {
            "poids": True,
            "frottements": True,
            "latence_boit": True,
            "portee": True,
            "duree_max": True,
            "progression": True,
            "degats_max": True,
            "gain_pv": True,
            "immunite": True,
            "multiplicateur": True,
        }

    acceptors = {
            "poids": lambda poids: float(poids) >= 0,
            "frottements": lambda frottements: float(frottements) >= 0,
            "latence_boit": lambda latence_boit: float(latence_boit) >= 0,
            "portee": lambda portee: float(portee) > 0,
            "duree_max": lambda duree_max: float(duree_max) > 0,
            "maladie": lambda maladie: maladie in Maladies.global_.trouve_stockage(Maladies).all_noms,
            "famille_maladie": lambda famille_maladie: famille_maladie in FamillesMaladies.global_.trouve_stockage(FamillesMaladies).all_noms,
            "progression": lambda progression: float(progression) >= 0,
            "degats_max": lambda degats_max: float(degats_max) >= 0,
            "gain_pv": lambda gain_pv: float(gain_pv) >= 0,
            "immunite": lambda immunite: float(immunite) >= 0,
            "multiplicateur": lambda multiplicateur: float(multiplicateur) >= 1,
        }

    avertissements = {
            "poids": "Le poids doit être positif.",
            "frottements": "Le frottement doit être positif.",
            "latence_boit": "La latence doit être positive.",
            "portee": "La portée des éclaboussures doit être positive.",
            "duree_max": "La durée maximale de survit des éclaboussures doit être positive.",
            "maladie": "Il faut choisir une maladie existante (peut-être qu'il n'en existe pas encore).",
            "famille_maladie": "Il faut choisir une famille de maladies existante (peut-être qu'il n'en existe pas encore).",
            "progression": "La progression doit être positive.",
            "degats_max": "Les dégâts max doivent être positifs.",
            "gain_pv": "Le gain de PV doit être positif.",
            "immunite": "L'immunité doit être positive.",
            "multiplicateur": "Le multiplicateur doit être supérieur ou égal à 1.",
        }
    
    conditionnels = {
            "mixte": lambda dictionnaire: dictionnaire["effet"] != "maladie",
            "portee": lambda dictionnaire: dictionnaire["mixte"] == "True",
            "duree_max": lambda dictionnaire: dictionnaire["mixte"] == "True",
            "maladie": lambda dictionnaire: dictionnaire["effet"] == "maladie" or dictionnaire["effet"] == "medicament" or dictionnaire["effet"] == "vaccin",
            "famille_maladie": lambda dictionnaire: dictionnaire["effet"] == "medicament" or dictionnaire["effet"] == "vaccin",
            "progression": lambda dictionnaire: dictionnaire["effet"] == "poison",
            "degats_max": lambda dictionnaire: dictionnaire["effet"] == "poison",
            "gain_pv": lambda dictionnaire: dictionnaire["effet"] == "soin",
            "immunite": lambda dictionnaire: dictionnaire["effet"] == "vaccin",
            "statistique boostee": lambda dictionnaire: dictionnaire["effet"] == "boost",
            "element": lambda dictionnaire: dictionnaire["effet"] == "boost" and dictionnaire["statistique boostee"] == "affinite",
            "terre": lambda dictionnaire: dictionnaire["effet"] == "boost" and dictionnaire["statistique boostee"] == "affinites",
            "feu": lambda dictionnaire: dictionnaire["effet"] == "boost" and dictionnaire["statistique boostee"] == "affinites",
            "glace": lambda dictionnaire: dictionnaire["effet"] == "boost" and dictionnaire["statistique boostee"] == "affinites",
            "ombre": lambda dictionnaire: dictionnaire["effet"] == "boost" and dictionnaire["statistique boostee"] == "affinites",
            "multiplicateur": lambda dictionnaire: dictionnaire["effet"] == "boost",
        }

    def __init__(self, nom: str, poids: list[float], frottements: list[float],
                 fantome: bool, latence_boit: list[float], effet: str, mixte: bool,
                 portee: list[float], duree_max: list[float], maladie: str, famille_maladie: str,
                 progression: list[float], degats_max: list[float], gain_pv: list[float],
                 immunite: list[float], statistique_boostee: str, element: mdl.Element,
                 terre: bool, feu: bool, glace: bool, ombre: bool, multiplicateur: list[float]):
        EntiteeNivele.__init__(self, nom)
        self.fantome = fantome
        self.poids = poids
        self.frottements = frottements
        self.latence_boit = latence_boit
        self.effet = effet
        self.mixte = mixte
        self.portee = portee
        self.duree_max = duree_max
        self.maladie = maladie
        self.famille_maladie = famille_maladie
        self.progression = progression
        self.degats_max = degats_max
        self.gain_pv = gain_pv
        self.immunite = immunite
        self.statistique_boostee = statistique_boostee
        self.element = element
        self.terre = terre
        self.feu = feu
        self.glace = glace
        self.ombre = ombre
        self.multiplicateur = multiplicateur

    def check(self) -> bool:
        return (self.maladie in Maladies.global_.trouve_stockage(Maladies).all_noms and
                self.famille_maladie in FamillesMaladies.global_.trouve_stockage(FamillesMaladies).all_noms and
                all([latence >= 0 for latence in self.latence_boit]) and
                all([poids >= 0 for poids in self.poids]) and
                all([frottements >= 0 for frottements in self.frottements]) and
                all([portee > 0 for portee in self.portee]) and
                all([duree_max > 0 for duree_max in self.duree_max]) and
                all([progression >= 0 for progression in self.progression]) and
                all([degats >= 0 for degats in self.degats_max]) and
                all([gain >= 0 for gain in self.gain_pv]) and
                all([immunite >= 0 for immunite in self.immunite]) and
                all([multiplicateur >= 1 for multiplicateur in self.multiplicateur]))

    def stringify(self) -> str:
        return f"""{{
    "type": "potion vierge",
    "nivele": true,
    "nom": "{self.nom}",
    "fantome": {self.fantome},
    "poids": {self.poids},
    "frottements": {self.frottements},
    "latence_impregne": {self.latence_boit},
    "effet": "{self.effet}",
    "mixte": {self.mixte},
    "portee": {self.portee},
    "duree_max": {self.duree_max},
    "maladie": "{self.maladie}",
    "famille_maladie": "{self.famille_maladie}",
    "progression": {self.progression},
    "degats_max": {self.degats_max},
    "gain_pv": {self.gain_pv},
    "immunite": {self.immunite},
    "statistique_boostee": "{self.statistique_boostee}",
    "element": "{self.element}",
    "terre": {self.terre},
    "feu": {self.feu},
    "glace": {self.glace},
    "ombre": {self.ombre},
    "multiplicateur": {self.multiplicateur}
}}"""

    @classmethod
    def parse(cls, json: str):
        dictionnaire = parse(json)
        return cls(dictionnaire["nom"], dictionnaire["fantome"], dictionnaire["poids"], dictionnaire["frottements"], dictionnaire["latence_boit"], dictionnaire["effet"], dictionnaire["mixte"], dictionnaire["portee"], dictionnaire["duree_max"], dictionnaire["maladie"], dictionnaire["famille_maladie"], dictionnaire["progression"], dictionnaire["degats_max"], dictionnaire["gain_pv"], dictionnaire["immunite"], dictionnaire["statistique_boostee"], dictionnaire["element"], dictionnaire["terre"], dictionnaire["feu"], dictionnaire["glace"], dictionnaire["ombre"], dictionnaire["multiplicateur"])

    def make(self, niveau:int) -> type[mdl.Potion]:
        """Retourne le potion correspondant."""
        effet: type[mdl.EffetAgissant]
        if self.effet == "maladie":
            maladie = Maladies.global_.make(self.maladie, niveau)
            assert isinstance(maladie, type) and issubclass(maladie, mdl.EffetAgissant)
            effet = maladie
        elif self.effet == "boost":
            effet = mdl.effets_boosts[(self.statistique_boostee, self.mixte)]
        else:
            effet = mdl.effets_potions[(self.effet, self.mixte)]
        class EffetPotion(effet):
            """L'effet de la potion."""
            if self.mixte and self.effet != "maladie": # Les maladies mixtes ont déjà une portée et une durée.
                portee = self.portee[niveau]
                duree_max = self.duree_max[niveau]
            match self.effet:
                case "poison":
                    progression = self.progression[niveau]
                    degats_max = self.degats_max[niveau]
                case "soin":
                    gain_pv = self.gain_pv[niveau]
                case "medicament":
                    if self.maladie:
                        maladie = self.maladie
                    elif self.famille_maladie:
                        famille = self.famille_maladie
                    else:
                        raise ValueError("Il faut choisir une maladie ou une famille de maladies.")
                case "vaccin":
                    if self.maladie:
                        maladie = self.maladie
                    elif self.famille_maladie:
                        famille = self.famille_maladie
                    else:
                        raise ValueError("Il faut choisir une maladie ou une famille de maladies.")
                    immunite = self.immunite[niveau]
                case "boost":
                    multiplicateur = self.multiplicateur[niveau]
                    match self.statistique_boostee:
                        case "affinite":
                            multiplicateur = self.multiplicateur[niveau]
                        case "affinites":
                            element: set[mdl.Element] = set()
                            if self.terre:
                                element.add(mdl.Element.TERRE)
                            if self.feu:
                                element.add(mdl.Element.FEU)
                            if self.glace:
                                element.add(mdl.Element.GLACE)
                            if self.ombre:
                                element.add(mdl.Element.OMBRE)
                        case _:
                            pass
                case _:
                    pass
        class BoitPotion(mdl.Boit):
            """L'action de boire une potion."""
            type_effet = EffetPotion
            latence_max = self.latence_boit[niveau]
        class PotionNiveau(mdl.Potion, mdl.Nomme):
            """Une potion."""
            poids = self.poids[niveau]
            frottements = self.frottements[niveau]
            fantome = self.fantome
            latence_boit = self.latence_boit[niveau]
            action_portee = BoitPotion
        PotionNiveau.nom = self.nom
        PotionNiveau.niveau = niveau
        return PotionNiveau

class Potions(StockageCategorieNivelee):
    """Les informations des potions."""
    nom = "Potions"
    titre_nouveau = "Nouvelle potion"
    description = "Les potions sont des items consommables qui s'activent sans mana. Elles peuvent contenir divers effets (poison, maladie, soin, boost, etc.)."
    avertissement = "Il existe déjà une potion avec ce nom !"
    elements = {
        "potion": PotionNivele
    }
