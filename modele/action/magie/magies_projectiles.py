from __future__ import annotations
from typing import TYPE_CHECKING

import carte as crt

# Imports des classes parentes
from .magie import MagieDirigee, CibleCase, PorteeLimitee

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ...entitee import Agissant, Projectile, ProjectileMagique
    from ...systeme import Actif

class InvocationProjectile(MagieDirigee):
    """La classe des magies qui créent un projectile (avec une direction associée)."""
    classe: type[ProjectileMagique]
    def __init__(self,skill:Actif,agissant:Agissant):
        MagieDirigee.__init__(self,skill,agissant)
        self.projectile = self.classe(crt.POSITION_ABSENTE)
        self.projectile.magie = self

    def invoque(self) -> Projectile:
        """Renvoie le projectile invoqué."""
        self.projectile.direction = self.direction
        return self.projectile

class MagieProjectileDecentre(InvocationProjectile,CibleCase,PorteeLimitee):
    """La magie qui invoque un projectile ailleurs que sur la case du lanceur."""
    def __init__(self,skill:Actif,agissant:Agissant):
        InvocationProjectile.__init__(self,skill,agissant)
        PorteeLimitee.__init__(self,skill,agissant)
        CibleCase.__init__(self,skill,agissant)

magies_projectiles: dict[bool, type[InvocationProjectile]] = {
    False: InvocationProjectile,
    True: MagieProjectileDecentre
}
"""
cible -> InvocationProjectile
"""
