from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import carte as crt
import affichage as af

# Imports des classes parentes
from ..entitee import Mobile

# Imports utilisés dans le code
from ..agissant.agissant import NOONE
from ...commons.etats_item import EtatsItems
from ...affichage.skins import SKIN_INGREDIENT
from ...effet.timings import OnDebutTourItem, OnFinTourItem, TimeLimited
from ...effet.item import OnHit

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ..agissant.agissant import Agissant
    from ...action.deplacement import Vole
    from ...labyrinthe.labyrinthe import Labyrinthe

class Item(Mobile):
    """La classe des entitées inanimées. Peuvent se situer dans un inventaire. Peuvent être lancés (déconseillé pour les non-projectiles)."""
    def __init__(self,labyrinthe:Labyrinthe,position:crt.Position, ID: Optional[int]=None):
        Mobile.__init__(self,position,ID)
        self.labyrinthe = labyrinthe
        self.etat = EtatsItems.INTACT #Le niveau l'évacuera s'il n'est plus intact.
        self.priorite = 0 #Pour avoir le droit de la ramasser.
        self.action:Optional[Vole] = None #Utile uniquement quand l'item est lancé. Les items ne peuvent que voler
        self.lanceur:Agissant = NOONE
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
            self.action = None #Pylint n'a pas l'air de comprendre que Vole hérite de Action
        self.hauteur = 0

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
            if self.action.execute(): #Le vol devrait toujours être répétable
                raise ValueError("L'item a fini son vol ?! C'est pas normal !")
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

class Consommable(Item):
    """La classe des items qui peuvent être consommés. Ajoute à l'agissant un effet. Disparait après usage."""

class Ingredient(Item):
    """La classe des ingrédients d'alchimie."""
    def get_classe(self):
        """Se limite aux catégories de l'inventaire."""
        return Ingredient

    @staticmethod
    def get_image():
        return SKIN_INGREDIENT
