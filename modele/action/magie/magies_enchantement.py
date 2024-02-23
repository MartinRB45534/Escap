"""
Les magies qui placent un enchantement sur un agissant ou un item.
"""

from __future__ import annotations
from typing import TYPE_CHECKING

# Imports des classes parentes
from .magie import Enchante, EnchanteAgissant, EnchanteItem

# Imports utilisés dans le code
from ...effet import EnchantementConfusion, EnchantementPochesTrouees, EnchantementForce, EnchantementVision, EnchantementPv, EnchantementPm, EnchantementVitesse, EnchantementImmunite, EnchantementAffinite, EnchantementArme, EnchantementBombe
from ...commons import Element

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ...entitee import Agissant
    from ...systeme import Actif

class MagieEnchantementConfusion(EnchanteAgissant):
    """La magie qui place un enchantement de confusion sur un agissant."""
    taux_confusion: float
    def __init__(self,skill:Actif,agissant:Agissant):
        EnchanteAgissant.__init__(self,skill,agissant)
        self.enchantement = EnchantementConfusion(self.duree,self.taux_confusion)

class MagieEnchantementPochesTrouees(EnchanteAgissant):
    """La magie qui place un enchantement de poches trouees sur un agissant."""
    taux_perte: float
    def __init__(self,skill:Actif,agissant:Agissant):
        EnchanteAgissant.__init__(self,skill,agissant)
        self.enchantement = EnchantementPochesTrouees(self.duree,self.taux_perte)

class MagieEnchantementForce(EnchanteAgissant):
    """La magie qui place un enchantement de force sur un agissant."""
    gain_force: float
    def __init__(self,skill:Actif,agissant:Agissant):
        EnchanteAgissant.__init__(self,skill,agissant)
        self.enchantement = EnchantementForce(self.duree,self.gain_force)

class MagieEnchantementVision(EnchanteAgissant):
    """La magie qui place un enchantement de vision sur un agissant."""
    gain_vision: float
    def __init__(self,skill:Actif,agissant:Agissant):
        EnchanteAgissant.__init__(self,skill,agissant)
        self.enchantement = EnchantementVision(self.duree,self.gain_vision)

class MagieEnchantementVitalite(EnchanteAgissant):
    """La magie qui place un enchantement de vitalité sur un agissant."""
    gain_pv: float
    def __init__(self,skill:Actif,agissant:Agissant):
        EnchanteAgissant.__init__(self,skill,agissant)
        self.enchantement = EnchantementPv(self.duree,self.gain_pv)

class MagieEnchantementAbsorption(EnchanteAgissant):
    """La magie qui place un enchantement d'absorption sur un agissant."""
    gain_pm: float
    def __init__(self,skill:Actif,agissant:Agissant):
        EnchanteAgissant.__init__(self,skill,agissant)
        self.enchantement = EnchantementPm(self.duree,self.gain_pm)

class MagieEnchantementCelerite(EnchanteAgissant):
    """La magie qui place un enchantement de célérité sur un agissant."""
    gain_vitesse: float
    def __init__(self,skill:Actif,agissant:Agissant):
        EnchanteAgissant.__init__(self,skill,agissant)
        self.enchantement = EnchantementVitesse(self.duree,self.gain_vitesse)

class MagieEnchantementImmunite(EnchanteAgissant):
    """La magie qui place un enchantement d'immunité sur un agissant."""
    superiorite: float
    def __init__(self,skill:Actif,agissant:Agissant):
        EnchanteAgissant.__init__(self,skill,agissant)
        self.enchantement = EnchantementImmunite(self.duree,self.superiorite)

class MagieEnchantementAffinite(EnchanteAgissant):
    """La magie qui place un enchantement d'affinité élémentale sur un agissant."""
    gain_affinite: float
    element: Element
    def __init__(self,skill:Actif,agissant:Agissant):
        EnchanteAgissant.__init__(self,skill,agissant)
        self.enchantement = EnchantementAffinite(self.duree,self.gain_affinite,self.element)

class MagieEnchantementRenforcement(EnchanteItem):
    """La magie qui place un enchantement de renforcement sur un item."""
    gain_force: float
    gain_portee: float
    def __init__(self,skill:Actif,agissant:Agissant):
        EnchanteItem.__init__(self,skill,agissant)
        self.enchantement = EnchantementArme(self.duree,self.gain_force,self.gain_portee)

class MagieEnchantementBombe(EnchanteItem):
    """La magie qui place un enchantement de bombe sur un item."""
    portee: float
    degats: float
    def __init__(self,skill:Actif,agissant:Agissant):
        EnchanteItem.__init__(self,skill,agissant)
        self.enchantement = EnchantementBombe(self.duree,self.portee,self.degats)

magies_enchantement: dict[str, type[Enchante]] = {
    "confusion": MagieEnchantementConfusion,
    "poches_trouees": MagieEnchantementPochesTrouees,
    "force": MagieEnchantementForce,
    "vision": MagieEnchantementVision,
    "vitalite": MagieEnchantementVitalite,
    "absorption": MagieEnchantementAbsorption,
    "celerite": MagieEnchantementCelerite,
    "immunite": MagieEnchantementImmunite,
    "affinite": MagieEnchantementAffinite,
    "renforcement": MagieEnchantementRenforcement,
    "bombe": MagieEnchantementBombe
}
"""
nom -> Enchantement
"""
