"""
Ce fichier contient les classes des projectiles et des items qui peuvent être lancés.
"""

from __future__ import annotations
from typing import TYPE_CHECKING
import carte as crt

# Imports des classes parentes
from .projectile import Projectile
from ..item import Item

# Imports des valeurs par défaut des paramètres
from ....commons import Element, EtatsItems
from ....effet import OnHit, Sursis

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ....labyrinthe.labyrinthe import Labyrinthe

class Explosif(Projectile):
    """La classe des projectiles qui explosent. Affectés différemment par certains skills."""

class Charge(Explosif):
    """Une charge explosive."""
    def __init__(self,labyrinthe:Labyrinthe,niveau:int,vitesse:float=0,poids:float=0,frottements:float=0,portee:float=0,degats:float=0,position:crt.Position=crt.POSITION_ABSENTE):
        Explosif.__init__(self,labyrinthe,vitesse,[OnHit(portee,degats)],position)
        self.poids = poids
        self.frottements = frottements
        self.niveau = niveau #On garde l'info pour un éventuel observateur

class Percant(Projectile):
    """La classe des projectiles qui peuvent transpercer un ennemi."""
    def heurte_agissant(self):
        self.frappe()
        self.ajoute_effet(Sursis())

class Fleche(Percant):
    """La classe des projectiles de type flèche. Affectés différemment par certains skills."""
    def __init__(self,labyrinthe:Labyrinthe,niveau:int,vitesse:float=0,poids:float=0,frottements:float=0,degats:float=0,position:crt.Position=crt.POSITION_ABSENTE):
        Percant.__init__(self,labyrinthe,vitesse,[OnHit(1,degats)],position)
        self.poids = poids
        self.frottements = frottements
        self.niveau = niveau #On garde l'info pour un éventuel observateur

class FlecheFantome(Fleche):
    """Une flèche qui peut traverser les murs. Est-ce l'âme d'une flèche décédée ?"""
    def __init__(self,labyrinthe:Labyrinthe,niveau:int,vitesse:float=0,poids:float=0,frottements:float=0,degats:float=0,position:crt.Position=crt.POSITION_ABSENTE):
        Fleche.__init__(self,labyrinthe,niveau,vitesse,poids,frottements,degats,position)
        self.fantome = True

class FlecheExplosive(Fleche,Explosif):
    """Une flèche explosive. C'est une flèche ou un explosif ? Mieux vaut rester loin en tous cas..."""
    def __init__(self,labyrinthe:Labyrinthe,niveau:int,vitesse:float=0,poids:float=0,frottements:float=0,portee:float=0,degats:float=0,position:crt.Position=crt.POSITION_ABSENTE):
        Fleche.__init__(self,labyrinthe,niveau,vitesse,poids,frottements,degats,position)
        Explosif.__init__(self,labyrinthe,vitesse,[OnHit(portee,degats)],position)
        # Fleche en premier pour que l'effet soit bien celui de l'explosion

class PerceArmure(Item):
    """La classe des items qui peuvent infliger des dégats sans être affectés par les défenses comme l'armure ou le bouclier."""

class Fragile(Item):
    """La classe des items qui se brisent lors d'un choc."""
    def heurte(self):
        self.etat = EtatsItems.BRISE
        self.arret()

class Evanescent(Item):
    """La classe des items qui disparaissent s'ils ne sont pas en mouvement (les sorts de projectiles, par exemple, qui sont des items...)."""
    def arret(self):
        self.etat = EtatsItems.BRISE
        super().arret()

class ProjectileMagique(Projectile,Evanescent):
    """La classe des projectiles créés par magie."""
    def __init__(self,labyrinthe:Labyrinthe,niveau:int,vitesse:float,poids:float,frottements:float,degats:float,element:Element,position:crt.Position=crt.POSITION_ABSENTE):
        Evanescent.__init__(self,labyrinthe,position)
        Projectile.__init__(self,labyrinthe,vitesse,[OnHit(1,degats,element)],position)
        self.poids = poids
        self.frottements = frottements
        self.niveau = niveau #On garde l'info pour un éventuel observateur

class MagieExplosive(Explosif,ProjectileMagique):
    """La classe des projectiles explosifs créés par magie."""
    def __init__(self,labyrinthe:Labyrinthe,niveau:int,vitesse:float,poids:float,frottements:float,portee:float,degats:float,element:Element,position:crt.Position=crt.POSITION_ABSENTE):
        ProjectileMagique.__init__(self,labyrinthe,niveau,vitesse,poids,frottements,degats,element,position)
        Explosif.__init__(self,labyrinthe,vitesse,[OnHit(portee,degats,element)],position)

class FlecheMagique(Fleche,ProjectileMagique):
    """La classe des flèches créées par magie."""
    def __init__(self, labyrinthe: Labyrinthe, niveau: int, vitesse: float, poids: float, frottements: float, degats: float, element: Element, position: crt.Position = crt.POSITION_ABSENTE):
        Fleche.__init__(self,labyrinthe,niveau,vitesse,poids,frottements,degats,position)
        ProjectileMagique.__init__(self,labyrinthe,niveau,vitesse,poids,frottements,degats,element,position)

class PerceArmureMagique(PerceArmure,ProjectileMagique):
    """La classe des projectiles perce_armures créés par magie."""
    def __init__(self, labyrinthe: Labyrinthe, niveau: int, vitesse: float, poids: float, frottements: float, degats: float, element: Element, position: crt.Position = crt.POSITION_ABSENTE):
        PerceArmure.__init__(self,labyrinthe,position)
        ProjectileMagique.__init__(self,labyrinthe,niveau,vitesse,poids,frottements,degats,element,position)

class MagieExplosivePercante(MagieExplosive,Percant):
    """La classe des projectiles explosifs perçant créés par magie."""
    def __init__(self, labyrinthe: Labyrinthe, niveau: int, vitesse: float, poids: float, frottements: float, portee: float, degats: float, element: Element, position: crt.Position = crt.POSITION_ABSENTE):
        Percant.__init__(self,labyrinthe,vitesse,[OnHit(portee,degats,element)],position)
        MagieExplosive.__init__(self,labyrinthe,niveau,vitesse,poids,frottements,portee,degats,element,position)
