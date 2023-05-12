from __future__ import annotations
from Affichage.Skins.Skins import *
from Jeu.Entitee.Entitee import *
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Jeu.Entitee.Agissant.Agissant import Agissant
    from Jeu.Controleur import Controleur

class Item(Mobile):
    """La classe des entitées inanimées. Peuvent se situer dans un inventaire. Peuvent être lancés (déconseillé pour les non-projectiles)."""
    def __init__(self,controleur:Controleur,position:Position, ID: Optional[int]=None):
        Entitee.__init__(self,controleur,position,ID)
        self.etat = "intact" #Le niveau l'évacuera s'il n'est plus intact.
        self.priorite = 0 #Pour avoir le droit de la ramasser.
        # self.porteur:Optional[int] = None #Utilisé ? /!\
        self.lanceur:Optional[Agissant] = None
        self.direction:Optional[Direction] = None #Utile uniquement quand l'item se déplace.
        self.latence:float = 0 #Utile uniquement quand l'item se déplace.
        self.vitesse:float = 1 #La quantitée soustraite à la latence chaque tour.
        self.taux_vitesse = {} #Le dictionnaire qui contient tous les multiplicateurs à appliquer à la vitesse. Correspond aux effets passager sur la vitesse.
        self.poids:float = 10 #Utile uniquement quand l'item est lancé. Détermine le temps qu'il faut à l'agissant pour le lancer et le temps que l'item se déplacera.
        self.frottements:float = 10 #Utile uniquement quand l'item se déplace. Détermine la latence à chaque déplacement.
        self.hauteur:float = 0 #Utile uniquement quand l'item se déplace. Diminue à chaque tour. L'item s'immobilise à 0 (éventuellement déclenche des effets).
        self.nom:str = "item"

    def get_direction(self):
        if self.direction is not None:
            return self.direction
        else:
            return DIRECTIONS[0]

    def get_vitesse(self):
        vitesse = self.vitesse
        for taux in self.taux_vitesse.values() :
            vitesse *= taux
        return vitesse

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
        self.latence = 0
        if "lancementv" in self.taux_vitesse:
            self.taux_vitesse.pop("lancementv")
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
        self.hauteur -= self.poids
        self.add_latence(self.frottements)
        if self.hauteur <= 0:
            self.atterit()

    def fin_tour(self):
        #C'est déjà fini ? Vivement le prochain !
        if self.hauteur > 0:
            self.latence -= self.get_vitesse()
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
    def utilise(self,porteur:Agissant):
        pass

class Ingredient(Item):
    """La classe des ingrédients d'alchimie."""
    def get_classe(self):
        return Ingredient

    @staticmethod
    def get_image():
        return SKIN_INGREDIENT

from Jeu.Entitee.Item.Projectile.Projectiles import Percant, Evanescent, Fragile
from Jeu.Effet.Effets_items import *