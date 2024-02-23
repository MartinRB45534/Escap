"""
Fichier contenant la classe de stockage des magies.
"""

from __future__ import annotations

import modele as mdl

from ..stockage import StockageNivele

class MagieNivele(StockageNivele):
    """Classe mère des classes de stockage de magie."""
    def make(self, niveau: int) -> type[mdl.Magie]:
        """Retourne l'entité correspondante."""
        raise NotImplementedError
