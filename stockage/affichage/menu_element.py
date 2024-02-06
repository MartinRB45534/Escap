"""
La classe du menu d'éléments.
"""

from __future__ import annotations

import affichage as af
import modele as mdl

class MenuElement(af.MenuDeroulant):
    """Le menu d'éléments. Il permet de sélectionner un élément."""
    def __init__(self):
        defaut = af.TexteMenuDeroulant(self, "(Sélectionnez un élément)")
        af.MenuDeroulant.__init__(self, defaut)
        self.set_contenu_liste([defaut] + [
            af.TexteMenuDeroulant(self, element.value) for element in mdl.Element
        ])

    @property
    def accepte(self):
        """Renvoie si la valeur saisie est acceptée."""
        return self.courant.get_texte() != "(Sélectionnez un élément)"

    def accepte_autre(self, valeur: str):
        """Renvoie si la valeur saisie est acceptée."""
        return valeur != "(Sélectionnez un élément)"

    @property
    def valeur(self):
        """Renvoie l'élément sélectionné."""
        return self.courant.get_texte()

    @valeur.setter
    def valeur(self, valeur: str):
        """Change l'élément sélectionné."""
        if valeur in mdl.Element:
            texte = self.liste.contenu[list(mdl.Element).index(mdl.Element(valeur))*2]
            assert isinstance(texte, af.TexteMenuDeroulant)
            texte.set_actif()
        else:
            raise ValueError("Cet élément n'existe pas !")
