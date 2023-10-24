from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import carte as crt
import affichage as af

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ..agissant.agissant import Agissant
    from ..entitee import NonSuperposable
    from ...effet.action.deplacement import Vole
    from ...labyrinthe.labyrinthe import Labyrinthe

# Imports des classes parentes
from ..entitee import Mobile

class Item(Mobile):
    """La classe des entitées inanimées. Peuvent se situer dans un inventaire. Peuvent être lancés (déconseillé pour les non-projectiles)."""
    def __init__(self,labyrinthe:Labyrinthe,position:crt.Position, ID: Optional[int]=None):
        Entitee.__init__(self,position,ID)
        self.labyrinthe = labyrinthe
        self.etat = EtatsItems.INTACT #Le niveau l'évacuera s'il n'est plus intact.
        self.priorite = 0 #Pour avoir le droit de la ramasser.
        self.action:Optional[Vole] = None #Utile uniquement quand l'item est lancé. Les items ne peuvent que voler
        self.lanceur:Optional[Agissant] = None
        self.direction:Optional[crt.Direction] = None #Utile uniquement quand l'item se déplace.
        self.poids:float = 10 #Utile uniquement quand l'item est lancé. Détermine le temps qu'il faut à l'agissant pour le lancer et le temps que l'item se déplacera.
        self.frottements:float = 10 #Utile uniquement quand l'item se déplace. Détermine la latence à chaque déplacement.
        self.hauteur:float = 0 #Utile uniquement quand l'item se déplace. Diminue à chaque tour. L'item s'immobilise à 0 (éventuellement déclenche des effets).
        self.nom:str = "item"

    def get_direction(self):
        if self.direction is not None:
            return self.direction
        else:
            return crt.Direction.HAUT # Direction par défaut

    def heurte_non_superposable(self,non_superposable:NonSuperposable):
        for effet in self.effets :
            if isinstance(effet,OnHit) :
                effet.execute(self)
        if isinstance(non_superposable,Agissant) and isinstance(self,Percant) :
            self.ajoute_effet(En_sursis())
        elif isinstance(self,(Fragile,Evanescent)):
            self.etat = EtatsItems.BRISE
            self.arret()
        else :
            self.arret()

    def heurte_mur(self):
        for effet in self.effets :
            if isinstance(effet,OnHit):
                effet.execute(self)
        if isinstance(self,(Fragile,Evanescent)):
            self.etat = EtatsItems.BRISE
            self.arret()
        else :
            self.arret()

    def atterit(self):
        for effet in self.effets :
            if isinstance(effet,OnHit) :
                effet.execute(self)
        if isinstance(self,Evanescent):
            self.etat = EtatsItems.BRISE
            self.arret()
        else :
            self.arret()

    def arret(self):
        if self.action is not None:
            self.action = None
        self.hauteur = 0

    #Découvrons le déroulé d'un tour, avec item-kun :
    def debut_tour(self):
        #Un nouveau tour commence, qui s'annonce remplit de bonne surprises et de nouvelles rencontres ! Pour partir du bon pied, on a quelques trucs à faire :
        for effet in self.effets:
            if isinstance(effet,OnDebutTour):
                effet.execute(self) #On exécute divers effets
            if isinstance(effet,TimeLimited):
                effet.wait()

    def pseudo_debut_tour(self):
        pass

    #Les agissants font leurs trucs, le controleur nous déplace, nous heurte (aïe !), tout le monde s'étripe...
    def vole(self):
        #On voooole (si on a été lancé)
        if self.action is not None:
            if self.action.execute():
                self.action = None # Ne devrait jamais arriver
                raise ValueError("L'item a fini son vol ?! C'est pas normal !")
        if self.hauteur <= 0:
            self.atterit()

    def fin_tour(self):
        #C'est déjà fini ? Vivement le prochain !
        for effet in self.effets:
            if isinstance(effet,On_fin_tour):
                effet.execute(self) #À condition qu'il y ait un prochain...

    @staticmethod
    def get_image():
        return af.SKIN_VIDE

class Consommable(Item):
    """La classe des items qui peuvent être consommés. Ajoute à l'agissant un effet. Disparait après usage."""
    pass

class Ingredient(Item):
    """La classe des ingrédients d'alchimie."""
    def get_classe(self):
        return Ingredient

    @staticmethod
    def get_image():
        return SKIN_INGREDIENT

# Imports utilisés dans le code
from ..entitee import Entitee
from .projectile.projectiles import Percant, Fragile, Evanescent
from .etats import EtatsItems
from ...affichage.skins import SKIN_INGREDIENT
from ...effet.effet import OnDebutTour, On_fin_tour, TimeLimited
from ...effet.effets_items import EnSursis, OnHit