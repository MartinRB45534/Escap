from __future__ import annotations
from typing import TYPE_CHECKING, Optional, List
import Carte as crt

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ..Entitee.Agissant.Agissant import Agissant
    from ..Entitee.Item.Equippement.Degainable.Bouclier.Bouclier import Bouclier
    from ..Effet.Attaque.Attaque import Attaque_case

# Imports des classes parentes
from ..Effet.Effet import One_shot, Evenement, Effet, On_post_action, Time_limited, On_attack

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
    def __init__(self,temps_restant:float,bouclier:Bouclier,directions:List[crt.Direction]):
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

    def action(self,attaque:Attaque_case):
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
    def action(self,attaque:Attaque_case):
        if attaque.element == Element.OMBRE:
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
from Old_Affichage.Skins.Skins import SKIN_PROTECTION, SKIN_PROTECTION_SACREE
from ..Systeme.Elements import Element
import copy