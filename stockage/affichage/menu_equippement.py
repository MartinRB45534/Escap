"""
La classe du menu d'équippement.
"""

from __future__ import annotations

import affichage as af

class MenuEquippement(af.MenuDeroulant):
    """Le menu d'équippement. Il permet de sélectionner un type d'équippement."""
    equippements = [
        "Anneau",
        "Armure",
        "Heaume",
    ]
    def __init__(self):
        defaut = af.TexteMenuDeroulant(self, "(Sélectionnez un type d'équippement)")
        af.MenuDeroulant.__init__(self, defaut)
        self.set_contenu_liste([defaut] + [
            af.TexteMenuDeroulant(self, equippement) for equippement in self.equippements
        ])

    @property
    def accepte(self):
        """Renvoie si la valeur saisie est acceptée."""
        return self.courant.get_texte() != "(Sélectionnez un type d'équippement)"

    def accepte_autre(self, valeur: str):
        """Renvoie si la valeur saisie est acceptée."""
        return valeur != "(Sélectionnez un type d'équippement)"

    @property
    def valeur(self):
        """Renvoie l'élément sélectionné."""
        return self.courant.get_texte()

    @valeur.setter
    def valeur(self, valeur: str):
        """Change l'élément sélectionné."""
        if valeur in self.equippements:
            texte = [texte for texte in self.liste.contenu if isinstance(texte, af.TexteMenuDeroulant) and texte.get_texte() == valeur][0]
            texte.set_actif()
        else:
            raise ValueError("Cet élément n'existe pas !")
