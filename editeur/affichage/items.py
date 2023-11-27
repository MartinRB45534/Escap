"""Le contenu de l'onglet de création d'items."""

from __future__ import annotations

import affichage as af
import stockage as stck

from .onglet_categorie import OngletCategorie

class OngletItems(af.Onglet):
    """L'onglet de création d'items."""
    def __init__(self, stockage:stck.StockageGlobal):
        self.onglets = af.Onglets(af.DirectionAff.LEFT)
        af.Onglet.__init__(self, "Items", self.onglets)
        self.stockage = stockage
        self.onglets.set_onglets([
            OngletCategorie(self.stockage.items.parchemin),
        ])
