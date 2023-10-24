from __future__ import annotations
from typing import TYPE_CHECKING

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ....entitee.item.Cadavre import Cadavre

# Imports des classes parentes
from ...effet import OneShot
from ...item.item import EffetItem

class Resurection(OneShot, EffetItem):
    """Un effet de résurection. Généralement placé sur le cadavre par une magie de résurection. Rend tous les pv et ne change pas l'appartenance à un groupe."""
    def __init__(self,cadavre:Cadavre):
        self.magie = cadavre

    def action(self):
        agissant = self.magie.agissant
        agissant.statistiques.pv = agissant.statistiques.pv_max
        agissant.etat = EtatsAgissants.VIVANT
        self.magie.etat = EtatsItems.BRISE

    def execute(self):
        self.action()

# Imports utilisés dans le code
from ....entitee.agissant.etats import EtatsAgissants
from ....entitee.item.etats import EtatsItems