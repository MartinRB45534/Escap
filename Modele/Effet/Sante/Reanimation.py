from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import Carte as crt

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ...Entitee.Item.Cadavre import Cadavre
    from ...Esprit.Esprit import Esprit

# Imports des classes parentes
from ..Effet import On_fin_tour

class Reanimation(On_fin_tour):
    """Un effet de réanimation. Généralement placé sur le cadavre par une magie de réanimation de zone ou un skill de réanimation."""
    def __init__(self,taux:float,esprit:Optional[Esprit]):
        self.phase = "démarrage"
        self.taux = taux
        self.esprit = esprit
        self.affiche = False

    def action(self,porteur:Cadavre):
        agissant = porteur.agissant
        agissant.pv = agissant.pv_max*self.taux
        agissant.etat = "vivant"
        porteur.etat = "brise"
        porteur.labyrinthe.position_case[porteur.position].agissant = agissant
        agissant.position = porteur.position
        porteur.position = crt.POSITION_ABSENTE
        if self.esprit is not None:
            if agissant.esprit is not None:
                agissant.esprit.retire_corp(agissant)
            self.esprit.ajoute_corp(agissant)

    def execute(self,porteur:Cadavre):
        if self.phase == "démarrage" :
            self.action(porteur)
            self.termine()