"""
La classe du menu d'éléments.
"""

from __future__ import annotations
from enum import StrEnum

import affichage as af

from ..stockage import StockageCategorieUnique, StockageCategorieNivelee, StockageSurCategorie

from .menu_enum import MenuEnum

class MenuStockage(MenuEnum):
    """Le menu d'éléments. Il permet de sélectionner un élément."""
    def __init__(self, stockage: StockageCategorieUnique|
                                 StockageCategorieNivelee|
                                 StockageSurCategorie):
        self.stockage = stockage
        self.noms = stockage.all_noms
        MenuEnum.__init__(self, type(StrEnum("Enum_" + stockage.nom, {nom: nom for nom in sorted(self.noms)})))

    def update(self):
        if self.noms != self.stockage.all_noms:
            self.noms = self.stockage.all_noms
            self.enum = StrEnum("Enum_" + self.stockage.nom,
                                {nom: nom for nom in sorted(self.noms)})
            textes = [af.TexteMenuDeroulant(self, element) for element in self.enum]
            self.set_contenu_liste(textes)
            try:
                self.valeur = self.valeur
            except ValueError:
                self.valeur = self.enum[0]
        af.MenuDeroulant.update(self)
