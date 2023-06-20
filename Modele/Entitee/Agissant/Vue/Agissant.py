from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import Carte as crt

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ....Systeme.Classe.Classe_principale import Classe_principale
    from .Inventaire import Inventaire_vu
    from .Statistiques import Statistiques_vues
    from ..Agissant import Agissant
    from ..Espece import Espece

class Agissant_vu:
    def __init__(self, ID:int, identite:Optional[str], statistiques:Statistiques_vues, espece: Espece, niveau:int, inventaire:Inventaire_vu, dir_regard:crt.Direction, classe_principale:Optional[Classe_principale]=None):
        self.ID = ID
        self.identite = identite
        self.statistiques = statistiques
        self.espece = espece
        self.classe_principale = classe_principale
        self.niveau = niveau
        self.inventaire = inventaire
        self.dir_regard = dir_regard

def voit_agissant(agissant:Agissant) -> Agissant_vu:
    return Agissant_vu(
        agissant.ID,
        agissant.identite,
        voit_statistiques(agissant.statistiques),
        agissant.espece,
        agissant.niveau,
        voit_inventaire(agissant.inventaire),
        agissant.dir_regard
        )

from .Inventaire import voit_inventaire
from .Statistiques import voit_statistiques