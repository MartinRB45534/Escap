"""L'affichage principal de l'éditeur."""

from __future__ import annotations

import affichage as af

class OngletTexte(af.NoeudHierarchiqueSinistreSommet,af.CenterTexte):
    """Un petit onglet pour tester."""
    def __init__(self, nom:str):
        af.NoeudHierarchiqueSinistreSommet.__init__(self)
        af.CenterTexte.__init__(self,nom)

class Onglet(af.NoeudHierarchiqueSinistreSommet,af.WrapperCliquable):
    """Un onglet qui contient un Cliquable quelconque."""
    def __init__(self, cliquable:af.Cliquable):
        af.NoeudHierarchiqueSinistreSommet.__init__(self)
        af.WrapperCliquable.__init__(self)
        contenu = af.PavageVertical()
        pavage = af.PavageHorizontal()
        pavage.set_contenu([af.MargeVerticale(),cliquable,af.MargeVerticale()],[-1,0,-1])
        contenu.set_contenu([af.MargeHorizontale(),pavage,af.MargeHorizontale()],[-1,0,-1])
        self.set_contenu(contenu)
        self.courant = cliquable
