from __future__ import annotations
from typing import TYPE_CHECKING

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
    def __init__(self,priorite:float):
        self.phase = "démarrage"
        self.responsable = 0
        self.priorite = priorite
        self.affiche = False

class Aura_permanente(Aura_elementale):
    """La classe des effets d'aura élémentales permanentes, celles qui représentent l'élément par défaut de la case."""

    def execute(self,case:Case):
        if self.phase == "démarrage":
            self.phase = "en cours"

class Aura_temporaire(Aura_elementale):
    """La classe des effets d'aura élémentales temporaires, celles qui sont appliquées par un agissant."""
    def __init__(self,responsable:Agissant,priorite:float):
        self.phase = "démarrage"
        self.responsable = responsable
        self.priorite = priorite
        self.distance = 0
        self.affiche = False

class Terre(One_shot,Aura_temporaire):
    """L'effet qui applique l'aura de terre à une case. Laissé ici par un agissant."""
    element = Element.TERRE
    def execute(self,case:Case):
        if self.phase == "démarrage":
            self.termine() #Pour l'instant elle ne fait rien. Rien qu'empêcher les autres auras de s'exprimer. Je suppose que ça peut servir quand on visite des étages non-terrestres.
        case.code += 1 #0 ou 1, selon que la case a une aura de Terre ou non

class Terre_permanente(Aura_permanente):
    """L'effet qui applique l'aura de terre à une case. Il a toujours été là, et il n'en bougera pas."""
    element = Element.TERRE
    def execute(self,case:Case):
        case.code += 1 #0 ou 1, selon que la case a une aura de Terre ou non

class Feu(Evenement,Aura_temporaire):
    """L'effet qui applique l'aura de feu à une case. Laissé ici par un agissant."""
    element = Element.FEU
    def __init__(self,responsable:Agissant,priorite:float,duree:float):
        Aura_temporaire.__init__(self,responsable,priorite)
        self.temps_restant = duree

    def action(self,case:Case):
        occupant = case.agissant
        if occupant is not None and occupant.esprit != self.responsable.esprit :
            occupant.subit(self.responsable,self.temps_restant,"proximité",self.element)
        case.code += 2 #0 ou 2, selon que la case a une aura de Feu ou non

    def execute(self,case:Case):
        self.temps_restant -= 1
        self.priorite -= 0.3 #La priorite diminue progressivement, donc une aura de feu descend rarement jusqu'à 0 dégats.
        if self.phase == "démarrage" :
            self.phase = "en cours"
        elif self.temps_restant <= 0 :
            self.termine()
        else :
            self.action(case)

class Feu_permanent(Aura_permanente):
    """L'effet qui applique l'aura de feu à une case. Il a toujours été là, et il n'en bougera pas."""

    def __init__(self,priorite:float,degats:float):
        Aura_permanente.__init__(self,priorite)
        self.degats = degats

    def action(self,case:Case):
        occupant = case.agissant
        if occupant is not None :
            occupant.subit(NoOne(),self.degats,"distance",self.element)
        case.code += 2 #0 ou 2, selon que la case a une aura de Feu ou non

class Glace(One_shot,Aura_temporaire):
    """L'effet qui applique l'aura de glace à une case. Laissé ici par un agissant."""
    element = Element.GLACE
    def __init__(self,responsable:Agissant,priorite:float,ralentissement:float):
        self.phase = "démarrage"
        self.responsable = responsable
        self.priorite = priorite
        self.ralentissement = ralentissement
        self.distance = 0
        self.affiche = False

    def action(self,case:Case):
        occupants = case.items | {case.agissant} if case.agissant is not None else case.items
        for occupant in occupants :
            if isinstance(occupant,Item) or (occupant.esprit != self.responsable.esprit and self.element not in occupant.immunites) :
                if occupant.action is not None :
                    occupant.action.taux_vitesse["aura"] = self.ralentissement
        case.code += 4 #0 ou 4, selon que la case a une aura de Glace ou non

    def execute(self,case:Case):
        if self.phase == "démarrage":
            self.action(case)
            self.termine()

class Glace_permanente(Aura_permanente):
    """L'effet qui applique l'aura de glace à une case. Il a toujours été là, et il n'en bougera pas."""
    element = Element.GLACE
    def __init__(self,priorite:float,ralentissement:float):
        self.phase = "démarrage"
        self.responsable = 0
        self.priorite = priorite
        self.ralentissement = ralentissement
        self.affiche = False

    def action(self,case:Case):
        occupants = case.items | {case.agissant} if case.agissant is not None else case.items
        for occupant in occupants :
            if  isinstance(occupant,Item) or self.element not in occupant.immunites :
                if occupant.action is not None :
                    occupant.action.taux_vitesse["aura"] = self.ralentissement
        case.code += 4 #0 ou 4, selon que la case a une aura de Glace ou non

class Ombre(One_shot,Aura_temporaire):
    """L'effet qui applique l'aura d'ombre à une case. Laissé ici par un agissant."""
    element = Element.OMBRE
    def __init__(self,responsable:Agissant,priorite:float,gain_opacite:float):
        self.phase = "démarrage"
        self.responsable = responsable
        self.priorite = priorite
        self.gain_opacite = gain_opacite
        self.distance = 0
        self.affiche = False

    def action(self,case:Case):
        case.opacite_bonus = self.gain_opacite
        case.code += 8 #0 ou 8, selon que la case a une aura d'Ombre ou non. Comme l'ombre et le reste sont incompatibles, les codes 9 à 15 sont libres. Le code maximum pour la partie élémentaire est 8

    def execute(self,case:Case):
        if self.phase == "démarrage":
            self.action(case)
            self.termine()

class Ombre_permanente(Aura_permanente):
    """L'effet qui applique l'aura d'ombre à une case. Il a toujours été là, et il n'en bougera pas."""
    element = Element.OMBRE
    def __init__(self,priorite:float,gain_opacite:float):
        self.phase = "démarrage"
        self.responsable = 0
        self.priorite = priorite
        self.gain_opacite = gain_opacite
        self.affiche = False

    def action(self,case:Case):
        case.opacite_bonus = self.gain_opacite
        case.code += 8 #0 ou 8, selon que la case a une aura d'Ombre ou non. Comme l'ombre et le reste sont incompatibles, les codes 9 à 15 sont libres. Le code maximum pour la partie élémentaire est 8

# Voilà maintenant les auras au niveau de l'agissant :

class Aura_terre(One_shot,On_debut_tour):
    """Le centre de l'aura de terre d'un agissant. Attaché à l'agissant, placera les effets voulus sur les cases voisines."""

    def __init__(self,portee:int,priorite:float,niveau:int):
        self.phase = "démarrage"
        self.niveau = niveau
        self.portee = portee
        self.priorite = priorite
        self.effet = Terre
        self.affiche = False

    def action(self,porteur:Agissant):
        zone = porteur.labyrinthe.a_portee(porteur.position,self.portee,Deplacement.SPATIAL,Forme.CERCLE,Passage(True, True, True, True, True))
        priorite = porteur.priorite + self.priorite
        for position in zone:
            porteur.labyrinthe.get_case(position).ajoute_aura(self.effet(porteur,priorite))

class Aura_feu(One_shot,On_debut_tour):
    """Le centre de l'aura de feu d'un agissant. Attaché à l'agissant, placera les effets voulus sur les cases voisines."""

    def __init__(self,portee:int,priorite:float,duree:int,niveau:int):
        self.phase = "démarrage"
        self.niveau = niveau
        self.portee = portee
        self.priorite = priorite
        self.duree = duree
        self.effet = Feu
        self.affiche = False

    def action(self,porteur:Agissant):
        zone = porteur.labyrinthe.a_portee(porteur.position,self.portee,Deplacement.SPATIAL,Forme.CERCLE,Passage(True, True, True, True, True))
        priorite = porteur.priorite + self.priorite
        for position in zone:
            porteur.labyrinthe.get_case(position).ajoute_aura(self.effet(porteur,priorite,self.duree))

class Aura_glace(One_shot,On_debut_tour):
    """Le centre de l'aura de glace d'un agissant. Attaché à l'agissant, placera les effets voulus sur les cases voisines."""

    def __init__(self,portee:int,priorite:float,ralentissement:float,niveau:int):
        self.phase = "démarrage"
        self.niveau = niveau
        self.portee = portee
        self.priorite = priorite
        self.ralentissement = ralentissement
        self.effet = Glace
        self.affiche = False

    def action(self,porteur:Agissant):
        zone = porteur.labyrinthe.a_portee(porteur.position,self.portee,Deplacement.SPATIAL,Forme.CERCLE,Passage(True, True, True, True, True))
        priorite = porteur.priorite + self.priorite
        for position in zone:
            porteur.labyrinthe.get_case(position).ajoute_aura(self.effet(porteur,priorite,self.ralentissement))

class Aura_ombre(One_shot,On_debut_tour):
    """Le centre de l'aura d'ombre d'un agissant. Attaché à l'agissant, placera les effets voulus sur les cases voisines."""

    def __init__(self,portee:int,priorite:float,gain_opacite:float,niveau:int):
        self.phase = "démarrage"
        self.niveau = niveau
        self.portee = portee
        self.priorite = priorite
        self.gain_opacite = gain_opacite
        self.effet = Ombre
        self.affiche = False

    def action(self,porteur:Agissant):
        zone = porteur.labyrinthe.a_portee(porteur.position,self.portee,Deplacement.SPATIAL,Forme.CERCLE,Passage(True, True, True, True, True))
        priorite = porteur.priorite + self.priorite
        for position in zone:
            porteur.labyrinthe.get_case(position).ajoute_aura(self.effet(porteur,priorite,self.gain_opacite))

# Imports utilisés dans le code
from ..Entitee.Agissant.Agissant import NoOne
from ..Entitee.Item.Item import Item
from ..Labyrinthe.Deplacement import Deplacement
from ..Labyrinthe.Forme import Forme
from ..Labyrinthe.Passage import Passage