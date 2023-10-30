"""L'agissant vu par un autre agissant."""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import carte as crt

from .inventaire import voit_inventaire
from .statistiques import voit_statistiques

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ....systeme.classe.classe_principale import ClassePrincipale
    from .inventaire import InventaireVu
    from .statistiques import StatistiquesVues
    from ..agissant import Agissant
    from ..espece import Espece

class AgissantVu:
    """L'agissant vu par un autre agissant."""
    def __init__(self, _id:int, identite:Optional[str], statistiques:StatistiquesVues, espece: Espece, niveau:int, inventaire:InventaireVu, dir_regard:crt.Direction, classe_principale:Optional[ClassePrincipale]=None):
        self.id = _id
        self.identite = identite
        self.statistiques = statistiques
        self.espece = espece
        self.classe_principale = classe_principale
        self.niveau = niveau
        self.inventaire = inventaire
        self.dir_regard = dir_regard

def voit_agissant(agissant:Agissant) -> AgissantVu:
    """Transforme un agissant en agissant vu."""
    return AgissantVu(
        agissant.id,
        agissant.identite,
        voit_statistiques(agissant.statistiques),
        agissant.espece,
        agissant.niveau,
        voit_inventaire(agissant.inventaire),
        agissant.dir_regard
    )
