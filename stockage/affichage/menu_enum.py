"""
La classe du menu d'éléments.
"""

from __future__ import annotations
from enum import StrEnum

import affichage as af

class MenuEnum(af.MenuDeroulant):
    """Le menu d'éléments. Il permet de sélectionner un élément."""
    def __init__(self, enum: type[StrEnum]):
        self.enum = enum
        textes = [af.TexteMenuDeroulant(self, element.value) for element in enum]
        af.MenuDeroulant.__init__(self, textes[0])
        self.set_contenu_liste(textes)

    @property
    def accepte(self):
        """Renvoie si la valeur saisie est acceptée."""
        return self.courant.get_texte() in self.enum

    def accepte_autre(self, _valeur: str):
        """Renvoie si la valeur saisie est acceptée."""
        return _valeur in self.enum

    @property
    def valeur(self):
        """Renvoie l'élément sélectionné."""
        return self.enum[self.courant.get_texte()].name

    @valeur.setter
    def valeur(self, valeur: str):
        """Change l'élément sélectionné."""
        try:
            texte = [texte for texte in self.liste.contenu
                     if isinstance(texte, af.TexteMenuDeroulant)
                     and texte.get_texte() == valeur][0]
            texte.set_actif()
        except IndexError as e:
            raise ValueError(f"L'élément {valeur} n'existe pas dans l'énumération.") from e
