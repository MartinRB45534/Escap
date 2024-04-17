"""Contient la classe Bouclier."""

from __future__ import annotations

# Imports des classes parentes
from ..degainable import Degainable
from ...role import EquippementTribal

# Imports utilisés dans le code
from ......affichage import SKIN_BOUCLIER
from ......effet import AttaqueCase

class Bouclier(Degainable):
    """La classe des boucliers. Permettent de se protéger des attaques lorsqu'ils sont utilisés."""
    degats_bloques:float
    taux_degats:float


    def intercepte(self,attaque:AttaqueCase):
        """Intercepte une attaque."""
        attaque.degats -= self.degats_bloques
        if attaque.degats < 0:
            attaque.degats = 0
        else :
            for taux in self.taux_stats.values():
                attaque.degats *=  taux
            attaque.degats *= self.taux_degats

    @staticmethod
    def get_image():
        return SKIN_BOUCLIER
    
class BouclierTribal(Bouclier, EquippementTribal):
    """Un bouclier tribal. Réduit ses statistiques si l'espèce n'est pas la bonne."""

boucliers: dict[tuple[bool], type[Bouclier]] = {
    (False,): Bouclier,
    (True,): BouclierTribal,
}
"""
(tribal,) -> classe du bouclier
"""
