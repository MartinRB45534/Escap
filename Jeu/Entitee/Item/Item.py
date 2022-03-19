from Jeu.Constantes import *
from Jeu.Skins.Skins import *
from Jeu.Entitee.Entitee import *
#from Jeu.Général import *

class Item(Mobile):
    """La classe des entitées inanimées. Peuvent se situer dans un inventaire. Peuvent être lancés (déconseillé pour les non-projectiles)."""
    def __init__(self,position):
        Entitee.__init__(self,position)
        self.etat = "intact" #Le niveau l'évacuera s'il n'est plus intact.
        self.priorite = 0 #Pour avoir le droit de la ramasser.
        self.porteur = None
        self.lanceur = None
        self.direction = None #Utile uniquement quand l'item se déplace.
        self.latence = 0 #Utile uniquement quand l'item se déplace.
        self.vitesse = 1 #La quantitée soustraite à la latence chaque tour.
        self.taux_vitesse = {} #Le dictionnaire qui contient tous les multiplicateurs à appliquer à la vitesse. Correspond aux effets passager sur la vitesse.
        self.poids = 10 #Utile uniquement quand l'item est lancé. Détermine le temps qu'il faut à l'agissant pour le lancer et le temps que l'item se déplacera.
        self.frottements = 10 #Utile uniquement quand l'item se déplace. Détermine la latence à chaque déplacement.
        self.hauteur = 0 #Utile uniquement quand l'item se déplace. Diminue à chaque tour. L'item s'immobilise à 0 (éventuellement déclenche des effets).
        self.nom = "item"

    def get_direction(self):
        if self.direction != None:
            return self.direction
        else:
            return HAUT

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
        if "lancementv" in self.taux_vitesse.keys():
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

    def get_skin_vue(self,forme):
        return SKINS_ITEMS_VUS[forme][self.nom]

    def get_skin(self):
        return SKIN_VIDE

    def get_titre(self,observation):
        return "Item"

    def get_description(self,observation):
        return ["Un item",f"Oopsie, on dirait que je n'ai pas codé la description pour {self}.","Désolé, et bonne chance."]

    def get_image():
        return SKIN_VIDE

class Cadavre(Item):

    def get_titre(self,observation):
        return "Cadavre"

    def get_description(self,observation):
        return ["Un cadavre","Où as-tu trouvé ça ?"]

    def get_image():
        return SKIN_CADAVRE

class Oeuf(Item):

    def get_titre(self,observation):
        return "Oeuf"

    def get_description(self,observation):
        return ["Un oeuf","Je n'ai rien pour le cuire..."]

    def get_image():
        return SKIN_OEUF

class Consommable(Item):
    """La classe des items qui peuvent être consommés. Ajoute à l'agissant un effet. Disparait après usage."""

class Ingredient(Item):
    """La classe des ingrédients d'alchimie."""
    def get_classe(self):
        return Ingredient

    def get_image():
        return SKIN_INGREDIENT

from Jeu.Entitee.Agissant.Agissant import Agissant
from Jeu.Entitee.Item.Projectile.Projectiles import Percant,Evanescent,Fragile
from Jeu.Effet.Effets_items import *