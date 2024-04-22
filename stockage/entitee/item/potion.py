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
            "maladie": "Il faut choisir une maladie existante (peut-être qu'il n'en existe pas encore).",
            "famille_maladie": "Il faut choisir une famille de maladies existante (peut-être qu'il n'en existe pas encore).",
            "progression": "La progression doit être positive.",
            "degats_max": "Les dégâts max doivent être positifs.",
            "gain_pv": "Le gain de PV doit être positif.",
            "immunite": "L'immunité doit être positive.",
            "multiplicateur": "Le multiplicateur doit être supérieur ou égal à 1.",
        }
    
    conditionnels = {
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
                 fantome: bool, latence_boit: list[float], effet: str, maladie: str,
                 famille_maladie: str, progression: list[float],
                 degats_max: list[float], gain_pv: list[float], immunite: list[float],
                 statistique_boostee: str, element: mdl.Element, terre: bool, feu: bool,
                 glace: bool, ombre: bool, multiplicateur: list[float]):
        EntiteeNivele.__init__(self, nom)
        self.fantome = fantome
        self.poids = poids
        self.frottements = frottements
        self.latence_boit = latence_boit
        self.effet = effet
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
        return cls(dictionnaire["nom"], dictionnaire["fantome"], dictionnaire["poids"], dictionnaire["frottements"], dictionnaire["latence_boit"], dictionnaire["effet"], dictionnaire["maladie"], dictionnaire["famille_maladie"], dictionnaire["progression"], dictionnaire["degats_max"], dictionnaire["gain_pv"], dictionnaire["immunite"], dictionnaire["statistique_boostee"], dictionnaire["element"], dictionnaire["terre"], dictionnaire["feu"], dictionnaire["glace"], dictionnaire["ombre"], dictionnaire["multiplicateur"])

    def make(self, niveau:int) -> type[mdl.Potion]:
        """Retourne le potion correspondant."""
        match self.effet:
            case "maladie":
                maladie = Maladies.global_.make(self.maladie, niveau)
                assert isinstance(maladie, type) and issubclass(maladie, mdl.Maladie)
                effet = maladie
            case "poison":
                class Poison(mdl.Poison):
                    progression = self.progression[niveau]
                    degats_max = self.degats_max[niveau]
                effet = Poison
            case "soin":
                class Soin(mdl.Soin):
                    gain_pv = self.gain_pv[niveau]
                effet = Soin
            case "antidote":
                class Antidote(mdl.Antidote):
                    pass
                effet = Antidote
            case "medicament":
                class Medicament(mdl.Medicament):
                    if self.maladie:
                        maladie = self.maladie
                    elif self.famille_maladie:
                        famille = self.famille_maladie
                    else:
                        raise ValueError("Il faut choisir une maladie ou une famille de maladies.")
                effet = Medicament
            case "vaccin":
                class Vaccin(mdl.Vaccin):
                    if self.maladie:
                        maladie = self.maladie
                    elif self.famille_maladie:
                        famille = self.famille_maladie
                    else:
                        raise ValueError("Il faut choisir une maladie ou une famille de maladies.")
                    immunite = self.immunite[niveau]
                effet = Vaccin
            case "boost":
                match self.statistique_boostee:
                    case "force":
                        class BoostForce(mdl.EffetForce):
                            multiplicateur = self.multiplicateur[niveau]
                            def modifie_force(self, force: float) -> float:
                                return force * self.multiplicateur
                        effet = BoostForce
                    case "vision":
                        class BoostVision(mdl.EffetVision):
                            multiplicateur = self.multiplicateur[niveau]
                            def modifie_vision(self, vision: float) -> float:
                                return vision * self.multiplicateur
                        effet = BoostVision
                    case "pv":
                        class BoostPv(mdl.EffetPv):
                            multiplicateur = self.multiplicateur[niveau]
                            def modifie_pv(self, pv: float) -> float:
                                return pv * self.multiplicateur
                        effet = BoostPv
                    case "pm":
                        class BoostPm(mdl.EffetPm):
                            multiplicateur = self.multiplicateur[niveau]
                            def modifie_pm(self, pm: float) -> float:
                                return pm * self.multiplicateur
                        effet = BoostPm
                    case "vitesse":
                        class BoostVitesse(mdl.EffetVitesse):
                            multiplicateur = self.multiplicateur[niveau]
                            def modifie_vitesse(self, vitesse: float) -> float:
                                return vitesse * self.multiplicateur
                        effet = BoostVitesse
                    case "affinite":
                        class BoostAffinite(mdl.EffetAffinite):
                            element = self.element
                            multiplicateur = self.multiplicateur[niveau]
                            def modifie_affinite(self, affinite: float) -> float:
                                return affinite * self.multiplicateur
                        effet = BoostAffinite
                    case "affinites":
                        class BoostAffinites(mdl.EffetAffinites):
                            element: set[mdl.Element] = set()
                            if self.terre:
                                element.add(mdl.Element.TERRE)
                            if self.feu:
                                element.add(mdl.Element.FEU)
                            if self.glace:
                                element.add(mdl.Element.GLACE)
                            if self.ombre:
                                element.add(mdl.Element.OMBRE)
                            multiplicateur = self.multiplicateur[niveau]
                            def modifie_affinite(self, affinite: float, element: mdl.Element) -> float:
                                if element in self.element:
                                    return affinite * self.multiplicateur
                                return affinite
                        effet = BoostAffinites
                    case "stats":
                        class BoostStats(mdl.EffetStats):
                            multiplicateur = self.multiplicateur[niveau]
                            def modifie_stats(self, stat: float) -> float:
                                return stat * self.multiplicateur
                        effet = BoostStats
                    case _:
                        raise ValueError("Il faut choisir une statistique à booster.")
        class BoitPotion(mdl.Boit):
            type_effet = effet
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
