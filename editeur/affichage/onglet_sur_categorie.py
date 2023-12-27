"""Le contenu de l'onglet qui contient des onglets de catégories."""

from __future__ import annotations

import affichage as af
import stockage as stck

from .onglet_categorie_unique import OngletCategorieUnique
from .onglet_categorie_nivelee import OngletCategorieNivelee

class OngletSurCategorie(af.Onglet):
    """L'onglet d'onglets"""
    def __init__(self, stockage:stck.StockageSurCategorie):
        self.onglets = af.Onglets(af.DirectionAff.LEFT)
        af.Onglet.__init__(self, stockage.nom, self.onglets)
        self.stockage = stockage
        self.onglets.set_onglets([
            OngletCategorieUnique(contenu)
            if isinstance(contenu, stck.StockageCategorieUnique) else
            OngletCategorieNivelee(contenu)
            if isinstance(contenu, stck.StockageCategorieNivelee) else
            OngletSurCategorie(contenu) for contenu in self.stockage.contenu.values()
        ])
