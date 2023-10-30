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
    from ...entitee.agissant.agissant import Agissant
    from ...entitee.item.item import Item
    from ...systeme.skill.actif import Actif

class MagieEnchantementConfusion(EnchanteAgissant):
    """La magie qui place un enchantement de confusion sur un agissant."""
    nom = "magie confusion"
    def __init__(self,skill:Actif,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,taux:float,duree:float,niveau:int,cible:Agissant):
        EnchanteAgissant.__init__(self,skill,agissant,gain_xp,cout_pm,latence,EnchantementConfusion(duree,taux),cible,niveau)

class MagieEnchantementPochesTrouees(EnchanteAgissant):
    """La magie qui place un enchantement de poches trouees sur un agissant."""
    nom = "magie poches trouees"
    def __init__(self,skill:Actif,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,taux:float,duree:float,niveau:int,cible:Agissant):
        EnchanteAgissant.__init__(self,skill,agissant,gain_xp,cout_pm,latence,EnchantementPochesTrouees(duree,taux),cible,niveau)

class MagieEnchantementForce(EnchanteAgissant):
    """La magie qui place un enchantement de force sur un agissant."""
    nom = "magie force"
    def __init__(self,skill:Actif,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,gain:float,duree:float,niveau:int,cible:Agissant):
        EnchanteAgissant.__init__(self,skill,agissant,gain_xp,cout_pm,latence,EnchantementForce(duree,gain),cible,niveau)

class MagieEnchantementVision(EnchanteAgissant):
    """La magie qui place un enchantement de vision sur un agissant."""
    nom = "magie vision"
    def __init__(self,skill:Actif,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,gain:float,duree:float,niveau:int,cible:Agissant):
        EnchanteAgissant.__init__(self,skill,agissant,gain_xp,cout_pm,latence,EnchantementVision(duree,gain),cible,niveau)

class MagieEnchantementVitalite(EnchanteAgissant):
    """La magie qui place un enchantement de vitalité sur un agissant."""
    nom = "magie vitalite"
    def __init__(self,skill:Actif,agissant:Agissant,gain_xp:int,cout_pm:int,latence:int,duree:int,gain_pv:int,niveau:int,cible:Agissant):
        EnchanteAgissant.__init__(self,skill,agissant,gain_xp,cout_pm,latence,EnchantementPv(duree,gain_pv),cible,niveau)

class MagieEnchantementAbsorption(EnchanteAgissant):
    """La magie qui place un enchantement d'absorption sur un agissant."""
    nom = "magie absorption"
    def __init__(self,skill:Actif,agissant:Agissant,gain_xp:int,cout_pm:int,latence:int,duree:int,gain_pm:int,niveau:int,cible:Agissant):
        EnchanteAgissant.__init__(self,skill,agissant,gain_xp,cout_pm,latence,EnchantementPm(duree,gain_pm),cible,niveau)

class MagieEnchantementCelerite(EnchanteAgissant):
    """La magie qui place un enchantement de célérité sur un agissant."""
    nom = "magie celerite"
    def __init__(self,skill:Actif,agissant:Agissant,gain_xp:int,cout_pm:int,latence:int,duree:int,gain_vitesse:int,niveau:int,cible:Agissant):
        EnchanteAgissant.__init__(self,skill,agissant,gain_xp,cout_pm,latence,EnchantementVitesse(duree,gain_vitesse),cible,niveau)

class MagieEnchantementImmunite(EnchanteAgissant):
    """La magie qui place un enchantement d'immunité sur un agissant."""
    nom = "magie immunite"
    def __init__(self,skill:Actif,agissant:Agissant,gain_xp:int,cout_pm:int,latence:int,duree:int,superiorite:int,niveau:int,cible:Agissant):
        EnchanteAgissant.__init__(self,skill,agissant,gain_xp,cout_pm,latence,EnchantementImmunite(duree,superiorite),cible,niveau)

class MagieEnchantementFlamme(EnchanteAgissant):
    """La magie qui place un enchantement de flamme sur un agissant."""
    nom = "magie flamme"
    def __init__(self,skill:Actif,agissant:Agissant,gain_xp:int,cout_pm:int,latence:int,duree:int,gain_affinite:int,niveau:int,cible:Agissant):
        EnchanteAgissant.__init__(self,skill,agissant,gain_xp,cout_pm,latence,EnchantementAffinite(duree,gain_affinite,Element.FEU),cible,niveau)

class MagieEnchantementNeige(EnchanteAgissant):
    """La magie qui place un enchantement de neige sur un agissant."""
    nom = "magie neige"
    def __init__(self,skill:Actif,agissant:Agissant,gain_xp:int,cout_pm:int,latence:int,duree:int,gain_affinite:int,niveau:int,cible:Agissant):
        EnchanteAgissant.__init__(self,skill,agissant,gain_xp,cout_pm,latence,EnchantementAffinite(duree,gain_affinite,Element.GLACE),cible,niveau)

class MagieEnchantementSable(EnchanteAgissant):
    """La magie qui place un enchantement de sable sur un agissant."""
    nom = "magie sable"
    def __init__(self,skill:Actif,agissant:Agissant,gain_xp:int,cout_pm:int,latence:int,duree:int,gain_affinite:int,niveau:int,cible:Agissant):
        EnchanteAgissant.__init__(self,skill,agissant,gain_xp,cout_pm,latence,EnchantementAffinite(duree,gain_affinite,Element.TERRE),cible,niveau)

class MagieEnchantementTenebre(EnchanteAgissant):
    """La magie qui place un enchantement de ténèbre sur un agissant."""
    nom = "magie tenebre"
    def __init__(self,skill:Actif,agissant:Agissant,gain_xp:int,cout_pm:int,latence:int,duree:int,gain_affinite:int,niveau:int,cible:Agissant):
        EnchanteAgissant.__init__(self,skill,agissant,gain_xp,cout_pm,latence,EnchantementAffinite(duree,gain_affinite,Element.OMBRE),cible,niveau)

class MagieEnchantementRenforcement(EnchanteItem):
    """La magie qui place un enchantement de renforcement sur un item."""
    nom = "magie renforcement"
    def __init__(self,skill:Actif,agissant:Agissant,gain_xp:int,cout_pm:int,latence:int,duree:int,gain_force:int,gain_portee:int,niveau:int,cible:Item):
        EnchanteItem.__init__(self,skill,agissant,gain_xp,cout_pm,latence,EnchantementArme(duree,gain_force,gain_portee),cible,niveau)

class MagieEnchantementBombe(EnchanteItem):
    """La magie qui place un enchantement de bombe sur un item."""
    nom = "magie bombe"
    def __init__(self,skill:Actif,agissant:Agissant,gain_xp:int,cout_pm:int,latence:int,duree:int,portee:int,degats:int,niveau:int,cible:Item):
        EnchanteItem.__init__(self,skill,agissant,gain_xp,cout_pm,latence,EnchantementBombe(duree,portee,degats),cible,niveau)
