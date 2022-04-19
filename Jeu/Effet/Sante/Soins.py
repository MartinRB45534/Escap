from Jeu.Effet.Effet import *
from Jeu.Effet.Sante.Maladies.Maladie import *
from Jeu.Effet.Sante.Poison import *
from Jeu.Constantes import *

class Antidote(One_shot,On_fin_tour):
    """Effet qui supprime les effets de poison du joueur."""
    def __init__(self):
        self.affiche = False
        self.phase = "démarrage"

    def action(self,porteur):
        for effet in porteur.effets:
            if isinstance(effet,Poison):
                effet.phase = "terminé" # Rajouter une condition de priorite

class Medicament(One_shot,On_fin_tour):
    """Effet qui supprime les effets de maladie du joueur."""
    def __init__(self):
        self.affiche = False
        self.phase = "démarrage"

    def action(self,porteur):
        for effet in porteur.effets:
            if isinstance(effet,Maladie): # Créer des médicaments différents selon les maladies ?
                effet.phase = "terminé" # Rajouter une condition de priorite

class Purification(One_shot,On_fin_tour):
    """Effet qui supprime les effets de poison ou maladie du joueur."""
    def __init__(self):
        self.affiche = False
        self.phase = "démarrage"

    def action(self,porteur):
        for effet in porteur.effets:
            if isinstance(effet,(Maladie,Poison)):
                effet.phase = "terminé" # Rajouter une condition de priorite

class Soin_case(On_post_action):
    """Un effet de soin. À répercuter sur les occupants éventuels de la case."""
    def __init__(self,gain_pv,responsable=0,cible="alliés"):
        self.phase = "démarrage"
        self.gain_pv = gain_pv
        self.responsable = responsable
        self.cible = cible
        self.affiche = True

    def action(self,case):
        cibles_potentielles = case.controleur.trouve_agissants_courants(case.position)
        for cible_potentielle in cibles_potentielles:
            if self.responsable == 0: #Pas de responsable. Sérieusement ?
                case.controleur.get_entitee(cible_potentielle).effets.append(Soin(self.responsable,self.gain_pv))
            else:
                esprit = case.controleur.get_esprit(case.controleur.get_entitee(self.responsable).esprit)
                if esprit == None: #Pas d'esprit ? Sérieusement ?
                    case.controleur.get_entitee(cible_potentielle).effets.append(Soin(self.responsable,self.gain_pv))
                elif self.cible == "alliés" and cible_potentielle in case.controleur.get_esprit(case.controleur.get_entitee(self.responsable).esprit).get_corps():
                    case.controleur.get_entitee(cible_potentielle).effets.append(Soin(self.responsable,self.gain_pv))
                elif self.cible == "neutres" and not cible_potentielle in case.controleur.get_esprit(case.controleur.get_entitee(self.responsable).esprit).get_ennemis():
                    case.controleur.get_entitee(cible_potentielle).effets.append(Soin(self.responsable,self.gain_pv))

    def execute(self,case):
        if self.phase == "démarrage" :
            self.action(case)
            self.termine()

class Soin(On_fin_tour):
    """Un effet de soin. Généralement placé sur l'agissant par une magie de soin, de soin de zone, ou d'auto-soin."""
    def __init__(self,responsable,gain_pv):
        self.phase = "démarrage"
        self.responsable = responsable
        self.gain_pv = gain_pv
        self.affiche = True

    def action(self,porteur):
        porteur.soigne(self.gain_pv)

    def execute(self,porteur):
        if self.phase == "démarrage" :
            self.action(porteur)
            self.termine()

    def get_skin(self):
        return SKIN_SOIN
