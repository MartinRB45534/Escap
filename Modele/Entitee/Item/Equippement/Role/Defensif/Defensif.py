from __future__ import annotations
from typing import TYPE_CHECKING

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ......Effet.Attaque.Attaque import Attaque_particulier

# Imports des classes parentes
from ...Equippement import Equippement

class Defensif(Equippement):
    """La classe des équipements défensifs. Réduit les dégats."""

    def intercepte(self,attaque:Attaque_particulier):
        pass
