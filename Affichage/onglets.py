"""L'affichage principal de l'éditeur."""

from __future__ import annotations
from typing import Optional, TYPE_CHECKING

# Imports des classes parentes
from .noeuds import NoeudHorizontalProfondeurAgnostique, NoeudVerticalProfondeurAgnostique
from .wrapper_noeud import WrapperNoeud

# Imports utilisés dans le code
from .pavage import PavageHorizontal, PavageVertical
from .marge import MargeHorizontale, MargeVerticale
from .bouton import Bouton
from .liste import ListeVerticale, ListeHorizontale
from .wrapper import Wrapper
from .texte import CenterTexte
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
        self.onglet = Wrapper()
        self.onglets: list[Onglet] = []
        self.boutons: list[Bouton] = []
        self.set_direction(direction)

        self.fond = (255,255,255)
        self.actif = True
        self.set_courant(None)

    def set_direction(self, direction: DirectionAff):
        """Définit la direction des onglets."""
        match direction:
            case DirectionAff.UP:
                self.contenu = PavageHorizontal()
                diptique = PavageVertical()
                self.liste_boutons = ListeHorizontale()
                self.liste_boutons.set_contenu([MargeVerticale() if i%2==0 else self.boutons[i//2] for i in range(2*len(self.boutons)+1)],[5 if i%2==0 else 0 for i in range(2*len(self.boutons)+1)])
                diptique.set_contenu([MargeHorizontale(),self.liste_boutons,MargeHorizontale(),self.onglet,MargeHorizontale()],[5,0,5,-1,5])
                self.contenu.set_contenu([MargeVerticale(),diptique,MargeVerticale()],[5,-1,5])
            case DirectionAff.DOWN:
                self.contenu = PavageHorizontal()
                diptique = PavageVertical()
                self.liste_boutons = ListeHorizontale()
                self.liste_boutons.set_contenu([MargeVerticale() if i%2==0 else self.boutons[i//2] for i in range(2*len(self.boutons)+1)],[5 if i%2==0 else 0 for i in range(2*len(self.boutons)+1)])
                diptique.set_contenu([MargeHorizontale(),self.onglet,MargeHorizontale(),self.liste_boutons,MargeHorizontale()],[5,-1,5,0,5])
                self.contenu.set_contenu([MargeVerticale(),diptique,MargeVerticale()],[5,-1,5])
            case DirectionAff.LEFT:
                self.contenu = PavageVertical()
                diptique = PavageHorizontal()
                self.liste_boutons = ListeVerticale()
                self.liste_boutons.set_contenu([MargeHorizontale() if i%2==0 else self.boutons[i//2] for i in range(2*len(self.boutons)+1)],[5 if i%2==0 else 0 for i in range(2*len(self.boutons)+1)])
                diptique.set_contenu([MargeVerticale(),self.liste_boutons,MargeVerticale(),self.onglet,MargeVerticale()],[5,0,5,-1,5])
                self.contenu.set_contenu([MargeHorizontale(),diptique,MargeHorizontale()],[5,-1,5])
            case DirectionAff.RIGHT:
                self.contenu = PavageVertical()
                diptique = PavageHorizontal()
                self.liste_boutons = ListeVerticale()
                self.liste_boutons.set_contenu([MargeHorizontale() if i%2==0 else self.boutons[i//2] for i in range(2*len(self.boutons)+1)],[5 if i%2==0 else 0 for i in range(2*len(self.boutons)+1)])
                diptique.set_contenu([MargeVerticale(),self.onglet,MargeVerticale(),self.liste_boutons,MargeVerticale()],[5,-1,5,0,5])
                self.contenu.set_contenu([MargeHorizontale(),diptique,MargeHorizontale()],[5,-1,5])
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
            texte = CenterTexte("L'onglet s'affichera ici")
            self.onglet.set_contenu(texte)
            self.courant = texte
        else:
            self.courant = element
        self.onglet.set_tailles(self.onglet.tailles)

    def set_onglets(self, onglets: list[Onglet]):
        """Définit les onglets."""
        self.onglets = onglets
        self.boutons = [Bouton(SKIN_SHADE,onglet.nom) for onglet in onglets]
        self.liste_boutons.set_contenu([MargeHorizontale() if i%2==0 else self.boutons[i//2] for i in range(2*len(self.boutons)+1)],[5 if i%2==0 else 0 for i in range(2*len(self.boutons)+1)])
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
