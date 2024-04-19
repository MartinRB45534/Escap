"""
Ce fichier contient les classes des projectiles et des items qui peuvent être lancés.
"""

from __future__ import annotations
from typing import TYPE_CHECKING
import carte as crt

# Imports des classes parentes
from .projectile import Projectile, Percant, Fragile, Evanescent

# Imports des valeurs par défaut des paramètres
from ....commons import Element
from ....effet import OnHit

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ....action import InvocationProjectile

class ProjectileSimple(Projectile):
    """Un projectile qui se contente d'un effet OnHit."""
    portee: float
    degats: float
    element: Element
    def __init__(self, position:crt.Position):
        Projectile.__init__(self,position)
        self.effets.add(OnHit(self.portee, self.degats, self.element))

class PercantSimple(Percant, ProjectileSimple):
    """Un projectile percant tout simple."""

class Fleche(Percant, ProjectileSimple):
    """La classe des projectiles de type flèche. Affectés différemment par certains skills."""

class Explosif(ProjectileSimple):
    """La classe des projectiles qui explosent. Affectés différemment par certains skills."""

class ExplosifPercant(Explosif, Percant):
    """Un explosif qui est aussi percant."""

class FlecheExplosive(Fleche,Explosif):
    """Une flèche explosive. C'est une flèche ou un explosif ? Mieux vaut rester loin en tous cas..."""

class FragileSimple(Fragile,ProjectileSimple):
    """Un fragile tout simple."""

class FragilePercant(FragileSimple, Percant):
    """Un fragile percant."""

class FlecheFragile(Fleche, FragileSimple):
    """Une flèche plus fragile que la normale."""

class ExplosifFragile(Explosif, FragileSimple):
    """Un explosif qui se brise à l'impact."""

class ExplosifFragilePercant(ExplosifFragile, FragilePercant):
    """Un explosif qui se brise à l'impact et qui est percant."""

class FlecheExplosiveFragile(FlecheExplosive, FragileSimple):
    """Une flèche explosive qui se brise à l'impact."""

class ProjectileMagique(ProjectileSimple, Evanescent):
    """La classe des projectiles créés par magie."""
    magie: InvocationProjectile

class MagiePercante(Percant, ProjectileMagique):
    """La classe des projectiles percants créés par magie."""

class MagieExplosive(Explosif, ProjectileMagique):
    """La classe des projectiles explosifs créés par magie."""

class FlecheMagique(Fleche, ProjectileMagique):
    """La classe des flèches créées par magie."""

class FlecheExplosiveMagique(FlecheExplosive, ProjectileMagique):
    """La classe des flèches explosives créées par magie."""

class MagieExplosivePercante(MagieExplosive, Percant):
    """La classe des projectiles explosifs perçant créés par magie."""

projectiles: dict[tuple[bool, bool, bool], type[ProjectileSimple]] = {
    (False, False, False): ProjectileSimple,
    (True, False, False): PercantSimple,
    (False, True, False): Fleche,
    (True, True, False): Fleche,
    (False, False, True): Explosif,
    (True, False, True): ExplosifPercant,
    (False, True, True): FlecheExplosive,
    (True, True, True): FlecheExplosive,
} # Les projectiles "permanents"
"""
(percant, fleche, explosif)
percant est ignoré si fleche est True
"""
projectiles_fragiles: dict[tuple[bool, bool, bool], type[FragileSimple]] = {
    (False, False, False): FragileSimple,
    (True, False, False): FragilePercant,
    (False, True, False): FlecheFragile,
    (True, True, False): FlecheFragile,
    (False, False, True): ExplosifFragile,
    (True, False, True): ExplosifFragilePercant,
    (False, True, True): FlecheExplosiveFragile,
    (True, True, True): FlecheExplosiveFragile,
} # Les projectiles fragiles, créés par des skills
"""
(percant, fleche, explosif)
percant est ignoré si fleche est True
"""
projectiles_magiques: dict[tuple[bool, bool, bool], type[ProjectileMagique]] = {
    (False, False, False): ProjectileMagique,
    (True, False, False): MagiePercante,
    (False, True, False): FlecheMagique,
    (True, True, False): FlecheMagique,
    (False, False, True): MagieExplosive,
    (True, False, True): MagieExplosivePercante,
    (False, True, True): FlecheExplosiveMagique,
    (True, True, True): FlecheExplosiveMagique,
} # Les projectiles magiques, créés par des magies
"""
(percant, fleche, explosif)
percant est ignoré si fleche est True
"""
