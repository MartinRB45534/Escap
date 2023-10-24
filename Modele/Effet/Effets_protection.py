from __future__ import annotations
from typing import TYPE_CHECKING, List
from warnings import warn
import carte as crt

from .effet import OneShot, OnPostAction, TimeLimited, OnAttack

if TYPE_CHECKING:
    from ..entitee.agissant.agissant import Agissant
    from ..entitee.item.equippement.degainable.bouclier.bouclier import Bouclier
    from ..effet.attaque.attaque import AttaqueCase

class ProtectionGroupe(OneShot,OnPostAction):
    def __init__(self,duree:float,degats:float):
        self.affiche = False
        self.phase = "démarrage"
        self.duree = duree
        self.degats = degats

    def action(self,porteur:Agissant):
        cibles = []
        if porteur.esprit != NOBODY:
            cibles = porteur.esprit.corps
        else:
            cibles = [porteur]
        for cible in cibles:
            if cible.etat == EtatsAgissants.VIVANT:
                cible.effets.append(ProtectionMur(self.duree,self.degats))

class ProtectionBouclier(TimeLimited,OnAttack):
    """La case protégée par le bouclier est 'entourée' par ce dernier, c'est à dire que pour y rentrer par certains côtés, une attaque doit d'abord être affectée par le bouclier."""
    def __init__(self,temps_restant:float,bouclier:Bouclier,directions:List[crt.Direction]):
        self.affiche = False
        self.temps_restant = temps_restant
        self.phase = "démarrage"
        self.bouclier = bouclier #Techniquement c'est le bouclier qui intercepte.
        self.directions = directions

    def action(self,attaque):
        if attaque.direction is None:
            warn("L'attaque n'a pas de direction, elle ne peut donc pas être interceptée par le bouclier.")
        elif attaque.oppose() in self.directions:
            self.bouclier.intercepte(attaque)

class ProtectionMur(TimeLimited,OnAttack):
    """Une protection qui agit comme un 'mur' autour de l'agissant, c'est à dire qu'elle absorbe les dégats jusqu'à se briser."""
    def __init__(self,temps_restant:float,PV:float):
        self.affiche = True
        self.temps_restant = temps_restant
        self.phase = "démarrage"
        self.PV = PV
        self.PV_max = PV #Pour afficher les PVs de la protection

    def action(self,attaque:AttaqueCase):
        if self.pv < attaque.degats:
            attaque.degats = -self.pv
            self.pv = 0
            self.termine()
        else:
            attaque.degats = 0 #Une attaque perçante peut quand même passer
            self.pv -= attaque.degats

class ProtectionSacree(ProtectionMur):
    """Particulièrement efficace contre les attaques d'ombre."""
    def action(self,attaque:AttaqueCase):
        if attaque.element == Element.OMBRE:
            if 2*self.pv < attaque.degats:
                attaque.degats = -2*self.pv
                self.pv = 0
                self.termine()
            else:
                attaque.degats = 0 #Une attaque perçante peut quand même passer
                self.pv -= attaque.degats//2
        else:
            ProtectionMur.action(self,attaque)

# Imports utilisés dans le code
from ..systeme.elements import Element
from ..entitee.agissant.etats import EtatsAgissants
from ..esprit.esprit import NOBODY