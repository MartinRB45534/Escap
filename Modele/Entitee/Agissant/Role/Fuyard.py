from __future__ import annotations

# Pas d'imports pour les annotations

# Imports des classes parentes
from ..agissant import Agissant

class Fuyard(Agissant):
    """Des agissants qui ne font que fuire ? À quoi bon ?"""

    def comporte_distance(self,degats:float=0):
        return 3

    def veut_attaquer(self,degats:float=0):
        return False

    def veut_fuir(self,degats:float=0):
        return True
