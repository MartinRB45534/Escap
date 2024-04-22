from __future__ import annotations
from typing import TYPE_CHECKING

import carte as crt

# Imports des classes parentes
from .magie import MagieDirigee, CibleCase, PorteeLimitee

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ...entitee import Projectile, ProjectileMagique

class InvocationProjectile(MagieDirigee):
    """La classe des magies qui créent un projectile (avec une direction associée)."""
    projectile: type[ProjectileMagique]

    def invoque(self) -> Projectile:
        """Renvoie le projectile invoqué."""
        projectile = self.projectile(crt.POSITION_ABSENTE)
        projectile.direction = self.direction
        projectile.magie = self
        return projectile

class MagieProjectileDecentre(InvocationProjectile,CibleCase,PorteeLimitee):
    """La magie qui invoque un projectile ailleurs que sur la case du lanceur."""

magies_projectiles: dict[bool, type[InvocationProjectile]] = {
    False: InvocationProjectile,
    True: MagieProjectileDecentre
}
"""
cible -> InvocationProjectile
"""
