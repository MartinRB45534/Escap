from __future__ import annotations
from typing import TYPE_CHECKING, List, Dict, Type
import carte as crt

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ..item.item import Item
    from ...labyrinthe.labyrinthe import Labyrinthe

# Imports des classes parentes
from ..entitee import NonSuperposable, Interactif

class Decors(NonSuperposable):
    """La classe des éléments de décors qu'on ne peut pas traverser. On peut interagir avec certains ?"""
    def __init__(self,position:crt.Position=crt.POSITION_ABSENTE):
        Entitee.__init__(self,position)
        self.etat  = "intact"

class Decors_interactif(Decors,Interactif):
    """La classe des éléments de décors avec lesquels on peut interagir."""
    pass

class Ustensile(Decors_interactif):
    """Permet de créer un Item à partir d'ingrédients"""
    def __init__(self,recettes:List[Dict[str,Dict[Type[Item],int]]],position:crt.Position=crt.POSITION_ABSENTE):
        Decors.__init__(self,position)
        self.recettes = recettes #Les recettes de création d'Item

    def get_recettes(self):
        return self.recettes

    def cuisine(self, labyrinthe:Labyrinthe, recette:Dict[str,Dict[Type[Item],int]]):
        return [produit(labyrinthe,crt.POSITION_ABSENTE) for produit in recette["produit"] for _ in range(recette["produit"][produit])]
    
# Imports utilisés dans le code
from ..entitee import Entitee