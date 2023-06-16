from __future__ import annotations
from typing import TYPE_CHECKING, List
import Carte as crt
from Modele.Labyrinthe.Labyrinthe import Labyrinthe

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ...Agissant.Agissant import Agissant
    from ....Labyrinthe.Labyrinthe import Labyrinthe
    from ....Systeme.Elements import Element

# Imports des classes parentes
from .Projectile import Projectile
from ..Item import Item
from ...Entitee import Fantome

class Explosif(Projectile):
    """La classe des projectiles qui explosent. Affectés différemment par certains skills."""
    pass

class Charge(Explosif):
    def __init__(self,labyrinthe:Labyrinthe,niveau:int,vitesse:float=0,poids:float=0,frottements:float=0,portee:float=0,degats:float=0,position:crt.Position=crt.POSITION_ABSENTE):
        Item.__init__(self,labyrinthe,position)
        self.etat = Etats_items.INTACT #Le niveau l'évacuera s'il n'est plus intact.
        self.priorite = 0
        self.porteur = None
        self.lanceur = None
        self.direction = None
        self.latence = 0
        self.vitesse = vitesse
        self.taux_vitesse = {}
        self.poids = poids
        self.frottements = frottements
        self.hauteur = 0
        self.effets = [On_hit(portee,degats)]
        self.niveau = niveau #On garde l'info pour un éventuel observateur

class Percant(Projectile):
    """La classe des projectiles qui peuvent transpercer un ennemi."""
    pass

class Fleche(Percant):
    """La classe des projectiles de type flèche. Affectés différemment par certains skills."""
    def __init__(self,labyrinthe:Labyrinthe,niveau:int,vitesse:float=0,poids:float=0,frottements:float=0,degats:float=0,position:crt.Position=crt.POSITION_ABSENTE):
        Item.__init__(self,labyrinthe,position)
        self.etat = Etats_items.INTACT
        self.priorite = 0 #Faire dépendre du niveau ?
        self.porteur = None
        self.lanceur = None
        self.direction = None
        self.latence = 0
        self.vitesse = vitesse
        self.taux_vitesse = {}
        self.poids = poids
        self.frottements = frottements
        self.hauteur = 0
        self.effets = [On_hit(1,degats)]
        self.niveau = niveau #On garde l'info pour un éventuel observateur

class Fleche_fantome(Fleche,Fantome):
    """Une flèche qui peut traverser les murs. Est-ce l'âme d'une flèche décédée ?"""
    def __init__(self,labyrinthe:Labyrinthe,niveau:int,vitesse:float=0,poids:float=0,frottements:float=0,degats:float=0,position:crt.Position=crt.POSITION_ABSENTE):
        Item.__init__(self,labyrinthe,position)
        self.etat = Etats_items.INTACT
        self.priorite = 0 #Faire dépendre du niveau ?
        self.porteur = None
        self.lanceur = None
        self.direction = None
        self.latence = 0
        self.vitesse = vitesse
        self.taux_vitesse = {}
        self.poids = poids
        self.frottements = frottements
        self.hauteur = 0
        self.effets = [On_hit(1,degats)]
        self.niveau = niveau #On garde l'info pour un éventuel observateur

class Fleche_explosive(Fleche,Explosif):
    """Une flèche explosive. C'est une flèche ou un explosif ? Mieux vaut rester loin en tous cas..."""
    def __init__(self,labyrinthe:Labyrinthe,niveau:int,vitesse:float=0,poids:float=0,frottements:float=0,portee:float=0,degats:float=0,position:crt.Position=crt.POSITION_ABSENTE):
        Item.__init__(self,labyrinthe,position)
        self.etat = Etats_items.INTACT
        self.priorite = 0 #Faire dépendre du niveau ?
        self.porteur = None
        self.lanceur = None
        self.direction = None
        self.latence = 0
        self.vitesse = vitesse
        self.taux_vitesse = {}
        self.poids = poids
        self.frottements = frottements
        self.hauteur = 0
        self.effets = [On_hit(portee,degats)]
        self.niveau = niveau #On garde l'info pour un éventuel observateur

class Perce_armure(Item):
    """La classe des items qui peuvent infliger des dégats sans être affectés par les défenses comme l'armure ou le bouclier."""

class Fragile(Item):
    """La classe des items qui se brisent lors d'un choc."""
    pass

class Evanescent(Item):
    """La classe des items qui disparaissent s'ils ne sont pas en mouvement (les sorts de projectiles, par exemple, qui sont des items...)."""
    pass

class Projectile_magique(Projectile,Evanescent):
    """La classe des projectiles créés par magie."""
    def __init__(self,labyrinthe:Labyrinthe,niveau:int,vitesse:float=0,poids:float=0,frottements:float=0,degats:float=0,element:Element=Element.TERRE,position:crt.Position=crt.POSITION_ABSENTE):
        Item.__init__(self,labyrinthe,position)
        self.etat = Etats_items.INTACT
        self.priorite = 0 #Faire dépendre du niveau ?
        self.porteur = None
        self.lanceur = None
        self.direction = None
        self.latence = 0
        self.vitesse = vitesse
        self.taux_vitesse = {}
        self.poids = poids
        self.frottements = frottements
        self.hauteur = 0
        self.effets = [On_hit(1,degats,element)]
        self.niveau = niveau #On garde l'info pour un éventuel observateur

class Magie_explosive(Explosif,Projectile_magique):
    """La classe des projectiles explosifs créés par magie."""
    def __init__(self,labyrinthe:Labyrinthe,niveau:int,vitesse:float=0,poids:float=0,frottements:float=0,portee:float=0,degats:float=0,element:Element=Element.TERRE,position:crt.Position=crt.POSITION_ABSENTE):
        Item.__init__(self,labyrinthe,position)
        self.etat = Etats_items.INTACT #Le niveau l'évacuera s'il n'est plus intact.
        self.priorite = 0
        self.porteur = None
        self.lanceur = None
        self.direction = None
        self.latence = 0
        self.vitesse = vitesse
        self.taux_vitesse = {}
        self.poids = poids
        self.frottements = frottements
        self.hauteur = 0
        self.effets = [On_hit(portee,degats,element)]
        self.niveau = niveau #On garde l'info pour un éventuel observateur

class Fleche_magique(Fleche,Projectile_magique):
    """La classe des flèches créées par magie."""
    def __init__(self, labyrinthe: Labyrinthe, niveau: int, vitesse: float = 0, poids: float = 0, frottements: float = 0, degats: float = 0, element: Element = Element.TERRE, position: crt.Position = crt.POSITION_ABSENTE):
        Projectile_magique.__init__(self,labyrinthe,niveau,vitesse,poids,frottements,degats,element,position)

class Perce_armure_magique(Perce_armure,Projectile_magique):
    """La classe des projectiles perce_armures créés par magie."""
    def __init__(self, labyrinthe: Labyrinthe, niveau: int, vitesse: float = 0, poids: float = 0, frottements: float = 0, degats: float = 0, element: Element = Element.TERRE, position: crt.Position = crt.POSITION_ABSENTE):
        Projectile_magique.__init__(self,labyrinthe,niveau,vitesse,poids,frottements,degats,element,position)

class Magie_explosive_percante(Magie_explosive,Percant):
    """La classe des projectiles explosifs perçant créés par magie."""
    def __init__(self, labyrinthe: Labyrinthe, niveau: int, vitesse: float = 0, poids: float = 0, frottements: float = 0, portee: float = 0, degats: float = 0, element: Element = Element.TERRE, position: crt.Position = crt.POSITION_ABSENTE):
        Magie_explosive.__init__(self,labyrinthe,niveau,vitesse,poids,frottements,portee,degats,element,position)

# Imports utilisés dans le code
from ....Effet.Effets_items import On_hit
from ....Systeme.Elements import Element
from ..Etats import Etats_items