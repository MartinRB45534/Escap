"""Contient le stockage global, qui devrait tout contenir."""

from __future__ import annotations

from .stockage import StockageCategorie, StockageSurCategorie
from .entitee import Items
from .espece import Especes

class StockageGlobal(StockageSurCategorie):
    """Le stockage global, qui devrait tout contenir."""
    nom:str = "StockageGlobal"
    elements:dict[str, type[StockageCategorie]|type[StockageSurCategorie]] = {
        "items": Items,
        "especes": Especes
    }
    global_:StockageGlobal

    def __init__(self):
        StockageSurCategorie.__init__(self)
        StockageGlobal.global_ = self

    def valide_nom(self, nom:str) -> bool:
        """Vérifie que le nom est valide."""
        return not nom in self.all_noms