"""L'affichage principal de l'éditeur."""

from __future__ import annotations
from typing import Optional, TYPE_CHECKING, List

# Imports des classes parentes
from .noeuds import NoeudHorizontalProfondeurAgnostique, NoeudVerticalProfondeurAgnostique
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

class Onglets(WrapperNoeud,NoeudHorizontalProfondeurAgnostique,NoeudVerticalProfondeurAgnostique):
    """L'affichage principal de l'éditeur."""
    def __init__(self,direction: DirectionAff = DirectionAff.UP):
        WrapperNoeud.__init__(self)
        NoeudHorizontalProfondeurAgnostique.__init__(self)
        NoeudVerticalProfondeurAgnostique.__init__(self)
        self.onglet = WrapperMarge()
        self.onglets: List[Onglet] = []
        self.boutons: List[Bouton] = []
        self.contenu = WrapperMarge()
        self.set_direction(direction)

        self.fond = (255,255,255)
        self.actif = True
        self.set_courant(None)

    def set_direction(self, direction: DirectionAff):
        """Définit la direction des onglets."""
        assert isinstance(self.contenu, WrapperMarge)
        match direction:
            case DirectionAff.UP:
                diptique = PavageVerticalMarge()
                self.liste_boutons = ListeMargeHorizontale()
                self.liste_boutons.set_contenu(self.boutons)
                diptique.set_contenu([self.liste_boutons,self.onglet],[0,-1])
                self.contenu.set_contenu(diptique)
            case DirectionAff.DOWN:
                diptique = PavageVerticalMarge()
                self.liste_boutons = ListeMargeHorizontale()
                self.liste_boutons.set_contenu(self.boutons)
                diptique.set_contenu([self.onglet,self.liste_boutons],[-1,0])
                self.contenu.set_contenu(diptique)
            case DirectionAff.LEFT:
                diptique = PavageHorizontalMarge()
                self.liste_boutons = ListeMargeVerticale()
                self.liste_boutons.set_contenu(self.boutons)
                diptique.set_contenu([self.liste_boutons,self.onglet],[0,-1])
                self.contenu.set_contenu(diptique)
            case DirectionAff.RIGHT:
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
                self.set_courant(self.onglets[self.boutons.index(selection)])
        self.onglet.set_tailles(self.onglet.tailles)

    def set_courant(self, element: Optional[Cliquable]):
        if element is None:
            contenu = WrapperCentre()
            texte = Texte("L'onglet s'affichera ici")
            contenu.set_contenu(texte)
            self.onglet.set_contenu(contenu)
            self.courant = texte
        else:
            self.courant = element
        self.onglet.set_tailles(self.onglet.tailles)

    def set_onglets(self, onglets: List[Onglet]):
        """Définit les onglets."""
        self.onglets = onglets
        self.boutons = [Bouton(SKIN_SHADE, onglet.nom) for onglet in onglets]
        self.liste_boutons.set_contenu(self.boutons)
        self.set_courant(self.onglets[0] if self.onglets else None)

    def in_up(self):
        if self.courant in self.boutons[1:]:
            self.set_courant(self.boutons[self.boutons.index(self.courant)-1])

    def in_down(self):
        if self.courant in self.boutons[:-1]:
            self.set_courant(self.boutons[self.boutons.index(self.courant)+1])

    def in_left(self):
        if self.courant in self.onglets:
            self.select(self.boutons[self.onglets.index(self.courant)])

    def in_right(self):
        if self.courant in self.boutons:
            self.select(self.onglets[self.boutons.index(self.courant)])
