"""Contient le stockage global, qui devrait tout contenir."""

from __future__ import annotations

from .stockage import Stockage, StockageCategorieUnique, StockageCategorieNivelee, StockageSurCategorie
from .maladie import MaladiesEtFamilles
from .entitee import Items
from .espece import Especes
from .magie import Magies

class StockageGlobal(StockageSurCategorie):
    """Le stockage global, qui devrait tout contenir."""
    nom:str = "StockageGlobal"
    elements:dict[str, type[StockageCategorieUnique]|type[StockageCategorieNivelee]|type[StockageSurCategorie]] = {
        "maladies": MaladiesEtFamilles,
        "especes": Especes,
        "magies": Magies,
        "items": Items,
    }

    def __init__(self):
        StockageSurCategorie.__init__(self)
        Stockage.global_ = self

    def valide_nom(self, nom:str) -> bool:
        """Vérifie que le nom est valide."""
        return not nom in self.all_noms
