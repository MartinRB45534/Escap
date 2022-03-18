from Jeu.Effet.Effet import *
from Jeu.Constantes import *
from Jeu.Systeme.Constantes_magies.Magies import *

# On va distinguer 3 types d'aura :
#   - Les auras naturellement attachées à une case. Ce sont des auras élémentaires. Elles peuvent être temporairement réprimée par une autre aura élémentale.
#   - Les auras non-élémentaires. Comme l'aura d'instakill ou l'aura divine, elles sont superposables autant qu'on veut, et attachées à un agissant.
#   - Les auras élémentaires attachées à un agissant. Celles qui nous embêtent le plus. La plus forte étouffe les autres, mais laisse les autres auras du même agissant s'exprimer.
# Peut-être considérer l'utilisation d'auras autour d'items comme la boule de feu ?

class Aura_elementale(Aura):
    """La classe des effets d'auras élémentales. Attaché à la case."""

    def action(self,porteur):
        cases = porteur.controleur.get_cases_touches(porteur.position,self.portee)
        priorite = porteur.priorite + self.priorite
        for case in cases:
            case.ajoute_aura(self.effet(self.niveau,porteur.ID,priorite))

class Aura_permanente(Aura_elementale):
    """La classe des effets d'aura élémentales permanentes, celles qui représentent l'élément par défaut de la case."""

    def execute(self,case,position):
        if self.phase == "démarrage":
            self.phase = "en cours"

class Terre(One_shot,Aura_elementale):
    """L'effet qui applique l'aura de terre à une case. Laissé ici par un agissant."""

    def __init__(self,responsable,priorite):
        self.phase = "démarrage"
        self.responsable = responsable
        self.priorite = priorite
        self.distance = 0
        self.affiche = False

    def execute(self,case,position):
        if self.phase == "démarrage":
            self.termine() #Pour l'instant elle ne fait rien. Rien qu'empêcher les autres auras de s'exprimer. Je suppose que ça peut servir quand on visite des étages non-terrestres.
        case.code += 1 #0 ou 1, selon que la case a une aura de Terre ou non

class Terre_permanente(Aura_permanente):
    """L'effet qui applique l'aura de terre à une case. Il a toujours été là, et il n'en bougera pas."""

    def __init__(self,priorite):
        self.phase = "démarrage"
        self.responsable = 0
        self.priorite = priorite
        self.affiche = False

    def execute(self,case,position):
        case.code += 1 #0 ou 1, selon que la case a une aura de Terre ou non

class Feu(Evenement,Aura_elementale):
    """L'effet qui applique l'aura de feu à une case. Laissé ici par un agissant."""

    def __init__(self,responsable,priorite,duree):
        self.phase = "démarrage"
        self.temps_restant = duree
        self.responsable = responsable
        self.priorite = priorite
        self.distance = 0
        self.affiche = False

    def action(self,case,position):
        contr = case.controleur
        occupants = contr.trouve_agissants_courants(position)
        lanceur = contr.get_entitee(self.responsable)
        for occupant in occupants :
            agissant = contr.get_entitee(occupant)
            if agissant.esprit != lanceur.esprit :
                agissant.subit(self.temps_restant,"proximité",FEU,self.responsable)
        case.code += 2 #0 ou 2, selon que la case a une aura de Feu ou non

    def execute(self,case,position):
        self.temps_restant -= 1
        self.priorite -= 0.3 #La priorite diminue progressivement, donc une aura de feu descend rarement jusqu'à 0 dégats.
        if self.phase == "démarrage" :
            self.phase = "en cours"
        elif self.temps_restant <= 0 :
            self.termine()
        else :
            self.action(case,position)

class Feu_permanent(Aura_permanente):
    """L'effet qui applique l'aura de feu à une case. Il a toujours été là, et il n'en bougera pas."""

    def __init__(self,priorite,degats):
        self.phase = "démarrage"
        self.responsable = 0
        self.priorite = priorite
        self.degats = degats
        self.affiche = False

    def action(self,case,position):
        contr = case.controleur
        occupants = contr.trouve_agissants_courants(position)
        for occupant in occupants :
            agissant = contr.get_entitee(occupant)
            agissant.subit(self.degats,"distance",FEU)
        case.code += 2 #0 ou 2, selon que la case a une aura de Feu ou non

class Glace(One_shot,Aura_elementale):
    """L'effet qui applique l'aura de glace à une case. Laissé ici par un agissant."""

    def __init__(self,responsable,priorite,gain_latence):
        self.phase = "démarrage"
        self.responsable = responsable
        self.priorite = priorite
        self.gain_latence= gain_latence
        self.distance = 0
        self.affiche = False

    def action(self,case,position):
        contr = case.controleur
        occupants = contr.trouve_mobiles_courants(position)
        lanceur = contr.get_entitee(self.responsable)
        for occupant in occupants :
            agissant = contr.get_entitee(occupant)
            if agissant.esprit != lanceur.esprit and GLACE not in agissant.immunites :
                agissant.latence += self.gain_latence
        case.code += 4 #0 ou 4, selon que la case a une aura de Glace ou non

    def execute(self,case,position):
        if self.phase == "démarrage":
            self.action(case,position)
            self.termine()

class Glace_permanente(Aura_permanente):
    """L'effet qui applique l'aura de glace à une case. Il a toujours été là, et il n'en bougera pas."""

    def __init__(self,priorite,gain_latence):
        self.phase = "démarrage"
        self.responsable = 0
        self.priorite = priorite
        self.gain_latence = gain_latence
        self.affiche = False

    def action(self,case,position):
        contr = case.controleur
        occupants = contr.trouve_mobiles_courants(position)
        for occupant in occupants :
            agissant = contr.get_entitee(occupant)
            if GLACE not in agissant.immunites :
                agissant.latence += self.gain_latence
        case.code += 4 #0 ou 4, selon que la case a une aura de Glace ou non

class Ombre(One_shot,Aura_elementale):
    """L'effet qui applique l'aura d'ombre à une case. Laissé ici par un agissant."""

    def __init__(self,responsable,priorite,gain_opacite):
        self.phase = "démarrage"
        self.responsable = responsable
        self.priorite = priorite
        self.gain_opacite = gain_opacite
        self.distance = 0
        self.affiche = False

    def action(self,case,position):
        case.opacite_bonus = self.gain_opacite
        case.code += 8 #0 ou 8, selon que la case a une aura d'Ombre ou non. Comme l'ombre et le reste sont incompatibles, les codes 9 à 15 sont libres. Le code maximum pour la partie élémentaire est 8

    def execute(self,case,position):
        if self.phase == "démarrage":
            self.action(case,position)
            self.termine()

class Ombre_permanente(Aura_permanente):
    """L'effet qui applique l'aura d'ombre à une case. Il a toujours été là, et il n'en bougera pas."""

    def __init__(self,priorite,gain_opacite):
        self.phase = "démarrage"
        self.responsable = 0
        self.priorite = priorite
        self.gain_opacite = gain_opacite
        self.affiche = False

    def action(self,case,position):
        case.opacite_bonus = self.gain_opacite
        case.code += 8 #0 ou 8, selon que la case a une aura d'Ombre ou non. Comme l'ombre et le reste sont incompatibles, les codes 9 à 15 sont libres. Le code maximum pour la partie élémentaire est 8

# Voilà maintenant les auras au niveau de l'agissant :

class Aura_terre(One_shot,On_debut_tour):
    """Le centre de l'aura de terre d'un agissant. Attaché à l'agissant, placera les effets voulus sur les cases voisines."""

    def __init__(self,niveau):
        self.phase = "démarrage"
        self.niveau = niveau
        self.portee = portee_aura_terre[self.niveau-1]
        self.priorite = priorite_aura_terre[self.niveau-1]
        self.effet = Terre
        self.affiche = False

    def action(self,porteur):
        cases = porteur.controleur.get_cases_touches(porteur.position,self.portee)
        priorite = porteur.priorite + self.priorite
        for case in cases:
            case.ajoute_aura(self.effet(porteur.ID,priorite))

class Aura_feu(One_shot,On_debut_tour):
    """Le centre de l'aura de feu d'un agissant. Attaché à l'agissant, placera les effets voulus sur les cases voisines."""

    def __init__(self,niveau):
        self.phase = "démarrage"
        self.niveau = niveau
        self.portee = portee_aura_feu[self.niveau-1]
        self.priorite = priorite_aura_feu[self.niveau-1]
        self.duree = duree_aura_feu[self.niveau-1]
        self.effet = Feu
        self.affiche = False

    def action(self,porteur):
        cases = porteur.controleur.get_cases_touches(porteur.position,self.portee)
        priorite = porteur.priorite + self.priorite
        for case in cases:
            case.ajoute_aura(self.effet(porteur.ID,priorite,self.duree))

class Aura_glace(One_shot,On_debut_tour):
    """Le centre de l'aura de glace d'un agissant. Attaché à l'agissant, placera les effets voulus sur les cases voisines."""

    def __init__(self,niveau):
        self.phase = "démarrage"
        self.niveau = niveau
        self.portee = portee_aura_glace[self.niveau-1]
        self.priorite = priorite_aura_glace[self.niveau-1]
        self.gain_latence = gain_latence_aura_glace[self.niveau-1]
        self.effet = Glace
        self.affiche = False

    def action(self,porteur):
        cases = porteur.controleur.get_cases_touches(porteur.position,self.portee)
        priorite = porteur.priorite + self.priorite
        for case in cases:
            case.ajoute_aura(self.effet(porteur.ID,priorite,self.gain_latence))

class Aura_ombre(One_shot,On_debut_tour):
    """Le centre de l'aura d'ombre d'un agissant. Attaché à l'agissant, placera les effets voulus sur les cases voisines."""

    def __init__(self,niveau):
        self.phase = "démarrage"
        self.niveau = niveau
        self.portee = portee_aura_ombre[self.niveau-1]
        self.priorite = priorite_aura_ombre[self.niveau-1]
        self.gain_opacite = gain_opacite_aura_ombre[self.niveau-1]
        self.effet = Ombre
        self.affiche = False

    def action(self,porteur):
        cases = porteur.controleur.get_cases_touches(porteur.position,self.portee)
        priorite = porteur.priorite + self.priorite
        for case in cases:
            case.ajoute_aura(self.effet(porteur.ID,priorite,self.gain_opacite))
