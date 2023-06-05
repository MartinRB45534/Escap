from __future__ import annotations
from typing import List, TYPE_CHECKING
if TYPE_CHECKING:
    from Placeholder import Placeheldholder

from .Affichable import Affichable
from .Parent import Parent
from .Cliquable import Cliquable
from .Noeud import Noeud

class Parent_noeud(Parent,Noeud):
    def __init__(self):
        Noeud.__init__(self)
        
        self.objets:List[Affichable] = [] #La liste des objets à afficher

    def clique(self,position:List[int],droit:bool=False):
        clique = Parent.clique(self,position,droit)
        if clique is self:
            self.set_actif()
        elif isinstance(clique, Placeheldholder):
            res = self.clique_placeholder(clique,droit)
            if not res:
                self.unset_actif()
                return clique
        elif clique:
            assert isinstance(clique,Cliquable)
            self.select(clique,droit)
            self.unset_actif()
        else:
            self.unset_actif()
        if clique:
            return self
        return False

    def clique_placeholder(self,placeheldholder:Placeheldholder,droit:bool=False):
        res = Affichable.clique_placeholder(self,placeheldholder,droit)
        if res:
            self.select(res,droit)
            return self
        return False

    def survol(self,position):
        survol = Parent.survol(self,position)
        if survol is self:
            self.marque_survol = True
        else:
            self.marque_survol = False
        if survol:
            return self
        return False
    
    def select(self,selection:Cliquable,droit:bool=False):
        if isinstance(selection,Noeud) and not droit:
            self.set_courant(selection)

from .Wrapper_noeud import Wrapper_noeud #Pour éviter les import circulaires
from .Placeholder import Placeheldholder