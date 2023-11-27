"""Contient la classe Effet et ses sous-classes."""

from __future__ import annotations

# Pas d'imports utilisés uniquement dans les annotations

# Pas de classe parente

class Effet :
    """Les effets regroupent des choses qui arrivent à des éléments du système. Ils peuvent cibler une case, un mur, un agissant, un étage, etc. et sont souvent limités dans le temps ou par d'autres conditions. Ils sont évalués par le controleur dans différentes circonstances."""
    def termine(self) -> bool:
        """Idique si l'effet est terminé."""
        return True
