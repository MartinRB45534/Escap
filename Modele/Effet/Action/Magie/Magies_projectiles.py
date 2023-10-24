from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import carte as crt

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ....entitee.agissant.agissant import Agissant
    from ....entitee.item.projectile.projectile import Projectile
    from ....systeme.skill.actif import Actif

# Imports des classes parentes
from .magie import Invocation_projectile,Cible_case,Portee_limitee

class Magie_projectile_decentre(Invocation_projectile,Cible_case,Portee_limitee):
    """La magie qui invoque une ombre futive."""
    nom = "magie ombre furtive"
    def __init__(self,skill:Actif,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,entitee:Projectile,direction:crt.Direction,portee:float,niveau:int,cible:Optional[crt.Position]=None):
        Invocation_projectile.__init__(self,skill,agissant,gain_xp,cout_pm,latence,entitee,direction,niveau)
        Portee_limitee.__init__(self,portee)
        Cible_case.__init__(self,cible)
