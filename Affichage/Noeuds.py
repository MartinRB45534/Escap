from __future__ import annotations

from .Affichable import Affichable
from .Direction import Direction, Direction_aff
from .Noeud import Noeud

class Noeud_vertical(Noeud):
    """Un élément dont le contenu est disposé verticalement (donc next et previous correspondent à haut et bas)."""
    def through_previous(self):
        assert self.courant is not None
        self.courant.unset_actif() # Devrait être inutile
        res = self.in_up()
        self.courant.set_actif()
        return res
    
    def through_next(self):
        if self.courant is None:
            raise RuntimeError("Noeud.through_next : self.courant is None")
        self.courant.unset_actif() # Devrait être inutile
        res = self.in_down()
        self.courant.set_actif()
        return res

class Noeud_vertical_profondeur_agnostique(Noeud):
    """Un knot_vertical qui ne fait pas de différence entre in et through (pour haut et bas)."""
    def through_up(self):
        assert self.courant is not None
        self.courant.unset_actif() # Devrait être inutile
        res = self.in_up()
        self.courant.set_actif()
        return res
    
    def through_down(self):
        assert self.courant is not None
        self.courant.unset_actif()
        res = self.in_down()
        self.courant.set_actif()
        return res
    
class Noeud_horizontal(Noeud):
    """Un élément dont le contenu est disposé horizontalement (donc next et previous correspondent à gauche et droite)."""
    def through_previous(self):
        assert self.courant is not None
        self.courant.unset_actif() # Devrait être inutile
        res = self.in_left()
        self.courant.set_actif()
        return res
    
    def through_next(self):
        assert self.courant is not None
        self.courant.unset_actif() # Devrait être inutile
        res = self.in_right()
        self.courant.set_actif()
        return res
    
class Noeud_horizontal_profondeur_agnostique(Noeud):
    """Un knot_horizontal qui ne fait pas de différence entre in et through (pour gauche et droite)."""
    def through_left(self):
        assert self.courant is not None
        self.courant.unset_actif() # Devrait être inutile
        res = self.in_left()
        self.courant.set_actif()
        return res
    
    def through_right(self):
        assert self.courant is not None
        self.courant.unset_actif()
        res = self.in_right()
        self.courant.set_actif()
        return res

class Noeud_hierarchique_sinistre(Noeud):
    """Un élément dont le contenu est hiérarchique de gauche à droite (donc gauche et droite correspondent à out et in)."""
    def in_left(self):
        return self.in_out()
    
    def through_left(self):
        return self.through_out()
    
    def in_right(self):
        return self.in_in()
    
class Noeud_hierarchique_sinistre_sommet(Noeud):
    """Au sommet de la hiérarchie (donc il n'y a rien à gauche)"""
    def through_left(self):
        return self.through_out()
    
    def in_right(self):
        return self.in_in()
    
class Noeud_hierarchique_sinistre_base(Noeud):
    """En bas de la hiérarchie (donc il n'y a rien à droite)"""
    def in_left(self):
        return self.in_out()
    
class Noeud_hierarchique_dextre(Noeud):
    """Un élément dont le contenu est hiérarchique de droite à gauche (donc gauche et droite correspondent à in et out)."""
    def in_left(self):
        return self.in_in()
    
    def through_right(self):
        return self.through_out()
    
    def in_right(self):
        return self.in_out()
    
class Noeud_hierarchique_dextre_sommet(Noeud):
    """Au sommet de la hiérarchie (donc il n'y a rien à droite)"""
    def through_right(self):
        return self.through_out()
    
    def in_left(self):
        return self.in_in()
    
class Noeud_hierarchique_dextre_base(Noeud):
    """En bas de la hiérarchie (donc il n'y a rien à gauche)"""
    def in_right(self):
        return self.in_out()

class Noeud_bloque(Noeud):
    """Un élément bloqué (pas de navigation, ni d'effets pour les clics)."""
    def navigue(self, direction: Direction):
        if self.actif:
            if direction == Direction_aff.IN:
                if self.courant is None:
                    raise(NotImplementedError("Un Noeud_bloque doit avoir un élément courant."))
                else:
                    self.unset_actif()
                    self.courant.set_actif()
                    return self
            elif direction == Direction_aff.OUT:
                self.unset_actif()
                return False
            elif direction == Direction_aff.PREVIOUS:
                self.unset_actif()
                return False
            elif direction == Direction_aff.NEXT:
                self.unset_actif()
                return False
        elif self.courant is None:
            raise(NotImplementedError("Un Wrapper_bloque doit avoir un élément courant."))
        else:
            nav = self.courant.navigue(direction)
            if nav:
                self.select(nav)
                return self
            else:
                if direction == Direction_aff.OUT:
                    self.set_actif()
                    return self
            return self
            
    def select(self, selection: Affichable, droit: bool = False):
        pass
