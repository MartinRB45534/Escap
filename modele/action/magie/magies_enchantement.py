"""
Les magies qui placent un enchantement sur un agissant ou un item.
"""

from __future__ import annotations
from typing import TYPE_CHECKING

# Imports des classes parentes
from .magie import EnchanteAgissant, EnchanteItem

# Imports utilisés dans le code
from ...effet import EnchantementConfusion, EnchantementPochesTrouees, EnchantementForce, EnchantementVision, EnchantementPv, EnchantementPm, EnchantementVitesse, EnchantementImmunite, EnchantementAffinite, EnchantementArme, EnchantementBombe
from ...commons import Element

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ...entitee import Agissant
    from ...systeme import Actif, Magie

class ActionMagieEnchantementConfusion(EnchanteAgissant):
    """La magie qui place un enchantement de confusion sur un agissant."""
    nom = "magie confusion"
    def __init__(self,skill:Actif,magie:Magie,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,duree:float,taux_confusion:float):
        EnchanteAgissant.__init__(self,skill,magie,agissant,gain_xp,cout_pm,latence,EnchantementConfusion(duree,taux_confusion))

class ActionMagieEnchantementPochesTrouees(EnchanteAgissant):
    """La magie qui place un enchantement de poches trouees sur un agissant."""
    nom = "magie poches trouees"
    def __init__(self,skill:Actif,magie:Magie,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,duree:float,taux_perte:float):
        EnchanteAgissant.__init__(self,skill,magie,agissant,gain_xp,cout_pm,latence,EnchantementPochesTrouees(duree,taux_perte))

class ActionMagieEnchantementForce(EnchanteAgissant):
    """La magie qui place un enchantement de force sur un agissant."""
    nom = "magie force"
    def __init__(self,skill:Actif,magie:Magie,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,duree:float,gain_force:float):
        EnchanteAgissant.__init__(self,skill,magie,agissant,gain_xp,cout_pm,latence,EnchantementForce(duree,gain_force))

class ActionMagieEnchantementVision(EnchanteAgissant):
    """La magie qui place un enchantement de vision sur un agissant."""
    nom = "magie vision"
    def __init__(self,skill:Actif,magie:Magie,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,duree:float,gain_vision:float):
        EnchanteAgissant.__init__(self,skill,magie,agissant,gain_xp,cout_pm,latence,EnchantementVision(duree,gain_vision))

class ActionMagieEnchantementVitalite(EnchanteAgissant):
    """La magie qui place un enchantement de vitalité sur un agissant."""
    nom = "magie vitalite"
    def __init__(self,skill:Actif,magie:Magie,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,duree:float,gain_pv:float):
        EnchanteAgissant.__init__(self,skill,magie,agissant,gain_xp,cout_pm,latence,EnchantementPv(duree,gain_pv))

class ActionMagieEnchantementAbsorption(EnchanteAgissant):
    """La magie qui place un enchantement d'absorption sur un agissant."""
    nom = "magie absorption"
    def __init__(self,skill:Actif,magie:Magie,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,duree:float,gain_pm:float):
        EnchanteAgissant.__init__(self,skill,magie,agissant,gain_xp,cout_pm,latence,EnchantementPm(duree,gain_pm))

class ActionMagieEnchantementCelerite(EnchanteAgissant):
    """La magie qui place un enchantement de célérité sur un agissant."""
    nom = "magie celerite"
    def __init__(self,skill:Actif,magie:Magie,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,duree:float,gain_vitesse:float):
        EnchanteAgissant.__init__(self,skill,magie,agissant,gain_xp,cout_pm,latence,EnchantementVitesse(duree,gain_vitesse))

class ActionMagieEnchantementImmunite(EnchanteAgissant):
    """La magie qui place un enchantement d'immunité sur un agissant."""
    nom = "magie immunite"
    def __init__(self,skill:Actif,magie:Magie,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,duree:float,superiorite:float):
        EnchanteAgissant.__init__(self,skill,magie,agissant,gain_xp,cout_pm,latence,EnchantementImmunite(duree,superiorite))

class ActionMagieEnchantementAffinite(EnchanteAgissant):
    """La magie qui place un enchantement d'affinité élémentale sur un agissant."""
    nom = "magie flamme"
    def __init__(self,skill:Actif,magie:Magie,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,duree:float,gain_affinite:float,element:Element):
        EnchanteAgissant.__init__(self,skill,magie,agissant,gain_xp,cout_pm,latence,EnchantementAffinite(duree,gain_affinite,element))

class ActionMagieEnchantementRenforcement(EnchanteItem):
    """La magie qui place un enchantement de renforcement sur un item."""
    nom = "magie renforcement"
    def __init__(self,skill:Actif,magie:Magie,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,duree:float,gain_force:float,gain_portee:float):
        EnchanteItem.__init__(self,skill,magie,agissant,gain_xp,cout_pm,latence,EnchantementArme(duree,gain_force,gain_portee))

class ActionMagieEnchantementBombe(EnchanteItem):
    """La magie qui place un enchantement de bombe sur un item."""
    nom = "magie bombe"
    def __init__(self,skill:Actif,magie:Magie,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,duree:float,degats:float,portee:float):
        EnchanteItem.__init__(self,skill,magie,agissant,gain_xp,cout_pm,latence,EnchantementBombe(duree,portee,degats))

magies_enchantement: dict[str, type[EnchanteAgissant|EnchanteItem]] = {
    "confusion": ActionMagieEnchantementConfusion,
    "poches_trouees": ActionMagieEnchantementPochesTrouees,
    "force": ActionMagieEnchantementForce,
    "vision": ActionMagieEnchantementVision,
    "vitalite": ActionMagieEnchantementVitalite,
    "absorption": ActionMagieEnchantementAbsorption,
    "celerite": ActionMagieEnchantementCelerite,
    "immunite": ActionMagieEnchantementImmunite,
    "affinite": ActionMagieEnchantementAffinite,
    "renforcement": ActionMagieEnchantementRenforcement,
    "bombe": ActionMagieEnchantementBombe
}
"""
nom -> Enchantement
"""
