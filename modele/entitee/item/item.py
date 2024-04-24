"""
Les items sont des entitées inanimées qui peuvent être ramassées, lancées, etc.
"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import carte as crt
import affichage as af

# Imports des classes parentes
from ..entitee import Mobile

# Imports utilisés dans le code
from ...commons import EtatsItems
from ...effet import OnDebutTourItem, OnFinTourItem, TimeLimited, OnHit

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ...action import Plane

class Item(Mobile):
    """La classe des entitées inanimées. Peuvent se situer dans un inventaire.
       Peuvent être lancés (déconseillé pour les non-projectiles)."""
    poids:float
    frottements:float
    _priorite:float
    cadavre=False
    def __init__(self,position:crt.Position):
        Mobile.__init__(self,position,None)
        self.etat = EtatsItems.INTACT #Le niveau l'évacuera s'il n'est plus intact.
        self.action:Optional[Plane] = None
        self.direction:Optional[crt.Direction] = None
        self.hauteur:float = 0

    def get_direction(self):
        if self.direction is not None:
            return self.direction
        else:
            return crt.Direction.HAUT # Direction par défaut

    def frappe(self):
        """L'item frappe quelque chose."""
        for effet in self.effets :
            if isinstance(effet,OnHit):
                effet.hit(self)

    def heurte_agissant(self):
        """L'item arrive sur une case qui contient un agissant."""
        self.frappe()
        self.heurte()

    def heurte_decors(self):
        """L'item arrive sur une case qui contient un décor."""
        self.frappe()
        self.heurte()

    def heurte_mur(self):
        """L'item arrive sur un mur."""
        self.frappe()
        self.heurte()

    def heurte(self):
        """L'item heurte quelque chose."""
        self.arret()

    def atterit(self):
        """L'item atterrit sur une case."""
        self.frappe()
        self.arret()

    def arret(self):
        """L'item s'arrête."""
        if self.action is not None:
            self.action = None
        self.hauteur = 0

    def add_latence(self,latence: float):
        """Ajoute de la latence à l'action de l'entitée."""
        if self.action is not None:
            self.action.latence += latence

    def set_latence(self,latence: float):
        """Modifie la latence de l'action de l'entitée."""
        if self.action is not None:
            self.action.latence = latence

    #Découvrons le déroulé d'un tour, avec item-kun :
    def debut_tour(self):
        #Un nouveau tour commence, qui s'annonce remplit de bonne surprises et de nouvelles rencontres ! Pour partir du bon pied, on a quelques trucs à faire :
        for effet in self.effets:
            if isinstance(effet,TimeLimited):
                effet.wait()
            if isinstance(effet,OnDebutTourItem):
                effet.debut_tour(self) #On exécute divers effets

    def pseudo_debut_tour(self):
        pass

    #Les agissants font leurs trucs, le controleur nous déplace, nous heurte (aïe !), tout le monde s'étripe...
    def vole(self):
        #On voooole (si on a été lancé)
        if self.action is not None:
            self.action.execute()
        if self.hauteur <= 0:
            self.atterit()

    def fin_tour(self):
        #C'est déjà fini ? Vivement le prochain !
        for effet in self.effets:
            if isinstance(effet,OnFinTourItem):
                effet.fin_tour(self) #À condition qu'il y ait un prochain...

    @staticmethod
    def get_image():
        """Retourne l'image de la classe d'item."""
        return af.SKIN_VIDE

class NoThing(Item):
    def __init__(self):
        pass

    def __equal__(self,other:Any):
        return isinstance(other,NoThing)

NOTHING = NoThing()
