"""
Classe de stockage des espèces.
"""

from __future__ import annotations
from typing import Optional
from json import loads as parse

import modele as mdl

from .stockage import Stockage, StockageGlobal

class Especes(Stockage):
    """Les informations des espèces."""
    def __init__(self):
        Stockage.__init__(self, "Especes")
        self.especes:dict[str, Espece] = {}

    def check(self) -> bool:
        return all([espece.check() for espece in self.especes.values()])
    
    def stringify(self) -> str:
        return f"""{{
    "Especes": [
        {", ".join([espece.stringify() for espece in self.especes.values()])}
    ]
}}"""
    
    @classmethod
    def parse(cls, json: str) -> Especes:
        dictionnaire = parse(json)
        especes = Especes()
        especes.especes = {
            espece["nom"]: Espece.parse(espece)
            for espece in dictionnaire["especes"]
        }
        return especes
    
    def make(self, nom:str) -> mdl.Espece:
        """Retourne l'espèce correspondante."""
        if nom in self.especes:
            return self.especes[nom].make()
        else:
            raise ValueError(f"L'espèce {nom} n'existe pas.")

class Espece(Stockage):
    """Les informations d'une espèce."""
    def __init__(self, nom: str, nb_doigts: int):
        Stockage.__init__(self, nom)
        self.nb_doigts = nb_doigts
        self.espece:Optional[mdl.Espece] = None

    def check(self) -> bool:
        return self.nb_doigts > 0

    def stringify(self) -> str:
        return f"""{{
    "nom": "{self.nom}",
    "nb_doigts": {self.nb_doigts}
}}"""

    @classmethod
    def parse(cls, json: str) -> Espece:
        dictionnaire = parse(json)
        return Espece(dictionnaire["nom"], dictionnaire["nb_doigts"])
    
    def make(self) -> mdl.Espece:
        """Retourne l'espèce correspondante."""
        if self.espece is None:
            self.espece = mdl.Espece(self.nom, self.nb_doigts)
        return self.espece # Il faut que ce soit le même objet à chaque fois

StockageGlobal.global_.especes = Especes()
