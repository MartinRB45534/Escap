"""Contient les classes des décors."""

from __future__ import annotations
from typing import TYPE_CHECKING
import carte as crt

# Imports des classes parentes
from ..entitee import NonSuperposable, Interactif
from ...commons import EtatsDecors

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ..item.item import Item
    from ...labyrinthe.labyrinthe import Labyrinthe

class Decors(NonSuperposable):
    """La classe des éléments de décors qu'on ne peut pas traverser. On peut interagir avec certains ?"""
    def __init__(self,position:crt.Position=crt.POSITION_ABSENTE):
        NonSuperposable.__init__(self,position)
        self.etat  = EtatsDecors.INTACT

    def ecrase(self):
        """Écrase le décors."""
        self.etat = EtatsDecors.ECRASE

class DecorsInteractif(Decors,Interactif):
    """La classe des éléments de décors avec lesquels on peut interagir."""

class Ustensile(DecorsInteractif):
    """Permet de créer un Item à partir d'ingrédients"""
    def __init__(self,recettes:list[dict[str,dict[type[Item],int]]],position:crt.Position=crt.POSITION_ABSENTE):
        DecorsInteractif.__init__(self,position)
        self.recettes = recettes #Les recettes de création d'Item

    def get_recettes(self):
        """Renvoie les recettes de l'ustensile."""
        return self.recettes

    def cuisine(self, labyrinthe:Labyrinthe, recette:dict[str,dict[type[Item],int]]):
        """Renvoie un Item à partir d'une recette."""
        return [produit(labyrinthe,crt.POSITION_ABSENTE) for produit in recette["produit"] for _ in range(recette["produit"][produit])]
