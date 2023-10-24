from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import carte as crt

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ....entitee.item.Cadavre import Cadavre
    from ....esprit.esprit import Esprit

# Imports des classes parentes
from ...effet import OneShot
from ...item.item import EffetItem

class Reanimation(OneShot, EffetItem):
    """Un effet de réanimation. Généralement placé sur le cadavre par une magie de réanimation de zone ou un skill de réanimation."""
    def __init__(self,cadavre:Cadavre,taux:float,esprit:Optional[Esprit]):
        self.magie = cadavre
        self.taux = taux
        self.esprit = esprit

    def action(self):
        agissant = self.magie.agissant
        agissant.statistiques.pv = agissant.statistiques.pv_max*self.taux
        agissant.etat = EtatsAgissants.VIVANT
        self.magie.etat = EtatsItems.BRISE
        self.magie.labyrinthe.position_case[self.magie.position].agissant = agissant
        agissant.position = self.magie.position
        self.magie.position = crt.POSITION_ABSENTE
        if self.esprit is not None:
            if agissant.esprit == NOBODY:
                agissant.esprit.retire_corp(agissant)
            self.esprit.ajoute_corp(agissant)

    def execute(self):
        self.action()

# Imports utilisés dans le code
from ....entitee.agissant.etats import EtatsAgissants
from ....entitee.item.etats import EtatsItems
from ....esprit.esprit import NOBODY