from __future__ import annotations
from typing import List, Optional, Tuple, TYPE_CHECKING
if TYPE_CHECKING:
    from Placeholder import Placeheldholder

from .Affichable import Affichable
from .Noeud import Noeud
from .Noeuds import Noeud_bloque
from .Wrapper import Wrapper
from .Wrapper_cliquable import Wrapper_cliquable

class Wrapper_noeud(Wrapper_cliquable,Noeud):
    """Un wrapper_cliquable qui a des enfants""" #Constitue la majorité de mon affichage
    def __init__(self):
        Noeud.__init__(self)

        self.objets:List[Affichable] = []
        self.contenu:Optional[Affichable] = None #L'objet qu'il 'contient'
        self.fond:Tuple = (0,0,0,0)

    def clique(self,position, droit:bool=False):
        clique = Wrapper.clique(self,position,droit)
        if clique is self:
            self.set_actif()
        elif isinstance(clique, Placeheldholder):
            res = self.clique_placeholder(clique, droit)
            if not res:
                self.unset_actif()
                return clique
        elif clique:
            self.select(clique, droit)
            self.unset_actif()
        else:
            self.unset_actif()
        if clique:
            return self
        return False
    
    def clique_placeholder(self,placeheldholder: Placeheldholder, droit:bool=False):
        res = Wrapper.clique_placeholder(self,placeheldholder, droit)
        if res:
            self.select(res, droit)
            return self
        return False

class Wrapper_noeud_bloque(Noeud_bloque,Wrapper_noeud):
    pass

from .Placeholder import Placeheldholder