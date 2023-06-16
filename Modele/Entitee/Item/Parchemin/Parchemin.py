from __future__ import annotations
from typing import TYPE_CHECKING, Type
import Carte as crt

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ....Effet.Effet import Effet
    from ....Labyrinthe.Labyrinthe import Labyrinthe

# Imports des classes parentes
from ..Item import Consommable

class Parchemin(Consommable):
    """La classe des consommables qui s'activent avec du mana."""
    def __init__(self,labyrinthe:Labyrinthe,effet:Effet,cout:float,duree:float=2,position:crt.Position=crt.POSITION_ABSENTE):
        Item.__init__(self,labyrinthe,position)
        self.effet = effet
        self.duree = duree
        self.cout = cout

    def get_titre(self,observation=0):
        return "Parchemin"

    def get_description(self,observation=0):
        return ["Un parchemin","C'est quoi ces gribouillis ?"]

    def get_classe(self):
        return Parchemin

    def get_skin(self):
        return SKIN_PARCHEMIN

    @staticmethod
    def get_image():
        return SKIN_PARCHEMIN

# Imports utilisés dans le code
from Old_Affichage.Skins.Skins import SKIN_PARCHEMIN
from ..Item import Item