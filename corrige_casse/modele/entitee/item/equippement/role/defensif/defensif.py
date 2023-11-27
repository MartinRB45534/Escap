"""Contient la classe Defensif."""

from __future__ import annotations
from typing import TYPE_CHECKING

# Imports des classes parentes
from ...equippement import Equippement

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ......effet.agissant.attaque import AttaqueParticulier

class Defensif(Equippement):
    """La classe des équipements défensifs. Réduit les dégats."""

    def intercepte(self,attaque:AttaqueParticulier):
        """Intercepte l'attaque. (Devrait en réduire les dégats.)"""
