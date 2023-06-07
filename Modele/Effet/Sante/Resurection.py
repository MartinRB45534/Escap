from __future__ import annotations
from typing import TYPE_CHECKING

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ..Entitee.Item.Cadavre import Cadavre

# Imports des classes parentes
from ..Effet.Effet import On_fin_tour

class Resurection(On_fin_tour):
    """Un effet de résurection. Généralement placé sur le cadavre par une magie de résurection. Rend tous les pv et ne change pas l'appartenance à un groupe."""
    def __init__(self):
        self.phase = "démarrage"
        self.affiche = False

    def action(self,porteur:Cadavre):
        agissant = porteur.agissant
        agissant.pv = agissant.pv_max
        agissant.etat = "vivant"
        porteur.etat = "brise"

    def execute(self,porteur:Cadavre):
        if self.phase == "démarrage" :
            self.action(porteur)
            self.termine()
