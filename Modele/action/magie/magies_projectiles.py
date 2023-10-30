from __future__ import annotations
from typing import TYPE_CHECKING
import carte as crt

# Imports des classes parentes
from .magie import InvocationProjectile,CibleCase,PorteeLimitee

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ...entitee.agissant.agissant import Agissant
    from ...entitee.item.projectile.projectile import Projectile
    from ...systeme.skill.actif import Actif

class MagieProjectileDecentre(InvocationProjectile,CibleCase,PorteeLimitee):
    """La magie qui invoque une ombre futive."""
    nom = "magie ombre furtive"
    def __init__(self,skill:Actif,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,entitee:Projectile,direction:crt.Direction,portee:float,niveau:int,cible:crt.Position=crt.POSITION_ABSENTE):
        InvocationProjectile.__init__(self,skill,agissant,gain_xp,cout_pm,latence,entitee,direction,niveau)
        PorteeLimitee.__init__(self,skill,agissant,gain_xp,cout_pm,latence,niveau,portee)
        CibleCase.__init__(self,skill,agissant,gain_xp,cout_pm,latence,niveau,cible)
