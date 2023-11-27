from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import carte as crt

# Imports des classes parentes
from .timings import OnFinTourCadavre

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ....entitee.item.cadavre import Cadavre
    from ....esprit.esprit import Esprit

class Reanimation(OnFinTourCadavre):
    """Un effet de réanimation. Généralement placé sur le cadavre par une magie de réanimation de zone ou un skill de réanimation."""
    def __init__(self,taux:float,esprit:Optional[Esprit]):
        self.taux = taux
        self.esprit = esprit

    def fin_tour(self,cadavre:Cadavre):
        agissant = cadavre.agissant
        agissant.statistiques.pv = agissant.statistiques.pv_max*self.taux
        agissant.etat = EtatsAgissants.VIVANT
        cadavre.etat = EtatsItems.BRISE
        cadavre.labyrinthe.position_case[cadavre.position].agissant = agissant
        agissant.position = cadavre.position
        cadavre.position = crt.POSITION_ABSENTE
        if self.esprit is not None:
            if not agissant.esprit: # NOBODY is falsy
                agissant.esprit.retire_corp(agissant)
            self.esprit.ajoute_corp(agissant)

# Imports utilisés dans le code
from ....commons.etats_agissant import EtatsAgissants
from ....commons.etats_item import EtatsItems