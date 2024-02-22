from __future__ import annotations
from typing import TYPE_CHECKING

# Imports des classes parentes
from .magie import InvocationProjectile,CibleCase,PorteeLimitee

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ...entitee import Agissant, Projectile
    from ...systeme import Actif, Magie

class ActionMagieProjectileDecentre(InvocationProjectile,CibleCase,PorteeLimitee):
    """La magie qui invoque une ombre futive."""
    nom = "magie ombre furtive"
    def __init__(self,skill:Actif,magie:Magie,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,entitee:Projectile,portee:float):
        InvocationProjectile.__init__(self,skill,magie,agissant,gain_xp,cout_pm,latence,entitee)
        PorteeLimitee.__init__(self,skill,magie,agissant,gain_xp,cout_pm,latence,portee)
        CibleCase.__init__(self,skill,magie,agissant,gain_xp,cout_pm,latence)
