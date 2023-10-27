"""
Les enchantements.
"""

from __future__ import annotations

# Imports des classes parentes
from .agissant.enchantement import EnchantementAgissant
from .agissant.statistiques import EffetForce, EffetVision, EffetPv, EffetPm, EffetVitesse, EffetAffinite
from .agissant.troubles_du_comportement import Confusion, PochesTrouees
from .agissant.sante.soins import Immunite
from .item.enchantement import EnchantementItem
from .item.items import EffetPortee, EffetTranchant, EffetBombe

# Imports des valeurs par défaut des paramètres
from ..commons import Element

class EnchantementForce(EnchantementAgissant,EffetForce):
    """Les Enchantements qui affectent la force (en positif ou négatif)."""
    def __init__(self,temps_restant:float,gain_force:float):
        EnchantementAgissant.__init__(self,temps_restant)
        self.gain_force = gain_force

    def modifie_force(self, force:float) -> float:
        return force + self.gain_force

class EnchantementVision(EnchantementAgissant,EffetVision):
    """Les Enchantements qui affectent le champ de vision (en positif ou négatif)."""
    def __init__(self,temps_restant:float,gain_vision:float):
        EnchantementAgissant.__init__(self,temps_restant)
        self.gain_vision = gain_vision

    def modifie_vision(self, vision:float) -> float:
        return vision + self.gain_vision

class EnchantementPv(EnchantementAgissant,EffetPv):
    """Les Enchantements qui affectent la régénération des PV (en positif ou négatif)."""
    def __init__(self,temps_restant:float,gain_pv:float):
        EnchantementAgissant.__init__(self,temps_restant)
        self.gain_pv = gain_pv

    def modifie_pv(self, pv:float) -> float:
        return pv + self.gain_pv

class EnchantementPm(EnchantementAgissant,EffetPm):
    """Les Enchantements qui affectent la régénération des PM (en positif ou négatif)."""
    def __init__(self,temps_restant:float,gain_pm:float):
        EnchantementAgissant.__init__(self,temps_restant)
        self.gain_pm = gain_pm

    def modifie_pm(self, pm:float) -> float:
        return pm + self.gain_pm

class EnchantementConfusion(EnchantementAgissant,Confusion):
    """Les Enchantements qui provoque des erreurs de direction."""
    def __init__(self,temps_restant:float,taux_erreur:float):
        EnchantementAgissant.__init__(self,temps_restant)
        Confusion.__init__(self,taux_erreur)

class EnchantementPochesTrouees(EnchantementAgissant,PochesTrouees):
    """Les Enchantements qui fait droper des items involontairement."""
    def __init__(self,temps_restant:float,taux_drop:float):
        EnchantementAgissant.__init__(self,temps_restant)
        PochesTrouees.__init__(self,taux_drop)

class EnchantementVitesse(EnchantementAgissant,EffetVitesse):
    """Les Enchantements qui affectent la vitesse (en positif ou négatif)."""
    def __init__(self,temps_restant:float,gain_vitesse:float):
        EnchantementAgissant.__init__(self,temps_restant)
        self.gain_vitesse = gain_vitesse

    def modifie_vitesse(self, vitesse:float) -> float:
        return vitesse + self.gain_vitesse

class EnchantementImmunite(EnchantementAgissant,Immunite):
    """Enchantement qui confère une immunité aux maladies, à condition de disposer de suffisamment de priorité."""
    def __init__(self,temps_restant:float,superiorite:float):
        EnchantementAgissant.__init__(self,temps_restant)
        Immunite.__init__(self,superiorite)

class EnchantementAffinite(EnchantementAgissant,EffetAffinite):
    """Enchantement qui augmente l'affinité à l'élément feu."""
    def __init__(self,temps_restant:float,gain_aff:float,element:Element):
        EnchantementAgissant.__init__(self,temps_restant)
        EffetAffinite.__init__(self,element)
        self.gain_aff = gain_aff

    def modifie_affinite(self, affinite:float) -> float:
        return affinite + self.gain_aff

class EnchantementArme(EnchantementItem,EffetTranchant,EffetPortee):
    """Enchantement qui modifie les statistiques d'une arme (en positif ou négatif)."""
    def __init__(self,temps_restant:float,gain_force:float,gain_portee:float):
        EnchantementItem.__init__(self,temps_restant)
        self.gain_force = gain_force
        self.gain_portee = gain_portee

    def modifie_portee(self, portee: float) -> float:
        return portee + self.gain_portee

    def modifie_tranchant(self, tranchant: float) -> float:
        return tranchant + self.gain_force

class EnchantementBombe(EnchantementItem,EffetBombe):
    """Enchantement qui confère des propriétés explosives à un item."""
    def __init__(self,temps_restant:float,portee:float,degats:float,element:Element=Element.TERRE):
        EnchantementItem.__init__(self,temps_restant)
        EffetBombe.__init__(self,portee,degats,element)
