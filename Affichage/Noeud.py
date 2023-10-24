"""
Le noeud est un élément qui réagit aux clics et qui peut contenir un autre élément actif.
"""

from __future__ import annotations
from typing import Optional, Literal
from warnings import warn

from .cliquable import Cliquable
from .direction import Direction, DirectionAff

class Noeud(Cliquable):
    """Un élément qui réagit aux clics et qui peut contenir un autre élément actif."""
    def __init__(self):
        super().__init__()
        self.courant = None #Quel est l'élément suivant dans la hiérarchie ?

    def trouve_actif(self):
        if self.actif:
            self.marque_actif = True
            if self.courant is not None:
                self.courant.marque_courant = True
        elif self.courant is not None:
            self.courant.trouve_actif()
        else:
            warn(f"Erreur : on a atteint {self} qui n'est pas actif, mais n'a pas de courant dénini !")

    def select(self, selection: Cliquable, droit:bool=False):
        """Sélectionne l'élément (fait plus de choses dans certaines classes filles)."""
        if not droit:
            self.set_courant(selection)

    def navigue(self,direction: Direction) -> Optional[Cliquable]|Literal[False]:
        if self.actif: #On est à ce niveau
            return self.navigue_in(direction)
        elif self.courant is None: # On est à un niveau inférieur, mais on est monté jusqu'ici quand même
            warn("Knot.navigue : On est à un niveau inférieur, mais on est monté jusqu'ici quand même avec self.courant qui vaut None")
            return False
        else:
            nav = self.courant.navigue(direction)
            if nav:
                self.select(nav)
                return self
            else:
                return self.navigue_through(direction)
    
    def set_default_courant(self):
        """Rend courant l'élément par défaut."""
        self.set_courant(None)
        self.unset_actif()

    def set_courant(self,element: Optional[Cliquable]):
        """Rend courant l'élément donné."""
        self.courant = element
        if element is None:
            self.set_actif()
        elif isinstance(element, Noeud):
            element.set_courant(element.courant) # Assure qu'il y aura un self.actif True quelque part
        else:
            element.set_actif()

    def navigue_in(self,direction: Direction) -> Optional[Cliquable]|Literal[False]: # On est l'élément actif
        """Navigue lorsque l'élément actif est son propre courant."""
        if direction == DirectionAff.IN:
            return self.in_in()
        elif direction ==  DirectionAff.OUT:
            return self.in_out()
        elif direction ==  DirectionAff.PREVIOUS:
            return self.in_previous()
        elif direction ==  DirectionAff.NEXT:
            return self.in_next()
        elif direction ==  DirectionAff.LEFT:
            return self.in_left()
        elif direction ==  DirectionAff.RIGHT:
            return self.in_right()
        elif direction ==  DirectionAff.UP:
            return self.in_up()
        elif direction ==  DirectionAff.DOWN:
            return self.in_down()
        else:
            warn(f"Knot.navigue_in : Direction inconnue : {direction}")
            return self

    def navigue_through(self,direction: Direction) -> Optional[Cliquable]|Literal[False]: # On est sur le chemin de l'élément actif
        """Navigue lorsque l'élément actif est un de ses enfants."""
        if direction == DirectionAff.IN:
            return self.through_in()
        elif direction ==  DirectionAff.OUT:
            return self.through_out()
        elif direction ==  DirectionAff.PREVIOUS:
            return self.through_previous()
        elif direction ==  DirectionAff.NEXT:
            return self.through_next()
        elif direction ==  DirectionAff.LEFT:
            return self.through_left()
        elif direction ==  DirectionAff.RIGHT:
            return self.through_right()
        elif direction ==  DirectionAff.UP:
            return self.through_up()
        elif direction ==  DirectionAff.DOWN:
            return self.through_down()
        else:
            warn(f"Knot.navigue_through : Direction inconnue : {direction}")
            return self
    
    def in_in(self) -> Optional[Cliquable]|Literal[False]: # On veut aller plus profond
        """Navigue vers l'élément suivant dans la hiérarchie."""
        if self.courant is None:
            self.set_default_courant()
        self.unset_actif()
        if self.courant is not None:
            self.courant.set_actif()
        return self

    def in_out(self) -> Optional[Cliquable]|Literal[False]: # On veut ressortir
        """Navigue vers l'élément précédent dans la hiérarchie."""
        self.unset_actif()
        return False
    
    def in_previous(self) -> Optional[Cliquable]|Literal[False]: # On veut aller au précédent de l'élément actuel
        """Navigue d'un enfant direct à un autre."""
        return False # On laisse faire l'élément parent
    
    def in_next(self) -> Optional[Cliquable]|Literal[False]: # On veut aller au suivant de l'élément actuel
        """Navigue d'un enfant direct à un autre."""
        return False
    
    def in_left(self) -> Optional[Cliquable]|Literal[False]: # On veut déplacer notre curseur (self.courant) vers la gauche
        """Navigue d'un enfant direct à un autre."""
        return False # On ne fait rien par défaut
    
    def in_right(self) -> Optional[Cliquable]|Literal[False]: # On veut déplacer notre curseur (self.courant) vers la droite
        """Navigue d'un enfant direct à un autre."""
        return False # On ne fait rien par défaut
    
    def in_up(self) -> Optional[Cliquable]|Literal[False]: # On veut déplacer notre curseur (self.courant) vers le haut
        """Navigue d'un enfant direct à un autre."""
        return False # On ne fait rien par défaut
    
    def in_down(self) -> Optional[Cliquable]|Literal[False]: # On veut déplacer notre curseur (self.courant) vers le bas
        """Navigue d'un enfant direct à un autre."""
        return False # On ne fait rien par défaut
    
    def through_in(self) -> Optional[Cliquable]|Literal[False]: # On veut aller plus profond, ça ne nous concerne pas
        """Navigue vers l'élément suivant dans la hiérarchie, à partir d'un enfant."""
        return False
    
    def through_out(self) -> Optional[Cliquable]|Literal[False]: # On veut revenir ici
        """Navigue vers l'élément précédent dans la hiérarchie, à partir d'un enfant.
           (donc on revient à self)
           """
        if self.courant is None:
            raise RuntimeError("Knot.through_out : self.courant is None")
        self.courant.unset_actif()
        self.set_actif()
        return self
    
    def through_previous(self) -> Optional[Cliquable]|Literal[False]: # On veut aller au précédent de notre élément actuel
        """Navigue d'un enfant à un autre."""
        return False # On ne fait rien par défaut
    
    def through_next(self) -> Optional[Cliquable]|Literal[False]: # On veut aller au suivant de notre élément actuel
        """Navigue d'un enfant à un autre."""
        return False # On ne fait rien par défaut
    
    def through_left(self) -> Optional[Cliquable]|Literal[False]: # On veut déplacer le curseur, ça ne nous concerne pas
        """Navigue d'un enfant à un autre."""
        return False
    
    def through_right(self) -> Optional[Cliquable]|Literal[False]: # On veut déplacer le curseur, ça ne nous concerne pas
        """Navigue d'un enfant à un autre."""
        return False
    
    def through_up(self) -> Optional[Cliquable]|Literal[False]: # On veut déplacer le curseur, ça ne nous concerne pas
        """Navigue d'un enfant à un autre."""
        return False
    
    def through_down(self) -> Optional[Cliquable]|Literal[False]: # On veut déplacer le curseur, ça ne nous concerne pas
        """Navigue d'un enfant à un autre."""
        return False
