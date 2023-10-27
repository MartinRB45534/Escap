from __future__ import annotations
from typing import TYPE_CHECKING
import carte as crt

# Imports des classes parentes
from ...timings import OnFinTourCadavre

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ....entitee.item.cadavre import Cadavre

class Resurection(OnFinTourCadavre):
    """Un effet de résurection. Généralement placé sur le cadavre par une magie de résurection. Rend tous les pv et ne change pas l'appartenance à un groupe."""
    def fin_tour(self,cadavre:Cadavre):
        agissant = cadavre.agissant
        agissant.statistiques.pv = agissant.statistiques.pv_max
        agissant.etat = EtatsAgissants.VIVANT
        cadavre.etat = EtatsItems.BRISE
        cadavre.labyrinthe.position_case[cadavre.position].agissant = agissant
        agissant.position = cadavre.position
        cadavre.position = crt.POSITION_ABSENTE

# Imports utilisés dans le code
from ....commons.etats_agissant import EtatsAgissants
from ....commons.etats_item import EtatsItems