"""L'ichage principal de l'éditeur."""

from __future__ import annotations
from typing import TYPE_CHECKING

# Imports des classes parentes
from .noeuds import NoeudHierarchiqueSinistreSommet
from .wrapper_cliquable import WrapperCliquable

# Imports utilisés dans le code
from .wrapper_marge import WrapperMarge

if TYPE_CHECKING:
    from .cliquable import Cliquable

class Onglet(NoeudHierarchiqueSinistreSommet,WrapperCliquable):
    """Un onglet qui contient un Cliquable quelconque."""
    def __init__(self, nom:str, cliquable:Cliquable):
        NoeudHierarchiqueSinistreSommet.__init__(self)
        WrapperCliquable.__init__(self)
        contenu = WrapperMarge()
        contenu.set_contenu(cliquable)
        self.set_contenu(contenu)
        self.courant = cliquable
        self.nom = nom
