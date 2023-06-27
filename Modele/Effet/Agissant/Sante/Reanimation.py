from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import Carte as crt

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ....Entitee.Item.Cadavre import Cadavre
    from ....Esprit.Esprit import Esprit

# Imports des classes parentes
from ...Effet import One_shot
from ...Item.Item import Effet_item

class Reanimation(One_shot, Effet_item):
    """Un effet de réanimation. Généralement placé sur le cadavre par une magie de réanimation de zone ou un skill de réanimation."""
    def __init__(self,cadavre:Cadavre,taux:float,esprit:Optional[Esprit]):
        self.cadavre = cadavre
        self.taux = taux
        self.esprit = esprit

    def action(self):
        agissant = self.cadavre.agissant
        agissant.statistiques.pv = agissant.statistiques.pv_max*self.taux
        agissant.etat = Etats_agissants.VIVANT
        self.cadavre.etat = Etats_items.BRISE
        self.cadavre.labyrinthe.position_case[self.cadavre.position].agissant = agissant
        agissant.position = self.cadavre.position
        self.cadavre.position = crt.POSITION_ABSENTE
        if self.esprit is not None:
            if agissant.esprit == NOBODY:
                agissant.esprit.retire_corp(agissant)
            self.esprit.ajoute_corp(agissant)

    def execute(self):
        self.action()

# Imports utilisés dans le code
from ....Entitee.Agissant.Etats import Etats_agissants
from ....Entitee.Item.Etats import Etats_items
from ....Esprit.Esprit import NOBODY