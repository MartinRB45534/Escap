from __future__ import annotations

# Pas d'imports pour les annotations

# Imports des classes parentes
from ..Entitee.Agissant.Agissant import Agissant

class Bourrin(Agissant):
    """Les agissants qui combattent en fonçant dans le tas."""

    def veut_fuir(self,degats:float=0):
        return not(self.veut_attaquer(degats)) #Il n'y a pas d'autre choix que fuir ou attaquer