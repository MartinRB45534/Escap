"""L'ichage principal de l'éditeur."""

from __future__ import annotations
from typing import TYPE_CHECKING

# Imports des classes parentes
from .wrapper_cliquable import WrapperCliquable
from .noeuds import NoeudBloque

if TYPE_CHECKING:
    from .cliquable import Cliquable

class Onglet(NoeudBloque,WrapperCliquable):
    """Un onglet qui contient un Cliquable quelconque."""
    def __init__(self, nom:str, contenu:Cliquable):
        NoeudBloque.__init__(self)
        WrapperCliquable.__init__(self)
        self.set_contenu(contenu)
        self.courant = contenu
        self.nom = nom
