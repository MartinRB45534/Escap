"""
Ce fichier contient les classes des magies de type boost.
"""

from __future__ import annotations
from typing import TYPE_CHECKING

# Imports des classes parentes
from .magie import Magie, CibleAgissant, CibleAgissants

# Imports utilisés dans le code
from ...effet.agissant.agissants import Dopage

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ...entitee import Agissant
    from ...systeme import Actif

class MagieDopage(Magie):
    """La magie qui crée un effet de dopage sur l'agissant."""
    taux: float
    duree: float
    def __init__(self,skill:Actif,agissant:Agissant):
        Magie.__init__(self,skill,agissant)

    def action(self):
        self.agissant.effets.append(Dopage(self.agissant,self.taux))

class MagieBoost(MagieDopage,CibleAgissant):
    """La magie qui crée un effet de dopage sur un autre agissant."""
    def __init__(self,skill:Actif,agissant:Agissant):
        MagieDopage.__init__(self,skill,agissant)
        CibleAgissant.__init__(self,skill,agissant)

    def action(self):
        if not self.cible: # NOONE is falsy
            self.interrompt()
        else:
            self.cible.effets.append(Dopage(self.agissant,self.taux))

class MagieMultiBoost(MagieDopage,CibleAgissants):
    """La magie qui crée un effet de dopage sur plusieurs autres agissants."""
    def __init__(self,skill:Actif,agissant:Agissant):
        MagieDopage.__init__(self,skill,agissant)
        CibleAgissants.__init__(self,skill,agissant)

    def action(self):
        for cible in self.cible:
            cible.effets.append(Dopage(self.agissant,self.taux))

magies_boost: dict[tuple[bool, bool], type[MagieDopage]] = {
    (False, False): MagieDopage,
    (True, False): MagieBoost,
    (True, True): MagieMultiBoost,
    (False, True): MagieDopage # Pas possible
}
"""
(cible, cible_multiple) -> MagieDopage
"""
