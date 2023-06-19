from __future__ import annotations
from typing import TYPE_CHECKING

from Modele.Labyrinthe.Case import Case

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ..Entitee.Agissant.Agissant import Agissant
    from ..Labyrinthe.Case import Case

# Imports des classes parentes
from .Effet import Aura, One_shot, On_debut_tour, Evenement

# Variables de classe
from ..Systeme.Elements import Element

# On va distinguer 3 types d'aura :
#   - Les auras naturellement attachées à une case. Ce sont des auras élémentaires. Elles peuvent être temporairement réprimée par une autre aura élémentale.
#   - Les auras non-élémentaires. Comme l'aura d'instakill ou l'aura divine, elles sont superposables autant qu'on veut, et attachées à un agissant.
#   - Les auras élémentaires attachées à un agissant. Celles qui nous embêtent le plus. La plus forte étouffe les autres, mais laisse les autres auras du même agissant s'exprimer.
# Peut-être considérer l'utilisation d'auras autour d'items comme la boule de feu ?

class Aura_elementale(Aura):
    """La classe des effets d'auras élémentales. Attaché à la case."""
    element:Element
    def __init__(self,niveau:int):
        self.phase = "démarrage"
        self.responsable = NOONE
        self.priorite = 0
        self.affiche = False

    def action(self, case:Case):
        """L'action de l'aura élémentale. Elle est appelée par le controleur."""
        pass

class Aura_permanente(Aura_elementale):
    """La classe des effets d'aura élémentales permanentes, celles qui représentent l'élément par défaut de la case."""

    def execute(self,case:Case):
        if self.phase == "démarrage":
            self.phase = "en cours"

class Aura_temporaire(Evenement,Aura_elementale):
    """La classe des effets d'aura élémentales temporaires, celles qui sont appliquées par un agissant."""
    def __init__(self,responsable:Agissant,priorite:float):
        self.phase = "démarrage"
        self.responsable = responsable
        self.priorite = priorite
        self.distance = 0
        self.affiche = False

class Degats(Aura_elementale):
    """Une aura élémentale qui inflige des dégats."""
    def __init__(self,degats:float):
        self.degats = degats

    def action(self,case:Case):
        occupant = case.agissant
        if occupant is not None and occupant.esprit != self.responsable.esprit :
            occupant.subit(self.degats,self.element)

class Degressif(Aura_temporaire):
    """Une aura élémentale qui perd en priorité à chaque tour."""
    def __init__(self, perte_priorite:float):
        self.perte_priorite = perte_priorite

    def execute(self, case:Case):
        self.temps_restant -= 1
        self.priorite -= self.perte_priorite
        if self.phase == "démarrage" :
            self.phase = "en cours"
        elif self.temps_restant <= 0 :
            self.termine()
        else :
            self.action(case)

class Degats_degressif(Degressif,Degats):
    """Une aura élémentale qui inflige des dégats, et qui perd en priorité et en dégats à chaque tour."""
    def __init__(self,degats:float,perte_priorite:float,perte_degats:float):
        Degressif.__init__(self,perte_priorite)
        Degats.__init__(self,degats)
        self.perte_degats = perte_degats

    def execute(self, case: Case):
        self.temps_restant -= 1
        self.priorite -= self.perte_priorite
        self.degats -= self.perte_degats
        if self.phase == "démarrage" :
            self.phase = "en cours"
        elif self.temps_restant <= 0 :
            self.termine()
        else :
            self.action(case)

class Modification_vitesse(Aura_elementale):
    """Aura élémentale qui ralentit les agissants."""
    def __init__(self,coef_vitesse:float):
        self.coef_vitesse = coef_vitesse

    def action(self,case:Case):
        pass # Les statistiques s'occupent de tout

class Modification_opacite(Aura_elementale):
    """L'effet qui applique l'aura d'ombre à une case. Laissé ici par un agissant."""
    element = Element.OMBRE
    def __init__(self,coef_opacite:float):
        self.coef_opacite = coef_opacite

    def action(self,case:Case):
        pass # La case s'occupe de tout

# Imports utilisés dans le code
from ..Entitee.Agissant.Agissant import NOONE