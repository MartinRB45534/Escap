"""Contient la classe Jeu."""

from __future__ import annotations
from typing import List$1

import modele as mdl

class Jeu:
    """Le jeu, du point de vue de l'éditeur. Contient toutes les informations saisies par l'utilisateur."""
    def __init__(self):
        self.especes:List[mdl.Espece] = []
