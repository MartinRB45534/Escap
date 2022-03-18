from Jeu.Skins.Skins import *
from Jeu.Constantes import *

class Effet :
    """Les effets regroupent des choses qui arrivent à des éléments du système. Ils peuvent cibler une case, un mur, un agissant, un étage, etc. et sont souvent limités dans le temps ou par d'autres conditions. Ils sont évalués par le controleur dans différentes circonstances."""
    def __init__(self):
        print("a surdéfinir")

    def action(self):
        """La fonction qui exécute l'action de l'effet. En général, renvoie des valeurs que le controleur traitera."""
        print("a surdéfinir")

    def execute(self):
        """La fonction qui est appelée par le controleur. Détermine, d'après les informations transmises par le controleur, si l'action doit être effectuée ou pas. Vérifie si l'effet doit encore exister ou non."""
        print("a surdéfinir")

    def termine(self):
        """La fonction qui termine l'effet."""
        if self.affiche:
            self.phase = "affichage"
        else:
            self.phase = "terminé"

    def get_skin(self):
        return SKIN_EFFET

#On distingue les effets par circonstances d'appel.
class On_need(Effet) :
    """Classe des effets appelés lors de circonstances particulières. Ils n'ont pas besoin d'être mis à jour, pris en compte ou quoique ce soit le reste du temps."""
    pass

class On_tick(Effet) :
    """La classe des effets appelés à chaque tour."""
    def execute(self,porteur): #En général, prend en paramètre le porteur de l'effet. Pas toujours.
        self.action(porteur)

class On_debut_tour(On_tick):
    """La classe des effets appelés au début du tour."""
    pass

class On_post_decision(On_tick):
    """La classe des effets appelés après la phase de décision."""
    pass

class On_action(On_tick):
    """La classe des effets appelés après un action."""
    pass

class On_post_action(On_tick):
    """La classe des effets appelés après la phase d'action."""
    pass

class On_pre_attack(On_tick):
    """La classe des effets appelés avant les attaques."""
    pass

class On_fin_tour(On_tick):
    """La classe des effets appelés à la fin du tour."""
    pass

class One_shot(Effet):
    """Classe des effets qui n'ont à être appelés qu'une seule fois."""

    def execute(self,parametre): # La plupart des one_shot sont de cette forme...
        if self.phase == "démarrage" :
            self.action(parametre)
            self.termine()

class Delaye(One_shot):
    """Classe des effets qui s'exécutent avec du retard."""

    def execute(self,parametre):
        if self.phase == "démarrage" :
            if self.delai > 0:
                self.delai -= 1
            else:
                self.action(parametre)
                self.termine()

class Evenement(On_tick):
    """La classe des effets limités par le temps, appelés une seule fois par tour."""
    def __init__(self,temps_restant):
        self.affiche = False
        self.temps_restant=temps_restant
        self.phase = "démarrage"

    def action(self):
        """La fonction qui exécute l'action de l'évènement."""
        print("a surdéfinir")

    def execute(self,parametre):
        self.temps_restant -= 1
        if self.phase == "démarrage" :
            self.phase = "en cours"
        elif self.temps_restant <= 0 :
            self.termine()
        else :
            self.action(parametre)

class Time_limited(Effet):
    """Classe des effets limités par le temps, qu'on ne peut pas considérer comme des événements car leur appel est irrégulier."""
    def __init__(self,temps_restant):
        self.affiche = False
        self.phase = "démarrage"
        self.temps_restant = temps_restant

    def wait(self):
        self.temps_restant -= 1
        if self.phase == "démarrage" :
            self.phase = "en cours"
        elif self.temps_restant <= 0 :
            self.termine()

class On_attack(Effet):
    """Classe des effets appelés lors d'une attaque."""
    def execute(self,attaque):
        self.action(attaque)

class Enchantement(Evenement) :
    """Des effets avec un temps très long ! Leur classe à part permet de les affecter différement."""
    def __init__(self,temps_restant):
        self.affiche = False
        self.temps_restant=temps_restant
        self.phase = "démarrage"

    def action(self):
        """La fonction qui exécute l'action de l'enchantement."""
        print("a surdéfinir")

class On_through(Effet):
    """La classe des effets déclenchés quand on traverse un mur."""
    pass

class On_step_in(Effet):
    """La classe des effets déclenchés lorsqu'on marche sur une case."""
    pass

class On_step_out(Effet):
    """La classe des effets déclenchés quand on quitte une case."""
    pass

class On_try_through(Effet):
    """La classe des effets déclenchés quand on essaye de traverser un mur."""

class Aura(On_tick):
    """La classe des auras (attachées à la case)."""
    pass #Ne doit pas être instanciée
