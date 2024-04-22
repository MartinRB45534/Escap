"""
Les enchantements des agissants
"""

from __future__ import annotations

# Imports des classes parentes
from .enchantement import EnchantementAgissant
from .statistiques import EffetForce, EffetVision, EffetPv, EffetPm, EffetVitesse, EffetAffinite
from .troubles_du_comportement import Confusion, PochesTrouees
from .sante import Immunite

class EnchantementForce(EnchantementAgissant, EffetForce):
    """Les Enchantements qui affectent la force (en positif ou négatif)."""
    gain_force: float
    def modifie_force(self, force:float) -> float:
        return force + self.gain_force

class EnchantementVision(EnchantementAgissant, EffetVision):
    """Les Enchantements qui affectent le champ de vision (en positif ou négatif)."""
    gain_vision: float
    def modifie_vision(self, vision:float) -> float:
        return vision + self.gain_vision

class EnchantementPv(EnchantementAgissant, EffetPv):
    """Les Enchantements qui affectent la régénération des PV (en positif ou négatif)."""
    gain_pv: float
    def modifie_pv(self, pv:float) -> float:
        return pv + self.gain_pv

class EnchantementPm(EnchantementAgissant, EffetPm):
    """Les Enchantements qui affectent la régénération des PM (en positif ou négatif)."""
    gain_pm: float
    def modifie_pm(self, pm:float) -> float:
        return pm + self.gain_pm

class EnchantementConfusion(EnchantementAgissant, Confusion):
    """Les Enchantements qui provoque des erreurs de direction."""

class EnchantementPochesTrouees(EnchantementAgissant, PochesTrouees):
    """Les Enchantements qui fait droper des items involontairement."""

class EnchantementVitesse(EnchantementAgissant, EffetVitesse):
    """Les Enchantements qui affectent la vitesse (en positif ou négatif)."""
    gain_vitesse: float
    def modifie_vitesse(self, vitesse:float) -> float:
        return vitesse + self.gain_vitesse

class EnchantementImmunite(EnchantementAgissant, Immunite):
    """Enchantement qui confère une immunité aux maladies, à condition de disposer de suffisamment de priorité."""

class EnchantementAffinite(EnchantementAgissant, EffetAffinite):
    """Enchantement qui augmente l'affinité à l'élément feu."""
    gain_aff: float
    def modifie_affinite(self, affinite:float) -> float:
        return affinite + self.gain_aff

enchantements_agissants: dict[str, type[EnchantementAgissant]] = {
    "confusion": EnchantementConfusion,
    "poches_trouees": EnchantementPochesTrouees,
    "force": EnchantementForce,
    "vision": EnchantementVision,
    "vitalite": EnchantementPv,
    "absorption": EnchantementPm,
    "celerite": EnchantementVitesse,
    "immunite": EnchantementImmunite,
    "affinite": EnchantementAffinite,
}
"""
nom -> Type[EnchantementAgissant]
"""
