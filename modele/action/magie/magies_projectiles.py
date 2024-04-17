from __future__ import annotations
from typing import TYPE_CHECKING

import carte as crt

# Imports des classes parentes
from .magie import MagieDirigee, CibleCase, PorteeLimitee
from ...entitee import projectiles_magiques, ProjectileMagique
from ...commons import Element

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ...entitee import Agissant, Projectile
    from ...systeme import Actif

class InvocationProjectile(MagieDirigee):
    """La classe des magies qui créent un projectile (avec une direction associée)."""
    percant: bool
    fleche: bool
    explosif: bool
    poids: float
    frottements: float
    portee: float
    degats: float
    element: Element
    fantome: bool
    def __init__(self,skill:Actif,agissant:Agissant):
        MagieDirigee.__init__(self,skill,agissant)
        classe = projectiles_magiques[(self.percant, self.fleche, self.explosif)]
        assert issubclass(classe, ProjectileMagique)
        self.projectile = classe(self.poids, self.frottements,
                                 self.portee, self.degats, self.element,
                                 crt.POSITION_ABSENTE)
        self.projectile.fantome = self.fantome
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
