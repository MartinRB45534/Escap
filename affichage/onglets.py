"""L'affichage principal de l'éditeur."""

from __future__ import annotations
from typing import Optional, TYPE_CHECKING

# Imports des classes parentes
from .wrapper_noeud import WrapperNoeud

# Imports utilisés dans le code
from .pavage import PavageHorizontalMarge, PavageVerticalMarge
from .bouton import Bouton
from .liste import ListeMargeVerticale, ListeMargeHorizontale
from .texte import Texte
from .wrapper_marge import WrapperMarge, WrapperCentre
from .skins import SKIN_SHADE
from .direction import DirectionAff

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from .onglet import Onglet
    from .cliquable import Cliquable

class Onglets(WrapperNoeud):
    """L'affichage principal de l'éditeur."""
    def __init__(self,direction: DirectionAff = DirectionAff.UP):
        WrapperNoeud.__init__(self)
        self.onglet = WrapperMarge((0, 0, 0, 0))
        self.onglets: list[Onglet] = []
        self.boutons: list[Bouton] = []
        self.contenu = WrapperMarge()
        self.set_direction(direction)

        self.fond = (255,255,255)
        self.set_courant(None)

    def set_direction(self, direction: DirectionAff):
        """Définit la direction des onglets."""
        assert isinstance(self.contenu, WrapperMarge)
        self.direction = direction
        match direction:
            case DirectionAff.UP:
                self.contenu.marges = (0, 5, 0, 0)
                diptique = PavageVerticalMarge()
                self.liste_boutons = ListeMargeHorizontale()
                self.liste_boutons.set_contenu(self.boutons)
                diptique.set_contenu([self.liste_boutons,self.onglet],[0,-1])
                self.contenu.set_contenu(diptique)
            case DirectionAff.DOWN:
                self.contenu.marges = (0, 0, 0, 5)
                diptique = PavageVerticalMarge()
                self.liste_boutons = ListeMargeHorizontale()
                self.liste_boutons.set_contenu(self.boutons)
                diptique.set_contenu([self.onglet,self.liste_boutons],[-1,0])
                self.contenu.set_contenu(diptique)
            case DirectionAff.LEFT:
                self.contenu.marges = (5, 0, 0, 0)
                diptique = PavageHorizontalMarge()
                self.liste_boutons = ListeMargeVerticale()
                self.liste_boutons.set_contenu(self.boutons)
                diptique.set_contenu([self.liste_boutons,self.onglet],[0,-1])
                self.contenu.set_contenu(diptique)
            case DirectionAff.RIGHT:
                self.contenu.marges = (0, 0, 5, 0)
                diptique = PavageHorizontalMarge()
                self.liste_boutons = ListeMargeVerticale()
                self.liste_boutons.set_contenu(self.boutons)
                diptique.set_contenu([self.onglet,self.liste_boutons],[-1,0])
                self.contenu.set_contenu(diptique)
            case _:
                raise ValueError("{self}.set_direction: ne prend que les directions UP, DOWN, LEFT et RIGHT, pas {direction}")

    def select(self, selection: Cliquable, droit: bool = False):
        if not droit:
            if selection in self.boutons:
                self.onglet.set_contenu(self.onglets[self.boutons.index(selection)])
                if self.actif:
                    self.unset_actif()
                    selection.set_actif()
            elif selection in self.onglets:
                self.onglet.set_contenu(selection)
                if self.actif:
                    self.unset_actif()
                    selection.set_actif()
            else:
                return
            self.set_courant(selection)
        self.set_tailles(self.tailles)

    def set_courant(self, element: Optional[Cliquable]):
        if element is None:
            contenu = WrapperCentre()
            texte = Texte("L'onglet s'affichera ici")
            contenu.set_contenu(texte)
            self.onglet.set_contenu(contenu)
            self.courant = texte
        elif element in self.boutons:
            self.courant = element
            self.onglet.set_contenu(self.onglets[self.boutons.index(element)])
        elif element in self.onglets:
            self.courant = element
            self.onglet.set_contenu(element)
        else:
            raise ValueError(f"{self}.set_courant : {element} n'est pas un élément de {self}")
        if self.tailles != (0,0):
            self.set_tailles(self.tailles)

    def set_onglets(self, onglets: list[Onglet]):
        """Définit les onglets."""
        self.onglets = onglets
        self.boutons = [Bouton(SKIN_SHADE, onglet.nom) for onglet in onglets]
        self.liste_boutons.set_contenu(self.boutons)
        if self.onglets:
            self.set_courant(self.boutons[0])
            self.boutons[0].set_actif()
        else:
            self.set_courant(None)

    def in_previous(self):
        if self.courant in self.boutons[1:]:
            self.set_courant(self.boutons[self.boutons.index(self.courant)-1])
            return self
        if self.courant in self.onglets[1:]:
            self.set_courant(self.onglets[self.onglets.index(self.courant)-1])
            return self
        return False

    def in_next(self):
        if self.courant in self.boutons[:-1]:
            self.set_courant(self.boutons[self.boutons.index(self.courant)+1])
            return self
        if self.courant in self.onglets[:-1]:
            self.set_courant(self.onglets[self.onglets.index(self.courant)+1])
            return self
        return False

    def in_up(self):
        if self.direction == DirectionAff.UP:
            if self.courant in self.onglets:
                self.select(self.boutons[self.onglets.index(self.courant)])
                return self
        elif self.direction == DirectionAff.DOWN:
            if self.courant in self.boutons:
                self.select(self.onglets[self.boutons.index(self.courant)])
                return self
        elif self.direction in [DirectionAff.LEFT, DirectionAff.RIGHT]:
            if self.courant in self.boutons[1:]:
                self.set_courant(self.boutons[self.boutons.index(self.courant)-1])
                return self
        return False

    def in_down(self):
        if self.direction == DirectionAff.UP:
            if self.courant in self.boutons:
                self.select(self.onglets[self.boutons.index(self.courant)])
                return self
        elif self.direction == DirectionAff.DOWN:
            if self.courant in self.onglets:
                self.select(self.boutons[self.onglets.index(self.courant)])
                return self
        elif self.direction in [DirectionAff.LEFT, DirectionAff.RIGHT]:
            if self.courant in self.boutons[:-1]:
                self.set_courant(self.boutons[self.boutons.index(self.courant)+1])
                return self
        return False

    def in_left(self):
        if self.direction == DirectionAff.LEFT:
            if self.courant in self.onglets:
                self.select(self.boutons[self.onglets.index(self.courant)])
                return self
        elif self.direction == DirectionAff.RIGHT:
            if self.courant in self.boutons:
                self.select(self.onglets[self.boutons.index(self.courant)])
                return self
        elif self.direction in [DirectionAff.UP, DirectionAff.DOWN]:
            if self.courant in self.boutons[1:]:
                self.set_courant(self.boutons[self.boutons.index(self.courant)-1])
                return self
        return False

    def in_right(self):
        if self.direction == DirectionAff.LEFT:
            if self.courant in self.boutons:
                self.select(self.onglets[self.boutons.index(self.courant)])
                return self
        elif self.direction == DirectionAff.RIGHT:
            if self.courant in self.onglets:
                self.select(self.boutons[self.onglets.index(self.courant)])
                return self
        elif self.direction in [DirectionAff.UP, DirectionAff.DOWN]:
            if self.courant in self.boutons[:-1]:
                self.set_courant(self.boutons[self.boutons.index(self.courant)+1])
                return self
        return False

    def through_left(self):
        if self.direction == DirectionAff.LEFT:
            if self.courant in self.onglets:
                self.courant.unset_actif()
                self.set_courant(self.boutons[self.onglets.index(self.courant)])
                self.set_actif()
                return self
        if self.direction == DirectionAff.RIGHT:
            if self.courant in self.boutons:
                self.courant.unset_actif()
                self.set_courant(self.onglets[self.boutons.index(self.courant)])
                self.courant.set_actif()
                return self
        if self.direction in [DirectionAff.UP, DirectionAff.DOWN]:
            if self.courant in self.boutons[1:]:
                self.courant.unset_actif()
                self.set_courant(self.boutons[self.boutons.index(self.courant)-1])
                self.courant.set_actif()
                return self
        return False

    def through_right(self):
        if self.direction == DirectionAff.RIGHT:
            if self.courant in self.onglets:
                self.courant.unset_actif()
                self.set_courant(self.boutons[self.onglets.index(self.courant)])
                self.set_actif()
                return self
        if self.direction == DirectionAff.LEFT:
            if self.courant in self.boutons:
                self.courant.unset_actif()
                self.set_courant(self.onglets[self.boutons.index(self.courant)])
                self.courant.set_actif()
                return self
        if self.direction in [DirectionAff.UP, DirectionAff.DOWN]:
            if self.courant in self.boutons[:-1]:
                self.courant.unset_actif()
                self.set_courant(self.boutons[self.boutons.index(self.courant)+1])
                self.courant.set_actif()
                return self
        return False

    def through_up(self):
        if self.direction == DirectionAff.UP:
            if self.courant in self.onglets:
                self.courant.unset_actif()
                self.set_courant(self.boutons[self.onglets.index(self.courant)])
                self.set_actif()
                return self
        if self.direction == DirectionAff.DOWN:
            if self.courant in self.boutons:
                self.courant.unset_actif()
                self.set_courant(self.onglets[self.boutons.index(self.courant)])
                self.courant.set_actif()
                return self
        if self.direction in [DirectionAff.LEFT, DirectionAff.RIGHT]:
            if self.courant in self.boutons[1:]:
                self.courant.unset_actif()
                self.set_courant(self.boutons[self.boutons.index(self.courant)-1])
                self.courant.set_actif()
                return self
        return False

    def through_down(self):
        if self.direction == DirectionAff.DOWN:
            if self.courant in self.onglets:
                self.courant.unset_actif()
                self.set_courant(self.boutons[self.onglets.index(self.courant)])
                self.set_actif()
                return self
        if self.direction == DirectionAff.UP:
            if self.courant in self.boutons:
                self.courant.unset_actif()
                self.set_courant(self.onglets[self.boutons.index(self.courant)])
                self.courant.set_actif()
                return self
        if self.direction in [DirectionAff.LEFT, DirectionAff.RIGHT]:
            if self.courant in self.boutons[:-1]:
                self.courant.unset_actif()
                self.set_courant(self.boutons[self.boutons.index(self.courant)+1])
                self.courant.set_actif()
                return self
        return False
