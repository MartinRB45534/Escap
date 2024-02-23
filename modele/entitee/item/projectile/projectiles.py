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
    from ....labyrinthe import Labyrinthe
    from ....action import InvocationProjectile

class ProjectileSimple(Projectile):
    """Un projectile qui se contente d'un effet OnHit."""
    def __init__(self, labyrinthe:Labyrinthe, poids:float, frottements:float, portee:float, degats:float, element:Element, position:crt.Position=crt.POSITION_ABSENTE):
        Projectile.__init__(self,labyrinthe,[OnHit(portee,degats,element)],position)
        self.poids = poids
        self.frottements = frottements

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

class FragilePercant(ProjectileSimple, Percant, Fragile):
    """Un fragile percant."""

class FlecheFragile(Fleche,Fragile):
    """Une flèche plus fragile que la normale."""

class ExplosifFragile(Explosif,Fragile):
    """Un explosif qui se brise à l'impact."""

class ExplosifFragilePercant(ExplosifFragile,Percant):
    """Un explosif qui se brise à l'impact et qui est percant."""

class FlecheExplosiveFragile(FlecheExplosive,Fragile):
    """Une flèche explosive qui se brise à l'impact."""

class ProjectileMagique(ProjectileSimple,Evanescent):
    magie: InvocationProjectile
    """La classe des projectiles créés par magie."""

class MagiePercante(Percant,ProjectileMagique):
    """La classe des projectiles percants créés par magie."""

class MagieExplosive(Explosif,ProjectileMagique):
    """La classe des projectiles explosifs créés par magie."""

class FlecheMagique(Fleche,ProjectileMagique):
    """La classe des flèches créées par magie."""

class FlecheExplosiveMagique(FlecheExplosive,ProjectileMagique):
    """La classe des flèches explosives créées par magie."""

class MagieExplosivePercante(MagieExplosive,Percant):
    """La classe des projectiles explosifs perçant créés par magie."""

projectiles: dict[tuple[bool, bool, bool, bool, bool], type[ProjectileSimple]] = {
    (False, False, False, False, False): ProjectileSimple,
    (True, False, False, False, False): PercantSimple,
    (False, True, False, False, False): Fleche,
    (True, True, False, False, False): Fleche,
    (False, False, True, False, False): Explosif,
    (True, False, True, False, False): ExplosifPercant,
    (False, True, True, False, False): FlecheExplosive,
    (True, True, True, False, False): FlecheExplosive,
    (False, False, False, True, False): FragileSimple,
    (True, False, False, True, False): FragilePercant,
    (False, True, False, True, False): FlecheFragile,
    (True, True, False, True, False): FlecheFragile,
    (False, False, True, True, False): ExplosifFragile,
    (True, False, True, True, False): ExplosifFragilePercant,
    (False, True, True, True, False): FlecheExplosiveFragile,
    (True, True, True, True, False): FlecheExplosiveFragile,
    (False, False, False, False, True): ProjectileMagique,
    (True, False, False, False, True): MagiePercante,
    (False, True, False, False, True): FlecheMagique,
    (True, True, False, False, True): FlecheMagique,
    (False, False, True, False, True): MagieExplosive,
    (True, False, True, False, True): MagieExplosivePercante,
    (False, True, True, False, True): FlecheExplosiveMagique,
    (True, True, True, False, True): FlecheExplosiveMagique,
    (False, False, False, True, True): MagiePercante,
    (True, False, False, True, True): MagiePercante,
    (False, True, False, True, True): FlecheMagique,
    (True, True, False, True, True): FlecheMagique,
    (False, False, True, True, True): MagieExplosivePercante,
    (True, False, True, True, True): MagieExplosivePercante,
    (False, True, True, True, True): FlecheExplosiveMagique,
    (True, True, True, True, True): FlecheExplosiveMagique
}
"""
(percant, fleche, explosif, fragile, magique)
percant est ignoré si fleche est True
fragile est ignoré si magique est True
"""
