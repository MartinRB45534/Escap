from __future__ import annotations
from typing import TYPE_CHECKING, Optional, List

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from Jeu.Controleur import Controleur
    from Jeu.Entitee.Agissant.Agissant import Agissant
    from Jeu.Entitee.Item.Equippement.Degainable.Bouclier.Bouclier import Bouclier
    from Jeu.Labyrinthe.Structure_spatiale.Position import Position
    from Jeu.Labyrinthe.Structure_spatiale.Direction import Direction
    from Jeu.Effet.Attaque.Attaque import Attaque

# Imports des classes parentes
from Jeu.Effet.Effet import One_shot, Evenement, Effet, On_post_action, Time_limited, On_attack

class Protection_general(Evenement,On_post_action):
    """Le joueur qui a utilisé un bouclier 'protège' une zone autour de lui. C'est à dire qu'à chaque tour, d'après sa position, sa direction et les murs, certaines cases reçoivent une protection jusqu'à la fin du tour."""
    def __init__(self,temps_restant:float,bouclier:Bouclier):
        self.affiche = False
        self.temps_restant = temps_restant
        self.phase = "démarrage"
        self.bouclier = bouclier #Techniquement c'est le bouclier qui intercepte.

    def action(self,agissant:Agissant):
        cases = agissant.controleur.get_cases_touches(agissant.get_position(),0) #Seule la case de l'agissant est protégée par cette version de la protection.
        for case in cases :
            case.effets.append(Protection_bouclier(1,self.bouclier,[agissant.dir_regard]))

class Protection_zone(One_shot,On_post_action):
    def __init__(self,protection:Effet,cible:str,position:Position,propagation:str,portee:float,direction:Optional[Direction]=None,traverse="tout"):
        self.affiche = False
        self.phase = "démarrage"
        self.position = position
        self.propagation = propagation
        self.portee = portee
        self.direction = direction
        self.traverse = traverse
        self.cible = cible
        self.protection = protection

    def action(self,porteur:Agissant):
        if self.cible == "case":
            cases = porteur.controleur.get_cases_touches(self.position,self.portee,self.propagation,self.direction,self.traverse,porteur)
            for case in cases :
                case.effets.append(copy.copy(self.protection))
        elif self.cible == "agissant":
            agissants = porteur.controleur.get_touches_pos(porteur,self.position,self.portee,self.propagation,self.direction)
            for agissant in agissants :
                agissant.effets.append(copy.copy(self.protection))

class Protection_groupe(One_shot,On_post_action):
    def __init__(self,duree:float,degats:float):
        self.affiche = False
        self.phase = "démarrage"
        self.duree = duree
        self.degats = degats

    def action(self,porteur:Agissant):
        cibles = []
        if porteur.esprit is not None:
            cibles = porteur.esprit.get_corps()
        else:
            cibles = [porteur]
        for cible in cibles:
            if cible.etat == "vivant":
                cible.effets.append(Protection_mur(self.duree,self.degats))

class Protection_bouclier(Time_limited,On_attack):
    """La case protégée par le bouclier est 'entourée' par ce dernier, c'est à dire que pour y rentrer par certains côtés, une attaque doit d'abord être affectée par le bouclier."""
    def __init__(self,temps_restant:float,bouclier:Bouclier,directions:List[Direction]):
        self.affiche = False
        self.temps_restant = temps_restant
        self.phase = "démarrage"
        self.bouclier = bouclier #Techniquement c'est le bouclier qui intercepte.
        self.directions = directions

    def action(self,attaque):
        if attaque.direction is None:
            print("ATTENTION : attaque sans direction ! Je n'intercepte pas.")
        elif attaque.oppose() in self.directions:
            self.bouclier.intercepte(attaque)

class Protection_mur(Time_limited,On_attack):
    """Une protection qui agit comme un 'mur' autour de l'agissant, c'est à dire qu'elle absorbe les dégats jusqu'à se briser."""
    def __init__(self,temps_restant:float,PV:float):
        self.affiche = True
        self.temps_restant = temps_restant
        self.phase = "démarrage"
        self.PV = PV
        self.PV_max = PV #Pour afficher les PVs de la protection

    def action(self,attaque:Attaque):
        if self.PV < attaque.degats:
            attaque.degats = -self.PV
            self.PV = 0
            self.termine()
        else:
            attaque.degats = 0 #Une attaque perçante peut quand même passer
            self.PV -= attaque.degats

    def get_skin(self):
        return SKIN_PROTECTION

class Protection_sacree(Protection_mur):
    """Particulièrement efficace contre les attaques d'ombre."""
    def action(self,attaque:Attaque):
        if attaque.element == OMBRE:
            if 2*self.PV < attaque.degats:
                attaque.degats = -2*self.PV
                self.PV = 0
                self.termine()
            else:
                attaque.degats = 0 #Une attaque perçante peut quand même passer
                self.PV -= attaque.degats//2
        else:
            Protection_mur.action(self,attaque)

    def get_skin(self):
        return SKIN_PROTECTION_SACREE

# Imports utilisés dans le code
from Affichage.Skins.Skins import SKIN_PROTECTION, SKIN_PROTECTION_SACREE
from Jeu.Constantes import *
import copy