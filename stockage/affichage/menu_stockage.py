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
                                 StockageSurCategorie, default: str = "Pas d'éléments"):
        self.stockage = stockage
        self.noms = stockage.all_noms
        enum = StrEnum("Enum_" + stockage.nom, {nom: nom for nom in sorted(self.noms)})
        self.default = default
        if len(enum.__members__) == 0: # type: ignore # Pylance is being dumb
            enum = StrEnum("Enum_" + stockage.nom, {"default": default})
        MenuEnum.__init__(self, enum) # type: ignore # Pylance is being dumb

    @property
    def accepte(self):
        """Renvoie si la valeur saisie est acceptée."""
        if self.courant.get_texte() == self.default:
            return False
        return super().accepte

    def update(self):
        if self.noms != self.stockage.all_noms:
            self.noms = self.stockage.all_noms
            self.enum = StrEnum("Enum_" + self.stockage.nom,
                                {nom: nom for nom in sorted(self.noms)})
            if len(self.enum.__members__) == 0: # type: ignore # Pylance is being dumb
                self.enum = StrEnum("Enum_" + self.stockage.nom, {"default": self.default})
            textes = [af.TexteMenuDeroulant(self, element) for element in self.enum]
            self.set_contenu_liste(textes)
            try:
                self.valeur = self.valeur
            except ValueError:
                self.valeur = textes[0].get_texte()
        af.MenuDeroulant.update(self)
