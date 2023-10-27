from __future__ import annotations
from typing import TYPE_CHECKING

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ......effet.attaque.attaque import AttaqueParticulier

# Imports des classes parentes
from ...equippement import Equippement

class Defensif(Equippement):
    """La classe des équipements défensifs. Réduit les dégats."""

    def intercepte(self,attaque:AttaqueParticulier):
        pass
