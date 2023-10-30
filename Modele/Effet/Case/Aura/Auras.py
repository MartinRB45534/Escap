"""Contient les classes des effets d'auras élémentales."""

from __future__ import annotations
from typing import TYPE_CHECKING

# Imports des classes parentes
from ..cases import DegatsCase, Ralenti, Opacite
from .aura import Aura
from ...time_limited import TimeLimited

# Variables de classe
from ....commons import Element

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ....entitee.agissant.agissant import Agissant

# On va distinguer 3 types d'aura :
#   - Les auras naturellement attachées à une case. Ce sont des auras élémentaires. Elles peuvent être temporairement réprimée par une autre aura élémentale.
#   - Les auras non-élémentaires. Comme l'aura d'instakill ou l'aura divine, elles sont superposables autant qu'on veut, et attachées à un agissant.
#   - Les auras élémentaires attachées à un agissant. Celles qui nous embêtent le plus. La plus forte étouffe les autres, mais laisse les autres auras du même agissant s'exprimer.
# Peut-être considérer l'utilisation d'auras autour d'items comme la boule de feu ?

class AuraElementale(Aura):
    """La classe des effets d'auras élémentales. Attaché à la case."""
    element:Element

class AuraPermanente(AuraElementale): # Probablement les seuls effets permanents du jeu
    """La classe des effets d'aura élémentales permanentes, celles qui représentent l'élément par défaut de la case."""
    def termine(self) -> bool: # Les auras permanentes ne se terminent jamais
        return False

class AuraTemporaire(TimeLimited,AuraElementale):
    """La classe des effets d'aura élémentales temporaires, celles qui sont appliquées par un agissant."""
    def __init__(self,niveau:int,responsable:Agissant,temps_restant:float):
        TimeLimited.__init__(self,temps_restant)
        AuraElementale.__init__(self,niveau,responsable)
        self.priorite = 0

class Degressif(AuraTemporaire):
    """Une aura élémentale qui perd en priorité à chaque tour."""
    def __init__(self,niveau:int,responsable:Agissant,temps_restant:float,perte_priorite:float):
        AuraTemporaire.__init__(self,niveau,responsable,temps_restant)
        self.perte_priorite = perte_priorite

    def wait(self):
        self.temps_restant -= 1
        self.priorite -= self.perte_priorite

class AuraDegatsDegressif(Degressif,DegatsCase):
    """Une aura élémentale qui inflige des dégats, et qui perd en priorité et en dégats à chaque tour."""
    def __init__(self,niveau:int,responsable:Agissant,temps_restant:float,degats:float,perte_priorite:float,perte_degats:float):
        Degressif.__init__(self,niveau,responsable,temps_restant,perte_priorite)
        DegatsCase.__init__(self,degats,responsable)
        self.perte_degats = perte_degats

    def wait(self):
        self.temps_restant -= 1
        self.priorite -= self.perte_priorite
        self.degats -= self.perte_degats
    
class AuraDegats(AuraElementale,DegatsCase):
    """Une aura élémentale qui inflige des dégats."""
    def __init__(self,niveau:int,responsable:Agissant,degats:float):
        AuraElementale.__init__(self,niveau,responsable)
        DegatsCase.__init__(self,degats,responsable)

class AuraRalenti(AuraElementale,Ralenti):
    """Aura élémentale qui ralentit les agissants."""
    def __init__(self,niveau:int,responsable:Agissant,ralentissement:float):
        AuraElementale.__init__(self,niveau,responsable)
        Ralenti.__init__(self,ralentissement)

class AuraOpacite(AuraElementale,Opacite):
    """L'effet qui applique l'aura d'ombre à une case. Laissé ici par un agissant."""
    element = Element.OMBRE
    def __init__(self,niveau:int,responsable:Agissant,opacite:float):
        AuraElementale.__init__(self,niveau,responsable)
        Opacite.__init__(self,opacite)
