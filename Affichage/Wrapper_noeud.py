"""
Contient les classes Wrapper_noeud et Wrapper_noeud_bloque
"""

from __future__ import annotations
from typing import Tuple, Literal, TYPE_CHECKING

from .noeud import Noeud
from .noeuds import NoeudBloque
from .wrapper import Wrapper
from .wrapper_cliquable import WrapperCliquable

if TYPE_CHECKING:
    from .placeholder import Placeheldholder
    from .cliquable import Cliquable

class WrapperNoeud(Noeud,WrapperCliquable):
    """Un wrapper_cliquable qui a des enfants""" #Constitue la majorité de mon affichage
    def __init__(self):
        Noeud.__init__(self)
        WrapperCliquable.__init__(self)

    def clique(self,position:Tuple[int,int], droit:bool=False) -> Cliquable|Literal[False]:
        clique = Wrapper.clique(self,position,droit)
        if clique is self:
            self.set_actif()
        elif clique:
            self.select(clique, droit)
            self.unset_actif()
            if isinstance(clique, Placeheldholder):
                res = self.clique_placeholder(clique, droit)
                if not res:
                    return clique
        else:
            self.unset_actif()
        if clique:
            return self
        return False

    def clique_placeholder(self,placeheldholder: Placeheldholder, droit:bool=False) -> Cliquable|Literal[False]:
        res = Wrapper.clique_placeholder(self,placeheldholder, droit)
        if res:
            self.select(res, droit)
            return self
        return False

class WrapperNoeudBloque(NoeudBloque,WrapperNoeud):
    """Un wrapper_noeud qui est bloqué"""

# Désolé pour ça, mais Placeheldholder hérite de WrapperNoeud donc il faut que ce soit après
from .placeholder import Placeheldholder
