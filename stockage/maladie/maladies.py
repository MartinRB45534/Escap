"""
Fichier contenant la classe de stockage des maladies.
"""

from __future__ import annotations

from ..stockage import StockageSurCategorie
from .famille import FamillesMaladies
from .maladie import Maladies

class MaladiesEtFamilles(StockageSurCategorie):
    """Les informations des maladies."""
    nom = "Maladies"
    elements = {
        "famille": FamillesMaladies,
        "maladie": Maladies,
    }
