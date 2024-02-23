"""Contient la classe Projectile."""

from __future__ import annotations
import carte as crt

# Imports des classes parentes
from ..item import Item

# Imports utilisés dans le code
from ....affichage import SKIN_PROJECTILE
from ....effet import Sursis
from ....commons import EtatsItems

class Projectile(Item):
    """La classe des items destinés à être lancés. Possèdent naturellement une vitesse non nulle."""
    def __init__(self,position:crt.Position):
        Item.__init__(self,position)

    @staticmethod
    def get_image():
        return SKIN_PROJECTILE

class Percant(Projectile):
    """La classe des projectiles qui peuvent transpercer un ennemi."""
    def heurte_agissant(self):
        self.frappe()
        self.ajoute_effet(Sursis())

class Fragile(Item):
    """La classe des items qui se brisent lors d'un choc."""
    def heurte(self):
        self.etat = EtatsItems.BRISE
        self.arret()

class Evanescent(Fragile):
    """La classe des items qui disparaissent s'ils ne sont pas en mouvement (les sorts de projectiles, par exemple, qui sont des items...)."""
    def arret(self):
        self.etat = EtatsItems.BRISE
        Item.arret(self)
