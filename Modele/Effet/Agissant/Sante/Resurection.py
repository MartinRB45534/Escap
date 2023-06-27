from __future__ import annotations
from typing import TYPE_CHECKING

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ....Entitee.Item.Cadavre import Cadavre

# Imports des classes parentes
from ...Effet import One_shot
from ...Item.Item import Effet_item

class Resurection(One_shot, Effet_item):
    """Un effet de résurection. Généralement placé sur le cadavre par une magie de résurection. Rend tous les pv et ne change pas l'appartenance à un groupe."""
    def __init__(self,cadavre:Cadavre):
        self.cadavre = cadavre

    def action(self):
        agissant = self.cadavre.agissant
        agissant.statistiques.pv = agissant.statistiques.pv_max
        agissant.etat = Etats_agissants.VIVANT
        self.cadavre.etat = Etats_items.BRISE

    def execute(self):
        self.action()

# Imports utilisés dans le code
from ....Entitee.Agissant.Etats import Etats_agissants
from ....Entitee.Item.Etats import Etats_items