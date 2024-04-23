"""
Les effets destinés à être placés dans des potions, avec possibilité de séjourner sur une case.
"""

from __future__ import annotations
from typing import TYPE_CHECKING

# Imports des classes parentes
from .potion import EffetMixte
from ..agissant import EffetAgissant, Antidote, Medicament, Purification, Soin, Vaccin, Immunite, EffetForce, EffetVision, EffetPv, EffetPm, EffetVitesse, EffetAffinite, EffetAffinites, EffetStats

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ...commons import Element

class AntidoteMixte(EffetMixte, Antidote):
    """Effet qui supprime les effets de poison de l'agissant et peut séjourner sur une case."""

class MedicamentMixte(EffetMixte, Medicament):
    """Effet qui supprime les effets de maladie de l'agissant et peut séjourner sur une case."""

class PurificationMixte(EffetMixte, Purification):
    """Effet qui supprime les effets de poison ou maladie de l'agissant et peut séjourner sur une case."""

class SoinMixte(EffetMixte, Soin):
    """Un effet de soin et peut séjourner sur une case."""

class VaccinMixte(EffetMixte, Vaccin):
    """Effet qui immunise l'agissant contre une maladie et peut séjourner sur une case."""

class ImmuniteMixte(EffetMixte, Immunite):
    """Enchantement qui confère une immunité aux maladies, à condition de disposer de suffisamment de priorité et peut séjourner sur une case."""

class BoostForce(EffetForce):
    """Effet qui démultiplie la force de l'agissant."""
    multiplicateur:float
    def modifie_force(self, force: float) -> float:
        return force * self.multiplicateur
    
class BoostForceMixte(EffetMixte, BoostForce):
    """Effet qui démultiplie la force de l'agissant et peut séjourner sur une case."""

class BoostVision(EffetVision):
    """Effet qui démultiplie la vision de l'agissant."""
    multiplicateur:float
    def modifie_vision(self, vision: float) -> float:
        return vision * self.multiplicateur
    
class BoostVisionMixte(EffetMixte, BoostVision):
    """Effet qui démultiplie la vision de l'agissant et peut séjourner sur une case."""

class BoostPv(EffetPv):
    """Effet qui démultiplie les points de vie de l'agissant."""
    multiplicateur:float
    def modifie_pv(self, pv: float) -> float:
        return pv * self.multiplicateur
    
class BoostPvMixte(EffetMixte, BoostPv):
    """Effet qui démultiplie les points de vie de l'agissant et peut séjourner sur une case."""

class BoostPm(EffetPm):
    """Effet qui démultiplie les points de mouvement de l'agissant."""
    multiplicateur:float
    def modifie_pm(self, pm: float) -> float:
        return pm * self.multiplicateur
    
class BoostPmMixte(EffetMixte, BoostPm):
    """Effet qui démultiplie les points de mouvement de l'agissant et peut séjourner sur une case."""

class BoostVitesse(EffetVitesse):
    """Effet qui démultiplie la vitesse de l'agissant."""
    multiplicateur:float
    def modifie_vitesse(self, vitesse: float) -> float:
        return vitesse * self.multiplicateur
    
class BoostVitesseMixte(EffetMixte, BoostVitesse):
    """Effet qui démultiplie la vitesse de l'agissant et peut séjourner sur une case."""

class BoostAffinite(EffetAffinite):
    """Effet qui démultiplie l'affinité de l'agissant."""
    multiplicateur:float
    def modifie_affinite(self, affinite: float) -> float:
        return affinite * self.multiplicateur
    
class BoostAffiniteMixte(EffetMixte, BoostAffinite):
    """Effet qui démultiplie l'affinité de l'agissant et peut séjourner sur une case."""

class BoostAffinites(EffetAffinites):
    """Effet qui démultiplie les affinités de l'agissant."""
    elements: set[Element]
    multiplicateur:float
    def modifie_affinite(self, affinite: float, element: Element) -> float:
        if element in self.elements:
            return affinite * self.multiplicateur
        return affinite
    
class BoostAffinitesMixte(EffetMixte, BoostAffinites):
    """Effet qui démultiplie les affinités de l'agissant et peut séjourner sur une case."""

class BoostStats(EffetStats):
    """Effet qui démultiplie les statistiques de l'agissant."""
    multiplicateur:float
    def modifie_stats(self, stat: float) -> float:
        return stat * self.multiplicateur
    
class BoostStatsMixte(EffetMixte, BoostStats):
    """Effet qui démultiplie les statistiques de l'agissant et peut séjourner sur une case."""

effets_potions: dict[tuple[str, bool], type[EffetAgissant]] = {
    ("antidote", False): Antidote,
    ("medicament", False): Medicament,
    ("purification", False): Purification,
    ("soin", False): Soin,
    ("vaccin", False): Vaccin,
    ("immunite", False): Immunite,
    ("antidote", True): AntidoteMixte,
    ("medicament", True): MedicamentMixte,
    ("purification", True): PurificationMixte,
    ("soin", True): SoinMixte,
    ("vaccin", True): VaccinMixte,
    ("immunite", True): ImmuniteMixte
}
"""
(nom, mixte) -> classe
"""

effets_boosts: dict[tuple[str, bool], type[EffetAgissant]] = {
    ("force", False): BoostForce,
    ("vision", False): BoostVision,
    ("pv", False): BoostPv,
    ("pm", False): BoostPm,
    ("vitesse", False): BoostVitesse,
    ("affinite", False): BoostAffinite,
    ("affinites", False): BoostAffinites,
    ("stats", False): BoostStats,
    ("force", True): BoostForceMixte,
    ("vision", True): BoostVisionMixte,
    ("pv", True): BoostPvMixte,
    ("pm", True): BoostPmMixte,
    ("vitesse", True): BoostVitesseMixte,
    ("affinite", True): BoostAffiniteMixte,
    ("affinites", True): BoostAffinitesMixte,
    ("stats", True): BoostStatsMixte
}
"""
(nom, mixte) -> classe
"""