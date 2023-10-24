"""
Contient la classe ParentNoeud, qui est un noeud qui peut contenir des objets
"""

from __future__ import annotations
from typing import List, Tuple, Literal, TYPE_CHECKING

from .affichable import Affichable
from .cliquable import Cliquable
from .noeud import Noeud

if TYPE_CHECKING:
    from placeholder import Placeheldholder

class ParentNoeud(Noeud):
    """Un noeud qui peut contenir des objets"""
    def __init__(self):
        Noeud.__init__(self)
        
        self.objets:List[Affichable] = [] #La liste des objets à afficher

    def clique(self,position:Tuple[int,int],droit:bool=False):
        clique = False
        if self.touche(position):
            clique = self
        for objet in self.objets:
            res = objet.clique(position,droit)
            if res:
                clique = res
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

    def clique_placeholder(self,placeheldholder:Placeheldholder,droit:bool=False) -> Cliquable|Literal[False]:
        res = Affichable.clique_placeholder(self,placeheldholder,droit)
        if res:
            self.select(res,droit)
            return self
        return False

    def survol(self,position:Tuple[int,int]):
        survol = False
        if self.touche(position):
            survol = self
        for objet in self.objets:
            res = objet.survol(position)
            if res:
                survol = res
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

#Pour éviter les import circulaires
from .placeholder import Placeheldholder