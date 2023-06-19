from __future__ import annotations
from typing import List, Optional
from warnings import warn

from .Affichable import Affichable
from .Cliquable import Cliquable
from .Direction import Direction, Direction_aff

class Noeud(Cliquable):
    def __init__(self):
        self.tailles = (0,0) #La largeur et la hauteur (ou l'inverse ?)
        self.position = (0,0)
        self.marque_survol = False #Est-ce que la souris est dessus ?
        self.marque_actif = False #Est-ce que c'est l'élément actif  de la hiérarchie ?
        self.marque_courant = False #Est-ce que c'est l'élément courant de l'élément actif ?
        self.est_courant = False #Est-ce que c'est l'élément courant de son élément parent ?
        self.actif = False #Est-ce que l'élément est actif ?
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

    def select(self, selection: Affichable, droit:bool=False):
        if isinstance(selection, Cliquable) and not droit:
            self.set_courant(selection)

    def clique(self,position: List[int],droit:bool=False):
        clique = Affichable.clique(self,position,droit)
        if clique is self:
            self.set_actif()
        elif clique:
            self.select(clique,droit)
            self.unset_actif()
        else:
            self.unset_actif()
        if clique:
            return self
        return False

    def survol(self,position):
        survol = Affichable.survol(self,position)
        if survol is self:
            self.marque_survol = True
        else:
            self.marque_survol = False
        if survol:
            return self
        return False

    def navigue(self,direction: Direction):
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
        self.set_courant(None)
        self.unset_actif()

    def set_courant(self,element: Optional[Cliquable]):
        self.courant = element
        if element is None:
            self.set_actif()
        elif isinstance(element, Noeud):
            element.set_courant(element.courant) # Assure qu'il y aura un self.actif True quelque part
        elif isinstance(element, Cliquable):
            element.set_actif()
        else:
            warn(f"Knot.set_courant : {self} a reçu {element}")

    def navigue_in(self,direction: Direction): # On est l'élément actif
        if direction == Direction_aff.IN:
            return self.in_in()
        elif direction ==  Direction_aff.OUT:
            return self.in_out()
        elif direction ==  Direction_aff.PREVIOUS:
            return self.in_previous()
        elif direction ==  Direction_aff.NEXT:
            return self.in_next()
        elif direction ==  Direction_aff.LEFT:
            return self.in_left()
        elif direction ==  Direction_aff.RIGHT:
            return self.in_right()
        elif direction ==  Direction_aff.UP:
            return self.in_up()
        elif direction ==  Direction_aff.DOWN:
            return self.in_down()
        else:
            warn(f"Knot.navigue_in : Direction inconnue : {direction}")
            return self

    def navigue_through(self,direction: Direction): # On est sur le chemin de l'élément actif
        if direction == Direction_aff.IN:
            return self.through_in()
        elif direction ==  Direction_aff.OUT:
            return self.through_out()
        elif direction ==  Direction_aff.PREVIOUS:
            return self.through_previous()
        elif direction ==  Direction_aff.NEXT:
            return self.through_next()
        elif direction ==  Direction_aff.LEFT:
            return self.through_left()
        elif direction ==  Direction_aff.RIGHT:
            return self.through_right()
        elif direction ==  Direction_aff.UP:
            return self.through_up()
        elif direction ==  Direction_aff.DOWN:
            return self.through_down()
        else:
            warn(f"Knot.navigue_through : Direction inconnue : {direction}")
            return self
    
    def in_in(self): # On veut aller plus profond
        if self.courant is None:
            self.set_default_courant()
        self.unset_actif()
        if self.courant is not None:
            self.courant.set_actif()
        return self

    def in_out(self): # On veut ressortir
        self.unset_actif()
        return False
    
    def in_previous(self): # On veut aller au précédent de l'élément actuel
        return False # On laisse faire l'élément parent
    
    def in_next(self): # On veut aller au suivant de l'élément actuel
        return False
    
    def in_left(self): # On veut déplacer notre curseur (self.courant) vers la gauche
        return False # On ne fait rien par défaut
    
    def in_right(self): # On veut déplacer notre curseur (self.courant) vers la droite
        return False # On ne fait rien par défaut
    
    def in_up(self): # On veut déplacer notre curseur (self.courant) vers le haut
        return False # On ne fait rien par défaut
    
    def in_down(self): # On veut déplacer notre curseur (self.courant) vers le bas
        return False # On ne fait rien par défaut
    
    def through_in(self): # On veut aller plus profond, ça ne nous concerne pas
        return False
    
    def through_out(self): # On veut revenir ici
        if self.courant is None:
            raise RuntimeError("Knot.through_out : self.courant is None")
        self.courant.unset_actif()
        self.set_actif()
        return self
    
    def through_previous(self): # On veut aller au précédent de notre élément actuel
        return False # On ne fait rien par défaut
    
    def through_next(self): # On veut aller au suivant de notre élément actuel
        return False # On ne fait rien par défaut
    
    def through_left(self): # On veut déplacer le curseur, ça ne nous concerne pas
        return False
    
    def through_right(self): # On veut déplacer le curseur, ça ne nous concerne pas
        return False
    
    def through_up(self): # On veut déplacer le curseur, ça ne nous concerne pas
        return False
    
    def through_down(self): # On veut déplacer le curseur, ça ne nous concerne pas
        return False
