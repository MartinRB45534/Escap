"""
Ce fichier contient les classes des magies de type boost.
"""

from __future__ import annotations

# Imports des classes parentes
from .magie import Magie, CibleAgissant, CibleAgissants

# Imports utilisés dans le code
from ...effet.agissant.agissants import Dopage

class MagieDopage(Magie):
    """La magie qui crée un effet de dopage sur l'agissant."""
    taux: float
    duree: float

    def action(self):
        self.agissant.effets.add(Dopage(self.agissant,self.taux))

class MagieBoost(MagieDopage,CibleAgissant):
    """La magie qui crée un effet de dopage sur un autre agissant."""
    def action(self):
        if not self.cible: # NOONE is falsy
            self.interrompt()
        else:
            self.cible.effets.add(Dopage(self.agissant,self.taux))

class MagieMultiBoost(MagieDopage,CibleAgissants):
    """La magie qui crée un effet de dopage sur plusieurs autres agissants."""

    def action(self):
        for cible in self.cible:
            cible.effets.add(Dopage(self.agissant,self.taux))

magies_boost: dict[tuple[bool, bool], type[MagieDopage]] = {
    (False, False): MagieDopage,
    (True, False): MagieBoost,
    (True, True): MagieMultiBoost,
    (False, True): MagieDopage # Pas possible
}
"""
(cible, cible_multiple) -> MagieDopage
"""
