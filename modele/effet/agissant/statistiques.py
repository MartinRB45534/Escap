"""
Les effets qui affectent les statistiques des agissants.
"""

from __future__ import annotations
from typing import TYPE_CHECKING

# Imports des classes parentes
from .agissant import EffetAgissant

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ...commons.elements import Element

class EffetForce(EffetAgissant):
    """Les effets qui affectent la force (en positif ou négatif)."""
    def modifie_force(self, force:float) -> float:
        """Modifie la stat force de l'agissant."""
        raise NotImplementedError

class EffetVision(EffetAgissant):
    """Les effets qui affectent le champ de vision (en positif ou négatif)."""
    def modifie_vision(self, vision:float) -> float:
        """Modifie la stat vision de l'agissant."""
        raise NotImplementedError

class EffetPv(EffetAgissant):
    """Les effets qui affectent la régénération des PV (en positif ou négatif)."""
    def modifie_pv(self, pv:float) -> float:
        """Modifie la stat pv de l'agissant."""
        raise NotImplementedError

class EffetPm(EffetAgissant):
    """Les effets qui affectent la régénération des PM (en positif ou négatif)."""
    def modifie_pm(self, pm:float) -> float:
        """Modifie la stat pm de l'agissant."""
        raise NotImplementedError

class EffetVitesse(EffetAgissant):
    """Les effets qui affectent la vitesse (en positif ou négatif)."""
    def modifie_vitesse(self, vitesse:float) -> float:
        """Modifie la stat vitesse de l'agissant."""
        raise NotImplementedError

class EffetAffinite(EffetAgissant):
    """Effet qui augmente l'affinité à un élément."""
    element:Element
    def modifie_affinite(self, affinite:float) -> float:
        """Modifie l'affinité à l'élément de l'agissant."""
        raise NotImplementedError

class EffetAffinites(EffetAgissant):
    """Effet qui modifie les affinités à plusieurs éléments."""
    def modifie_affinite(self, affinite:float, elements:Element) -> float:
        """Modifie l'affinité à l'élément de l'agissant."""
        raise NotImplementedError

class EffetStats(EffetAgissant):
    """Effet qui modifie toutes les statistiques."""
    def modifie_stats(self, stat:float) -> float:
        """Modifie toutes les statistiques de l'agissant."""
        raise NotImplementedError
