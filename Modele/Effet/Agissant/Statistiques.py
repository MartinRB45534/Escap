from __future__ import annotations
from typing import TYPE_CHECKING

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ...Systeme.Elements import Element

# Imports des classes parentes
from .Agissant import Effet_agissant

class Effet_force(Effet_agissant):
    """Les effets qui affectent la force (en positif ou négatif)."""
    def modifie_force(self, force:float) -> float:
        raise NotImplementedError

class Effet_vision(Effet_agissant):
    """Les effets qui affectent le champ de vision (en positif ou négatif)."""
    def modifie_vision(self, vision:float) -> float:
        raise NotImplementedError

class Effet_pv(Effet_agissant):
    """Les effets qui affectent la régénération des PV (en positif ou négatif)."""
    def modifie_pv(self, pv:float) -> float:
        raise NotImplementedError

class Effet_pm(Effet_agissant):
    """Les effets qui affectent la régénération des PM (en positif ou négatif)."""
    def modifie_pm(self, pm:float) -> float:
        raise NotImplementedError

class Effet_vitesse(Effet_agissant):
    """Les effets qui affectent la vitesse (en positif ou négatif)."""
    def modifie_vitesse(self, vitesse:float) -> float:
        raise NotImplementedError

class Effet_affinite(Effet_agissant):
    """Effet qui augmente l'affinité à un élément."""
    element:Element
    def modifie_affinite(self, affinite:float) -> float:
        raise NotImplementedError
    
class Effet_stats(Effet_agissant):
    """Effet qui modifie toutes les statistiques."""
    def modifie_stats(self, stat:float) -> float:
        raise NotImplementedError