from __future__ import annotations
from typing import TYPE_CHECKING, Optional

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from Jeu.Controleur import Controleur
    from Jeu.Labyrinthe.Structure_spatiale.Position import Position
    from Jeu.Labyrinthe.Structure_spatiale.Direction import Direction
    from Jeu.Entitee.Agissant.Agissant import Agissant
    from Jeu.Entitee.Entitee import Non_superposable
    from Jeu.Action.Deplacement import Vole

# Imports des classes parentes
from Jeu.Entitee.Entitee import Mobile

# Valeurs par défaut des paramètres
from Jeu.Labyrinthe.Structure_spatiale.Position import ABSENT

class Item(Mobile):
    """La classe des entitées inanimées. Peuvent se situer dans un inventaire. Peuvent être lancés (déconseillé pour les non-projectiles)."""
    def __init__(self,controleur:Controleur,position:Position, ID: Optional[int]=None):
        Entitee.__init__(self,controleur,position,ID)
        self.etat = "intact" #Le niveau l'évacuera s'il n'est plus intact.
        self.priorite = 0 #Pour avoir le droit de la ramasser.
        self.action:Optional[Vole] = None #Utile uniquement quand l'item est lancé. Les items ne peuvent que voler
        self.lanceur:Optional[Agissant] = None
        self.direction:Optional[Direction] = None #Utile uniquement quand l'item se déplace.
        self.poids:float = 10 #Utile uniquement quand l'item est lancé. Détermine le temps qu'il faut à l'agissant pour le lancer et le temps que l'item se déplacera.
        self.frottements:float = 10 #Utile uniquement quand l'item se déplace. Détermine la latence à chaque déplacement.
        self.hauteur:float = 0 #Utile uniquement quand l'item se déplace. Diminue à chaque tour. L'item s'immobilise à 0 (éventuellement déclenche des effets).
        self.nom:str = "item"

    def get_direction(self):
        if self.direction is not None:
            return self.direction
        else:
            return DIRECTIONS[0]

    def heurte_non_superposable(self,non_superposable:Non_superposable):
        for effet in self.effets :
            if isinstance(effet,On_hit) :
                effet.execute(self.lanceur,self.position,self.controleur)
        if isinstance(non_superposable,Agissant) and isinstance(self,Percant) :
            self.ajoute_effet(En_sursis())
        elif isinstance(self,(Fragile,Evanescent)):
            self.etat = "brisé"
            self.arret()
        else :
            self.arret()

    def heurte_mur(self):
        for effet in self.effets :
            if isinstance(effet,On_hit):
                effet.execute(self.lanceur,self.position,self.controleur)
        if isinstance(self,(Fragile,Evanescent)):
            self.etat = "brisé"
            self.arret()
        else :
            self.arret()

    def atterit(self):
        for effet in self.effets :
            if isinstance(effet,On_hit) :
                effet.execute(self.lanceur,self.position,self.controleur)
        if isinstance(self,Evanescent):
            self.etat = "brisé"
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
            if isinstance(effet,On_debut_tour):
                effet.execute(self) #On exécute divers effets
            if isinstance(effet,Time_limited):
                effet.wait()

    def pseudo_debut_tour(self):
        pass

    #Les agissants font leurs trucs, le controleur nous déplace, nous heurte (aïe !), tout le monde s'étripe...
    def vole(self):
        #On voooole (si on a été lancé)
        if self.action is not None:
            if self.action.execute():
                self.action = None # Ne devrait jamais arriver
                print("L'item a fini son vol !?!?")
        if self.hauteur <= 0:
            self.atterit()

    def fin_tour(self):
        #C'est déjà fini ? Vivement le prochain !
        for effet in self.effets:
            if isinstance(effet,On_fin_tour):
                effet.execute(self) #À condition qu'il y ait un prochain...

    def get_classe(self):
        return Item

    def get_skin_vue(self,forme):
        return SKINS_ITEMS_VUS[forme][self.nom]

    def get_skin(self):
        return SKIN_VIDE

    def get_titre(self,observation=0):
        return "Item"

    def get_description(self,observation=0):
        return ["Un item",f"Oopsie, on dirait que je n'ai pas codé la description pour {self}.","Désolé, et bonne chance."]

    @staticmethod
    def get_image():
        return SKIN_VIDE

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
from Jeu.Entitee.Entitee import Entitee
from Jeu.Entitee.Item.Projectile.Projectiles import Percant, Fragile, Evanescent
from Jeu.Labyrinthe.Structure_spatiale.Direction import DIRECTIONS
from Affichage.Skins.Skins import SKIN_VIDE, SKIN_INGREDIENT, SKINS_ITEMS_VUS
from Jeu.Effet.Effet import On_debut_tour, On_fin_tour, Time_limited
from Jeu.Effet.Effets_items import En_sursis, On_hit