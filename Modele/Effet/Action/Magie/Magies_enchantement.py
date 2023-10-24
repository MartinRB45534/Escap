from __future__ import annotations
from typing import TYPE_CHECKING, Optional

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ....entitee.agissant.agissant import Agissant
    from ....systeme.skill.actif import Actif

# Imports des classes parentes
from .magie import Enchante_agissant, Enchante_item

class Magie_enchantement_confusion(Enchante_agissant):
    """La magie qui place un enchantement de confusion sur un agissant."""
    nom = "magie confusion"
    def __init__(self,skill:Actif,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,taux:float,duree:float,niveau:int,cible:Optional[Agissant]=None):
        Enchante_agissant.__init__(self,skill,agissant,gain_xp,cout_pm,latence,EnchantementConfusion(duree,taux),cible,niveau)

class Magie_enchantement_poches_trouees(Enchante_agissant):
    """La magie qui place un enchantement de poches trouees sur un agissant."""
    nom = "magie poches trouees"
    def __init__(self,skill:Actif,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,taux:float,duree:float,niveau:int,cible:Optional[Agissant]=None):
        Enchante_agissant.__init__(self,skill,agissant,gain_xp,cout_pm,latence,EnchantementPochesTrouees(duree,taux),cible,niveau)

class Magie_enchantement_force(Enchante_agissant):
    """La magie qui place un enchantement de force sur un agissant."""
    nom = "magie force"
    def __init__(self,skill:Actif,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,gain:float,duree:float,niveau:int,cible:Optional[Agissant]=None):
        Enchante_agissant.__init__(self,skill,agissant,gain_xp,cout_pm,latence,EnchantementForce(duree,gain),cible,niveau)

class Magie_enchantement_vision(Enchante_agissant):
    """La magie qui place un enchantement de vision sur un agissant."""
    nom = "magie vision"
    def __init__(self,skill:Actif,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,gain:float,duree:float,niveau:int,cible:Optional[Agissant]=None):
        Enchante_agissant.__init__(self,skill,agissant,gain_xp,cout_pm,latence,EnchantementVision(duree,gain),cible,niveau)

class Magie_enchantement_vitalite(Enchante_agissant):
    """La magie qui place un enchantement de vitalité sur un agissant."""
    nom = "magie vitalite"
    def __init__(self,skill:Actif,agissant:Agissant,gain_xp:int,cout_pm:int,latence:int,duree:int,gain_pv:int,niveau:int,cible:Optional[Agissant]=None):
        Enchante_agissant.__init__(self,skill,agissant,gain_xp,cout_pm,latence,EnchantementPv(duree,gain_pv),cible,niveau)

class Magie_enchantement_absorption(Enchante_agissant):
    """La magie qui place un enchantement d'absorption sur un agissant."""
    nom = "magie absorption"
    def __init__(self,skill:Actif,agissant:Agissant,gain_xp:int,cout_pm:int,latence:int,duree:int,gain_pm:int,niveau:int,cible:Optional[Agissant]=None):
        Enchante_agissant.__init__(self,skill,agissant,gain_xp,cout_pm,latence,EnchantementPm(duree,gain_pm),cible,niveau)

class Magie_enchantement_celerite(Enchante_agissant):
    """La magie qui place un enchantement de célérité sur un agissant."""
    nom = "magie celerite"
    def __init__(self,skill:Actif,agissant:Agissant,gain_xp:int,cout_pm:int,latence:int,duree:int,gain_vitesse:int,niveau:int,cible:Optional[Agissant]=None):
        Enchante_agissant.__init__(self,skill,agissant,gain_xp,cout_pm,latence,EnchantementVitesse(duree,gain_vitesse),cible,niveau)

class Magie_enchantement_immunite(Enchante_agissant):
    """La magie qui place un enchantement d'immunité sur un agissant."""
    nom = "magie immunite"
    def __init__(self,skill:Actif,agissant:Agissant,gain_xp:int,cout_pm:int,latence:int,duree:int,superiorite:int,niveau:int,cible:Optional[Agissant]=None):
        Enchante_agissant.__init__(self,skill,agissant,gain_xp,cout_pm,latence,EnchantementImmunite(duree,superiorite),cible,niveau)

class Magie_enchantement_flamme(Enchante_agissant):
    """La magie qui place un enchantement de flamme sur un agissant."""
    nom = "magie flamme"
    def __init__(self,skill:Actif,agissant:Agissant,gain_xp:int,cout_pm:int,latence:int,duree:int,gain_affinite:int,niveau:int,cible:Optional[Agissant]=None):
        Enchante_agissant.__init__(self,skill,agissant,gain_xp,cout_pm,latence,EnchantementFlamme(duree,gain_affinite),cible,niveau)

class Magie_enchantement_neige(Enchante_agissant):
    """La magie qui place un enchantement de neige sur un agissant."""
    nom = "magie neige"
    def __init__(self,skill:Actif,agissant:Agissant,gain_xp:int,cout_pm:int,latence:int,duree:int,gain_affinite:int,niveau:int,cible:Optional[Agissant]=None):
        Enchante_agissant.__init__(self,skill,agissant,gain_xp,cout_pm,latence,EnchantementNeige(duree,gain_affinite),cible,niveau)

class Magie_enchantement_sable(Enchante_agissant):
    """La magie qui place un enchantement de sable sur un agissant."""
    nom = "magie sable"
    def __init__(self,skill:Actif,agissant:Agissant,gain_xp:int,cout_pm:int,latence:int,duree:int,gain_affinite:int,niveau:int,cible:Optional[Agissant]=None):
        Enchante_agissant.__init__(self,skill,agissant,gain_xp,cout_pm,latence,EnchantementSable(duree,gain_affinite),cible,niveau)

class Magie_enchantement_tenebre(Enchante_agissant):
    """La magie qui place un enchantement de ténèbre sur un agissant."""
    nom = "magie tenebre"
    def __init__(self,skill:Actif,agissant:Agissant,gain_xp:int,cout_pm:int,latence:int,duree:int,gain_affinite:int,niveau:int,cible:Optional[Agissant]=None):
        Enchante_agissant.__init__(self,skill,agissant,gain_xp,cout_pm,latence,EnchantementTenebre(duree,gain_affinite),cible,niveau)

class Magie_enchantement_renforcement(Enchante_item):
    """La magie qui place un enchantement de renforcement sur un item."""
    nom = "magie renforcement"
    def __init__(self,skill:Actif,agissant:Agissant,gain_xp:int,cout_pm:int,latence:int,duree:int,gain_force:int,gain_portee:int,niveau:int,cible:Optional[Item]=None):
        Enchante_item.__init__(self,skill,agissant,gain_xp,cout_pm,latence,EnchantementArme(duree,gain_force,gain_portee),cible,niveau)

class Magie_enchantement_bombe(Enchante_item):
    """La magie qui place un enchantement de bombe sur un item."""
    nom = "magie bombe"
    def __init__(self,skill:Actif,agissant:Agissant,gain_xp:int,cout_pm:int,latence:int,duree:int,portee:int,degats:int,niveau:int,cible:Optional[Item]=None):
        Enchante_item.__init__(self,skill,agissant,gain_xp,cout_pm,latence,EnchantementBombe(duree,OnHit(portee,degats)),cible,niveau)

# Imports utilisés dans le code
from ...enchantements import *
from ...item.item import OnHit