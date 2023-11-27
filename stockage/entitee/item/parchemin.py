"""
Fichier contenant la classe de stockage des parchemins.
"""

from __future__ import annotations
from typing import List, Dict, Optional, Type, Callable, Tuple
from json import loads as parse

import modele as mdl
import carte as crt

from ...stockage import StockageCategorie, StockageNivele, StockageUnique
from ..entitee import Entitee, EntiteeNivele

class Parchemins(StockageCategorie):
    """Les informations des parchemins."""
    def __init__(self):
        StockageCategorie.__init__(self, "Parchemins")
        self.parchemins:Dict[str, ParcheminVierge|ParcheminViergeNivele] = {}

    def check(self) -> bool:
        return all([parchemin.check() for parchemin in self.parchemins.values()])

    def stringify(self) -> str:
        return f"""{
    [
        {", ".join([parchemin.stringify() for parchemin in self.parchemins.values()])}
    ]
}"""

    @classmethod
    def parse(cls, json: str) -> Parchemins:
        dictionnaire = parse(json)
        parchemin = Parchemins()
        parchemin.parchemins = {
            parchemin["nom"]: ParcheminVierge.parse(parchemin)
            for parchemin in dictionnaire["parchemins"]
        }
        return parchemin

    def make(self, nom: str, labyrinthe: mdl.Labyrinthe, position: crt.Position,
             niveau:Optional[int]=None) -> mdl.Parchemin:
        """Retourne le parchemin correspondant."""
        if nom not in self.parchemins:
            raise ValueError(f"Le parchemin {nom} n'existe pas.")
        parchemin = self.parchemins[nom]
        if isinstance(parchemin, StockageNivele):
            if niveau is None:
                raise ValueError(
                    f"Le parchemin {nom} est nivele, il faut donc spécifier un niveau."
                )
            else:
                return parchemin.make(labyrinthe, position, niveau)

        else:
            assert isinstance(parchemin, Entitee)
            if niveau is not None:
                raise ValueError(
                    f"Le parchemin {nom} n'est pas nivele, il ne faut donc pas spécifier de niveau."
                )
            else:
                return parchemin.make(labyrinthe, position)

    @classmethod
    @property
    def elements(cls) -> dict[str, Type[StockageUnique]|Tuple[Type[StockageUnique], Type[StockageNivele]]]:
        return {
            "parchemins vierges": (ParcheminVierge, ParcheminViergeNivele)
        }

class ParcheminVierge(Entitee):
    """Les informations d'un parchemin vierge."""
    def __init__(self, nom: str, latence_impregne:float,
                 taux_cout_caste: float, taux_cout_impregne: float,
                 taux_latence_caste: float, taux_latence_impregne: float):
        Entitee.__init__(self, nom)
        self.latence_impregne = latence_impregne
        self.taux_cout_caste = taux_cout_caste
        self.taux_cout_impregne = taux_cout_impregne
        self.taux_latence_caste = taux_latence_caste
        self.taux_latence_impregne = taux_latence_impregne

    def check(self) -> bool:
        return self.latence_impregne >= 0 and self.taux_cout_caste >= 0 and self.taux_cout_impregne >= 0 and self.taux_latence_caste >= 0 and self.taux_latence_impregne >= 0

    def stringify(self) -> str:
        return f"""{{
    "nom": "{self.nom}",
    "latence_impregne": {self.latence_impregne},
    "taux_cout_caste": {self.taux_cout_caste},
    "taux_cout_impregne": {self.taux_cout_impregne},
    "taux_latence_caste": {self.taux_latence_caste},
    "taux_latence_impregne": {self.taux_latence_impregne}
}}"""

    @classmethod
    def parse(cls, json: str) -> ParcheminVierge:
        dictionnaire = parse(json)
        return ParcheminVierge(dictionnaire["nom"], dictionnaire["latence_impregne"], dictionnaire["taux_cout_caste"], dictionnaire["taux_cout_impregne"], dictionnaire["taux_latence_caste"], dictionnaire["taux_latence_impregne"])

    @classmethod
    @property
    def champs(cls) -> dict[str, Type[int|str|float]]:
        return {
            "latence_impregne": float,
            "taux_cout_caste": float,
            "taux_cout_impregne": float,
            "taux_latence_caste": float,
            "taux_latence_impregne": float
        }

    @classmethod
    @property
    def acceptors(cls) -> dict[str, Callable[[str], bool]]:
        return {
            "latence_impregne": lambda latence: float(latence) >= 0,
            "taux_cout_caste": lambda taux: float(taux) >= 0,
            "taux_cout_impregne": lambda taux: float(taux) >= 0,
            "taux_latence_caste": lambda taux: float(taux) >= 0,
            "taux_latence_impregne": lambda taux: float(taux) >= 0
        }

    @classmethod
    @property
    def avertissements(cls) -> dict[str, str]:
        return {
            "latence_impregne": "La latence d'impregnation doit être positive.",
            "taux_cout_caste": "Le taux de cout de caste doit être positif.",
            "taux_cout_impregne": "Le taux de cout d'impregnation doit être positif.",
            "taux_latence_caste": "Le taux de latence de caste doit être positif.",
            "taux_latence_impregne": "Le taux de latence d'impregnation doit être positif."
        }

    def make(self, labyrinthe: mdl.Labyrinthe, position:crt.Position) -> mdl.ParcheminVierge:
        """Retourne le parchemin correspondant."""
        effet = mdl.Impregne(mdl.NOONE, self.latence_impregne, mdl.NOWRITTING, self.taux_cout_impregne, self.taux_cout_caste, self.taux_latence_impregne, self.taux_latence_caste)
        parchemin = mdl.ParcheminVierge(labyrinthe, effet, position)
        return parchemin

class ParcheminViergeNivele(EntiteeNivele):
    """Les informations d'un parchemin vierge."""
    def __init__(self, nom: str, latences_impregne: List[float], taux_cout_caste: List[float], taux_cout_impregne: List[float], taux_latence_caste: List[float], taux_latence_impregne: List[float]):
        EntiteeNivele.__init__(self, nom)
        self.latences_impregne = latences_impregne
        self.taux_cout_caste = taux_cout_caste
        self.taux_cout_impregne = taux_cout_impregne
        self.taux_latence_caste = taux_latence_caste
        self.taux_latence_impregne = taux_latence_impregne

    def check(self) -> bool:
        return len(self.latences_impregne) == 10 and len(self.taux_cout_caste) == 10 and len(self.taux_cout_impregne) == 10 and len(self.taux_latence_caste) == 10 and len(self.taux_latence_impregne) == 10 and all([latence >= 0 for latence in self.latences_impregne]) and all([taux >= 0 for taux in self.taux_cout_caste]) and all([taux >= 0 for taux in self.taux_cout_impregne]) and all([taux >= 0 for taux in self.taux_latence_caste]) and all([taux >= 0 for taux in self.taux_latence_impregne])

    def stringify(self) -> str:
        return f"""{{
    "latences_impregne": {self.latences_impregne},
    "taux_cout_caste": {self.taux_cout_caste},
    "taux_cout_impregne": {self.taux_cout_impregne},
    "taux_latence_caste": {self.taux_latence_caste},
    "taux_latence_impregne": {self.taux_latence_impregne}
}}"""

    @classmethod
    def parse(cls, json: str) -> ParcheminViergeNivele:
        dictionnaire = parse(json)
        return ParcheminViergeNivele(dictionnaire["nom"],  dictionnaire["latences_impregne"], dictionnaire["taux_cout_caste"], dictionnaire["taux_cout_impregne"], dictionnaire["taux_latence_caste"], dictionnaire["taux_latence_impregne"])

    @classmethod
    @property
    def champs(cls) -> dict[str, Type[int|str|float]]:
        return {
            "latence_impregne": float,
            "taux_cout_caste": float,
            "taux_cout_impregne": float,
            "taux_latence_caste": float,
            "taux_latence_impregne": float
        }

    @classmethod
    @property
    def acceptors(cls) -> dict[str, Callable[[str], bool]]:
        return {
            "latence_impregne": lambda latence: float(latence) >= 0,
            "taux_cout_caste": lambda taux: float(taux) >= 0,
            "taux_cout_impregne": lambda taux: float(taux) >= 0,
            "taux_latence_caste": lambda taux: float(taux) >= 0,
            "taux_latence_impregne": lambda taux: float(taux) >= 0
        }

    @classmethod
    @property
    def avertissements(cls) -> dict[str, str]:
        return {
            "latence_impregne": "La latence d'impregnation doit être positive.",
            "taux_cout_caste": "Le taux de cout de caste doit être positif.",
            "taux_cout_impregne": "Le taux de cout d'impregnation doit être positif.",
            "taux_latence_caste": "Le taux de latence de caste doit être positif.",
            "taux_latence_impregne": "Le taux de latence d'impregnation doit être positif."
        }

    def make(self, labyrinthe: mdl.Labyrinthe, position:crt.Position, niveau:int) -> mdl.ParcheminVierge:
        """Retourne le parchemin correspondant."""
        effet = mdl.Impregne(mdl.NOONE, self.latences_impregne[niveau], mdl.NOWRITTING, self.taux_cout_impregne[niveau], self.taux_cout_caste[niveau], self.taux_latence_impregne[niveau], self.taux_latence_caste[niveau])
        parchemin = mdl.ParcheminVierge(labyrinthe, effet, position)
        return parchemin
        